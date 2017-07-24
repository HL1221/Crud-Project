import csv
import code
import operator

numberofproducts = 0

products = []

csv_file_path = "products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)


numberofproducts = len(products)

def show_product():
    ProductID = input("Please enter your products Identifier: ")
    for product in products:
        if int(ProductID) == int(product["id"]):
            print("ID: " + product["id"])
            print("Name: " + product["name"])
            print("Aisle: " + product["aisle"])
            print("Department: " + product["department"])
            print("Price: " + product["price"])

def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:")
    product_aisle = input("aisle is:")
    product_department = input("department is:")
    product_price = input("price is:")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)

def update_product():
    itemnumber = input("Please Enter The Item Number You want to change: ")
    for product in products:
        if int(itemnumber) == int(product["id"]):
            product["name"]= input("Change name from : " + product["name"] + " to: ")
            product["aisle"]= input("Change aisle from : " + product["aisle"] + " to: ")
            product["department"]= input("Change aisle from : " + product["department"] + " to: ")
            product["price"]= input("Change price from : " + product["price"] + " to: ")

def destroy_product():
    itemnumber = input("Please enter the item number you want to destroy: ")
    for product in products:
        if int(itemnumber) == int(product["id"]):
            del product["id"]
            del product["name"]
            del product["aisle"]
            del product["department"]
            del product["price"]
    print(products)

print("There are " + str(len(products)) + " products in the database. Please select an operation:")
print("     operation  |  description")
print("     ---------  |  -------------------------------")
print("     'List'     |  Display a list of product identifiers and names.")
print("     'Show'     |  Show information about a product.")
print("     'Create'   |  Add a new product.")
print("     'Update'   |  Edit an existing product.")
print("     'Destroy'  |  Delete an existing product.")
print("     'Done'     |  Exit.")

while True:
    operation = 0
    itemnumber = 0

    operation = input("Please enter your operation: ")
    operation = operation.lower()

    numberofproducts = len(products)

    if operation == "list":
       for row in products:
           print (row)
    elif operation == "show":
        show_product()
    elif operation == "create":
        create_product()
    elif operation == "update":
        update_product()
    elif operation == "destroy":
        destroy_product()
    elif operation == "done":
         break
    else:
        print("Please try again")


other_path = "new_products.csv"
with open(other_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
