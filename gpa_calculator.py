run = True
while run==True:
    try:
        number_dict = {}
        print('Insert Marks-->')
        total_point = 0
        for value in range(4):
            if value==0:
                bangla_marks = int(input("Bangla: "))
                number_dict['Bangla'] = [bangla_marks]
            elif value==1:
                english_marks = int(input("English: "))
                number_dict['English'] = [english_marks]
            elif value==2:
                mathematics_marks = int(input("Mathematics: "))
                number_dict['Math'] = [mathematics_marks]
            elif value==3:
                science_marks = int(input("Science: "))
                number_dict['Science'] = [science_marks]
            else:
                print('something went wrong')
        # determines the grade point per subject
        for value in number_dict.values():
            if value[0] <= 40 and value[0] >= 0:
                value.append('F')
                value.append(0.0)
            elif value[0] <=60 and value[0] >= 41:
                value.append('D')
                value.append(1.0)
            elif value[0] <= 70 and value[0] >= 61:
                value.append('C')
                value.append(2.0)
            elif value[0] <= 80 and value[0] >=71:
                value.append('B')
                value.append(3.0)
            elif value[0] <= 90 and value[0] >= 81:
                value.append('A')
                value.append(4.0)
            elif value[0] <= 100 and value[0] >= 81:
                value.append('A+')
                value.append(5.0)
            else:
                value.append('Null')
                value.append('Null')

        print('\nSubject Name | Obtained Marks | Letter GPA | Grade Point')
        for k,v in number_dict.items():
            print(f'{k.upper()}\t\t {v[0]}\t\t {v[1]}\t\t {v[2]}')
            total_point += v[2]
        print(f'Grade point avg(GPA): {total_point/4}')
        print('\n')
        x = input("Try Again??(y/n): ")
        if x.lower()=='n':
            run = False
    except ValueError:
        print('"Hello?? Marks contains only numbers no laters!! Try Again."')