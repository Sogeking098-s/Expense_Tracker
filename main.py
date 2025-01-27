import add_expense
import argparse
import update_expense
import display_expense
import delete_expense

parser = argparse.ArgumentParser()
main_argument = parser.add_subparsers(dest = "command")

# For add
add_argument = main_argument.add_parser("add", help = "--name (Name of the expense) --amount (Amount spent)")
add_argument.add_argument("--month",type=int,help="If you want to add your expense in a specific month or by defualt it will be current month --month (Num of the month)")
add_argument.add_argument("--name", type=str , required=True , help = "Add the name of the expense")
add_argument.add_argument("--amount", type=int , required=True , help = "Add the amount of the expense")

# args = parser.parse_args()

# for delete
delete_argument = main_argument.add_parser("delete", help="delete --id (Id of the expense you want to delete)")
delete_argument.add_argument("--month",type=int,help="If you want to delete your expense in a specific month or by defualt it will be current month --month (Num of the month)")
delete_argument.add_argument("--id",type=int,required=True, help="To delete a paticular expense")

# args = parser.parse_args()

# delete_expense.delete(args.id)


# parser = argparse.ArgumentParser()
# to list
list_argument=main_argument.add_parser("list", help="Enter --id to list a paticular id or --all to list all the expense of the current month")
list_argument.add_argument("--month",type=int,help="If you want to list your expense in a specific month or by defualt it will be current month --month (Num of the month)")
list_argument.add_argument("--id",type=int,help="Enter --id (Id) of the expenese")
list_argument.add_argument("--all",action="store_true",help="Enter --all to list all the expense in hte month")
list_argument.add_argument("--total",action="store_true",help="Enter to find teh total expenses of the month")

# args = parser.argsparser()

# if not args.id or args.add:
#     print("Please enter a valid argument")
# if args.add:
#     try:
#         with open("storage.json", "r") as update:
#             file = json.load(update)
#     except ValueError:
#         print("The file is empty please enter a valid input")
#         exit()
#     except FileNotFoundError:
#         print("No json file to store exits please add first")
#         exit
#         current = datetime.now().strftime("%B")
#         if current not in file:
#             print("No expense added this month please add a expense")
#             exit
#     change = file[current]
#     for to_change in change:
#         print(f"Id : {to_change['Id']}")
#         print(f"Description : {to_change['Description']}")
#         print(f"Amount : {to_change['Amount']}")
#         exit()
# else:
#     display_expense(args.id)

# parser = argparse.ArgumentParser()
# To update
update_argument=main_argument.add_parser("update")
update_argument.add_argument("--month",type=int,help="If you want to list your expense in a specific month or by defualt it will be current month --month (Num of the month)")
update_argument.add_argument("--id",type=int,required=True,help="Enter the id you want to edit he expense")
update_argument.add_argument("--name",type=str,help="Enter --name to edit the name")
update_argument.add_argument("--amount",type=int,help="Enter --amount to edit the amount")


args=parser.parse_args()

if args.command == "add":
    add_expense.add(args.name,args.amount,args.month)
elif args.command == "delete":
    delete_expense.delete(args.id,args.month)
elif args.command == "update":
    update_expense.update_expense(args.id,args.name,args.amount)
elif args.command == "list":
    display_expense.display_expense(args.id,args.all,args.total,args.month)
else:
    print("Enter add --month(if you want to add expense in different month than current) --name(Name of the expense) --amount(Enter the amount you spent)")
    print("ENter delete --month(if you want to delete expense in different month than current) --id (Enter the id to delete)")
    print("Enter list --month(if you want to list expense in different month than current) --id (To list a paticular id) --all (To list every expense) --total (For total spent)")
    print("Enter update --month(if you want to add expense in different month than current) --id (Id of the expense) --name (To change the name) --amount (To change the amount) ")


# update_expense(args.id,args.name,args.amount)