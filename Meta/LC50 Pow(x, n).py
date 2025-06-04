# method 1: iterative. time o(logn) space o(1)
def power_x_n(x: float, n: int) -> float:
    if n == 0:
        return 1

    # Handle case where, n < 0.
    if n < 0:
        n = -1 * n
        x = 1.0 / x

    # Perform Binary Exponentiation.
    result = 1
    while n != 0:
        # If 'n' is odd 
        if n % 2 == 1:
            result *= x
            n -= 1
        # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
        x *= x
        n //= 2
    return result

# method2: recursive time O(logn) space O(h) at most o(logn)
def power_x_n_recur(self, x: float, n: int) -> float:
    if x == 0: return 0
    if x == 1: return 1
    if n == 0: return 1
    if n < 0: 
        return 1/self.myPow(x, -n)
    if n % 2 == 0:
        return self.myPow(x*x, n // 2)
    else: # n%2==1
        return x * self.myPow(x, n - 1) # x在外面乘