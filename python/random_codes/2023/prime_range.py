start = int(input("Start of prime range: "))
stop = int(input("End of prime range: "))
primes_per_line = int(input("Number of primes per line: "))

prime_numbers = []
count = 0

for number in range(start, stop + 1):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)
            count += 1

            if count % primes_per_line == 0:
                print(number)
            else:
                print(number, end=", ")

print("\nTotal prime numbers found:", count)

