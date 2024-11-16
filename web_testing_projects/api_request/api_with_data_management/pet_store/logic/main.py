from web_testing_projects.api_request.api_with_data_management.pet_store.infra.api_wrapper import ApiWrapper
from web_testing_projects.api_request.api_with_data_management.pet_store.logic.home_page import ApiHomePage


def new_options():
    try:
        option = input("Please choose an option:\n1. Get pet by id\n2. Show pets\n3. Exit\n")
        if option == "1":
            pet_id = input("Enter pet id: ")
            new_pet = ApiHomePage(ApiWrapper())
            new_pet.save_pet(pet_id)
        elif option == "2":
            new_pet = ApiHomePage(ApiWrapper())
            new_pet.get_all_pets()
        elif option == "3":
            print("Thank you for using pet store app!")
            exit()
        else:
            print("Please insert a correct option.")
    except Exception as e:
        print(e)


def main():
    while True:
        try:
            print("Welcome to pet store app!")
            option = input("Please choose an option:\n1. Get pet by id\n2. Exit\n")
            if option == "1":
                pet_id = input("Enter pet id: ")
                new_pet = ApiHomePage(ApiWrapper())
                new_pet.save_pet(pet_id)
                while True:
                    try:
                        new_options()
                    except Exception as e:
                        print(e)
            elif option == "2":
                print("Thank you for using pet store app!")
                break
            else:
                print("Please insert a correct option.")
        except Exception as e:
            print(e)


main()
