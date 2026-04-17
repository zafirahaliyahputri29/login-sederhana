def f(u, p):
    if u == "admin" and p == "123":
        print("Login berhasil")
    else:
        print("Login gagal")

user - input("Username: ")
password - input("Password: ")

f(user, pw)