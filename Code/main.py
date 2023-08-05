from funcs import *

print("Welcome to Trishan's Mini Programs!")
print("\n1. Simple Addition Program\n2. 3 Times Table\n3. Times Table Generator\n4. Concatenator\n5. Kilogram to Stones & Pounds Converter\n")
while True:
  try:
    ques = int(input("Which program would you like to access? (Specify the number) -> "))
    if ques < 1 or ques > 5:
      raise ValueError
  except ValueError:
    print("Invalid input, please enter a number that is 1-5")
  else:
    if ques in function_dict:
      function_dict[ques]()
      choosie = str(input("\nWould you like to access another program? (Y/N) -> "))
      if choosie.upper()[0] == "Y":
        continue
      elif choosie.upper()[0] == "N":
        print("Thank you for using my program!")
        break