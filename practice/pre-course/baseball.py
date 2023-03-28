from random import randint


def generate_numbers():
    numbers = []
    for i in range(3):
        rand = randint(0,9)
        while rand in numbers:
            rand = randint(0, 9)
        numbers.append(rand)
    # 여기에 코드를 작성하세요
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    # 여기에 코드를 작성하세요
    num = 1
    while num <= 3:
        guess = int(input(f'{num}번째 숫자를 입력하세요: '))
        if guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        if guess < 0 or guess > 9:
            print("범위를 벗어난 숫자입니다. 다시 입력하세요.")
            continue
        new_guess.append(guess)
        num += 1
    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    # 여기에 코드를 작성하세요
    for i in range(len(guesses)):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1
    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 여기에 코드를 작성하세요
while True:
    tries += 1
    new_guess = take_guess()
    st, b = get_score(new_guess, ANSWER)
    print(f'{st}S {b}B')
    if st == 3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
