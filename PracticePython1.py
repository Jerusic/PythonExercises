name = input("Enter your name: " )
age = int(input("How old will you turn at the end of 2017? "))
centennial = 2017 + 100 - age
repeat = int(input("Repeat the message how many times? "))

def repeatMessage(n):
    assert repeat > 0 and isinstance(repeat, int), "Please enter an integer > 0."
    for i in range(n):
        print("Hello {}. You'll turn 100 in the year {}.".format(name,centennial))

repeatMessage(repeat)
