def divisor_list(number):
    result = []
    end = int(number ** 0.5) + 1
    for i in range(1, end):
        if number % i == 0:
            result.append(i)
            result.append(number // i)
    return set(result)


n, k = map(int, input().split())
divisor = sorted(divisor_list(n))

if k > len(divisor):
    print(0)
else:
    print(divisor[k-1])
