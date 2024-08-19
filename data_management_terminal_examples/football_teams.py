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


def football():
    teams = []
    while True:
        option = input("Hello! Please choose an option:\n1. Add a team\n2. Show teams\n3. Exit\n")
        if option == "1":
            create_a_team(teams)
        elif option == "2":
            if teams:
                print("Teams:", ", ".join(teams))
            else:
                print("No teams created yet.")
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Please insert a correct option.")


football()
