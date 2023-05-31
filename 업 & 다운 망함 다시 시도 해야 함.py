import random

computer_number = random.randrange(1, 101,1)
print(computer_number)
while player_number != computer_number:
  player_number = int(input("숫자를 입력하세요: "))
  if player_number > computer_number:
    print("UP")
  elif computer_number==player_number:
    print("정답!")
  elif computer_number<player_number:
    print("DOWN")
  else:
    print('Get out')
