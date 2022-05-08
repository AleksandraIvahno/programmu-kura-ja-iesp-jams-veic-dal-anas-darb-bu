def Atlaide(sum):
  newSum = sum
  if sum >= 200 and sum <= 499:
    Atlaide = sum * 0.1
    newSum = sum - Atlaide
  elif sum >= 500:
    Atlaide = sum * 0.2
    newSum = sum - Atlaide
  return newSum

print("Ievadiet pirkuma summu:")

summa = float(input("Summa: "))

print("Jūsu pirkuma cena:", Atlaide(summa))