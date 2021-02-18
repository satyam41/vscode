import pickle
file = open("emp.dat","ab")
emp = {}
ans = 'y'
while ans == 'y':
    emp_id = int(input("Enter emp id: "))
    emp_name = input("Enter name: ")
    emp_sal = float(input("Enter salary: "))
    emp["Emp_id"] = emp_id
    emp["Emp_name"] = emp_name
    emp["Emp_salary"] = emp_sal
    writer = pickle.dump(emp,file)
    ans = input("Want to add more records? (y/n): ")
    if ans == 'n':
        print("Thank You")
        break
file.close()


import pickle
def countSal():
    file = open("emp.dat","rb")
    try:
        while True:
            data = pickle.load(file)
            if emp_sal > 20000:
                print(data)
    except:
        file.close()
countSal()