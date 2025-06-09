'''
我们要构建一个用于管理机器学习数据集的系统 其主要目的是：
跟踪不同数据集的schema, schema定义了字段名与其数据类型的映射
每个数据集是一个记录(record)列表 每条记录是一个字段名到字段值的映射
匹配逻辑:此题定义“match”为“exact match” 即记录的字段名和数据类型与schema完全一致
Part 1:验证器实现
目标：实现一个函数，验证一个给定的数据集是否匹配一个给定的 schema。
每条记录字段必须与 schema 完全一致，字段数、字段名、字段类型都一致；
支持嵌套类型 如:list[str], list[list[int]]
考虑用递归处理嵌套类型
Part 2:推断schema
目标:实现一个函数 根据一个数据集推断出schema
需要遍历所有记录；
需考虑记录间字段可能不一致的情况 例如某条记录缺少字段
支持推断嵌套结构类型 例如 list[str], list[list[int]]
Part 3:schema 管理器扩展
目标：实现一个 schema 管理器，支持以下两个方法：
注册一个新的schema:register_schema(schema)
查找与一个给定数据集匹配的schema:get_schema(dataset) 若找不到就注册一个新的
优化方向：
初始做法是遍历所有 schema 做验证 O(N)
提示优化方案: schema序列化 + 哈希（加快查找），或使用 Trie 树结构压缩存储

-- clarification:
类型只支持:str, int, bool, list[type], list[list[type]]
所有字段要求完全匹配（包括字段名、数量和数据类型）
假设数据集初期fit in memory
思路:
Part 1: 校验函数
遍历每条 record 逐字段检查是否与 schema 一致。
支持基础类型 int, str, bool 和嵌套类型 list[str], list[list[int]]。
若任何一条 record 校验失败，则整个数据集无效。
Part 2: 推断 schema
选第一条记录作为“代表样本”推断每个字段的类型
对嵌套列表递归判断内部元素类型；
验证推断出的 schema 是否适用于整个数据集（确保一致性）
Part 3: schema 注册 + 查找
用 OrderedDict 保证字段顺序一致性；
用 md5(schema_string) 做哈希作为唯一 key
get_schema 自动注册不存在的 schema
复杂度标注在code各个函数中
'''
import hashlib

class SchemaManager:
    def __init__(self):
        self.hash_to_schema = {} # part 3 用到
    # n:# of record, m:# of fields -> T(n*m)
    def check_schema(self, schema, dataset):
        for record in dataset:
            if not self.check_record(record, schema):
                return False
        return True
    # check fields是否完全对应 然后check data中的值是否真的是schema中的type
    def check_record(self, record, schema):
        record_fields = record.keys()
        schema_fields = schema.keys()
        if sorted(record_fields) != sorted(schema_fields):
            return False
        for field in schema_fields:
            dtype = schema[field]
            dvalue = record[field]
            if not self.check_data(dvalue, dtype):
                return False
        return True

    def check_data(self, dvalue, dtype):
        if dtype == 'int':
            return type(dvalue) == int
        elif dtype == 'str':
            return type(dvalue) == str
        elif dtype == 'bool':
            return type(dvalue) == bool
        elif dtype.startswith('list[') and dtype.endswith(']'):
            inner_type = dtype[5:-1] # list[xxx] 取出xxx部分
            if type(dvalue) != list:
                return False
            for inner_value in dvalue:
                if not self.check_data(inner_value, inner_type):
                    return False
            return True
        else:
            return False
    # T(n*m)
    def infer_schema(self, dataset):
        if not dataset:
            raise ValueError("empty dataset")
        first_record = dataset[0]
        schema = {}
        for field, dvalue in first_record.items():
            schema[field] = self.infer_type(dvalue)

        if not self.check_schema(schema, dataset):
            raise ValueError("Input dataset does not have a consistent schema")
        return schema

    def infer_type(self, dvalue):
        if type(dvalue) == int:
            return 'int'
        elif type(dvalue) == str:
            return 'str'
        elif type(dvalue) == bool:
            return 'bool'
        elif type(dvalue) == list:
            if not dvalue:
                raise ValueError("Cannot infer schema from empty list")
            inner_dvalue = dvalue[0]
            inner_type = self.infer_type(inner_dvalue)
            if not self.check_data(inner_dvalue, inner_type):
                raise ValueError("Inconsistent inner types in list")
            return f'list[{inner_type}]'
        else:
            raise ValueError(f"Unsupported type: {type(dvalue)}")
    # 单次register T(m*logm) -> sort fields and serilization
    def register_schema(self, schema):
        hash = self.calculate_hash(schema)
        self.hash_to_schema[hash] = schema

    def get_schema(self, dataset):
        schema = self.infer_schema(dataset)
        hash = self.calculate_hash(schema)
        if hash not in self.hash_to_schema:
            self.hash_to_schema[hash] = schema
        return self.hash_to_schema[hash]

    def calculate_hash(self, schema):
        items = sorted(schema.items()) # 返回list[tuple[str,str]] 
        hash = hashlib.md5(str(items).encode()).hexdigest() # 序列化成str再转化成md5
        return hash