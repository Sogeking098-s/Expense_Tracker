import json
from datetime import datetime
import calendar

def add(name,amount,month=None):
    file = "storage.json"
    if month:
        time = calendar.month_name[month]
    else:
        time = datetime.now().strftime("%B")
    try:
        with open ("storage.json", "r") as addition:
            data = json.load(addition)
    except FileNotFoundError:
        with open ("storage.json", 'w') as create:        
            json.dump({},create, indent=4)
    except ValueError:
        with open ("storage.json", 'w') as create:        
            json.dump({},create, indent=4)
    if time not in data:
            data[time] = []

    data[time].append({"Id":len(data[time]) + 1,"Description" : name, "Amount" : amount})
    with open ("storage.json",'w') as expesne:
                json.dump(data,expesne,indent=4)
    print(f"The expense {name} has been add with the amount {amount} in {time}")

# parser = argparse.ArgumentParser()

# main_argument = parser.add_subparsers(dest = "command")

# argument = main_argument.add_parser("add", help = "--name (Name of the expense) --amount (Amount spent)")
# #argument.add_argument("Help", help="--name (Name of the expense) --amount (Amount spent)")
# argument.add_argument("--name", type=str , required=True , help = "Add the name of the expense")
# argument.add_argument("--amount", type=int , required=True , help = "Add the amount of the expense")

# args = parser.parse_args()

# add(args.name,args.amount)
