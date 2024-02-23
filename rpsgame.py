import random

def get_user_choice():
    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").strip().lower()
        if user_choice in ["가위", "바위", "보"]:
            return user_choice
        else:
            print("유효한 입력이 아닙니다.")

def get_computer_choice():
    return random.choice(["가위", "바위", "보"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        return "사용자 승리"
    else:
        return "컴퓨터 승리"

def main():
    user_wins = 0
    user_losses = 0
    draws = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "사용자 승리":
            user_wins += 1
        elif result == "컴퓨터 승리":
            user_losses += 1
        else:
            draws += 1

        while True:
            play_again = input("다시 하시겠습니까? (y/n): ").strip().lower()
            if play_again in ["y", "n"]:
                break
            else:
                print("유효한 입력이 아닙니다.")

        if play_again != "y":
            break

    print(f"승: {user_wins} 패: {user_losses} 무승부: {draws}")
    print("게임을 종료합니다.")

if __name__ == "__main__":
    main()
