'''
TODO: 解题思路.
'''
from collections import OrderedDict
import hashlib

class SchemaManager:
    def __init__(self):
        self._registry = {}

    def check_schema(self, schema, dataset):
        for record in dataset:
            if not self.check_record(record, schema):
                return False
        return True

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
            inner_dtype = dtype[5:-1]
            if type(dvalue) != list:
                return False
            for inner_dvalue in dvalue:
                if not self.check_data(inner_dvalue, inner_dtype):
                    return False
            return True
        else:
            return False

    def infer_schema(self, dataset):
        record_0 = dataset[0]
        schema = {}
        for field, dvalue in record_0.items():
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

    def register_schema(self, schema):
        schema_hash = self._get_schema_hash(schema)
        self._registry[schema_hash] = schema

    def get_schema(self, dataset):
        inferred_schema = self.infer_schema(dataset)
        schema_hash = self._get_schema_hash(inferred_schema)
        if schema_hash not in self._registry:
            self._registry[schema_hash] = inferred_schema
        return self._registry[schema_hash]

    def _get_schema_hash(self, schema):
        ordered_schema = OrderedDict()
        for field in sorted(schema.keys()):
            ordered_schema[field] = schema[field]
        schema_hash = hashlib.md5(str(ordered_schema).encode()).hexdigest()
        return schema_hash