import statistics
from statistics import mean as mn #in order to not write module.func
from random import shuffle aa sfl

def main():
	notes1 = [
		10, 12, 14,
		16, 18, 20,
	]

	mean1 = statistics.mean(notes1)
	print("Note1 {} , mean = {}".format(notes1, mean1))

	notes2 = [
		20, 19, 14,
		18, 16, 15,
	]

	mean2 = mn(notes2)
	print("Notes2 {}, mean {}".format(notes2, mean2))
	#mix = sfl(notes2)
	#print("Notes2 mixed {}".format(mix))

if __name__ == '__main__':
	main()
