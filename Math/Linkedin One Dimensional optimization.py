'''
给定一个convet function f(x), 已知它在[i,r]之间有最小值. 给定一个method:

evaluateAt(float x) -> float

evaluateAt可以evaluate f(x)的任何值

求f(x)的最小值

another same question: given an array that its values first decrease and then increase, find it's min value. 
array example:
[10, 5, 0, 2, 3, 5, 7, 15, 20]

variants:
1. find min for a non-convex but unimodal function? (全局还是只有一个极值点)
binary search still holds.
2. time complexity?
O( log(L/epsilon) )
3. what if N > 1 dimension? how does time complexity grow with N?
O(T) -> O(N*T), since each N dimension needs calcuate gradient and applies a descent
4. how to wirte UT?
 a. prepare different target fucntions
 b. call calculaute_min_val() with target functions. verify output.
'''

def evaluate_at(x: float) -> float:
    pass

def calculate_min_val(left: float, right: float) -> float:
    if (right < left):
        raise ValueError("invalid input")
    
    epsilon = 1e-5
    while (right - left > epsilon):
        mid = left + (right - left) / 2
        mid_with_epsilon = mid + epsilon

        mid_val = evaluate_at(mid)
        mid_with_epsilon_val = evaluate_at(mid_with_epsilon)

        if mid_val > mid_with_epsilon_val:
            left = mid          # negative gradient (x->x+delta_x, val decreases) min locates to the right 
        else:
            right = mid         # postive gradient (x->x+delta_x, val increases) min locates to the left 
    return (left + right) / 2


'''
followup: what if the input is a convex function and a random point x?
apply gradient descent
'''
def calc_min_with_GD(x: float) -> float:
    learning_rate = 0.02
    epsilon = 1e-5
    iter_times = 10000

    cur = x
    while iter_times:
        x_with_epsilon = cur + epsilon
        gradient = calc_gradient(cur, x_with_epsilon)
        if abs(gradient) < epsilon:                     # consider converging
            return cur
        cur -= learning_rate * gradient
        iter_times -= 1
    return cur

# calcuate gradient
def calc_gradient(cur_pos: float, pos_with_epsilon: float) -> float:
    return (evaluate_at(pos_with_epsilon) - evaluate_at(cur_pos)) / (pos_with_epsilon - cur_pos)
