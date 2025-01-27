import json
import argparse
from datetime import datetime
import calendar
def delete(id,month=None):
    try:
        with open ("storage.json", "r") as delete:
            file = json.load(delete)
    except FileNotFoundError:
            print("Pls use add command to add the a expense because no expense file exits")
            return
    if month:
        time = calendar.month_name[month]
    else:
        time=datetime.now().strftime("%B")
    if time not in file or not isinstance(file[time], list) or not file[time]:
        print("No file with that exits")
    expense = file[time]
    cut = None
    for remove in expense:
        if remove.get("Id") == int(id):
            cut = remove
            break
    else:
        print(f"No expense exits with the {id}")
        return
    expense.remove(cut)
    print(f"The file with  id {id} has been removed in {time}")
    for index,task in enumerate(expense):
        task["Id"] = index + 1

    with open("storage.json","w") as update:
        json.dump(file,update,indent=4)

# parser = argparse.ArgumentParser()

# main_argument = parser.add_subparsers(dest="command",help="To delete any paticular expense")
# argument = main_argument.add_parser("delete", help="delete --id (Id of the expense you want to delete)")
# argument.add_argument("--id",type=int,required=True, help="To delete a paticular expense")

# args = parser.parse_args()

# delete(args.id)