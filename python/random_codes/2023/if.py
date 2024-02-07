
def main():
	anarana = input("Your name : ")
	if anarana != "Hatix" or anarana != "Ntsoa":
		#here "and" acts like "&&" in shell
		# "or" like "||"
		main() #recursive call
	else:
		print("Hello {}".format(anarana))
		#here we have a nice thing
		#{} acts like a format
		#.format() will replace with its value
		#whatever the type is


if __name__ == '__main__':
	main()
