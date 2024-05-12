class Pub:
    def __init__(self):
        self.prices = {
            'breakfast' : 30,
            'lunch' : 50,
            'dinner' : 60,
            'desserts' : 15,
            'drinks' : 10
        }
        self.sales = {
            'breakfast' : 0,
            'lunch' : 0,
            'dinner' : 0,
            'desserts' : 0,
            'drinks' : 0
        }
        
        self.profit_margins = {
            'breakfast' : 0.6,
            'lunch' : 0.5,
            'dinner' : 0.3, 
            'desserts' : 0.3,
            'drinks' : 0.5
        }

        self.min_sales_for_profit = 1200    # pragul minim pt a realiza profit


    def sell_item(self, item_type, quantity):
        if item_type in self.sales:
            self.sales[item_type] += quantity
        else:
            print(f"Produsul {item_type} nu este recunoscut")

    def calculate_total_sales(self):
        total_sales = sum(self.sales[item] * self.prices[item] for item in self.sales)
        return total_sales
    
    def calculate_profit(self):
        total_sales = self.calculate_total_sales()
        if total_sales >= self.min_sales_for_profit:
            return sum(self.sales[item] * self.prices[item] * self.profit_margins[item] for item in self.sales)
        return 0
     
    def report(self):
        print("Raport vanzari: ")
        for item, count in self.sales.items():
            item_sales = count * self.prices[item]
            if self.calculate_total_sales() >= self.min_sales_for_profit:
                item_profit = item_sales * self.profit_margins[item]
            else:
                item_profit = 0
            print(f"{item.capitalize()}: {count} vandute, Vanzari totale: {item_sales} lei, Profit {item_profit} lei")
        print(f"Vanzari totale pentru o zi: {self.calculate_total_sales()} lei")
        print(f"Profit {self.calculate_profit()} lei")

pub = Pub()
pub.sell_item('breakfast', 10)
pub.sell_item('lunch', 50)
pub.sell_item('dinner', 40)
pub.sell_item('desserts', 20)
pub.sell_item('drinks', 100)
pub.report()