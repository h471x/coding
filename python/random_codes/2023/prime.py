
number = int(input("\n  Number : "))
if number < 1:
  print("\n {} is not a prime number".format(number))
else:
  for i in range(2, number):
    if number % i == 0:
      print("\n {} is not a prime number".format(number))
      break
  else:
    print("\n {} is a prime number".format(number))
