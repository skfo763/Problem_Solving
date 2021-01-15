"""
(1) 최대공약수 : GCD
유클리드 호제법 : 나머지가 0이 될 때 까지 나눈다.
a = b * q1 + r1
b = r1 * q2 + r2
r1 = r2 * q3 + r3
..
rn-1 = rn * qn+1 + 0
따라서, gcd(a, b) = rn

while r != 0:
    r = a % b
    a = b
    b = r

(2) 최소공배수 : LCM
lcm(a, b) = (a * b) / gcd(a, b)
"""


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


b, a = sorted(map(int, input().split()))
print(gcd(a, b))
print(lcm(a, b))
