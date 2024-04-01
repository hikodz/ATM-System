# class i need import

from backend.database import DataBaseUsage
from backend.Card import Card
from backend.effect import Effect
from backend.ATM import Transaction

# library i need import
from inquirer import Text, prompt, List,Checkbox
from enum import Enum

class Grade(Enum):
    GRADE1=["Search for client","Deposite With ID" ,"Logout"]
    GRADE2=["Search for employee","Search for card"]
    GRADE3=["Remove account","Add cash to ATM"]


class Employee:
    def __init__(self) -> None:
        self.effect  = Effect()

    def Grade_choice(self,data:dict) -> None:
        if data["Grade"] == 1:
            choices_emp = [
            List('type',
                            message=f"What choice do you need?",
                            choices=Grade.GRADE1.value
                        ),
            ]
            active =prompt(choices_emp)
            if active["type"] =="Search for client":
                pass
            elif active["type"] =="Search for client":
                    pass
            else:
                self.effect.Clear()
                return
        elif data["Grade"] == 2:
            choices_emp = [
            List('type',
                            message=f"What choice do you need?",
                            choices=Grade.GRADE2.value +Grade.GRADE1.value
                        ),
            ]
            active =prompt(choices_emp)
            if active["type"] =="Search for client":
                pass
            elif active["type"] =="Deposite With ID":
                    pass
            elif active["type"] =="Search for employee":
                        pass
            elif active["type"] =="Search for card":
                            pass
            else:
                self.effect.Clear()
                return
        elif data["Grade"] == 3:
            choices_emp = [
            List('type',
                            message=f"What choice do you need?",
                            choices=Grade.GRADE3.value +Grade.GRADE2.value +Grade.GRADE1.value
                        ),
            ]
            active =prompt(choices_emp)
            if active["type"] =="Search for client":
                pass
            elif active["type"] =="Deposite With ID":
                    pass
            elif active["type"] =="Search for employee":
                        pass
            elif active["type"] =="Search for card":
                    pass
            elif active["type"] =="Remove account":
                    pass
            elif active["type"] =="Add cash to ATM":
                    pass
            else:
                self.effect.Clear()
                return





class EmpGrade1:
    def Search_client(self):
        pass
    def Deposite(self):
        pass

class EmpGrade2(EmpGrade1):
    def Search_emp(self):
        pass
    def Search_card(self):
        pass

class EmpGrade3(EmpGrade2):
    def Remove_account(self):
        pass
    def Add_cash_atm(self):
        pass
