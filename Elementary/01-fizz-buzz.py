def checkio(number):
    ans = str(number)
    if number % 3 == 0:
        ans = "Fizz"
    if number % 5 == 0:
        ans = "Buzz"
    if number % 3 == 0 and number % 5 == 0:
        ans = "Fizz Buzz"
    return ans
print(checkio(int(input())))