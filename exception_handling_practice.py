#With this code we want to execute exception handling to avoid incorrect user input of a 0 or a string variable
a = 1

try: #Code to execute
    b = int(input("Enter a number to divide a:"))
    a = a/b
except ZeroDivisionError: #Execute code if there is a ZeroDivisionError
    print('You cannot divide by 0')
except ValueError: #Execute code if there is a ValueError
    print('Please provide a number')
except: #execute code if there is any exception
    print('Error')
else:
    print('a=', a)
finally:
    print('Completed')
