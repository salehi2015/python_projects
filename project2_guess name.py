import random

names = ['ali','fatemeh','sara','dara','abas','amir','nika']

selected_name = random.choice(names).lower()

guess_count = len(selected_name)
guess_list = ["_"]*guess_count
current_guess = " ".join(guess_list)
print(current_guess)

while guess_count > 0 :
    guessed_char = input("enter a char : ")
    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guess_list:
                print("this charactor already exist , guess new")
            else:
                for idx , char in enumerate(selected_name):
                    if char == guessed_char:
                        guess_list[idx] = guessed_char
                current_guess = " ".join(guess_list)
                print(current_guess)
                if "_" not in guess_list:
                    print("you won")
                    break


        else:
            guess_count -= 1
            print(f"wrong! ,remained guess : {guess_count}")

    else:
        print("please enter valid charactor")