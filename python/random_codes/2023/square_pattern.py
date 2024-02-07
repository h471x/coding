
def square_pattern(n):
  for i in range(0, n):
    for j in range(0, n):
      print("* ")
  print("\r")

dim = int(input("Enter the xender pattern dimension : "))
print("\n")
square_pattern(dim-1)
