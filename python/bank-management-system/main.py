import random
import json
import string
from pathlib import Path

class Bank:
    database = Path(__file__).parent / "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("NO SUCH FILE EXISTS!")

    except Exception as err:
        print(f"AN EXCEPTION OCCURRED AS {err}")

    @staticmethod
    def __update():
        with open(Bank.database, "w") as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*", k = 1)

        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name": input("TELL YOUR NAME: "),
            "age": int(input("ENTER YOUR AGE: ")),
            "email": input("ENTER YOUR EMAIL ID: "),
            "pin": int(input("ENTER YOUR 4 NUMBER PIN: ")),
            "account-no": Bank.__accountgenerate(),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("SORRY! YOU CANNOT CREATE YOUR ACCOUNT!")
        else:
            print("YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY!")

            for i in info:
                print(f"{i} : {info[i]}")
            
            print("PLEASE NOTE DOWN YOUR ACCOUNT NUMBER!")

            Bank.data.append(info)

            Bank.__update()

    def depositemoney(self):
        accno = input("PLEASE ENTER YOUR ACCOUNT NUMBER: ")
        pin = int(input("PLEASE ENTER YOUR PIN: "))
        
        userdata = [i for i in Bank.data if i["account-no"] == accno and i["pin"] == pin]

        if userdata == False:
            print("PLEASE ENTER VALID DETAILS: ")
        else:
            amount = int(input("ENTER HOW MUCH MONEY YOU WANT TO DEPOSITE: "))
            if amount > 100000:
                print("SORRY THE AMOUNT IS TOO MUCH TO DEPOSITE! YOU CAN DEPOSITE BELOW 100000")
            elif amount < 0:
                print("PLEASE ENTER VALID AMOUNT TO DEPOSIE!")
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print("AMOUNT DEPOSITED SUCCESFULLY!")

    def withdrawmoney(self):
        accno = input("PLEASE ENTER YOUR ACCOUNT NUMBER: ")
        pin = int(input("PLEASE ENTER YOUR PIN: "))
        
        userdata = [i for i in Bank.data if i["account-no"] == accno and i["pin"] == pin]

        if userdata == False:
            print("PLEASE ENTER VALID DETAILS: ")
        else:
            amount = int(input("ENTER HOW MUCH MONEY YOU WANT TO WITHDRAW: "))
            if amount > 50000:
                print("SORRY THE AMOUNT IS TOO MUCH TO WITHDRAW! YOU CAN WITHDRAW BELOW 50000")
            elif amount < 0:
                print("PLEASE ENTER VALID AMOUNT TO WITHDRAW!")
            elif userdata[0]["balance"] < amount:
                print("SORRY YOU DON'T HAVE SUFFICIENT BALANCE TO WITHDRAW MONEY!")
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print("AMOUNT WITHDREW SUCCESFULLY!")

    def showdetails(self):
        accno = input("PLEASE ENTER YOUR ACCOUNT NUMBER: ")
        pin = int(input("PLEASE ENTER YOUR PIN: "))

        userdata = [i for i in Bank.data if i["account-no"] == accno and i["pin"] == pin]

        print("YOUR DETAILS ARE: ")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accno = input("PLEASE ENTER YOUR ACCOUNT NUMBER: ")
        pin = int(input("PLEASE ENTER YOUR PIN: "))

        userdata = [i for i in Bank.data if i["account-no"] == accno and i["pin"] == pin]

        if not userdata:
            print("PLEASE ENTER VALID DETAILS: ")
            return
        else:
            print("YOU CANNOT CHANGE THE AGE, ACCOUNT NUMBER AND BALANCE!")

            print("LEAVE EMPTY IF YOU DON'T WANT TO CHANGE!")

            newdata = {
                "name": input("PLEASE ENTER NEW NAME OR PRESS ENTER TO SKIP: "),
                "email": input("PLEASE ENTER NEW EMAIL OR PRESS ENTER TO SKIP: "),
                "pin": input("PLEASE ENTER NEW PIN OR PRESS ENTER TO SKIP: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]

            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]

            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            else:
                newdata["pin"] = int(newdata["pin"])

            newdata["age"] = userdata[0]["age"]
            newdata["account-no"] = userdata[0]["account-no"]
            newdata["balance"] = userdata[0]["balance"]

            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            
            Bank.__update()
            print("DETAILS UPDATED SUCCESSFULLY!")

    def delete(self):
        accno = input("PLEASE ENTER YOUR ACCOUNT NUMBER: ")
        pin = int(input("PLEASE ENTER YOUR PIN: "))

        userdata = [i for i in Bank.data if i["account-no"] == accno and i["pin"] == pin]

        if userdata == False:
            print("PLEASE ENTER VALID DETAILS: ")
        else:
            check = input("PRESS Y IF YOU ACTUALLY WANT TO DELETE ACCOUNT OR PRESS N")

            if check == "n" or check == "N":
                print("YOUR ACCOUNT IS SAFE!")
            else:
                idx = Bank.data.index(userdata[0])
                Bank.data.pop(idx)
                Bank.__update()
                print("ACCOUNT DELETED SUCCESSFULLY!")

user = Bank()

print("PRESS 1 FOR CREATING AN ACCOUNT")
print("PRESS 2 FOR DEPOSITING THE MONEY IN THE BANK")
print("PRESS 3 FOR WITHDRAWING THE MONEY")
print("PRESS 4 FOR DETAILS")
print("PRESS 5 FOR UPDATING THE DETAILS")
print("PRESS 6 FOR DELETING YOUR ACCOUNT")

check = int(input("TELL YOUR RESPONSE: "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositemoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()