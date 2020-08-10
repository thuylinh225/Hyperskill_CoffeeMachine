class CoffeeMachine():

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def espresso(self):
        self.water -= 250
        self.coffee -= 16
        self.cups -= 1
        self.money += 4

    def latte(self):
        self.water -= 350
        self.milk -= 75
        self.coffee -= 20
        self.cups -= 1
        self.money += 7

    def cappuccino(self):
        self.water -= 200
        self.milk -= 100
        self.coffee -= 12
        self.cups -= 1
        self.money += 6

    def buy(self):
        self.option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.option == "back":
            pass
        elif self.option == '1':
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee < 16:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.espresso()
        elif self.option == '2':
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee < 20:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.latte()
        elif self.option == '3':
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee < 12:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.cappuccino()

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print (f"I gave you ${self.money}")
        self.money = 0

    def remaining(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money""")

    def action(self):
        print()
        self.work = input("Write action (buy, fill, take, remaining, exit):\n")
        print()
        if self.work == "buy":
            self.buy()
        elif self.work == "fill":
            self.fill()
        elif self.work == "take":
            self.take()
        elif self.work == "remaining":
            self.remaining()
        else:
            exit()

coffee = CoffeeMachine()
while True:
    coffee.action()
