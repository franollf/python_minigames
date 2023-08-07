print('Welcome to the South American Country Quiz!')
print('The goal is to choose the correct country that belongs to South America!')
quiz = input('Do you want to play? ')
score = 0
if quiz.lower() != "yes":
    quit()

print('Alright Lets get started then!')
print ('Which Country Resides in South America')
answer = input('Argentina or Cuba ')
if answer.lower() == 'argentina':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Bolivia or Spain ')
if answer.lower() == 'bolivia':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Mexico or Brazil ')
if answer.lower() == 'brazil':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Colombia or Guatemala ')
if answer.lower() == 'colombia':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Peru or France ')
if answer.lower() == 'peru':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Ecuador or Netherlands ')
if answer.lower() == 'ecuador':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('United Arab Emirates or Venezuela ')
if answer.lower() == 'venezuela':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Guyana or United States ')
if answer.lower() == 'guyana':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Suriname or Andorra ')
if answer.lower() == 'suriname':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Paraguay and Malta ')
if answer.lower() == 'paraguay':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Chile or Liechtenstein ')
if answer.lower() == 'chile':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('Uruguay or Maldives ')
if answer.lower() == 'uruguay':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('Thanks for playing! You got ' + str(score) + ' correct!')
print('Which is ' + str(score/12) + ' %')