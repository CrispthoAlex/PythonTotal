from random import *


class Person:
    """

    """
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class Client(Person):

    def __init__(self, name, lastname, account_number, balance):
        super().__init__(name, lastname)
        self.account_number = account_number
        self.balance = balance

    @staticmethod
    def __value_in():
        cash_in = 0
        while cash_in not in range(1, 1 * (10 ** 6)):
            cash_in = round(float(input("Value in $ ")), 2)
        return cash_in

    def income(self):
        income = self.__value_in()
        print(f"Your income was $ {income}")
        self.balance = round(self.balance + income, 2)

    def __value_out(self):
        cash_out = 0
        while cash_out not in range(1, int(self.balance)):
            cash_out = round(float(input("Value out $ ")), 2)
            if cash_out > int(self.balance):
                print("Insufficient funds. Check your balance")
        return cash_out

    def outcome(self):
        outcome = self.__value_out()
        print(f"Your outcome was $ {outcome}")
        self.balance = round(self.balance - outcome, 2)

    def __str__(self):
        return (f"{'#' * 40}\n"
                f"PYTHON BANK\n"
                f"{'-' * 40}\n"
                f"Client: \t\t{self.name} {self.lastname}\n"
                f"N° Account: \t{self.account_number}\n"
                f"Balance: \t\t$ {self.balance}\n"
                f"{'-' * 40}\n"
                f"{'#' * 40}\n")


"""
create cliente flow
- Ask for:
    - name + lastname
    - account
    - balance => random value 200 to 5000
"""


def input_info():
    """

    :return:
    """
    name = input("Type your name |> ")
    lastname = input("Type your lastname |> ")
    return name, lastname


def create_client():
    print("Create your client\n")
    name, lastname = input_info()
    account_nb = "5070000" + str(randint(50, 9999))
    balance = round(uniform(200, 5000), 2)

    return Client(name, lastname, account_nb, balance)


def selecting_option():
    option = "-1"
    while not option.isnumeric() or int(option) not in range(0, 4):
        print("""Do you want to:
                    [1] Deposit money
                    [2] Withdraw money
                    [3] Print info client
                    [0] Exit""")
        option = input(f"""|> """)
    return int(option)


def init():
    print(
        f'{"#" * 50}\n'
        f"{' ' * 14}WELCOME TO PYTHON BANK{' ' * 14}\n"
        f'{"#" * 50}\n'
    )
    new_client = create_client()
    print(f"Welcome {new_client.name},\n")
    option = -1
    while option != 0:
        option = selecting_option()
        match option:
            case 1:
                new_client.income()
            case 2:
                new_client.outcome()
            case 3:
                print(new_client)
            case 0:
                print(f"Bye {new_client.name}\n"
                      f"...Closing program...")
                break


# Launch program
init()

