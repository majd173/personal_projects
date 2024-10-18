
# def to_to():
#     tasks = []
#     while True:
#         print(
#             'What would you like to do?\n1. Add a new task.\n2. View all tasks\n3. Mark all() task async complete.\n4. Exit.\n')
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             task_name = input("Enter task name: ")
#             tasks.append(task_name)
#         elif choice == '2':
#             print(f'Current tasks: {tasks}')
#         elif choice == '3':
#             tasks = []
#         elif choice == '4':
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
#
# def contact():
#     contacts = []
#     while True:
#         print('Hello! here you can adda new contact!\nPlease choos an option:\n1. Add a new contact'
#               '\n2. View all contacts\n3. Search for a contact\n4. Delete a contact\n5. Exit')
#         choice = input('Enter your option here: ')
#         if choice == '1':
#             contact_name = input('Enter contact name: ')
#             contact_id = input('Enter contact id: ')
#             contact_phone_number = input('Enter contact phone number: ')
#             contacts.append({'name': contact_name, 'id': contact_id, 'phone_number': contact_phone_number})
#         elif choice == '2':
#             print(contacts)
#         elif choice == '3':
#             contact_name = input('Enter contact name: ')
#             for contact in contacts:
#                 if contact['name'] == contact_name:
#                     print(contact)
#                 else:
#                     print('Contact not found')
#         elif choice == '4':
#             contact_name = input('Enter contact name: ')
#             for contact in contacts:
#                 if contact['name'] == contact_name:
#                     contacts.remove(contact)
#                 else:
#                     print('Contact not found')
#         elif choice == '5':
#             break
#         else:
#             print('Invalid choice. Please try again.')
#
#
# def quiz():
#     quizes = [{'quiz_1': 'Whats is the capital city of Nigeria?',
#                'options': ['Abuja', 'Lagos', 'Ibadan', 'Kano'],
#                'answer_1': 'Abuja'},
#               {'quiz_2': 'Who is the president of USA?',
#                'options': ['Donald Trump', 'Joe Biden', 'Barak Obama', 'Bill Clinton'],
#                'answer_2': 'Joe Biden'}]
#     correct_answers = 0
#     while True:
#         print(
#             'Welcome to the quizes program! lets start:')
#         print(f'{quizes[0]["quiz_1"]}\nOptions: {quizes[0]["options"]}')
#         answer = input('Enter your answer: ')
#         if answer == quizes[0]['answer_1']:
#             print('Correct')
#             correct_answers += 1
#         else:
#             print('Wrong')
#         print(f'{quizes[1]["quiz_2"]}\nOptions: {quizes[1]["options"]}')
#         answer = input('Enter your answer: ')
#         if answer == quizes[1]['answer_2']:
#             print('Correct')
#             correct_answers += 1
#         else:
#             print('Wrong')
#         print(f'Your score: {correct_answers} of {len(quizes)}')
#         break
#
#
# def quiz_2():
#     # List of quizzes with questions, options, and correct answers
#     quizzes = [
#         {
#             'question': 'What is the capital city of Nigeria?',
#             'options': ['Abuja', 'Lagos', 'Ibadan', 'Kano'],
#             'answer': 'Abuja'
#         },
#         {
#             'question': 'Who is the president of the USA?',
#             'options': ['Donald Trump', 'Joe Biden', 'Barack Obama', 'Bill Clinton'],
#             'answer': 'Joe Biden'
#         },
#         {
#             'question': 'What is the largest planet in our solar system?',
#             'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
#             'answer': 'Jupiter'
#         }
#     ]
#
#     correct_answers = 0
#
#     print('Welcome to the quiz program! Let\'s start:\n')
#
#     for quiz in quizzes:
#         # Display question and options
#         print(quiz['question'])
#         for idx, option in enumerate(quiz['options'], start=1):
#             print(f"{idx}. {option}")
#
#         # Input from user
#         answer = input('Enter your answer (type the option number or the answer): ')
#
#         # Check if the answer matches either the number or the actual answer
#         if answer.isdigit():
#             answer_index = int(answer) - 1
#             if answer_index >= 0 and answer_index < len(quiz['options']):
#                 selected_answer = quiz['options'][answer_index]
#                 if selected_answer == quiz['answer']:
#                     print('Correct!')
#                     correct_answers += 1
#                 else:
#                     print('Wrong! The correct answer is:', quiz['answer'])
#             else:
#                 print('Invalid option number!')
#         else:
#             if answer.strip() == quiz['answer']:
#                 print('Correct!')
#                 correct_answers += 1
#             else:
#                 print('Wrong! The correct answer is:', quiz['answer'])
#
#         print()  # Blank line for better readability
#
#     print(f'Your score: {correct_answers} out of {len(quizzes)}.')
#
#
# # Run the quiz
# quiz_2()
import os

# ----------------------------------------------------------------------------------------------------

class Bank:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = float(balance)


    def __str__(self):
        print(f"Name: {self.name}\nAccount number: {self.account_number}\nBalance: {self.balance}")

    def deposit(self, amount):
        amount = float(amount)
        if amount >= 0:
            self.balance += amount
            print(f"Hey {self.name}! Deposit Successful. New balance is {self.balance}.")
        else:
            if amount < 0:
                print("Amount cannot be negative.")

    def withdraw(self, amount):
        amount = float(amount)
        if amount >= 0:
            self.balance -= amount
            print(f"Hey {self.name}! Withdrawal Successful. New balance is {self.balance}.")
        else:
            if amount < 0:
                print("Amount cannot be negative.")

    def check_balance(self):
        print(f"Hey {self.name}! Balance is {self.balance}.")



def main():
    print("Welcome to python bank!\nPlease choose an option:\n1. Create an account."
          "\n2. Exit.")
    while True:
        option = input("Write your option: ")
        if option == "1":
            name = input("Please enter your name: ")
            account_number = input("Please enter your account number: ")
            balance = input("Please enter your balance: ")
            customer = Bank(name, account_number, balance)
            print("Your account has been created.")
            print("Please choose an option:\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Exit.")
            while True:
                option = input("Please insert your option: ")
                if option == "1":
                    amount = input("Please enter the amount you want to deposit: ")
                    customer.deposit(float(amount))
                elif option == "2":
                    amount = input("Please enter the amount you want to withdraw: ")
                    customer.withdraw(float(amount))
                elif option == "3":
                    customer.check_balance()
                elif option == "4":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            if option == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


main()
