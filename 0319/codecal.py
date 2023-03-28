import math

# 덧셈 뺄셈 나누기 곱하기 함수로 4개 작성
# 인풋풋입렵값에 숫자 두개 받기 연산자하나 받기
# q로 반복문 종료하기 전까지 계속 반복



def mkstr(str):
# 반복문을 돌려서 스플릿으로 연산자 기준으로 쪼갠 결과의 길이가 2면 쪼갠 기준의 연산자가
#쓰여진것 근데 길이가 1이 나오면 예시)"1+1"인 1인 길이가 나오기때문에 그 연산자가 아닌것
  n1 = 0
  n2 = 0
  operator = ""
  ops = ["+", "-", "*", "/"]

  for op in  ops:
    test = str.split(op)
    if len(test) == 2:
      operator = op
      n1 = int(test[0].strip())
      n2 = int(test[1].strip())
      break

  return n1, n2, operator
  
def operation(tup):
  input_num1, input_num2, operator = tup
  if operator == "+":
    answer = input_num1 + input_num2
  elif operator == "-":
    answer = input_num1 - input_num2
  elif operator == "*":
    answer = input_num1 * input_num2
  elif operator == "/":
    answer = input_num1 / input_num2
  return answer
  

while True:
  read = input("계산식을 입력하세요('q'를 입력하면 프로그램이 종료됩니다.): ")
  if read == "q":
    print("q를 입력하여 반복문 종료")
    break
  try:
    print(f"{operation(mkstr(read))}")
  except:
    print("제대로 다시 입력하세요.")
