# me a program that prompts users to enter three numbers and returns the largest number
#a program that users enter a year and checks whether its a leap year or not


year=int(input("Enter your year"))
if year % 4==0:
    print("Its a leap year")
elif year % 100==0:
    print("Its not a leap year")
elif year % 400==0:
    print("Its a leap year")
else:
    print("Its not a leap year")