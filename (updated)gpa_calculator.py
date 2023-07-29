subjects = ['Bangla', 'English', 'Mathematics', 'Science']
marks_list = []
# input taking marks per subject
for subject in subjects:
    x = int(input(f'{subject}: '))
    marks_list.append(x)
# claculating average
total = 0
for mark in marks_list:
     total += mark
avg = total/4
# determining the result
if avg <= 40 and avg >= 0:
     print('Result: GPA-0.00 (F) ')
elif avg <=60 and avg >= 41:
     print('Result: GPA-1.00 (D) ')
elif avg <= 70 and avg >= 61:
     print('Result: GPA-2.00 (C) ')
elif avg <= 80 and avg >=71:
     print('Result: GPA-3.00 (B) ')
elif avg <= 90 and avg >= 81:
     print('Result: GPA-4.00 (A) ')
elif avg <= 100 and avg >= 81:
     print('Result: GPA-5.00 (A+) ')
else:
     print('Something went wrong')