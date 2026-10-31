from utils import add_expense , get_all_expenses , set_budget ,get_budget, get_total_expenses,get_remaining_budget,get_expenses_by_category,export_expenses_to_csv

def main():
    print("=== Student Expense Tracker ===")
    
    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. View Summary(Total, budget, remaining)")
        print("4. set budget")
        print("5. Exit")
        print("6. Export expenses to CSV")
    
        choice = input("enter your choice (1/2/3/4/5/6) : ").strip()
        
        if choice=="1":       
            while True:
                category=input("Category (e.g. Food,Travel,Books):").strip()
                if category:
                    break
                print("Category cannot be empty.")
                
            while True:     
                amount_str=input("Amount (price): ").strip()
                try:
                    amount=float(amount_str)
                    if(amount<=0):
                        print("Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number for amount.")
                    
            while True:
                description=input("Description (short note) : ").strip()
                if description:
                    break
                print("Description cannot be empty.")
            
            add_expense(category, amount, description)
            
            print("Expense added successfully.")
            
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
            total = get_total_expenses()
            budget = get_budget()
            remaining = get_remaining_budget()
            category_totals=get_expenses_by_category()
            
            print("=== Summary ===")
            print("Total Expenses",total)
            print("Budget",budget)
            print("Remaining",remaining)
            
            print("\nCategory-wise expenses:")
            if not category_totals:
                print("No expenses yet.")
            else:
                for category, amount in category_totals.items():
                    print(category, ":", amount)
            
        elif choice=="4":
            while True:
                budget_str=input("Enter budget (taka) :").strip()
                try:
                    budget=float(budget_str)
                    if(budget<=0):
                        print("Budget must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number for budget.")
                    
            set_budget(budget)
                
            print("Budget set successfully")
            print("Current budget : ",get_budget())
                
        elif choice =="5":
            print("Goodbye")
            break
        
        elif choice=="6":
            filename=export_expenses_to_csv()
            if filename:
                print("Expenses exported to :",filename)
                    
        else:
            print("Invalid choice, please try again.")
        
        
    
if __name__ == "__main__" :
    main()