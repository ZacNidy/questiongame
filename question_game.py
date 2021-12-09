
name = input('Name: ')
play = input('Welcome {}, would you like to play? (y,n): '.format(name)).lower()

score = 0

if play != 'y'.lower():
    print('Quitting...')
    quit()

print('Okay lets get it started')

while True:
    user_answer = input('What is the capital of the United States? ').lower()
    if user_answer == 'united states':
        print('That is correct!')
        score += 1
    else:
        print('That is not correct')
        restart = input('Would you like to restart? (y,n): ').lower()
        if restart != 'y'.lower():
            print('Quitting...')
            break
        else:
            continue
