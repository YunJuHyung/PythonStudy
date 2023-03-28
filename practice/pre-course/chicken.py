with open("vocabulary.txt", "a") as f:
  while True:
    user_input = input("영어 단어를 입력하세요: ")
    if user_input == "q":
      break
    user_input2 = input("한국어 단어를 입력하세요: ")
    if user_input2 == "q":
      break
    f.write("{}: {}\n".format(user_input, user_input2))