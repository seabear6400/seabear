import random

# 카드의 값
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# 카드의 종류
suits = ["♠", "♥", "♣", "♦"]

# 카드를 섞는다.
cards = []
for suit in suits:
  for value in values:
    cards.append((suit, value))
random.shuffle(cards)

# 플레이어의 수를 입력받는다.
players_count = int(input("플레이어의 수를 입력하세요: "))

# 플레이어를 생성한다.
players = []
for i in range(players_count):
  players.append({
    "name": input("플레이어 {}의 이름을 입력하세요: ".format(i + 1)),
    "cards": []
  })

# 각 플레이어에게 5장의 카드를 나누어 준다.
for i in range(players_count):
  for j in range(5):
    players[i]["cards"].append(cards.pop())

# 게임을 시작한다.
turn = 0
while len(cards) > 0:
  # 현재 플레이어의 카드를 출력한다.
  print("현재 플레이어: {} / 카드: {}".format(players[turn]["name"], players[turn]["cards"]))

  # 현재 플레이어의 카드 중 가장 높은 카드를 찾는다.
  highest_card = max(players[turn]["cards"], key=lambda x: (x[1], x[0]))

  # 현재 플레이어의 카드 중 가장 높은 카드를 출력한다.
  print("현재 플레이어의 가장 높은 카드: {}".format(highest_card))

  # 다음 플레이어로 넘어간다.
  turn = (turn + 1) % players_count

  # 다음 플레이어가 카드를 내지 못하는 경우, 덱에서 카드를 한 장 뽑는다.
  if len(players[turn]["cards"]) == 0:
    players[turn]["cards"].append(cards.pop())

# 게임이 끝난다.
winner = players[turn]["name"]
print("게임의 승자는 {}입니다!".format(winner))
