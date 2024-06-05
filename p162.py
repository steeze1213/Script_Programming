def get_square(a, b, c):
    a_sq = a ** 2
    b_sq = b ** 2
    c_sq = c ** 2
    return a_sq, b_sq, c_sq

a = 1
b = 2
c = 3

a_sq, b_sq, c_sq = get_square(a, b, c)
print(f"{a} 제곱: {a_sq}, {b} 제곱: {b_sq}, {c} 제곱: {c_sq}")
