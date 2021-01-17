import sys
input = sys.stdin.readline

while True:
    seq = input().rstrip()
    if seq == "0":
        break
    else:
        seq = list(seq)
        mid = len(seq) // 2
        left, right = [], []
        if len(seq) % 2 == 0:
            for i in range(0, mid):
                left.append(seq[i])
            for i in range(mid, len(seq)):
                right.append(seq[i])
        else:
            for i in range(0, mid):
                left.append(seq[i])
            for i in range(mid+1, len(seq)):
                right.append(seq[i])
        if left == list(reversed(right)):
            print("yes")
        else:
            print("no")