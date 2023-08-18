import os
desktop_path = os.path.expanduser("~/Desktop")
file_path = os.path.join(desktop_path,"student.txt")

def main():
    while True:
        menu()
        choice = int(input("Please choose:"))
        if choice == 0:
            answer = input("Are you sure you want to exit the system? y/n")
            if answer == 'y' or answer == 'Y':
                print("Thank you for using!!!")
                break  # Exit the system
            else:
                continue
        elif choice== 1:
            insert()
        elif choice== 2:
            search()
        elif choice== 3:
            delete()   
        elif choice== 4:
            modify()
        elif choice== 5:
            sort_records()
        elif choice== 6:
            total()
        elif choice== 7:
            show()    

def menu():
    print("=============================== Student Information Management System ===============================") 
    print("--------------------------------------- Function Menu -----------------------------------") 
    print("\t\t\t1. Enter student information") 
    print("\t\t\t2. Search for student information") 
    print("\t\t\t3. Delete student information") 
    print("\t\t\t4. Modify student information") 
    print("\t\t\t5. Sort") 
    print("\t\t\t6. Total number of students") 
    print("\t\t\t7. Display all student information") 
    print("\t\t\t0. Exit system") 
    print("---------------------------------------------------------------------------------------") 

def insert():
    student_list = []
    while True:
        Id = input("Please enter ID (e.g. 1001):")
        if not Id: 
            break
        Name = input("Please enter name:")
        if not Name:
            break
        try: 
            English = int(input("Please enter English grade:"))
            Python = int(input("Please enter Python grade:")) 
            Java = int(input("Please enter Java grade:")) 
        except:
            print("Invalid input, not an integer type, please re-enter!")
            continue
        # Save the entered student information in a dictionary
        student = {"Id":Id, "Name":Name,"English":English,"Python":Python,"Java":Java}     
        student_list.append(student)
        answer = input("Do you want to continue adding? y/n\n")
        if answer == "y":
           continue
        else:
            break
       # Call save function
    save(student_list)
    print("Student information saved successfully")

def save(lst):  
    try:
        stu_txt = open(file_path,'a',encoding="utf-8")    
    except:
        stu_txt = open(file_path,'w',encoding="utf-8") 
    for item in lst:
        stu_txt.write(str(item) + "\n")        
    stu_txt.close()    

def search():
    student_query = []
    while True:
        id = ""
        name = ""
        if os.path.exists(file_path):
            mode = input("Search by ID please enter 1, search by name please enter 2:")
            if mode == "1":
                id = input("Please enter student ID:")
            elif mode == "2":
                name = input("Please enter student name:")
            else:
                print("Your input is incorrect, please re-enter")    
                search()
            with open(file_path, "r", encoding="utf-8") as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != "":
                        if d["Id"] == id:
                            student_query.append(d)   
                    elif name != "":
                        if d["Name"] == name:
                            student_query.append(d)
            show_student(student_query)                        
            student_query.clear()
            answer = input("Do you want to continue the search? y/n\n")
            if answer == "y":
                continue
            else:
                break
        else:
            print("No student information saved yet")
            return 

def show_student(lst):
    if len(lst) == 0:
        print("No student information found, no data to display!!!")        
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format("ID", "Name", "English Grade", "Python Grade", "Java Grade", "Total Grade"))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get("Id"),
                                item.get("Name"),
                                item.get("English"),
                                item.get("Python"),
                                item.get("Java"),
                                int(item.get("English")) + int(item.get("Python")) + int(item.get("Java"))
                                ))
        
def delete():
    while True:
        student_Id = input("Please enter the ID of the student you want to delete: ")
        if student_Id != "":
            if os.path.exists(file_path):
                with open(file_path, 'r',encoding="utf-8") as file:
                    student_old = file.readlines()
            else:        
                student_old = []
            flag = False  # Flag to check if deletion happened
            if student_old:
                with open(file_path, 'w', encoding="utf-8") as wfile:    
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d["Id"] != student_Id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                if flag:
                    print(f"Student with ID {student_Id} has been deleted")
                else:
                    print(f"Cannot find student with ID {student_Id}")      
            else:
                print("No student information available")     
                break
            show()
            answer = input("Do you want to continue deleting? y/n\n")
            if answer == "y":
                continue
            else:
                break 

def modify():
    show()
    if os.path.exists(file_path):
        with open(file_path, 'r',encoding="utf-8") as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_Id = input("Please enter the ID of the student you want to modify:")
    with open(file_path, 'w', encoding="utf-8") as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d["Id"] == student_Id:
                print("Found student information, you can now modify it!")         
                while True:
                    try:
                        d["Name"] = input("Please enter name:")
                        d["English"] = input("Please enter English grade:")
                        d["Python"] = input("Please enter Python grade:")
                        d["Java"] = input("Please enter Java grade:")
                    except:
                        print("Your input is incorrect, please re-enter!!!")
                    else:
                        break    
                wfile.write(str(d) + "\n")  
                print("Modification successful")
            else:
                wfile.write(str(d) + "\n")          
        answer = input("Do you want to continue modifying other student information? y/n\n")                 
        if answer == "y":
            modify()

def sort_records():
    show()
    if os.path.exists(file_path):
        with open(file_path,"r", encoding="utf-8") as rfile:
            student_list = rfile.readlines()
        student_new = []    
        for student in student_list:
            d = dict(eval(student))
            student_new.append(d)
    else:
        return
    ase_or_desc = input('Please choose (0. Ascending 1. Descending):')
    if ase_or_desc == '0':
        ase_or_desc_bool = False
    elif ase_or_desc == '1':
        ase_or_desc_bool = True
    else:
        print('Your input is incorrect, please re-enter')
        sort_records()        
    mode = input('Please choose the sorting method (1. Sort by English grade 2. Sort by Python grade 3. Sort by Java grade 0. Sort by total grade)')
    if mode == '1':
        student_new.sort(key = lambda x: int(x['English']), reverse = ase_or_desc_bool)
    elif mode == '2':
        student_new.sort(key = lambda x: int(x['Python']), reverse = ase_or_desc_bool)
    elif mode == '3':
        student_new.sort(key = lambda x: int(x['Java']), reverse = ase_or_desc_bool)
    elif mode == '0':
        student_new.sort(key = lambda x: int(x['Python']) + int(x['Java']) + int(x['English']), reverse = ase_or_desc_bool)
    else:
        print("Your input is incorrect, please re-enter!!!")    
        sort_records()
    show_student(student_new)

def total():
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding= 'utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f"There are a total of {len(students)} students")
            else:
                print('No student information has been entered yet')    
    else:
        print('No student information saved yet')            

def show():
    student_list = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            for item in student:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)    

if __name__ == "__main__":
    main()
