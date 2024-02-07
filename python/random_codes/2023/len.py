
def main():
	password = input("Enter your password : ")
	password_length = len(password)
	#len() gets the length of a string

	check = ("{} characters : Perfect !".format(password_length), "Only {} ? Not enough !".format(password_length))[password_length <= 8]
	print(check)


if __name__ == '__main__':
	main()
