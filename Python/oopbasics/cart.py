class Cart :
    def __init__(self,cart : list[tuple]):
        self.items = cart 

    def add_item(self,name,price):
        self.items.append((name,price))

        print(f"{name} added to cart")

    def remove_item(self,name):
        for item_name in self.items:
            if item_name[0] == name :
                self.items.remove(item_name)
                print(f"{item_name[0]} removed from cart")
                return
        print(f"{name} not found in cart")
    
    def total_price(self):
        total = 0
        for item_in_cart in self.items:
            total += item_in_cart[1]

        return total
    def most_expensive_item(self):
        if not self.items :
            print("Cart is empty")
            return
        expensive = self.items[0]
        for item in self.items:
            if item[1] > expensive[1]:
                expensive = item
        
        print("most expensive item :")
        print(f"{expensive[0]} - ₹{expensive[1]}")
    def find_item(self,name):
        for item in self.items:
            if item[0] == name:
                return item

        return None

    def apply_discount(self,percentage):
        for i,(name,price) in enumerate(self.items):
            discounted_price = price * (1 - percentage/100)
            self.items[i] = (name,discounted_price)
        return self.items
    def display_cart(self):
        print("Cart items")
        for items_in_cart in self.items:
            print(f"'{items_in_cart[0]}' - \u20b9{items_in_cart[1]}")


            
        