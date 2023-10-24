import random

# 문제와 답 리스트
물리_초급 = [
    ("물체의 운동 상태를 변화시키기 위한 힘을 무엇이라고 할까요?", "작용력"),
    ("운동하는 물체에 작용하는 힘이 없으면 어떻게 되나요?", "등속운동")
]

물리_중급 = [
    ("질량이 2배인 두 물체가 같은 속도로 움직일 때, 그 운동 에너지는 어떻게 될까요?", "같다"),
    ("힘과 방향이 모두 같은 경우에만 발생하는 원인을 무엇이라고 할까요?", "정지마찰력")
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

    num_of_questions = int(input("출제할 문제 개수를 입력하세요: "))  # 사용자로부터 출제할 문제 개수 입력 받음

    while len(asked_questions) < num_of_questions:
        category = input("문제 카테고리를 선택하세요 (물리/화학): ")

        if category == '물리':
            difficulty = input("난이도를 선택하세요 (초급/중급): ")
            if difficulty == '초급':
                question, answer = select_question(asked_questions, 물리_초급)
                questions_list = 물리_초급
            elif difficulty == '중급':
                question, answer = select_question(asked_questions, 물리_중급)
                questions_list = 물리_중급
            else:
                print("잘못된 난이도입니다. 다시 입력해주세요.")
                continue

        else:
            print("잘못된 카테고리입니다. 다시 입력해주세요.")
            continue

        if question is None:
            break

        print("🌟 문제:", question)

        user_answer = input("🔍 정답을 입력하세요: ")

        if user_answer.lower() == answer.lower():
            score += 1
            print("✅ 정답입니다!")
        else:
            hint_index = random.randint(0, len(answer) - 1)
            hint_char = answer[hint_index]

            # 오답 시 힌트 제공 및 재도전 여부 확인
            while True:
                show_hint_choice = input('❓ 정답을 맞추지 못하셨습니다. 힌트를 보시겠습니까? (y/n): ')
                if show_hint_choice.lower() == 'y':
                    print(f"⭐️ 힌트: 정답의 {hint_index + 1}번째 글자는 '{hint_char}'입니다.")
                    break
                elif show_hint_choice.lower() == 'n':
                    break

            # 힌트를 보고도 정답을 맞추지 못한 경우
            if show_hint_choice.lower() == 'n' and user_answer.lower() != answer.lower():
                retry_choice = input('🔄 다시 도전하시겠습니까? (y/n): ')
                if retry_choice.lower() != 'y':
                    break

        asked_questions.append((question, answer))

    print(f"🏁 게임 종료! 총 점수: {score}/{num_of_questions}")

# 게임 실행
play_game()
