import random

def radnomquiz(f):
  comb= int(f)
  randint(comb,)


  with open("vocabulary.txt", "r") as f:
    line = f.strip()
    line_devide = line.split(": ")
    korean_words = line_devide[1].strip()
    english_words = line_devide[0]
    quiz = input(f"{korean_words}: ")
    
  #input(f"{korean_words}: {user_input}")
    if quiz == english_words:
      print("맞았습니다!\n")

    else:
      print(f"아쉽습니다. 정답은 {english_words}입니다.\n")
    
  
  