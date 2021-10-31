from Transaction import Transaction


class Member:
    #  This function will make a new member with his/her own balance and transaction history within a group
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = 0
        self.transactions = []

    #  The purpose of this function is to add transaction for each member within his/her group.
    def add_transaction(self, transaction):
        self.balance += float(transaction.amount)
        self.transactions.insert(0, Transaction(float(transaction.amount), transaction.subject))

    #  The purpose of this function is to remove a transaction if needed.
    def remove_transaction(self, index):
        self.balance -= float(self.transactions[index].amount)
        self.transactions.remove(self.transactions[index])

    #  The purpose of this function is to update a transaction with new values if mistakes were made.
    def update_transaction(self, index, updated_transaction):
        old_transaction_amount = self.transactions[index].amount
        self.balance -= old_transaction_amount  # Removing the old transaction amount from the balance.

        new_transaction_amount = updated_transaction.amount
        self.balance += new_transaction_amount  # Adding the new transaction amount to the balance

        # Replacing the old transaction with the updated version of the transaction.
        self.transactions[index] = Transaction(float(updated_transaction.amount), updated_transaction.subject)

    # This function prints out the member with his/her transaction history within his/her group
    def print_transactions(self):
        for transaction in self.transactions:
            if transaction.amount > 0:
                print(f"\t{self.transactions.index(transaction) + 1}. +{transaction.amount:.2f}: {transaction.subject}")
            else:
                print(f"\t{self.transactions.index(transaction) + 1}. {transaction.amount:.2f}: {transaction.subject}")
        print()
