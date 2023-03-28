def convert_decimal_to_binary(decimal_num):
  answer = "0b"
  list = []
  while decimal_num // 2 != 0:
    list.append(decimal_num % 2)
    decimal_num = decimal_num // 2
  list.append(decimal_num)
  i = len(list) - 1
  while i >= 0:
    answer += str(list[i])
    i -= 1
  return answer
  
  
print(convert_decimal_to_binary(10)) # 예상 출력값: "0b1010"
print(convert_decimal_to_binary(42)) # 예상 출력값: "0b101010"
print(convert_decimal_to_binary(255)) # 예상 출력값: "0b11111111"
print(convert_decimal_to_binary(7)) # 예상 출력값: "0b111"