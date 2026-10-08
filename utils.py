import json
import os

DATA_FILE="data/expenses.json"

def load_data():  
    if not os.path.exists(DATA_FILE):
        return { "budget":0, "expenses":[] }
    
    with open(DATA_FILE,"r",encoding="utf-8") as f:
        return (json.load(f))
    
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
        
    