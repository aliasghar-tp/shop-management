import json
from datetime import datetime


with open("products.json", "r" ) as file:
    list_products = json.load(file)


with open("sales.json", "r") as file:
    list_sales = json.load(file)


def save_sale(list_sales):
    with open("sales.json", "w") as file:
        json.dump(list_sales, file, indent = 4)


def save_product(list_products):
    with open("products.json", "w") as file:
        json.dump(list_products, file, indent = 4)


def add_product(list_products):
    id = max((p.get("id", 0) for p in list_products if isinstance(p, dict)), default = 0) + 1
    name = input("enter name of product: ")
    f = True
    while f:
        try:
            price = float(input("enter the price of products: "))
            if price <= 0:
                raise ValueError
            f = False
        except ValueError:
            print(("please enter a integer number!"))
    f = True
    while f:
        try:
            quantity = int(input("enter the quantity of products: "))
            if quantity <= 0:
                raise ValueError
            f = False
        except ValueError:
            print(("please enter a integer number!"))
    category = input("enter a category of product: ")

    new_product = {
        "id" : id,
        "name" : name,
        "price" : price,
        "quantity" : quantity,
        "category" : category 
    }

    list_products.append(new_product)
    save_product(list_products)
    print(".....")
    print("The product was added successfully")


def show_product(list_products):
    print("")
    if list_products:
        for i in list_products:
            print("id: ", i['id'])
            print("name: ", i['name'])
            print("price: ", i['price'])
            print("quantity: ", i['quantity'])
            print("category: ", i['category'])
            print("******")
    else:
        print("No product available!")
        print("")


def search_product(list_products):
    search = input("What are you looking for? ")
    n = 0
    for i in list_products:        
        if search.lower() in i["name"].lower() or search.lower() in i['category'].lower():
            print("")
            print("id: ", i['id'])
            print("name: ", i['name'])
            print("price: ", i['price'])
            print("quantity: ", i['quantity'])
            print("category: ", i['category'])
            print("******")
            n += 1
    if n == 0:
        print("No items found!")
        print("")
            

def edit_product(list_products):
    for index, i in enumerate(list_products):
        print(f"{index + 1}.{i['name']}-->{i['price']}")
    print("")
    f = True
    while f:
        try:
            num = input("enter the product number ('to exit, enter exit'): ")
            if num.lower() == "exit":
                print("....")
                print("Exiting edit menu.")
                print("")
                f = False
            else:
                num = int(num)

                if num < 1 or num > len(list_products):
                    print(f"Invalid product number! please enter a number between 1 to {len(list_products)}")
                else:
                    select_product = list_products[num -1]
                    print("edit item: ", select_product["name"])
                    print("1.name")
                    print("2.price")
                    print("3.quantity")
                    print("4.category")
                    print("5.all items")
                    print("6.Exite")

                    edit_item_num = int(input("Enter the item to edit (1-5): "))

                    if edit_item_num == 1:
                        new_name = input("enter the new name for product: ")
                        select_product['name'] = new_name
                        print("Changes have been successfully saved")

                    elif edit_item_num == 2:
                        f = True
                        while f:
                            try:
                                new_price = float(input("enter the new price for product: "))
                                if new_price <= 0:
                                    raise ValueError
                                f = False
                            except ValueError:
                                print(("please enter a integer number!"))
                        select_product["price"] = new_price
                        print("Changes have been successfully saved")

                    elif edit_item_num == 3:
                        f = True
                        while f:
                            try:
                                new_quantity = int(input("enter the new quantity for product: "))
                                if new_quantity <= 0:
                                    raise ValueError
                                f = False
                            except ValueError:
                                print(("please enter a integer number!"))
                        select_product["quantity"] = new_quantity
                        print("Changes have been successfully saved")

                    elif edit_item_num == 4:
                        new_category = input("enter the new category for product: ")
                        select_product["category"] = new_category
                        print("Changes have been successfully saved")

                    elif edit_item_num == 5:
                        new_name = input("enter the new name for product: ")
                        select_product['name'] = new_name

                        f = True
                        while f:
                            try:
                                new_price = float(input("enter the new price for product: "))
                                if new_price <= 0:
                                    raise ValueError
                                f = False
                            except ValueError:
                                print(("please enter a integer number!"))
                        select_product["price"] = new_price

                        f = True
                        while f:
                            try:
                                new_quantity = int(input("enter the new quantity for product: "))
                                if new_quantity <= 0:
                                    raise ValueError
                                f = False
                            except ValueError:
                                print(("please enter a integer number!"))
                        select_product["quantity"] = new_quantity           

                        new_category = input("enter the new category for product: ")
                        select_product["category"] = new_category
                        print("....")
                        print("Changes have been successfully saved")

                    elif edit_item_num == 6:
                        print("Exiting edit menu.")
                    
                    else:
                        print("Invalid item number! Enter between 1 to 6!")
                        print("")

                    save_product(list_products)
                    f = False

        except ValueError:
            print("Invalid input. Please enter numbers where required.")
            print("")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def remove_product(list_products):
    print("")
    
    f = True
    while f:
        for index, i in enumerate(list_products):
            print(f"{index + 1}.{i['name']}-->{i['price']}")

        try:
            num = input("enter the product number (to exit, enter <exit>: ") 
            if num.lower() == "exit":
                print("....")
                print("Exiting edit menu.")
                print("")
                f = False
            else:
                num = int(num)

                if num < 1 or num > len(list_products):
                    print(f"Invalid product number! please enter a number between 1 to {len(list_products)}")
                    print("")
                else:
                    print("")
                    select_product = list_products[num - 1]
                    print("id: ", select_product['id'])
                    print("name: ", select_product['name'])
                    print("price: ", select_product['price'])
                    print("quantity: ", select_product['quantity'])
                    print("category: ", select_product['category'])
                    print("******")
                    
                    a = input("Are you sure you want to delete this? y/n : ")
                    print("....")
                    a = a.lower()
                    if a == "y":
                        list_products.remove(select_product)
                        print("The item was successfully deleted")
                        print("")
                        save_product(list_products)
                        
                    elif a == "n":
                        print("deletion of the selected product was cancelled!")
                        print("")
                    else:
                        print("The command entered is not valid!")
                        print("")
                    

        except ValueError:
            print("Invalid input. Please enter numbers where required.")
            print("")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def sale_product(list_products):
    print("")
    flag = True
    while flag:
        for index, i in enumerate(list_products):
            print(f"{index + 1}.{i['name']}-->{i['price']}")

        try:
            num = input("enter the product number ('to exit, enter exit'): ") 
            if num.lower() == "exit":
                print("Exiting edit menu.")
                flag = False
            else:
                num = int(num)

                if num < 1 or num > len(list_products):
                    print(f"Invalid product number! please enter a number between 1 to {len(list_products)}")
                    print("")
                else:
                    print("")
                    select_product = list_products[num - 1]
                    print("id: ", select_product['id'])
                    print("name: ", select_product['name'])
                    print("price: ", select_product['price'])
                    print("quantity: ", select_product['quantity'])
                    print("category: ", select_product['category'])
                    print("******")

                    f = True
                    while f:
                        try:
                            Quantity_ = input("Enter the purchased product(to exit, enter exit): ")
                            if Quantity_.lower() == "exit":
                                print("....")
                                print("Exiting sale menu.")
                                print("")
                                f = False
                            elif Quantity_ == "0":
                                    print("quantity must be > 0!")
                                    print("")
                            else:
                                Quantity_ = int(Quantity_)

                                if Quantity_ <= select_product['quantity']:
                                    name = select_product['name']
                                    quantity  = Quantity_
                                    unit_price = select_product['price']
                                    total_amount = quantity * unit_price
                                    time = datetime.now().strftime((("%Y-%m-%d %H:%M:%S")))

                                    new_sale = {
                                        "name" : name,
                                        "quantity" : quantity,
                                        "unit_price" : unit_price,
                                        "total_amount" : total_amount,
                                        "time" : time
                                    }
                                    list_sales.append(new_sale)
                                    save_sale(list_sales)
                                    print("The sale has been successfully recorded")
                                    print("")

                                    select_product['quantity'] = select_product['quantity'] - Quantity_
                                    f = False

                                    if select_product['quantity'] == 0:
                                        list_products.remove(select_product)

                                    save_product(list_products)

                                else:
                                    print("The product is out of stock!")
                                    print("")
                                    flag = False


                        except ValueError:
                            print("please enter a number!")

        except ValueError:
            print("Invalid input. Please enter numbers where required.")
            print("")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def sale_show(list_sales):
    print("")
    if list_sales:
        for i in list_sales:
            print("name : ", i['name'])
            print("quantity : ", i['quantity'])
            print("unit_price : ", i['unit_price'])
            print("total_price : ", i['total_amount'])
            print("time : ", i['time'])
            print("******")
            print("")

    else:
        print("No sale available!")
        print("")


def total_amount(list_sales):
    print("")
    total_amount = 0
    for index, i in enumerate(list_sales):
        print(f"{index +1}.{i['name']}-->{i['total_amount']}")
        total_amount += i['total_amount']

    print("....")
    print("total_amount: ", total_amount)


print("====Store Management System====")
print("")


flag = True
while flag:
    print("1.Add Product")
    print("2.Show Product")
    print("3.Search Product")
    print("4.Edit Product")
    print("5.Remove Product")
    print("6.Record Sale")
    print("7.Show Sale")
    print("8.Total Sale")
    print("9.Exit")
    print("")

    try:
        num = int(input("Please choose one: "))

    except ValueError:
        print("Please enter a number between 1 to 9!")

    if 1 <= num <= 9:

        if num == 1:
            add_product(list_products)

        if num == 2:
            show_product(list_products)

        if num == 3:
            search_product(list_products)

        if num == 4:
            edit_product(list_products)

        if num == 5:
            remove_product(list_products)

        if num == 6:
            sale_product(list_products)
      
        if num == 7:
            sale_show(list_sales)

        if num == 8:
            total_amount(list_sales)

        if num == 9:
            flag = False