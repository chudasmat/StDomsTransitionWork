from funcs import *

print("Welcome to Trishan's Mini Programs!\n")
while True:
  try:
    ques = int(input("Which program would you like to access? -> "))
    if ques < 1 or ques > 5:
      raise ValueError
  except ValueError:
    print("Invalid input, please enter a number that is 1-5")
  else:
    if ques in function_dict:
      function_dict[ques]()
      choosie = str(input("\nWould you like to access any other program? (Y/N) -> ")).upper()
      if choosie[0] == "Y":
        continue
      elif choosie[0] == "N":
        print("Thank you for using my program!")
        break