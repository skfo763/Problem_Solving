import sys

input = sys.stdin.readline

base_str = [
    "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.",
    "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",
    "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
]
base_question = "\"재귀함수가 뭔가요?\""
base_answer = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
base_end = "라고 답변하였지."


def add_underscore(str_seq, input_n, k):
    char_list = list(str_seq)
    for _ in range((4 * (input_n - k))):
        char_list.insert(0, "_")
    return "".join(char_list)


def recursion(input_n, k):
    if k == 1:
        print(add_underscore(base_question, input_n, k))
        print(add_underscore(base_answer, input_n, k))
        print(add_underscore(base_end, input_n, k))
    else:
        print(add_underscore(base_question, input_n, k))
        for i in base_str:
            print(add_underscore(i, input_n, k))
        recursion(input_n, k-1)
        print(add_underscore(base_end, input_n, k))


n = int(input().rstrip())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursion(n+1, n+1)
