from myarray import Array2D

filename = "examgrades.txt"

gradeFile = open( filename, "r" )

numStudents = int( gradeFile.readline() )
numExams = int( gradeFile.readline() )

examGrades = Array2D( numStudents, numExams )

# Extract the grades from the remaining lines
i = 0
for stu in gradeFile:
    grades = stu.split()
    for j in range( numExams ):
        examGrades[i, j] = int( grades[j] )
    i += 1

gradeFile.close()

# Compute the avg exam grade
for i in range( numStudents ):
    total = 0
    for j in range( numExams ):
        total += examGrades[i,j]

    examAvg = total / numExams
    print "%2d: %6.2f" % (i+1, examAvg)
