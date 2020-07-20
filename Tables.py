#Script to write maths tables based on user input
#gets two inputs, i. Table number ii. Table limit value
print("Maths Tables Generator")
success = False

#Table calculation logic
def table_logic(x,y):
    for i in range(1,(y+1)):
        print(f'{i} X {x} = {x * i}')

while not success:
    try:
        table_number = int(input("Enter the table number : "))
        table_limit = int(input("Enter the end limit of the table : "))
        if (table_number >= 0) & (table_limit >= 0):
             table_logic(table_number,table_limit)
             print("Table ends!")
             success = True
        else:
             print("The input values should be a positive integer")

    except ValueError:
             print("Expected only numerical values!")
