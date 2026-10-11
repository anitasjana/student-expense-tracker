from utils import add_expense , get_all_expenses

def main():
    print("=== student expence tracker ===")
    
    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. Exit")
    
        choice = input("enter your choice (1/2/3) : ").strip()
        
        if choice=="1":
            category=input("Category (e.g. Food,Travel,Books):").strip()
            
            while True:
                amount_str=input("Amount (price): ").strip()
                try:
                    amount=float(amount_str)
                    break
                except ValueError:
                    print("Please enter the valid number of value.")
            
            description=input("Description (short) : ").strip()
            
            add_expense(category, amount, description)
            
            print("Expence added successfully.")
            
        elif choice=="2":
            expenses=get_all_expenses()
            
            if not expenses:
                print("No expenses yet.")
                
            else:
                for exp in expenses:
                    print("Date : ",exp["date"])
                    print("category : ",exp["category"])
                    print("amount : ",exp["amount"])
                    print("description : ",exp["description"])
                    print("-"*30)
                    
        elif choice=="3":
            print("Goodbye")
            break
        
        else:
            print("Invalid choice, please try again.")
        
        
    
if __name__ == "__main__" :
    main()