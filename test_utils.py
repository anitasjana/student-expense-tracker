from utils import (
    add_expense , 
    get_all_expenses , 
    set_budget ,
    get_budget, 
    get_total_expenses,
    get_remaining_budget,
    get_expenses_by_category,
)

def test_add_and_get_expense():
    """Test adding an expense and reading it back."""
    before=len(get_all_expenses())
    add_expense("Food",100,"test lunch")
    after=len(get_all_expenses())
    
    assert after == before+1,"expense was not added correctly"

def test_total_expense():
    """Test total expenses calculation."""
    total=get_total_expenses()
    
    assert total >= 0, "Total expenses should not be negative."
    
def test_budget_and_remaining():
    """Test budget test and remaining calculation."""
    set_budget(1000)
    budget=get_budget()
    remaining=get_remaining_budget()
    
    assert budget ==1000,"Budget was not set correctly."
    assert remaining == budget-get_total_expenses(),"Remaining budget calculation is wrong."
    
def test_category_totals():
    """Test category-wise expense totals. """
    add_expense("Food",50,"test snack")
    totals=get_expenses_by_category()
    
    assert "Food" in totals,"Food category should be present in torals."
    assert totals["Food"]>0,"Food total should be greater then 0."
    
    
if __name__=="__main__":
    test_add_and_get_expense()
    test_total_expense()
    test_budget_and_remaining()
    test_category_totals()
    print("All test passed.")
