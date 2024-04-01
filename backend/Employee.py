# class i need import
from backend.database import DataBaseUsage
from backend.Card import Card
from backend.effect import Effect
from backend.Account import
from enum import Enum

class Grade(Enum):
    GRADE1=["Search for client","Deposite With ID"]
    GRADE2=["Search for employee","Search for card"]
    GRADE3=["Remove account","Add cash to ATM"]


class Employee:
    def Grade_choice(self):
        pass





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
