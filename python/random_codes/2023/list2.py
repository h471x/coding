

def main():
	login = input("Login format => mail user password : ").split(" ")
	#this will remove the ("x") for the input and add the
	#remaining object to a list array
	print(login)
	print("Hello {}".format(login[1]))


if __name__ == '__main__':
	main()
