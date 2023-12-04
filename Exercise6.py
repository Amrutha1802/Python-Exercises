# 1. Budget App
# Create a Budget class that can instantiate objects based on different budget categories like food,
# clothing, and entertainment. These objects should allow for depositing and withdrawing funds from
# each category, as well computing category balances and transferring balance amounts between categories
class Budget:
    def __init__(self, category):
        self.category = category
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount {amount}$ deposited")
        else:
            print("Inavlid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insuffiicient funds or invalid amont")
            return False

    def transfer(self, other_category, amount):
        if self.withdraw(amount):
            other_category.deposit(amount)
            print(
                f"{amount}$ transferred from {self.category} to {other_category.category}"
            )
        else:
            print("Inavlid amount or insufficient funds")

    def get_balance(self):
        return self.balance


food_budget = Budget("Food")
clothing_budget = Budget("Clothing")
food_budget.deposit(1000)
clothing_budget.deposit(1230)
clothing_budget.withdraw(230)
print(f"balance in food_budget is {food_budget.get_balance()}")
clothing_budget.transfer(food_budget, 200)
print(f"balance in clothing_budget is {clothing_budget.get_balance()}")
print(f"balance in food_budget is {food_budget.get_balance()}")
