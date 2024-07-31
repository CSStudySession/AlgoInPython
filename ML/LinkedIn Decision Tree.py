'''
design and implement a decision tree. focus on termination criteria and OOP.
assume boolean features and boolean lable variables.

'''
import math
from typing import List
from collections import Counter

class Feature:
    def __init__(self, name:str = "", val:bool = False):
        self.name = name
        self.val = val
    def __eq__(self, other) -> bool:
        if isinstance(other, Feature):
            return self.name == other.name
        return False
    def __hash__(self):
        return hash(self.name)
    
class Instance:
    def __init__(self, features:set[Feature] = set(), label:bool = False):
        self.features = features
        self.label = label

# decision tree node defination
class Node:
    def __init__(self, left:'Node' = None, right:'Node' = None, feature:Feature = None):
        self.left = left
        self.right = right
        self.feature = feature

# init a descision tree and return the root of the tree. Note that this is a recursive function.
def init_decision_tree(instances:List[Instance], features:set[Feature]) -> Node:
    if not instances or not features:
        return None
    
    # base case: 已经hit leaf node, 直接返回一个空root即可
    if hit_termination_condition(instances):
        return Node()
    
    max_gain_feature = find_max_gain_feature(instances, features)
    left_instances, right_instances = split_instances(instances, max_gain_feature)
    
    # for features with binary label, it won't split on the same feature again. 
    # it doesn't apply for dense features (dense means continuous) 
    features.remove(max_gain_feature)

    left_node = init_decision_tree(left_instances, features)
    right_node = init_decision_tree(right_instances, features)
    
    return Node(left_node, right_node, max_gain_feature)

    

# 当instances里面所有label都一样时 可以结束split了 否则还需要接着split
def hit_termination_condition(instances:List[Instance]) -> bool:
    counter = Counter(ins.label for ins in instances)
    return True if len(counter.keys()) == 1 else False # 以label为key


# 计算可以获得最大收益的split feature
def find_max_gain_feature(instances:List[Instance], features:set[Feature]) -> Feature:
    max_gain = float('-inf')
    ret = None
    for feature in features:
        cur_gain = calculate_info_gain(instances, feature)
        if cur_gain > max_gain:
            max_gain = cur_gain
            ret = feature
    return ret

'''
entropy = -( p*ln(p) + (1-p)*ln(1-p) )
where ln is natural logarithm, and p is probability that the bool type feature equals to 1
'''
def calculate_entropy(instances:List[Instance], feature: Feature) -> float:
    feat_cnt = 0
    for ins in instances:
        # count how many this target feature in instances
        if feature in ins.features:
            feat_cnt += 1
    prob = feat_cnt / len(instances) # feature出现的概率
    return - (prob * math.log(prob) + (1 - prob) * math.log(1 - prob))

def split_instances(instances:List[Instance], target_feature:Feature) -> tuple[Instance]:
    left_instances, right_instances = [], []
    for ins in instances:
        if target_feature in ins.features:
            right_instances.append(ins)
        else:
            left_instances.append(ins)
    return (left_instances, right_instances)

'''
calculate information gain per target feature split
gain = paraent entropy - weighted avg of the child node's entropies.
'''
def calculate_info_gain(instances:List[Instance], feature:Feature) -> float:
    cur_entropy = calculate_entropy(instances, feature)
    
    left_instances, right_instances = split_instances(instances, feature)
    
    left_entropy = calculate_entropy(left_instances, feature)
    right_entropy = calculate_entropy(right_instances, feature)

    left_weight = len(left_instances) / len(instances)
    right_weight = len(right_instances) / len(instances)

    ret = cur_entropy - left_weight * left_entropy - right_weight * right_entropy
    return ret