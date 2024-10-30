def create_a_team(teams):
    while True:
        team_name = input("Enter name of the team: ").lower()
        if team_name:
            if team_name not in teams:
                teams.append(team_name)
                print("Your team has been created successfully.")
            else:
                print("Team already exists.")
            break
        else:
            print("Please insert a correct name.")


def delete_a_team(teams):
    while True:
        team_name = input("Enter name of the team: ").lower()
        if team_name:
            for team in teams:
                if team_name == team:
                    teams.remove(team)
                    print("Your team has been deleted successfully.")
        print("Team does not exist.")
        break


def football():
    teams = []
    while True:
        option = input("Hello! Please choose an option:\n1. Add a team\n"
                       "2. Show teams\n3. Delete a team\n4. Exit\n")
        if option == "1":
            create_a_team(teams)
        elif option == "2":
            if teams:
                print("Teams:", ", ".join(teams))
            else:
                print("No teams created yet.")
        elif option == "3":
            delete_a_team(teams)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Please insert a correct option.")


football()
