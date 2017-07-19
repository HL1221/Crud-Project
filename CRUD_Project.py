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

# print("There are " + str(numberofproducts) + " products in the database. Please select an operation:
# print("     operation  |  description")
# print("     ---------  |  -------------------------------")
# print("     'List'     |  Display a list of product identifiers and names.")
# print("     'Show'     |  Show information about a product.")
# print("     'Create'   |  Add a new product.")
# print("     'Update'   |  Edit an existing product.")
# print("     'Destroy'  |  Delete an existing product.")
# print("     'Done'     |  Exit.")
#
operation = 0

# operation = input("Please enter your operation: ")

operation = "Show"

if operation == "List":
   for row in products:
       print (row)
elif operation == "Show":
    ProductID = input("Please enter your products Identifier: ")
    for product in products:
        if int(ProductID) == int(product["id"]):
            print(dict(product))
elif operation == "Create":
    print("pro")
elif operation == "Update":
    itemnumber = input("Please Enter The Item Number You want to change: ")
    for itemnumber in products:
        if int(itemnumber) == int(product["id"]):
            product["name"]= input("Change name from : " + product["name"] + " to: ")
            product["aisle"]= input("Change aisle from : " + product["asisle"] + " to: ")
else:
    print("Please try again")
