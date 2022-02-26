import re

store = []


def register():
    email_pattern = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]+\w+[.]\w{2,3}$'
    email_username = input("Create mail id: ")
    while True:
        if not re.search(email_pattern, email_username):
            print("This is not a proper mail id, Please create a valid mail!")
            register()
            break
        else:
            print("Mail id created successfully")
            store.append(email_username)
            break
    while True:
        password_input = input("create a password :")
        flag = 0
        if not len(password_input) in range(5, 17):
            flag = -1
            break
        elif not re.search('[a-z]', password_input):
            flag = -1
            break
        elif not re.search('[A-Z]', password_input):
            flag = -1
            break
        elif not re.search('[0-9]', password_input):
            flag = -1
            break
        elif not re.search('[\W_]', password_input):
            flag = -1
            break
        elif re.search('\s', password_input):
            flag = -1
            break
        else:
            print("password created successfully")
            store.append(password_input)
            file = open("db.txt", "a")
            file.write(email_username + ',' + password_input + '\n')
            break
    if flag == -1:
        print("""password must be in the following format:
                password length must be between 5 to 16,
                Must have minimum one special character,
                one digit,
                one uppercase,
                one lowercase character""")
        register()


def login():
    file2 = open('db.txt', 'r')
    db = file2.readlines()
    file2.close()
    db_l = []
    log_id = input("Enter Login id:")
    password_login = input("Enter password:")
    for i in db:
        db_l.append(i.strip())
    print(db_l)
    for j in db_l:
        n, m = j.split(",")
        if log_id == n and password_login == m:
            print("Logged in Succesfully", n, m)
            break
    else:
        print(
            "username and Password doesn't match" + '\n' + "If you haven't register, Please register and then login" + "\n" +
            "If you have forgot password, please reset password" + '\n')
        choice()


def forgot_password():
    db = open("db.txt", "r")
    read_db = db.readlines()
    to_check_id = input("Please enter your mail id:")
    f = []
    for i in read_db:
        f.append(i.strip())
    for j in f:
        a, b = j.split(',')
        if to_check_id == a:
            print("Your password is :", b)
            break
    else:
        print("user id is not available in the database , Please register ")
        register()


def choice():
    user_choice = input("""Enter 1 for registration
Enter 2 for login
Enter 3 for forgot password
PLEASE ENTER YOUR CHOICE:""")
    while True:
        if user_choice == "1":
            register()
            break
        elif user_choice == "2":
            login()
            break
        elif user_choice == "3":
            forgot_password()
            break
        else:
            print("Enter right choice" + '\n')
            choice()
            break


choice()
