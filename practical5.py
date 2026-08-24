print("================= Monthly Expensentr tracker ======================")

n=int(input("Enter the number if initial expenses :"))

expenses=[]
total=0

for i in range (n):
    amount=float(input(f"Enter expenses{i+1}:"))
    expenses.append(amount)
    total+=amount

while True:
    print("\n--------------- Expenese Tracker Menu------------------------")
    print("1. Show All Expenses ")
    print("2. Show Total Expenses ")
    print("3. Add new Expenses ")
    print("4. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        print("\nExpense List :")
        for i in range(len(expenses)):
            print(f"Expense{i+1}:{expenses[i]}")
    elif choice==2:
        print("Total Monthly  Expense =",total)
    elif choice==3:
        new_expense =float(input("Enter  new expenses :"))
        expenses.append(new_expense)
        total+=new_expense
    elif choice==4:
        print("Thank You for using the Monthly Expenses Tracker !")
        break
    else:
        print("Invalid choice! Please try again .")