import json
import os

DATA_FILE="data/expenses.json"

def load_data():  
    """Load expense data from the JSON file.
    
    returns:
        dict:A dictionary with 'budget' and 'expenses'.  
    """
    if not os.path.exists(DATA_FILE):
        return { "budget":0, "expenses":[] }
    try:
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            return (json.load(f))
    except (json.JSONDecodeError,OSError):
        print("Warning: Could not read data file. Starting with empty data.")
        return { "budget":0, "expenses":[] }
    
def save_data(data):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)

def add_expense(category, amount, description, date_str=None):
    from datetime import datetime
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    data = load_data()
    
    expense = {
        "date":date_str,
        "category":category,
        "amount":amount,
        "description":description
    }
    
    data["expenses"].append(expense)
    
    save_data(data)
    
def get_all_expenses():
    data=load_data()
    return data["expenses"]

def set_budget(amount):
    data=load_data()
    data["budget"]=amount
    save_data(data)

def get_budget():
    data=load_data()
    return data["budget"]

def get_total_expenses():
    data=load_data()
    total=0
    for exp in data["expenses"]:
        total+=exp["amount"]
    return total
    
def get_remaining_budget():
    budget=get_budget()
    total=get_total_expenses()
    return budget - total
    
def get_expenses_by_category():
    data=load_data()
    category_totals={}
    
    for exp in data["expenses"]:
        category=exp["category"]
        amount=exp["amount"]
        
        if category in category_totals:
            category_totals[category] +=amount
        else:
            category_totals[category] = amount
    return category_totals
import csv
def export_expenses_to_csv(filename="expenses_export.csv"):
    """Export all expenses to a CSV file.
    
    Args:
        filename(str):Name of the CSV file to create.
    
    Returns:
        str: Path of the created CSV file.
    """ 
    data=load_data()
    expenses=data["expenses"]
    
    try:
        with open(filename,"w", newline="",encoding="utf-8") as f:
            writer=csv.DictWriter(f,fieldnames=["date","category","amount","description"])
            writer.writeheader()
            
            for exp in expenses:
                writer.writerow(exp)
        return filename
    except OSError:
        print("Error: Could not write CSV file.")
        return None