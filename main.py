def division(first, second):
  if second == 0:
    print("Nedalīt ar nulli!!")
  else:
    answer = first / second
    print(first, "dalīt ar", second, "=", answer)

firstNum = int(input("Ievadiet pirmo numuru: "))
secondNum = int(input("Ievadiet dalītāju: "))
division(firstNum, secondNum)