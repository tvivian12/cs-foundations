user_name = input('What is your name?')
user_score = input("What score did you get on the test? ")

user_score = int(user_score)

if user_score < 0 or user_score > 100:
    print("Invalid score. Please enter a score between 0 and 100.") 
else: 
    if user_score >= 90:
        grade = 'A'
    elif user_score >= 80:
        grade = 'B'
    elif user_score >= 70:
        grade = 'C'
    elif user_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(user_name, 'earned a', grade + '.')
    
          