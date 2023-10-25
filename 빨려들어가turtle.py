import turtle

# 색상 리스트를 만듭니다.
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

# 거북이를 생성합니다.
t = turtle.Pen()
turtle.bgcolor('black')

# 거북이의 속도를 설정합니다.
t.speed(0)

# 360번 반복하는 루프를 만듭니다.
for x in range(360):
    # 색상 리스트에서 색을 선택합니다.
    t.pencolor(colors[x%6])
    # 앞으로 x 만큼 이동합니다. (x는 반복문이 돌 때마다 1씩 증가합니다.)
    t.forward(x)
    # 오른쪽으로 59도 회전합니다.
    t.right(59)

