import db

text = "!"
while text != "":
    command = input("Введите что будете проверять(reg - для регистрации, enter - для входа): ")
    if command == "reg":
        phone = input("Введите телефон: ")
        email = input("Введите почту: ")
        password = input("Введите пароль: ")
        print(db.reg(phone, email, password))
        db.print_db()
    elif command == "enter":
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        print(db.is_reg(login, password))
    elif command == "print":
        db.print_db()
    else:
        break
