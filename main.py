from utils import add_expense

def main():
    print("=== student expence tracker ===")
    
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
    
if __name__ == "__main__" :
    main()