def q1():
  print("\nSimple Addition Program")
  while True:
    try:
      num1 = int(input("\nPlease enter your FIRST number: "))
      num2 = int(input("Please enter your SECOND number: "))
    except:
      print("\nNot a number")
    else:
      print(f'\nYour total is {num1 + num2}')
      break

def q2():
  print("\n3 Times Table\n")
  while True:
    try:
      limit = int(input("How high do you want the times table to go to: "))
      if limit < 1:
        raise ValueError # raise an exception to disallow inputs that are negative
    except ValueError:
      print("\nOnly integers that are larger than 0 are allowed\n")
    else:
      break
  print(" ")
  for i in range(1, limit + 1):
    print(f'{i} x 3 = {i * 3}')

def q3():
  print("\nTimes Table Generator\n")
  ttable = int(input("Please enter the number of the times table you would like: "))
  while True:
    try:
      limit = int(input("How high do you want the times table to go to: "))
      if limit < 0:
        raise ValueError  # raise an exception to disallow inputs that are negative
    except ValueError:
      print("\nOnly integers that are larger than 0 are allowed\n")
    else:
      break
  print(" ")
  for i in range(1, limit + 1):
    print(f'{i} x {ttable} = {i * ttable}')

def q4():
  print("\nConcatenator\n")
  fore = str(input("Please enter first name: "))
  last = str(input("Please enter last name: "))
  print(f'Your Full Name is {fore} {last}')

def q5():
  print("\nKilogram to Stones & Pounds Converter\n")
  while True:
    try:
      kgMass = float(input("Please enter your mass in kilograms: "))
      if kgMass < 0:
        raise ValueError # exception raised if value provided is negative
    except ValueError:
      print("Mass has to be a positive value")
    else:
      break
  kgToPounds = kgMass * 2.20462
  stones = int(kgToPounds / 14)  # 'int' function rounds down the conversion from pounds to stones (better than importing math module)
  pounds = round(kgToPounds % 14, 3)
  if stones == 0 and pounds != 0:
    print(f'{int(kgMass) if kgMass % 1 == 0 else kgMass}kg is equal to {pounds}lb')
  elif stones != 0 and pounds == 0:
    print(f'{int(kgMass) if kgMass % 1 == 0 else kgMass}kg is equal to {stones}st')
  else:
    print(f'{int(kgMass) if kgMass % 1 == 0 else kgMass}kg is equal to {stones}st and {pounds}lb')

function_dict = {
    1: q1,
    2: q2,
    3: q3,
    4: q4,
    5: q5
}