USERS = {
    "admin": "123",
}

def validate_login(username, password):
    return username in USERS and USERS[username] == password

def show_success():
    print("Login berhasil")

def show_error():
    print("Login gagal")

username_input = input("username: ")
password_input = input("password: ")

if validate_login(username_input, password_input):
    show_success()
else:
    show_error()