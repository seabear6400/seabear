import random

# 문제와 답 리스트
questions = [
    ("지구에서 가장 큰 대륙은?", "아프리카"),
    ("태양계의 3번째 행성은?", "지구"),
    ("물의 화학식은?", "H2O"),
    ("식물이 광합성을 하기 위해 사용하는 빛의 파장대는?", "녹색"),
    ("산소 원자 번호는 몇 번인가요?", "8"),
]

# 문제 선택 함수 (중복 제거)
def select_question(asked_questions):
    available_questions = [q for q in questions if q not in asked_questions]
    
    if len(available_questions) == 0:
        return None
    
    return random.choice(available_questions)

# 게임 실행 함수
def play_game():
    score = 0  # 정답 개수 초기화
    asked_questions = []  # 이미 출제된 문제 기록
    
    print("🎯 퀴즈 게임을 시작합니다! 🎯")
    
    while True:
        question, answer = select_question(asked_questions)
        
        if question is None:
            break
        
        print("\n🌟 문제:", question)
        user_answer = input("🔍 정답을 입력하세요: ")

        if user_answer == answer:
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 오답입니다. 정답은 '{answer}' 입니다.")
        
        asked_questions.append((question, answer))

        play_again = input("\n🔄 다시 플레이하시겠습니까? (y/n): ")
        
        if play_again.lower() != "y":
            break
    
    print(f"\n🏁 게임 종료! 총 점수: {score}/{len(questions)}")

# 게임 실행
play_game()
