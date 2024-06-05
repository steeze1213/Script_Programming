n = int(input("n을 입력하시오: "))

snake = []

for i in range(1, n**2 + 1, n):
    row = list(range(i, i + n))
    if len(snake) % 2 == 1:
        row.reverse()
    snake.append(row)

for row in snake:
    print(*row)
