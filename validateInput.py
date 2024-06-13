
while True:
    try:
        print('Enter your Age:')
        age = input()
        if age.isdecimal():
            break
        else:
            print('Invalid input. Please enter a valid age.')
    except:
        print('Invalid input. Please enter a valid age.')
        
