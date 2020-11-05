
def solve(meal_cost, tip_percent, tax_percent):
    after_tip = meal_cost * (tip_percent / 100)
    after_tax = meal_cost * (tax_percent / 100)
    
    print("The total meal cost is %s dollars." % int(round(meal_cost + after_tip + after_tax)))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)