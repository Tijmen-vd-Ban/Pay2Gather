"""
Tijmen van den Ban

"Pay 2 Gather"

Version: 1.0

Inputs: Asks the user to add a group, remove a group, select a group, add members to a selected group, add transactions
        to the selected group, remove transactions form selected group, update transaction within a group.

Outputs: Print list of options, Print list of groups, Print list of member within a group, Print list of transactions
        of a group, Print list of transactions for each member within a group.

Description: This program helps to keep track of purchases that have been done by a group and show the user how much
            each member of the group payed, and how much they are in debt with members within the same group. The user
            can create multiple groups, each with their own members.
"""
from Group import Group


# This functions allows the user to make a new group and give it a name
def add_group():
    name = input("What is the name of your group: \n")
    new_group = Group(name)
    groups.append(new_group)


# This Function allows the user to delete a group
def remove_group(group):
    groups.remove(group)
    print(f"{group.group_name} successfully removed.")


# This Function allows the user to add a member to a group by defining his/her firstname and lastname
def add_member_to_group(group):
    while True:
        firstname = input("What is the firstname: ")
        lastname = input("What is the lastname: ")
        group.add_member(firstname, lastname)  # function of the group class
        print(f"{firstname} {lastname} added to {group.group_name}.\n")

        # This part of the function allows the user to easily add another member to the group without going through
        # the menu again
        add_another_member = input("Add another member? 'Y' for yes, 'N' for no: ").lower()
        if add_another_member == "n":
            break
        elif add_another_member != "y" and add_another_member != "n":
            print(f"This is not a valid option.")
            break


# This functions allows the user to add transactions to the group by defining the person that payed, the subject of
# the payment and the amount he/her payed for it
def add_transaction_to_group(group):
    while True:
        group.print_member_list()  # Show the list of members within th group

        # Asks the user to input the index number of the member in the list that payed
        member_index = int(input("Select the index number of the member that payed: ")) - 1

        if 0 <= member_index < len(group.members):  # makes sure you select a valid option
            member_payed = group.members[member_index]
            subject = input("What did her/she pay for: ")  # Ask the user for the subject of the payment
            # ("restaurant", "groceries", "football tickets" etc.)

            amount = float(input("What was the total amount: "))  # Ask the user for the total amount of the payment

            group.add_transaction(member_payed, amount, subject)
            print(f"{member_payed.firstname} {member_payed.lastname} payed ${amount} for {subject}.\n")
        else:
            print(f"This is not a valid option")

        # This part of the functions allows the user to easily add another transaction to the group without going
        # through the menu again
        add_another_transaction = input("Add another transaction? 'Y' for yes, 'N' for no: ").lower()
        if add_another_transaction == "n":
            break
        elif add_another_transaction != "y" and add_another_transaction != "n":
            print(f"This is not a valid option.")
            break


def remove_transaction_from_group(group):
    while True:

        # Prints the transactions of this group so
        group.print_group_transactions()

        #  Asks the user to input the index number of the transaction he/she wants to remove
        index = int(input("Select the index number of the transaction you want to remove: ")) - 1

        #  Makes sure the input value is valid for further processing
        if 0 <= index < len(group.transactions):
            print(f"Item is removed.\n")

            #  removes the transaction from the list.
            group.remove_transaction(index)  # Function of the group class
        else:
            print(f"This is not a valid option.")

        # This part of the functions allows the user to easily remove another transaction from the group without going
        # through the menu again
        remove_another_transaction = input("Remove another transaction? 'Y' for yes, 'N' for no: ").lower()
        if remove_another_transaction == "n":
            break
        elif remove_another_transaction != "y" and remove_another_transaction != "n":
            print(f"This is not a valid option.")
            break


def update_transaction_in_group(group):
    while True:
        group.print_group_transactions()  # Show the list of transactions within th group
        index = int(input("Select the index number of the transaction that needs to be updated: ")) - 1

        #  Makes sure the input value is valid for further processing
        if 0 <= index < len(group.transactions):
            subject = input("What did her/she pay for: ")
            amount = float(input("What was the total amount: "))

            #  Updates the the transaction with new values
            group.update_transaction(index, amount, subject)  # function from the group class
            print(f"Transaction for {subject} was updated.")
        else:
            print(f"This is not a valid option.")

        # This part of the functions allows the user to easily update another transaction of the group without going
        # through the menu again
        update_another_transaction = input("Update another transaction? 'Y' for yes, 'N' for no: ").lower()
        if update_another_transaction == "n":
            break
        elif update_another_transaction != "y" and update_another_transaction != "n":
            print(f"This is not a valid option.")
            break


# Function that prints the transactions of the group
def print_transactions_of_this_group(group):
    group.print_group_transactions()


# Function that prints the transaction of each member within the group
def print_transactions_of_the_members(group):
    group.print_members_transactions()


# Function that prints the list of members of the group
def print_list_of_group_members(group):
    group.print_member_list()


# Function that prints a list of all groups
def list_of_groups():
    print("All groups:")
    for group in groups:
        print(f"\t{groups.index(group) + 1}. {group.group_name}")
    print(f" ")


# Print a list of all the general options when you start the application
def print_general_options():
    print(f"Options: \n"
          f"\t 1. Add group\n"
          f"\t 2. Select group\n"
          f"\t 3. Remove group\n"
          f"\t 4. Print list of groups\n"
          f"\t 5. Print options\n"
          f"\t 6. Quit program\n")


# Prints a list of the options when you have selected the group for further processing
def print_process_options():
    print(f"Options: \n"
          f"\t 1. Add members to this group\n"
          f"\t 2. Add transaction\n"
          f"\t 3. Remove transaction\n"
          f"\t 4. Update transaction\n"
          f"\t 5. Print transactions of the group\n"
          f"\t 6. Print transactions of the members\n"
          f"\t 7. Print list of group members\n"
          f"\t 8. Quit selected group\n")


groups = []  # list of all the groups
print_general_options()  # Print a the general options.

# This part of the code allows the user to go through the menu's and add groups, remove a group, add members to a group,
# add transactions, remove transactions and update transactions
while True:

    option = input("Select option by entering a valid number: \n")  # Asks the user to select an option

    # Makes sure that the option selected is a valid option.
    if option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6":
        print(f"This is not a valid option. Try again")

    else:
        option_nr = int(option)  # cast the input to an int to be used for the rest

        # Option 1 allows the user to add a group
        if option_nr == 1:
            add_group()

        # Option 2 allows the user to select a group to do further processing
        elif option_nr == 2:
            list_of_groups()
            index_nr = int(input("Select option by entering a valid number: \n")) - 1

            selected_group = groups[index_nr]  # Select the group to do further processing

            print_process_options()

            # Starts the menu to allow the user to do any processing for the selected group
            while True:
                process_option = input("Select option by entering a valid number: \n")

                # Makes sure that the option selected is a valid option.
                if process_option != "1" and process_option != "2" and process_option != "3" and process_option != "4" \
                        and process_option != "5" and process_option != "6" and process_option != "7"\
                        and process_option != "8":
                    print(f"This is not a valid option. Try again")
                else:
                    process_option_nr = int(process_option)  # cast input to an int

                    # Option 1 allows the user to add members to the selected group
                    if process_option_nr == 1:
                        add_member_to_group(selected_group)

                    # Option 2 allows the user to add transactions to the selected group
                    elif process_option_nr == 2:
                        add_transaction_to_group(selected_group)

                    # Option 3 allows the user to remove a transaction from the selected group
                    elif process_option_nr == 3:
                        remove_transaction_from_group(selected_group)

                    # Option 4 allows the user to update a transaction of the selected group
                    elif process_option_nr == 4:
                        update_transaction_in_group(selected_group)

                    # Option 5 allows the user to print the transaction of the selected group
                    elif process_option_nr == 5:
                        print_transactions_of_this_group(selected_group)

                    # Option 6 allows the user to print the transaction history for each member within the
                    # selected group
                    elif process_option_nr == 6:
                        print_transactions_of_the_members(selected_group)

                    # Option 7 allows the list of members of the selected group
                    elif process_option_nr == 7:
                        print_list_of_group_members(selected_group)

                    # Option 8 allows the user to quit the selected group and go back the the general options
                    elif process_option_nr == 8:
                        break

                    # Show this if it is not a valid input
                    else:
                        print(f"This is not a valid option. Try again.")

        # Option 3 allows the user to remove a group
        elif option_nr == 3:
            list_of_groups()
            group_to_remove = groups[int(input("Select the group you want to remove: ")) - 1]
            remove_group(group_to_remove)

        # Option 4 allows the use to print a list of the groups
        elif option_nr == 4:
            list_of_groups()

        # Option 5 allows the user to print the general options
        elif option_nr == 5:
            print_general_options()

        # Option 6 allows the user to quit the application
        elif option_nr == 6:
            print(f"Shutting down...")
            break

        # Show this if it is not a valid input
        else:
            print(f"This is not a valid option. Try again.")
