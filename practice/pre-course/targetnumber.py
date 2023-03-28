import random

# 여기에 코드를 작성하세요
count = 4 # 기회
i = 0 # 몇번만에 맞혔는지
answer = random.randint(1, 21)
player = int()
total = input(f"기회가 {count}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: {player}")


def updown(player):
    if player < answer:
        print("Up")
    
    elif player > answer:
        print("Down")
        
    return 0


for i in range(1, 4):
    if count == 1:
        print(input(f"아쉽습니다. 정답은 {answer}였습니다."))
        break
    if player == answer:
        print(f"축하합니다. {i}번만에 숫자를 맞히셨습니다.")
        break
        
    print(total)
    updown(player)
    
    
    count -= 1
    i += 1
    
