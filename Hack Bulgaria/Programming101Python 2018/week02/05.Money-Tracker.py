
def get_data(file): 
    file_o = open(file, "r")
    data = {}
    cur_date = ""
    price_type = []

    for line in file_o.readlines():
        if line[0:3] == "===":
            cur_date = ""
            for let in line:
                if let in "-1234567890":
                    cur_date += let
            data[cur_date] = {"expense": [], "income": []}
        elif "Income" in line:
            price_type = line.split(",")
            price_type[0] = dec_format(float(price_type[0]))
            data[cur_date]["income"].append((price_type[0], price_type[1][1:]))
        elif "Expense" in line:
            price_type = line.split(",")
            price_type[0] = dec_format(float(price_type[0]))
            data[cur_date]["expense"].append((price_type[0], price_type[1][1:]))
    return data    

def list_user_data(data):
    
    for date in data:
        print("=== " + date + " ===")
        for i in data[date]:
            if i == "expense":
                for j in data[date]["expense"]:
                    print(str(j[0]) + ", " + j[1] + ", New Expense")
            elif i == "income":
                for j in data[date]["income"]:
                    print(str(j[0]) + ", " + j[1] + ", New Income")

    print("\n\n")

def show_user_data_per_date(date, data):
    
    if date in data:
        print("=== " + date + " ===")
        for i in data[date]:
            if i == "expense":
                for j in data[date]["expense"]:
                    print(str(j[0]) + ", " + j[1] + ", New Expense")
            elif i == "income":
                for j in data[date]["income"]:
                    print(str(j[0]) + ", " + j[1] + ", New Income")
    else:
        print("No such date in the data!")

    print("\n\n")

def list_user_expenses_ordered_by_categories(data):   
    sorted_arr = []

    for date in data:
        for i in data[date]:
            if i == "expense":
                for j in data[date][i]:
                    sorted_arr.append(str(j[0]) + " " + j[1])
    item = []
    for el in sorted(sorted_arr):
        item = el.split(" ")
        print("Expense: " + item[0] + ", " + item[1])
    print("\n\n")    


def add_income(income_category, money, date, data):

    money = dec_format(money)
    if date in data:
        data[date]["income"].append((money, income_category))
    else:
        data[date] = {"expense":[], "income":[]} 
        data[date]["income"].append((money, income_category))

    print("\n\n")
    return data

def add_expense(expense_category, money, date, data):

    money = dec_format(money)
    if date in data:
        data[date]["expense"].append((money, expense_category))
    else:
        data[date] = {"expense":[], "income":[]} 
        data[date]["expense"].append((money, expense_category))

    print("\n\n")
    return data


def save_changes(data, file):
    
    file_o = open(file, "w")

    for date in data:
        file_o.write("=== " + date + " ===\n")
        for i in data[date]:
            if i == "expense":
                for j in data[date]["expense"]:
                    file_o.write(str(j[0]) + ", " + j[1] + ", New Expense\n")
            elif i == "income":
                for j in data[date]["income"]:
                    file_o.write(str(j[0]) + ", " + j[1] + ", New Income\n")
                
    file_o.close()

def dec_format(double):
    if double % 1 == 0: return int(double)
    return double

def main():

    data = get_data("files/money_tracker.txt")

    while True:
        print("Choose one of the following options to continue:")
        print("1 - show all data")
        print("2 - show data for specific date")
        print("3 - show expenses, ordered by categories")
        print("4 - add new income")
        print("5 - add new expense")
        print("6 - exit\n")

        command = input()
        try:
            command = int(command)
            if command not in range(1, 7):
                print("This number is invalid!\n")
            elif command == 1:
               list_user_data(data)
            elif command == 2:
                date = input("Enter a date: ")
                show_user_data_per_date(date, data)
            elif command == 3:
                list_user_expenses_ordered_by_categories(data)
            elif command == 4:
                while 1:
                    money = input("New income amount:\n")
                    try:
                        money = float(money)
                        if money < 0:
                            raise ValueError
                    except ValueError:
                        print("Enter a positive number!")
                    else:
                        break                     
                income_category = input("New income type:\n")
                date = input("New income date:\n")
                data = add_income(income_category, money, date, data)
            elif command == 5:
                while 1:
                    money = input("New expense amount:\n")
                    try:
                        money = float(money)
                        if money < 0:
                            raise ValueError
                    except ValueError:    
                        print("Enter a positive number!")
                    else:
                        break                     
                expense_category = input("New expense type:\n")
                date = input("New expense date:\n")
                data = add_expense(expense_category, money, date, data)
            elif command == 6:
                save_changes(data, "files/money_tracker.txt")
                break
        except ValueError:
            print("Enter an integer in range 1 to 6!\n")

if __name__ == "__main__":
    main()   