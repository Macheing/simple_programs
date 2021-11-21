def student_score():
    score = input("Enter student score: ")
    #print(score)
    try:
        # convert score float
        score = float(score)
    except:
        # can't convert letter to a float
        score = -1
        print("Exception error:", 'please enter score as a number')
        return score

    grade = ''
    if score <= 100 and score >= 90:
        grade = 'A'
        print(grade)
    elif score < 90 and score >= 80:
        grade = 'B'
        print(grade)
    elif score < 80 and score >= 70:
        grade = 'C'
        print(grade)
    elif score < 70 and score >= 60:
        grade = 'D'
        print(grade)          
    elif score < 60 and score >=0:
        grade = 'F'
        print(grade)  
    else:
        print(str(score), "is not in specified score range!")
        return -1
    return grade
    
student_score()