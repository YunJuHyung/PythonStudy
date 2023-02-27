def solution(num_apple, num_carrot, k):
    answer = 0
    
    if num_apple < num_carrot * 3: # 사과 5 당근 1
        answer = num_apple // 3 # 주스 1
    else:
        answer = num_carrot    #당근의 수만큼 주스가 나옴
                              #2차결과 else로 돌아와서 당근이 0개

    num_apple -= answer * 3 #사과 5 -= 주스 1*3 그럼 사과는 2
    num_carrot -= answer #당근 1 -= 주스 1 결과 0

    i = 0
    while k - (num_apple + num_carrot + i) > 0:
        if i % 4 == 0:
            answer -= 1
        i = i + 1
        
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")