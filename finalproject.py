# MSIT 501 - Project 5
#
# Initial code developed by: Frank J. Mitropoulos
#
# Final code implemented by: Stefani Walker


import pickle


class Item:


    def __init__(self, category, desc, value, quant):

        self.category = category
        self.desc = desc
        self.value = value
        self.quant = quant

    def display(self):

        print("{:<30}{:<18}{:8.2f}{:7d}".format(self.desc, self.category, self.value, self.quant))

    def displaycategory(self):

        print(self.category)

    def displaycollectionvalue(self):

        print(sum(self.value))

class Collection:


    def __init__(self):

        self.items = []

    def addItem(self, category, desc, value, quant):

        item = Item(category, desc, value, quant)
        self.items.append(item)



    def __str__(self):
        s = ""
        for item in self.items:
            s = s + str(item) + "\n"
        return s

    def displayAllItems(self):
        print("{:<30}{:<18}{:8}{:7}".format("Description", "Category", "  Value", "  Amount"))
        print("-" * 65)
        for x in self.items:
            x.display()

    def displayAllCategories(self):

        print("Categories")
        print("-" * 10)
        for x in self.items:
            x.displaycategory()

    def displayAllItemsForCategory(self, category):
        print("Items for category:", category)
        print("{:<30}{:<18}{:8}{:7}".format("Description", "Category", "  Value", "  Amount"))
        print("-" * 65)
        for x in self.items:
             if x.category == category:
                 x.display()
             else:
                print("Category not found")
                break

    def displayItemsOverValue(self, valueone):
        print("Items over", valueone)
        print("{:<30}{:<18}{:8}{:7}".format("Description", "Category", "  Value", "  Amount"))
        print("-" * 65)
        for x in self.items:
            if x.value > valueone:
                x.display()
            else:
                print("No items to be listed")
                break

    def displayItemFromDescription(self, itemToFind):

        print("{:<30}{:<18}{:8}{:7}".format("Description", "Category", "  Value", "  Amount"))
        print("-" * 65)
        for x in self.items:
            if x.desc == itemToFind:
                x.display()
            else:
                print("Description not found")
                break


    def displayCollectionValue(self):

        val = 0
        for x in self.items:
            val = val + x.value * x.quant
        print("$", val)

def printMenu():
    print("")
    print("1. Display all items in my collection")
    print("2. Display all categories of my items")
    print("3. Display all items in a given category")
    print("4. Search for an item by description")
    print("5. Add an new item to my collection")
    print("6. Display all items above a given value")
    print("7. Calculate the total value of my collection")
    print("S. Save to disk")
    print("L. Load data from disk")
    print("Q. Quit")
    print()


def main():
    stuff = Collection()
    print()
    print('Welcome to my Collection Manager')
    while True:
        printMenu()
        selection = input("Please enter a selection: ").strip().upper()
        if selection not in ['1', '2', '3', '4', '5', '6', '7', 'S', 'L', 'Q']:
            print("Please enter a valid choice...")
            continue
        if selection == '1':
            stuff.displayAllItems()
        elif selection == '2':
            stuff.displayAllCategories()
        elif selection == '3':
            category = input("Enter category: ").strip()
            stuff.displayAllItemsForCategory(category)
        elif selection == '4':
            itemToFind = input("Enter item's description: ").strip()
            stuff.displayItemFromDescription(itemToFind)
        elif selection == '5':
            cat = input("Enter the item's category: ").strip()
            desc = input("Enter the item's description: ").strip()
            value = eval(input("Enter the item's value: "))
            quant = eval(input("Enter the item's quantity: "))
            stuff.addItem(cat, desc, value, quant)
            print("Item added")
        elif selection == '6':
            valueone = eval(input("Enter the value: "))
            stuff.displayItemsOverValue(valueone)
        elif selection == '7':
            stuff.displayCollectionValue()
        elif selection == 'S':
            pickle.dump(stuff, open("stuff.p", "wb"))
            print("Data saved...")
        elif selection == 'L':
            stuff = pickle.load(open("stuff.p", "rb"))
            print("Data loaded...")
        else:
            print("Thanks for using my Collection Manager")
            break

if __name__ == "__main__":
    main()
