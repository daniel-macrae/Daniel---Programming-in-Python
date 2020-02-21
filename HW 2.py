#HOMEWORK 2: STUDENT SCORES

#PRINTING STUDENT NAMES AND SCORES

names = ['Nils','Mark','Marilyn','Mariam','Albert']
homework = [2,10,4,6,7]
exam = [20,55,33,60,0] 
project = [12,30,21,24,0] #added zeroes because numbers were missing for Albert

def print_names(names, homework, exam, project):
    print("Name:","Homework:","Exam:","Project:")
    for m,n,o,p in zip(names, homework, exam, project):
        print(m,n,o,p)


print("Original names and scores:")
print_names(names, homework, exam, project)





#CALCULATING TOTAL SCORE AND FAIL/PASS RESULT

def print_results(names,homework,exam,project,total,result):
    print("Name:","Homework:","Exam:","Project:","Total:","Result:")
    total=[x+y+z for x,y,z in zip(homework,exam,project)]
    result=[]
    for i in total:
        if i>=50: 
            result.append("Pass")
        else:
            result.append("Fail")
    for m,n,o,p,q,r in zip(names, homework, exam, project,total,result):
        print(m,n,o,p,q,r)

print("Original students results:")
print_results(names,homework,exam,project,total,result)

    


#ADDING NEW STUDENTS

def add_student(names,homework,exam,project):
    names.append(str(input("Enter student name")))
    homework.append(int(input("Enter homework score")))
    exam.append(int(input("Enter exam score")))
    project.append(int(input("Enter project score")))

add_student(names,homework,exam,project)
add_student(names,homework,exam,project)
add_student(names,homework,exam,project)

print(" ")
print("New names and scores:")
print_names(names, homework, exam, project)

print(" ")
print("New results:")
print_results(names,homework,exam,project,total,result)





