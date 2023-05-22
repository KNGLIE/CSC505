import jsonlines

database = {}


def menu():
    choice = input('0. To exit:\n1. To create login:\n2. To login:\n')
    if choice == '1':
        create_login()
    elif choice == '2':
        login()
    else:
        print('Thank you, have a good day.')


def create_login():
    username = input("Username:\n")
    with jsonlines.open('atm.jsonl', 'r') as reader:
        # print(reader)
        # reader.read()
        new_user = True
        for user in reader.iter(type=dict, skip_invalid=True):

            if username in user.keys():
                new_user = False
                print('That username has already been used, please select another.\n')
                create_login()
        # print(new_user)
        if new_user:
            passcode = input("4 Digit passcode:\n")
            user_balance = int(input('How much money are you depositing?\n'))
            # if username not in database:
            database[username] = passcode, user_balance
            with jsonlines.open('atm.jsonl', mode='a') as add:
                add.write(database)


def login():
    incorrect = 0
    user_lookup = input('Username:\n')

    with jsonlines.open('atm.jsonl', 'r') as reader:
        for obj in reader:
            while user_lookup in obj:
                user_pw = input('Password:\n')
                for i, n in obj.items():
                    if n[0] != user_pw:
                        incorrect += 1
                        while incorrect < 4:
                            print('That was the incorrect password, try again.\n')
                            user_pw = input('Password:\n')
                            if user_pw == n[0]:
                                continue
                            else:
                                break
                        menu()
                    elif n[0] == user_pw:
                        if n[-1] == 0:
                            pass
                        elif n[-1] >= 0:
                            de_wi_choice = input('1. View balance\n2. Withdrawal\n3. Deposit\n0. Exit\n')
                            if de_wi_choice == '1':
                                print(n[-1])
                            elif de_wi_choice == '2':
                                withdrawal = int(input('Amount to withdrawal\n'))
                                if withdrawal > n[-1]:
                                    print('You do not have enough funds to withdrawal\nAvailable funds: ', n[-1])
                                elif withdrawal < n[-1]:
                                    n[-1] = n[-1] - withdrawal
                                    print('New balance: ', n[-1])
                                else:
                                    n[-1] = n[-1] - withdrawal
                                    print('You have removed all funds, your account will now be closed')
                                    del obj
                            elif de_wi_choice == '3':
                                deposit = int(input('How much would you like to deposit?\n'))
                                deposit = deposit + n[-1]
                                print('New balance: ', deposit)

                        # def withdrawal():

                        else:
                            print(n[-1])
                            break
                break
menu()
