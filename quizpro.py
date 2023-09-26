print('...HEY WELCOME TO QUIZ GAME...')
now = input('have u want to play? ')
score = 0
if now=='yes':
    print('--lets start to play this game--')
    question = '1.what the mean of cpu'
    print(question)
    answer = input('write the ans..')
    if answer=='central processing unit':
        print('congratulations')
        print('correct!.')
        score +=1
    else:
        print('extreamly sorry')
        print('thats incorrect!.')
    question = '2.what the mean of GPU'
    print(question)
    answer = input('write the ans..')
    if answer == 'graphics processing unit':
        print('congratulations')
        print('correct!.')
        score +=1
    else:
        print('extreamly sorry')
        print('thats incorrect!.')
    question = '3.what the mean of WWW'
    print(question)
    answer = input('write the ans..')
    if answer =='world wide web':
        print('congratulations')
        print('correct!.')
        score +=1
    else:
        print('extreamly sorry')
        print('thats incorrect!.')
    question = '4.what the mean of ram'
    print(question)
    answer = input('write the ans..')
    if answer =='random access memory':
        print('congratulations')
        print('correct!.')
        score +=1
    else:
        print('extreamly sorry')
        print('thats incorrect!.')
    print(f'you are successfully completed the quiz')
    print(f'congats.!.you have won {score} score...')

else:
    print('...ok fine no problem...')
    print('try next time')
    print('*** *** ***')

