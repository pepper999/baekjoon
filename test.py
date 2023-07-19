def lcm(x, y, z): 
    return int(x * y / z)

# 유클리드 호제법을 이용하여 최소공배수를 구함
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a, b = map(int, input().split())
c, d = map(int, input().split())
e = gcd(b, d)
f = int(lcm(b, d, e))
a = a*(f/b)
c = c*(f/d)
print(int(a+c), f)