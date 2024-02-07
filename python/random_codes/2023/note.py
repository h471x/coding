
def main():
	note1 = int(input("First note : "))
	note2 = int(input("Second note : "))
	note3 = int(input("Third note : "))
	#here the function input only take string so we have
	# to convert those notes to integers
	print("Mean = " + str((note1 + note2 + note3)/3))


if __name__ == '__main__':
	main()


