import random

# 문제와 답 리스트
물리 = [
    ("물체의 운동 상태를 변화시키기 위한 힘을 무엇이라고 할까요?", "작용력"),
    ("운동하는 물체에 작용하는 힘이 없으면 어떻게 되나요?", "등속운동"),
    ("질량이 2배인 두 물체가 같은 속도로 움직일 때, 그 운동 에너지는 어떻게 될까요?", "같다"),
    ("힘과 방향이 모두 같은 경우에만 발생하는 원인을 무엇이라고 할까요?", "정지마찰력"),
    ("탄성력과 반대 방향으로 작용하여 속도를 줄여주는 힘을 무엇이라고 할까요?", "감속력")
]

화학 = [
    ("불꽃시험에서 어느 색상의 불꽃이 나오는지로 원소를 판별할 수 있습니다. 이 색상은 무엇일까요?", "노랑색"),
    ("원자가 전자를 잃어버리면 전하상태가 어떻게 될까요?", "양전하"),
    ("분자 내에서 서로 다른 원자들 사이에 이루어지는 결합은 무엇일까요?", "공유결합"),
    ("산소 분자(O2)의 전하 상태(전하량)는 얼마인가요? (양수 혹은 음수)", "0")
]

# 문제 선택 함수 (중복 제거)
def select_question(asked_questions, questions_list):
    available_questions = [q for q in questions_list if q not in asked_questions]

    if len(available_questions) == 0:
        return None

    return random.choice(available_questions)

# 게임 실행 함수
def play_game():
    score = 0  # 정답 개수 초기화
    asked_questions = []  # 이미 출제된 문제 기록

    print("🎯 고1 수준의 과학 문제를 풀어보세요! 🎯")

    while True:
        category = input("문제 카테고리를 선택하세요 (물리/화학): ")

        if category == '물리':
            question, answer = select_question(asked_questions, 물리)
            questions_list = 물리
        elif category == '화학':
            question, answer = select_question(asked_questions, 화학)
            questions_list = 화학
        else:
            print("잘못된 카테고리입니다. 다시 입력해주세요.")
            continue

        if question is None:
            break

        print("🌟 문제:", question)
        user_answer = input("🔍 정답을 입력하세요: ")

        if user_answer == answer:
            score += 1
        else:
            print(f"❌ 오답입니다. 정답은 '{answer}' 입니다.")

        asked_questions.append((question, answer))

        play_again = input("🔄 다시 플레이하시겠습니까? (y/n): ")

        if play_again.lower() != "y":
            break

    print(f"🏁 게임 종료! 총 점수: {score}/{len(questions_list)}")

# 게임 실행
play_game()
