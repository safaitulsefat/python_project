
student_record={}

def add_student():
  Student_ID = input("Enter student id: ")
  First_Name = input("Enter first Name: ")
  Last_Name =  input('ENTER LAST NAME: ')
  Date_Of_Birth = input('Enter date of birth: ')
  Course_Enrolled = input('Enter courses enrolled (comma-separated): ').split(',')

  student = {
       'Student_ID' :  Student_ID,
       'First_Name' : First_Name,
       'Last_Name' : Last_Name,
       'Date_Of_Birth': Date_Of_Birth,
       'Course_Enrolled': Course_Enrolled
  }
  student_record[Student_ID] = student
  print(f'student {Student_ID} add succsessfully')

def searching_student():
  search = input("enter student id: ")
  for key,value in student_record.items():
    if search == key:
      print(value)
    else:
      print('student id cannot find')

def delete_student():
  id = input("enter student id: ")
  if id in student_record:
      del student_record[id]
      print(f"delete {id} successfully")
  else:
    print('invalid student id')

def edit_student():
  id = input("enter student id: ")
  for key,value in student_record.items():
     if id == key:
      First_Name = input("Enter first Name: ")
      Last_Name =  input('ENTER LAST NAME: ')
      Date_Of_Birth = input('Enter date of birth: ')
      Course_Enrolled = input('Enter courses enrolled (comma-separated): ').split(',')
      student = {
       'Student_ID' :  key,
       'First_Name' : First_Name,
       'Last_Name' : Last_Name,
       'Date_Of_Birth': Date_Of_Birth,
       'Course_Enrolled': Course_Enrolled
      }
      student_record[key]=student
'''def edit_student():
  id = input('enter the student id: ')

  for key,value in student_record.items():
    field = input('enter which field you edit:').capitalize()
    if field in value:
      change = input("enter ")
      value[field]=change'''
def save_student_data(filename, student_records):
    with open(filename, 'w') as file:
        for student_id, student in student_records.items():
            file.write(f"Student_ID: {student_id}\n")
            file.write(f"First_Name: {student['First_Name']}\n")
            file.write(f"Last_Name: {student['Last_Name']}\n")
            file.write(f"Date_Of_Birth: {student['Date_Of_Birth']}\n")
            file.write(f"Course_Enrolled: {', '.join(student['Course_Enrolled'])}\n")
            file.write('\n')

# Call this function to save student data to a file
  


while True:
  print('select option: ')
  print('---------------------------------------')
  print('1.add student in database')
  print('2.searching student')
  print('3.dispaly all student ')
  print('4.delete student id')
  print('5.edit student')
  print('q stop this program')
  print('--------------------------------------')

  t = input("enter option: ")
  if t=='1':
    add_student()
  elif t=='2':
    searching_student()
  elif t=='3':
    print(student_record)
  elif t=='4':
    delete_student()
  elif t=='5':
    edit_student()
  elif t=='6':
    save_student_data('student_data.txt', student_record)
  elif t=='q':
    break
  else:
    print('this option not: ')

