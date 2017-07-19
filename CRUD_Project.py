import csv

numberofproducts = 0

products = []
with open("CRUD_Project.csv") as myfile:
    firstline = True
    for line in myfile:
        numberofproducts = numberofproducts + 1
        if firstline:
            mykeys = "".join(line.split()).split(',')
            firstline = False
        else:
            values = "".join(line.split()).split(',')
            products.append({mykeys[n]:values[n] for n in range(0,len(mykeys))})

print("There are " + str(numberofproducts) + " products in the database. Please select an operation:")
print("")
print("     operation  |  description")
print("     ---------  |  -------------------------------")
print("     'List'     |  Display a list of product identifiers and names.")
print("     'Show'     |  Show information about a product.")
print("     'Create'   |  Add a new product.")
print("     'Update'   |  Edit an existing product.")
print("     'Destroy'  |  Delete an existing product.")
print("     'Done'     |  Exit.")

operation = 0

operation = input("Please enter your operation: ")

# if operation == "list" or "List" or "LIst" or "LIST":

if operation == "Show":
    ProductID = input("Please enter your products Identifier: ")
    for product in products:
        if int(ProductID) == int(product["id"]):
            price_usd = '${0:.2f}'.format(product["price"])
            print("Product Name: " + product["name"] + "Product Aisle: " + product["Aisle"] + "Department: " + product["Department"] + " (" + price_usd + ")")
            subtotal=subtotal+product["price"]
if operation == "Update":
    itemnumber = input("Please Enter The Item Number You want to change: ")
    for itemnumber in result:
        if int(itemnumber) == int(product["id"]):
            product["name"]= input("Change name from : " + product["name"] + " to: ")
            product["aisle"]= input("Change aisle from : " + product["asisle"] + " to: ")
else:
    print("Please try again")
    # if operat ion == "Done" or "DOne" or "done":
    #     break
    # else
    #     break
    #     print("Please use a known operation")
