user_name=input('What is your name?')
user_score=input("What was you score on the test?")

if int(user_score) < 0 or int(user_score) > 100:
    print("Invalid Score")
else:
    if int(user_score) >= 90:
        grade = 'A'
    elif int(user_score) >= 80:
        grade = 'B'
    elif int(user_score) >= 70:
        grade = 'C'
    elif int(user_score) >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(user_name, 'earned a', grade + '.')
