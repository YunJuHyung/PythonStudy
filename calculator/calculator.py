
def mkstr(str):
  num1 = 0
  num2 = 0
  operator = ""
  op = ["+", "-", "*", "/"]

  for i in op:           ##이 부분 줫내 어렵네
    test = str.split(i)
    if len(test) == 2:
      operator = i
      num1 = int(test[0].strip())
      num2 = int(test[1].strip())
      break

  return num1, num2, operator


def operation(num1, num2, operator):
  answer = 0
  if operator == '+':
    answer = num1 + num2
  elif operator == '-':
    answer = num1 - num2
  elif operator == '*':
    answer = num1 * num2
  elif operator == '/':
    answer = num1 / num2

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