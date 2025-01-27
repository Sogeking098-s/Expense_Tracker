import json
import calendar
from datetime import datetime

def display_expense(id=None,all=None,total=None,month=None):
    if all:
        try:
            with open("storage.json", "r") as update:
                file = json.load(update)
        except ValueError:
            print("The file is empty please enter a valid input")
            exit()
        except FileNotFoundError:
            print("No json file to store exits please add first")
            exit
        if month:
            current = calendar.month_name[month]
            if current not in file:
                print("No expense added this month please add a expense")
                exit
            change = file[current]
            print("-" * 20)
            for to_change in change:
                print(f"Id : {to_change['Id']}")
                print(f"Description : {to_change['Description']}")
                print(f"Amount : {to_change['Amount']}")
                print("-" * 20)
            return
        elif not month:
            for month, expenses in file.items():
                print(f"{month}:")
                print("-" * 20)
                for expense in expenses:
                    print(f"    Id: {expense['Id']}")
                    print(f"    Description: {expense['Description']}")
                    print(f"    Amount: {expense['Amount']}")
                    print("-" * 20)
    elif id:
        try:
            with open("storage.json", "r") as update:
                file = json.load(update)
        except ValueError:
            print("The file is empty please enter a valid input")
            return
        except FileNotFoundError:
            print("No json file to store exits please add first")
            return
        current = datetime.now().strftime("%B")
        if current not in file:
            print("No expense added this month please add a expense")
            return
        change = file[current]
        to_change = None
        for now in change:
            if now.get("Id") == id:
                to_change = now
                break
        else:
            print("Please enter a valid id")
            return
    
        print(f"Id : {to_change['Id']}")
        print(f"Description : {to_change['Description']}")
        print(f"Amount : {to_change['Amount']}")
    elif total:
        try:
            with open("storage.json","r") as sum:
                file = json.load(sum)
        except ValueError:
            print("The file is empty please add a value")
            return
        except FileNotFoundError:
            print("No such file exits you can add a expense to make a new file")
            return
        if month:
            time = calendar.month_name[month]
        else:
            time = datetime.now().strftime("%B")
        if not time in file or not isinstance(file[time],list) or not file[time]:
            print("You have not entered a expense this month")
        to_list =  file[time]
        sum = 0
        for show in to_list:
            sum = sum + show["Amount"]
        if sum != 0:
            print(f"You have spend {sum} in {time}")
            return
        else:
            print("You haven't spent a penny")

    else:
        print("Enter atleast one argument")



# def arguments():
    # parser = argparse.ArgumentParser()
    # main_argument = parser.add_subparsers(dest="command")
    # argument=main_argument.add_praser("list", help="Enter --id to list a paticular id or --all to list all the expense of the current month")
    # argument.add_argument("--id",type=int,help="Enter --id (Id) of the expenese")
    # argument.add_argument("--all",type=None,help="Enter --all to list all the expense in hte month")

    # args = parser.argsparser()

    # if not args.id or args.add:
    #     print("Please enter a valid argument")
    # if args.all:
    #     try:
    #         with open("storage.json", "r") as update:
    #             file = json.load(update)
    #     except ValueError:
    #         print("The file is empty please enter a valid input")
    #         exit()
    #     except FileNotFoundError:
    #         print("No json file to store exits please add first")
    #         exit
    #     current = datetime.now().strftime("%B")
    #     if current not in file:
    #         print("No expense added this month please add a expense")
    #         exit
    #     change = file[current]
    #     for to_change in change:
    #         print(f"Id : {to_change['Id']}")
    #         print(f"Description : {to_change['Description']}")
    #         print(f"Amount : {to_change['Amount']}")
    #         exit()
    # else:
    #     display_expense(args.id)