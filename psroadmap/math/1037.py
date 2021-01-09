# A가 N의 진짜 약수이다 -> N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# if A == 진짜_약수(N), N % A == 0 && A != 1 && A != N
# 특정 수 N의 진짜 약수를 모두 알고 있을 때 N이 뭔지 구하시오.
# 어떤 배열을 받든 간에, 배열의 첫 번째 수와 배열 끝 수를 곱한 값이 그 수.
# 만약 배열에 item 이 한개만 있는 경우를 예외상황으로 고려해야 함.

count = int(input())
real_list = list(map(int, input().split()))
real_list.sort()

if len(real_list) == 1:
    target_number = real_list[0] ** 2
    print(str(target_number))
else:
    target_number = real_list[0] * real_list[-1]
    print(str(target_number))
