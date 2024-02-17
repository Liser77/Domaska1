class CashRegister:
    def __init__(self, money):
        self.money = money
        
    def top_up(self, x):
        self.money += x
    
    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, x):
        if self.money >= x:
            self.money -= x
        else:
            raise ValueError("Недостаточно денег в кассе")
        
cash_register = CashRegister(5000)
print(cash_register.count_1000())