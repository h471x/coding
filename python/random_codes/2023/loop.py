def main():
  for i in range(1, 6): # ≈ for(i=1;i<5;i++){}
    print("N°", i)
  print("\n")

  greet = ["morning", "afternoon", "evening"]
  days = ["mon", "tues", "wednes", "thurs", "fri", "satur", "sun"]
  for day in greet:
    print("Good ", day)
	# int tab[nbMax];
	# ≈ for(int i  = 0; i < nbMax; i++){
		#printf("%d", &tab[i]);
	#}
  print("\n")
  for prefix in days:
    print("{}day".format(prefix))
  print("\n")
  numbers = ["1", "one", "2", "two", "3", "three"]
  digits = ["1", "2", "3"]

  for num in numbers:
    if num in digits:
      print("{} is not a letter".format(num))
      continue
	  # this will continue the first loop
	  # use break to break all the loops
	print("{}".format(num))

if __name__ == '__main__':
	main()
