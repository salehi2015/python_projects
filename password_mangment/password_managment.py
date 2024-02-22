from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open(".\mykey.key" , "wb") as f :
#         f.write(key)
# write_key()

def load_key():
    with open(".\mykey.key" , "rb") as f:
        return f.read()

key = load_key()
fernet = Fernet(key)

def add_pass(username , password):
    with open(".\password.txt" , "a") as f :
        encrypt_pass = fernet.encrypt(password.encode()).decode()
        f.write(f"{username} | {encrypt_pass}\n")
    print("added")

def view_pass():
    with open(".\password.txt" , "r") as f :
        for item in f:
            item = item.rstrip()
            username , encrypt_pass = item.split("|")
            password = fernet.decrypt(encrypt_pass.encode()).decode()
            print(f"username : {username} | password : {password}")



while True:
    user_input = input('enter your mode("a" for add , "v" for view , "q" for quit) : ')

    if user_input == "a":
        username = input("please enter username : ")
        password = input("please enter username : ")
        add_pass(username , password)


    elif user_input == "v":
        print("your password are as follows :")
        view_pass()

    elif user_input == "q" :
        break
    else:
        print("your mode is wrong")