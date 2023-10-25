import turtle

# 색상 리스트를 만듭니다.
# 이 리스트는 거북이가 그릴 때 사용할 색상을 순서대로 담고 있습니다.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# 거북이를 생성합니다.
star = turtle.Turtle()

# 거북이의 속도를 설정합니다.
# 숫자가 클수록 거북이가 그림을 그리는 속도가 빨라집니다.
star.speed(10)

# 60번 반복하는 루프를 만듭니다.
# 이 루프 안에서 거북이가 별을 그리고, 오른쪽으로 조금씩 회전합니다.
for i in range(60):
    # 색상 리스트에서 색을 선택합니다.
    # 반복문이 돌 때마다 i 값이 1씩 증가하므로, i를 6으로 나눈 나머지를 인덱스로 색상을 선택하면 6가지 색상이 순서대로 반복됩니다.
    star.color(colors[i%6])
    # 별을 그립니다.
    if i%6 == 0:
        star.right(75)
    for side in range(5):
        star.forward(100)
        star.right(144)
    # 별을 그린 뒤에는 거북이를 오른쪽으로 5도 회전합니다.
    # 이렇게 하면 거북이가 원형으로 별을 그리게 됩니다.
    star.right(5)

# 그림 그리기를 마칩니다.
turtle.done()
