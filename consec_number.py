#To give even and odd positioned values
#gets inputs based on number of contents needed by user
print("Odd or Even")
input_list = []
success = False

#splitting logic
def oddeven_logic(x):
    print("\nOutput : ")
    for i in x:
        evenval = ''
        oddval = ''
        Even = True
        for j in i:
            if Even:
                evenval = evenval + j
                Even = False
            else:
                oddval = oddval + j
                Even = True
        print(f'even string is {evenval} and odd string is {oddval}')

while not success:
    inp_no = input("Enter no. of lines : ")
    try:
        if (int(inp_no) > 0):
            for i in range(int(inp_no)):
                contents = input(f'Enter content {i + 1}: ')
                if not len(contents) < 2:
                    input_list.append(contents)
                else:
                    print(f"Content {i + 1} can't be splitted")
            oddeven_logic(input_list)
            success = True
        else:
             print("No. of lines should be a positive value")

    except ValueError:
             print("Expected only numerical values!")
