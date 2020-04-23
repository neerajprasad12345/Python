#program to display student's marks from records
student_name=(input("Enter The name:"))
marks={'Ayush':50 , 'Abhi':60, 'Pratik':99}
#
for student in marks:
    if student==student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found')
    