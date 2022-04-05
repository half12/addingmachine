while True:
    try:
        num1 = int(input('what is the first number you want to add?'))
        num2 = int(input('what is the second number you want to add?'))
        sum = num1+num2
        print('The sum of your two numbers is:', sum)
        break
    except:
        print('u gotta input an integer buddy')