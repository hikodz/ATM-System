# class i need import
from backend.database import DataBaseUsage
from backend.effect import Effect
# library i need import
from inquirer import Text, prompt, List,Checkbox
from simple_chalk import chalk
from re import match
from abc import ABC



class Atm:
    def __init__(self) -> None:
        self.db = DataBaseUsage()
        self.effect = Effect()
        self.data = {}

    def Add_card(self):

        info = [
            Text('Card Number', message="Please Enter Card Number",validate=lambda _, x: match(r'^[0-9]{12,19}$', x),default="1001...."),
            Text('CVV', message="Please Enter CVV",validate=lambda _, x: match(r"^[0-9]{3,4}$", x),default="1234")
                    ]

        info = prompt(info)
        check = self.db.SearchCard(info['Card Number'],info['CVV'])
        if check:
                self.data = check
                self.effect.Clear()
                print(f"{chalk.green("Hello")} {chalk.yellow(self.data["FullName"])} {chalk.green("In ATM")} {self.data["country"]}!")

                while True:
                    option_ATM = [
                            List('type',
                                            message=f"What choice do you need?",
                                            choices=[
                                                    "Transfer",
                                                    "Withdraw",
                                                    "Balance Inquiry",
                                                    "Quit"
                                            ]
                                        ),
                            ]

                    option_ATM = prompt(option_ATM)

                    if option_ATM["type"] == "Deposite":
                        pass
                    elif option_ATM["type"] == "Transfer":
                        pass
                    elif option_ATM["type"] == "Withdraw":
                        pass
                    elif option_ATM["type"] == "Balance Inquiry":
                        pass
                    else:
                        self.effect.Clear()
                        return
        self.effect.Clear()
        print(chalk.red("Please check your informatino card!!"))








class Transaction(ABC):
    pass
