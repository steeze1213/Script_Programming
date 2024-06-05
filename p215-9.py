def overlap(A, B):

    max_overlap = 0
    overlap_str = ''

    for i in range(1, min(len(A), len(B)) + 1):
        if A[-i:] == B[:i]:
            max_overlap = i

    if max_overlap == min(len(A), len(B)):
        return B

    overlap_str = A + B[max_overlap:]
    return overlap_str

A = input("A: ")
B = input("B: ")
C = overlap(A, B)

print("A+B:", C)
