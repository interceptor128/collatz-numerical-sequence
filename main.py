# Collatz Sequence
def collatz(number):
    if number == 1:
        return 0

    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(number * 3 + 1)


number = int(input())
print(number)
while number != 1:
    number = collatz(number)
    print(number)
