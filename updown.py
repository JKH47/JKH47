import random

def updown_game():
    while True:
        answer = random.randint(1, 100)
        guess = None
        attempts = 0

        print("1부터 100 사이의 숫자를 맞춰보세요.")

        while guess != answer:
            try:
                guess = int(input("숫자를 입력하세요: "))
                if guess < 1 or guess > 100:
                    raise ValueError("1부터 100 사이의 숫자를 입력하세요.")
            except ValueError as e:
                print(e)
                continue

            attempts += 1

            if guess < answer:
                print("Up! 더 큰 수를 입력하세요.")
            elif guess > answer:
                print("Down! 더 작은 수를 입력하세요.")
            else:
                print(f"정답입니다! {attempts}번 만에 맞추셨습니다.")
                break

        play_again = input("다시 시작하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            print("게임을 종료합니다.")
            break

updown_game()
