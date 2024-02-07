
def main():
	list = ["bengy", "Hatix", "Goat"]
	print(list) #display the whole list
	print(list[0]) #display the first element
	print(list[2]) #display the third of knowm element
	print(list[len(list) - 1]) #display the last element
	#here the len gets the length of the array list[]
	#so here we have n elements
	#but since we count position from 0, we substract 1 to this value
	#otherwise we get a list index out of range error

	list[0] = "Hatix_Ntsoa"
	print("Updated list {}, bengy changes to {}".format(list, list[0])) #update list value

	list.insert(2, "intrus") #here to insert an element in n position
	print("Updated list again, {}, {} inserted !".format(list, list[2]))

	list[2:4] = ["a", "b"] #update multiple value, from n to m
	print("Multiple change {}".format(list))
	#if len[new_values] < m:
	#	len--

	list.append("end") #here to insert at EOF
	print("Single EOF added {}".format(list))

	list.extend(["x", "y"]) #insert multiple EOF
	print("Multiple EOF added {}".format(list))

	del list[1] #removing by position with del
	print("Removed a value  {}".format(list))

	list.pop(1) #removing by position with pop()
	print("Removed again {}".format(list))

	list.remove("b") #removing by name
	print("Removed {}".format(list))

	#list.clear() or del list[:] to remove all

if __name__ == '__main__':
	main()
