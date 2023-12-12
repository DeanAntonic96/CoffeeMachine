import tkinter as tk
from tkinter import messagebox

class CoffeeMachine_OFF_ON:
    
    def __init__(self):
        self.in_use = False
 
    def turn_on(self):
        self.in_use = True
   
    def turn_off(self):
        self.in_use = False
    
class CoffeeMachine:
    def __init__(self):
        self.machine = CoffeeMachine_OFF_ON()

class CoffeeMachineGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Coffee Machine")
        self.value = CoffeeMachine_OFF_ON
        self.coffee_machine = CoffeeMachine()
        self.total_money = 0
        self.total_sugar = 0
        self.max_total_sugar = 10
        self.total_water = 1000
        self.total_milk = 1000
        self.total_coffee = 1000
        self.total_sugar_1 = 1000
        self.max_value = 2000
        self.espresso_price = 150
        self.cappuccino_price = 180
        self.latte_price = 210
        self.doppo_price = 120
        
        self.turn_on_button = tk.Button(self.master, text="Turn On Machine", command=self.turn_on_machine)
        self.turn_on_button.pack()

        self.turn_off_button = tk.Button(self.master, text="Turn Off Machine", command=self.turn_off_machine)
        self.turn_off_button.pack()
        
        self.status_label = tk.Label(self.master, text="Machine turned off", bd=1, relief=tk.SUNKEN, anchor=tk.SE)
        self.status_label.pack(side=tk.RIGHT)
        
        self.total_sugar_label = tk.Label(self.master, text=f"Total sugar: {self.total_sugar}")
        self.total_sugar_label.place(x=10, y= 320)
        
        self.add_sugar_button = tk.Button(self.master, text="Add 2g of sugar", command=lambda: self.add_sugar_to_coffee(2))
        self.add_sugar_button.place(x=10, y=340)

        self.label_water_total = tk.Label(self.master, text=f"Water Total: {self.total_water}")
        self.label_water_total.place(x=100, y=160)

        self.label_sugar_total_1 = tk.Label(self.master, text=f"Sugar Total: {self.total_sugar_1}")
        self.label_sugar_total_1.place(x=100, y=280)

        self.label_coffee_total = tk.Label(self.master, text=f"Coffee Total: {self.total_coffee}")
        self.label_coffee_total.place(x=100, y=200)

        self.total_milk_label = tk.Label(self.master, text=f"Milk Total: {self.total_milk}")
        self.total_milk_label.place(x=100, y=240)

       
        self.total_label = tk.Label(self.master, text=f"Total money: {self.total_money}")
        self.total_label.place(x=10, y=10)

        self.button_5 = tk.Button(self.master, text="Add 5", command=lambda: self.add_money(5))
        self.button_5.place(x=10, y=40)

        self.button_10 = tk.Button(self.master, text="Add 10", command=lambda: self.add_money(10))
        self.button_10.place(x=80, y=40)

        self.button_20 = tk.Button(self.master, text="Add 20", command=lambda: self.add_money(20))
        self.button_20.place(x=150, y=40)

        self.button_50 = tk.Button(self.master, text="Add 50", command=lambda: self.add_money(50))
        self.button_50.place(x=220, y=40)

        self.button_100 = tk.Button(self.master, text="Add 100", command=lambda: self.add_money(100))
        self.button_100.place(x=290, y=40)

        self.button_cancel = tk.Button(self.master, text="Cancel", command=self.cancel)
        self.button_cancel.place(x=10, y=80)

        self.add_water_button = tk.Button(self.master, text="Add water", command=self.add_water)
        self.add_water_button.place(x=10, y=160)

        self.add_coffee_button = tk.Button(self.master, text="Add coffee", command=self.add_coffee)
        self.add_coffee_button.place(x=10, y=200)

        self.add_milk_button = tk.Button(self.master, text="Add milk", command=self.add_milk)
        self.add_milk_button.place(x=10, y=240)

        self.add_sugar_button = tk.Button(self.master, text="Add sugar", command=self.add_sugar_1)
        self.add_sugar_button.place(x=10, y=280)

        self.espresso_button = tk.Button(self.master, text="Espresso", command=self.make_espresso)
        self.espresso_button.place(x=300, y=300)

        self.cappuccino_button = tk.Button(self.master, text="Cappuccino", command=self.make_cappuccino)
        self.cappuccino_button.place(x=300, y=330)
    
        self.latte_button = tk.Button(self.master, text="Latte", command=self.make_latte)
        self.latte_button.place(x=300, y=360)

        self.doppio_button = tk.Button(self.master, text="Doppio", command=self.make_doppio)
        self.doppio_button.place(x=300, y=390)
 
    def turn_on_machine(self):
        self.coffee_machine.machine.turn_on()
        self.refresh_status()
        self.enable_options()

    def turn_off_machine(self):
        self.coffee_machine.machine.turn_off()
        self.refresh_status()
        self.disable_options()
    
    def add_money(self, amount):
        self.total_money += amount
        self.total_label.config(text=f"Total money: {self.total_money}")

    def cancel(self):
        if self.total_money > 0:
            self.total_money = 0
            message = "Take your money. Thank you!"
        else:
            message = "No money to take."

        self.total_label.config(text=f"Total money: {self.total_money}")
        messagebox.showinfo("Cancelled", message)
    
    def add_water(self):
        self.total_water += 100
        self.label_water_total.config(text=f"Total water : {self.total_water}")
        if self.total_water >= self.max_value:
            message = "Water level is full!"
            messagebox.showinfo("Level", message)  
        
    def add_coffee(self):
        self.total_coffee += 100
        self.label_coffee_total.config(text=f"Total coffee : {self.total_coffee}")
        if self.total_coffee >= self.max_value:
            message = "Coffee level is full!"
            messagebox.showinfo("Level", message)  
    
    def add_milk(self):
        self.total_milk += 100
        self.total_milk_label.config(text=f"Total milk : {self.total_milk}")
        if self.total_milk >= self.max_value:
            message = "Milk level is full!"
            messagebox.showinfo("Level", message)  
    
    def add_sugar_1(self):
        self.total_sugar_1 += 100
        self.label_sugar_total_1.config(text=f"Total sugar : {self.total_sugar_1}")
        if self.total_sugar >= self.max_value:
            message = "Sugar level is full!"
            messagebox.showinfo("Level", message)  
 
    def add_sugar_to_coffee(self, sugar_amount):
        if self.total_sugar < 10:
            self.total_sugar += sugar_amount
        else:
            message = "You've added the maximum sugar amount." 
            messagebox.showinfo("Level", message)    
        self.total_sugar_label.config(text=f"Total sugar : {self.total_sugar}")

    def refresh_status(self):
        if self.coffee_machine.machine.in_use:
            self.status_label.config(text="Machine turned on", bg="green", fg="white")
        else:
            self.status_label.config(text="Machine turned off", bg="red", fg="white")

    def refresh_state_label(self):
        self.state_label.config(text=self.format_state())

    def format_state(self):
        state = "Ingredients state:\n"
        for ingredient, quantity in self.coffee_machine.machine.ingredients.items():
            state += f"{ingredient.capitalize()}: {quantity} ml\n"
        return state
    
    def make_espresso(self):
        if self.total_water > 30 and self.total_coffee > 10 and self.total_money >= self.espresso_price:    
            self.total_water -= 30
            self.total_money -= self.espresso_price
            self.total_coffee -= 10
            self.total_sugar_1 -= self.total_sugar
            self.total_sugar -= self.total_sugar
            message = "Coffee is made!" 
            messagebox.showinfo("Take your coffee", message)
            
            self.total_label = tk.Label(self.master, text=f"Total money: {self.total_money}")
            self.total_label.place(x=10, y=10)
            self.total_water_label = tk.Label(self.master, text=f"Total water: {self.total_water}")
            self.total_water_label.place(x=100, y=160)
            self.total_sugar_label = tk.Label(self.master, text=f"Total sugar: {self.total_sugar_1}")
            self.total_sugar_label.place(x=100, y=280)
            self.total_coffee_label = tk.Label(self.master, text=f"Total coffee: {self.total_coffee}")
            self.total_coffee_label.place(x=100, y=200)
            self.total_milk_label = tk.Label(self.master, text=f"Total milk: {self.total_milk}")
            self.total_milk_label.place(x=100,  y=240)
            self.total_sugar_label.config(text=f"Total sugar : {self.total_sugar}") 
                
        elif self.total_coffee < 10 and self.total_water < 30 and self.total_money >= self.espresso_price : 
            message = "Not enough ingredients for coffee! \n Refill the machine."
            messagebox.showinfo("Error", message) 
        elif self.total_coffee > 10 and self.total_water > 30 and self.total_money < self.espresso_price :
            message = "Not enough money for coffee! \n Insert money."
            messagebox.showinfo("Error", message) 
            
    def make_cappuccino(self):
        if self.total_water > 50 and self.total_coffee > 10 and self.total_milk > 60 and self.total_money >= self.cappuccino_price:    
            self.total_water -= 50
            self.total_money -= self.espresso_price
            self.total_coffee -= 10
            self.total_milk -= 60
            self.total_sugar_1 -= self.total_sugar
            self.total_sugar -= self.total_sugar
            message = "Coffee is made!" 
            messagebox.showinfo("Take your coffee", message)
            
            self.total_label = tk.Label(self.master, text=f"Total money: {self.total_money}")
            self.total_label.place(x=10, y=10)
            self.total_water_label = tk.Label(self.master, text=f"Total water: {self.total_water}")
            self.total_water_label.place(x=100, y=160)
            self.total_sugar_label = tk.Label(self.master, text=f"Total sugar: {self.total_sugar_1}")
            self.total_sugar_label.place(x=100, y=280)
            self.total_coffee_label = tk.Label(self.master, text=f"Total coffee: {self.total_coffee}")
            self.total_coffee_label.place(x=100, y=200)
            self.total_milk_label = tk.Label(self.master, text=f"Total milk: {self.total_milk}")
            self.total_milk_label.place(x=100,  y=240)
            self.total_sugar_label.config(text=f"Total sugar : {self.total_sugar}") 
                
        elif self.total_water < 50 and self.total_coffee < 10 and self.total_milk < 60 and self.total_money >= self.cappuccino_price:
            message = "Not enough ingredients for coffee! \n Refill the machine!"
            messagebox.showinfo("Error", message) 
        elif self.total_water > 50 and self.total_coffee > 10 and self.total_milk > 60 and self.total_money < self.cappuccino_price:
            message = "Not enough money for coffee! \n Insert money!"
            messagebox.showinfo("Error", message) 

    def make_doppio(self):
        if self.total_water > 20 and self.total_coffee > 50 and self.total_money >= self.price_doppio:    
            self.total_water -= 50
            self.total_money -= self.price_doppio
            self.total_coffee -= 20
            self.total_sugar_1 -= self.total_sugar
            self.total_sugar -= self.total_sugar
            message = "Coffee is made!"
            messagebox.showinfo("Take your coffee", message)

            self.label_total_money = tk.Label(self.master, text=f"Total money: {self.total_money}")
            self.label_total_money.place(x=10, y=10)
            self.label_total_water = tk.Label(self.master, text=f"Total water: {self.total_water}")
            self.label_total_water.place(x=100, y=160)
            self.label_total_sugar = tk.Label(self.master, text=f"Total sugar: {self.total_sugar_1}")
            self.label_total_sugar.place(x=100, y=280)
            self.label_total_coffee = tk.Label(self.master, text=f"Total coffee: {self.total_coffee}")
            self.label_total_coffee.place(x=100, y=200)
            self.label_total_milk = tk.Label(self.master, text=f"Total milk: {self.total_milk}")
            self.label_total_milk.place(x=100,  y=240)
            self.total_sugar_label.config(text=f"Total sugar: {self.total_sugar}") 
                
        elif self.total_water < 20 and self.total_coffee < 50 and self.total_money >= self.price_doppio:  
            message = "Not enough ingredients for coffee! \n Refill!"
            messagebox.showinfo("Error!", message) 
        elif self.total_water > 20 and self.total_coffee > 50 and self.total_money < self.price_doppio: 
            message = "Not enough money for coffee! \n Insert money!"
            messagebox.showinfo("Error!", message)

    def make_latte(self):
        if self.total_water > 50 and self.total_coffee > 20 and self.total_milk > 80 and self.total_money >= self.price_latte:    
            self.total_water -= 50
            self.total_money -= self.price_latte
            self.total_coffee -= 20
            self.total_milk -= 80
            self.total_sugar_1 -= self.total_sugar
            self.total_sugar -= self.total_sugar
            message = "Coffee is made!"
            messagebox.showinfo("Take your coffee", message)

            self.label_total_money = tk.Label(self.master, text=f"Total money: {self.total_money}")
            self.label_total_money.place(x=10, y=10)
            self.label_total_water = tk.Label(self.master, text=f"Total water: {self.total_water}")
            self.label_total_water.place(x=100, y=160)
            self.label_total_sugar = tk.Label(self.master, text=f"Total sugar: {self.total_sugar_1}")
            self.label_total_sugar.place(x=100, y=280)
            self.label_total_coffee = tk.Label(self.master, text=f"Total coffee: {self.total_coffee}")
            self.label_total_coffee.place(x=100, y=200)
            self.label_total_milk = tk.Label(self.master, text=f"Total milk: {self.total_milk}")
            self.label_total_milk.place(x=100,  y=240)
            self.total_sugar_label.config(text=f"Total sugar: {self.total_sugar}") 
                
        elif self.total_water < 50 and self.total_coffee < 20 and self.total_milk < 80 and self.total_money >= self.price_latte: 
            message = "Not enough ingredients for coffee! \n Refill!"
            messagebox.showinfo("Error!", message) 
        elif self.total_water > 50 and self.total_coffee > 20 and self.total_milk > 80 and self.total_money < self.price_latte: 
            message = "Not enough money for coffee! \n Insert money!"
            messagebox.showinfo("Error!", message)
    def enable_options(self):
        # Enable all the buttons and widgets
        self.button_5["state"] = tk.NORMAL
        self.button_10["state"] = tk.NORMAL
        self.button_20["state"] = tk.NORMAL
        self.button_50["state"] = tk.NORMAL
        self.button_100["state"] = tk.NORMAL
        self.button_cancel["state"] = tk.NORMAL
        self.add_sugar_button["state"] = tk.NORMAL
        self.cappuccino_button["state"] = tk.NORMAL
        self.espresso_button["state"] = tk.NORMAL
        self.latte_button["state"] = tk.NORMAL
        self.doppio_button["state"] = tk.NORMAL
        self.add_water_button["state"] = tk.NORMAL
        self.add_coffee_button["state"] = tk.NORMAL
        self.add_milk_button["state"] = tk.NORMAL
        self.add_sugar_button["state"] = tk.NORMAL
        self.turn_on_button["state"] = tk.NORMAL

    def disable_options(self):
        # Disable all the buttons and widgets
        self.button_5["state"] = tk.DISABLED
        self.button_10["state"] = tk.DISABLED
        self.button_20["state"] = tk.DISABLED
        self.button_50["state"] = tk.DISABLED
        self.button_100["state"] = tk.DISABLED
        self.button_cancel["state"] = tk.DISABLED
        self.add_sugar_button["state"] = tk.DISABLED
        self.cappuccino_button["state"] = tk.DISABLED
        self.espresso_button["state"] = tk.DISABLED
        self.latte_button["state"] = tk.DISABLED
        self.doppio_button["state"] = tk.DISABLED
        self.add_water_button["state"] = tk.DISABLED
        self.add_coffee_button["state"] = tk.DISABLED
        self.add_milk_button["state"] = tk.DISABLED
        self.add_sugar_button["state"] = tk.DISABLED
        self.turn_off_button["state"] = tk.NORMAL

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeMachineGUI(root)
    
    root.geometry("1366x768")
    root.mainloop()    

