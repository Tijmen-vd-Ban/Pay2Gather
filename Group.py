from Member import Member
from Transaction import Transaction


class Group:
    #  This function will make a new group
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []  # List of members within this group
        self.transactions = []

    # This function makes it possible to add members to this group
    def add_member(self, firstname, lastname):
        member = Member(firstname, lastname)  # Make a new member
        self.members.append(member)  # Add new member to the group

    # This function will add a transaction to the group and will divide the amount that has been payed over the total
    # amount of members within this group
    def add_transaction(self, member_payed,  amount, subject):
        total_amount_of_members = len(self.members)  # Total amount of members in this group
        amount_per_member = float(amount / total_amount_of_members)  # Portion of the payment for each member

        # Calculating the amount for the member that payed to be added to his/her transaction history.
        # Amount = portion of the payment * (all members -(minus) him/herself)
        amount_member_payed = amount_per_member * (total_amount_of_members - 1)

        # Adding the transaction to the top of the list (index 0). To show the most recent transaction.
        self.transactions.insert(0, Transaction(float(amount), subject))

        #  Make a separate transaction for the member that payed
        transaction_for_member_payed = Transaction(amount_member_payed, subject)

        #  And a make a transaction for the rest of the members within the group
        transaction_rest_of_the_group = Transaction(-amount_per_member, subject)

        #  Add the portion of payment to each member within the group.
        for member in self.members:
            if member.firstname == member_payed.firstname and member.lastname == member_payed.lastname:
                member.add_transaction(transaction_for_member_payed)  # Method from the member class
            else:
                member.add_transaction(transaction_rest_of_the_group)  # Method from the member class

    # This function will remove the transaction from the group and from the members itself
    def remove_transaction(self, number):
        index_nr = number
        self.transactions.remove(self.transactions[index_nr])  # remove the transaction from the group

        # Remove the transaction from the transaction history for each member
        for member in self.members:
            member.remove_transaction(index_nr)

    #  This function will update the transaction with new values in cas mistake were made
    def update_transaction(self, number, amount, subject):
        index_nr = number
        total_amount_of_members = len(self.members)  # Total amount of members in this group
        amount_per_member = float(amount / total_amount_of_members)  # Portion of the payment for each member

        # Calculating the amount for the member that payed to be added to his/her transaction history.
        # Amount = portion of the payment * (all members -(minus) him/herself)
        amount_member_payed = amount_per_member * (total_amount_of_members - 1)

        #  Replace the old transaction of this group with the updated version
        self.transactions[index_nr] = Transaction(amount, subject)

        #  Make a separate transaction for the member that payed
        transaction_for_member_payed = Transaction(amount_member_payed, subject)

        #  And a make a transaction for the rest of the members within the group
        transaction_rest_of_the_group = Transaction(-amount_per_member, subject)

        #  Add the portion of payment to each member within the group.
        for member in self.members:
            transaction = member.transactions[index_nr]
            if transaction.amount > 0:
                member.update_transaction(index_nr, transaction_for_member_payed)  # Method from the member class
            else:
                member.update_transaction(index_nr, transaction_rest_of_the_group)  # Method from the member class

    # Print a list of members and their transaction history and their current balance within the group
    def print_members_transactions(self):
        print(f"{self.group_name}:")
        for member in self.members:
            print(f"{member.firstname} {member.lastname}: {member.balance:.2f}")
            member.print_transactions()

    # Print the transaction history of the group
    def print_group_transactions(self):
        print(f"{self.group_name}:")
        for transaction in self.transactions:
            print(f"\t{self.transactions.index(transaction) + 1}. {transaction.amount}: {transaction.subject}")
        print()

    # Print list of members within this group
    def print_member_list(self):
        print(f"Members:")
        for member in self.members:
            print(f"\t{self.members.index(member) + 1}. {member.firstname} {member.lastname}")
