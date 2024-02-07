
def main():
	name = input("Name : ")
	test = ("Hello {}".format(name), "Nope")[name != "Hatix"]
	#(false, true)[condition]
	print(test)

if __name__ == '__main__':
	main()
