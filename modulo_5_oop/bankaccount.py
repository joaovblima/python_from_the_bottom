class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Essa operação não pode ser realizada.")
        else:
            self.balance -= amount


banca_joao = BankAccount(3000)
banca_joao.deposit(200)
print(banca_joao.balance)
banca_joao.withdraw(349)
print(banca_joao.balance)