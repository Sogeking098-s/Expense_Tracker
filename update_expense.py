import json
import argparse
from datetime import datetime

def update_expense(id,name = None,amount=None):
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
        print("No expense added this month please add")
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
    if type(name) == str:
        to_change["Description"] = name
        with open("storage.json", "w") as create:
            json.dump(file,create,indent=4)
    if type(amount) == int:
        to_change["Amount"] = amount
        with open("storage.json","w") as create:
            json.dump(file,create,indent=4)
    else:
        print("Please for god sake be valid")
        return

# parser = argparse.ArgumentParser()
# main_argument= parser.add_subparsers(dest="command",help="Enter --id to update the id and --name to edit the name or --amount to edit the amount")
# argument=main_argument.add_parser("update")
# argument.add_argument("--id",type=int,required=True,help="Enter the id you want to edit he expense")
# argument.add_argument("--name",type=str,help="Enter --name to edit the name")
# argument.add_argument("--amount",type=int,required=True,help="Enter --amount to edit the amount")
# args=parser.parse_args()

# if not args.name and not args.amount:
#     print("At least use --name or --amount after update")


# update_expense(args.id,args.name, args.amount)
    


