import random as rand
data_name=["admin"]
data_id=[0]
data_age=["Unavailable"]
data_password=[""]
data_passphrase=["waterballoon"]
sample_passphrase=["waterballoon", "purringkitten", "barkingdog", "warmday", "winterhusky", "dev's easteregg", "goldengoose", "linuxpenguin", "windows", "macaroni", "smartdroid", "apple", "copyparrot", "dancingpeacock", "githubthebest", "asimplepassphrase", "thedevgreetsyou", "spices-herbs"]
while True:
    name=''
    userid=-1
    age=''
    password=''
    confirmpassword=' '
    passphrase=''
    decide=''
    cont=1
    randomnum=0
    opervalopt=['a', 'e', 'al', 'c']
    editvalopt=['n', 'a', 'p', 'pa']
    while decide not in opervalopt:
        decide=input("(A): To add a new entry to the database, (C): To check an existing entry, (E): To edit an existing entry, (AL): Admin Login: ")
        decide=decide.lower()
        if decide not in opervalopt:
            print("Please select a valid option")
    if decide=='a':
        name=input("Please enter your full name: ")
        age=input("Please enter your age: ")
        while password!=confirmpassword or len(password)<=3:
            password=input("Please create a password ('It should be longer than 3 characters'): ")
            confirmpassword=input("Please confirm your password: ")
            if password!=confirmpassword:
                print("The given passwords don't match up, please re-enter your password")
            if len(password)<=3:
                print("The given password is too small")
        print("Please note down this password as this will be used to verify your identity")
        randomnum=rand.randrange(0, len(sample_passphrase)-1, 1)
        passphrase=sample_passphrase[randomnum]
        data_id.append(len(data_id))
        print("Your userid is", len(data_id)-1, ". Please note down this id as this will be used to access your records.")
        print("Please note down this passphrase:", passphrase, ". This passphrase will be used to login incase you forget your password.")
        data_passphrase.append(passphrase)
        data_password.append(password)
        data_name.append(name)
        data_age.append(age)
    elif decide=='c':
        while userid<0 or userid>len(data_id)-1:
            userid=int(input("Enter your user id: "))
            if userid<0 or userid>len(data_id)-1:
                print("Please enter a valid userid")
            while password!=data_password[userid]:
                password=input("Please enter your password: ")
                if password!=data_password[userid]:
                    print("The password is incorrect, please try again")
            print("You have successfully logged into your account")
            print("Your record details are listed below:")
            print("Full name:", data_name[userid])
            print("Age:", data_age[userid])
            print("Password:", data_password[userid])
            print("Passphrase:", data_passphrase[userid])
            print("End of Record")
    elif decide=='e':
        while userid<0 or userid>len(data_id)-1:
            userid=int(input("Enter your user id: "))
            if userid<0 or userid>len(data_id)-1:
                print("Please enter a valid userid")
            while password!=data_password[userid]:
                password=input("Please enter your password: ")
                if password!=data_password[userid]:
                    print("The password is incorrect, please try again")
            print("You have successfully logged into your account")
            print("Your record details are listed below:")
            print("Full name:", data_name[userid])
            print("Age:", data_age[userid])
            print("Password:", data_password[userid])
            print("Passphrase:", data_passphrase[userid])
            while decide not in editvalopt:
                decide=input("(N): To edit your name, (A): To edit your age, (P): To change your password, (PA): To generate a new passphrase: ")
                decide=decide.lower()
                if decide not in editvalopt:
                    print("Please select a valid option")
            if decide=='n':
                name=input("Please enter your full name: ")
                data_name[userid]=name
            if decide=='a':
                age=input("Please enter your age: ")
                data_age[userid]=age
            if decide=='p':
                while password!=confirmpassword or len(password)<=3:
                    password=input("Please create a password ('It should be longer than 3 characters'): ")
                    confirmpassword=input("Please confirm your password: ")
                    if password!=confirmpassword:
                        print("The given passwords don't match up, please re-enter your password")
                    if len(password)<=3:
                        print("The given password is too small")
                print("Please note down this password as this will be used to verify your identity")
            if decide=='pa':
                randomnum=rand.randrange(0, len(sample_passphrase)-1, 1)
                passphrase=sample_passphrase[randomnum]
                data_passphrase[userid]=passphrasea
