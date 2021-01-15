"""
   0     1     2     3     4     5     6     ...     n                      n+1
1  0     1     1     1     1     1     1     ...     1(n%1 == 0 ? 1 : 0)    1(n%1 == 0 ? 1 : 0)
2              2           2           2     ...     n-1%2 ? 2 : 0          n%2 == 0 ? 2 : 0
3                    3                 3     ...     n-1%3 ? 3 : 0          n%3 == 0 ? 3 : 0
4                          4                 ...     n-1%4 ? 4 : 0          n%4 == 0 ? 4 : 0
5                                5           ...     n-1%5 ? 5 : 0          n%5 == 0 ? 5 : 0
6                                      6     ...     n-1%6 ? 6 : 0          n%6 == 0 ? 6 : 0
n-1                                                  n(n-1%n-1 ? n-1 : 0)   n%n-1 == 0 ? n-1 : 0
n                                                    0(n-1%n ? n-1 : 0)     n(n%n == 0 ? n : 0)

sudo code
result = [1 for i in range(n+1)]
for i in range(2, n+1):
    for j in range(1, n//i, 1):
        result[i*j] += i

for i in range(1, n+1):
    result[i] += result[i-1]
"""
import sys

input = sys.stdin.readline
output = sys.stdout.write
n = 1000000
result = [1 for i in range(n+1)]
result[0] = 0

count = int(input())

for i in range(2, n+1):
    for j in range(1, (n//i)+1, 1):
        result[i*j] += i

for i in range(1, n+1):
    result[i] += result[i - 1]

for _ in range(count):
    output("{}\n".format(result[int(input())]))
