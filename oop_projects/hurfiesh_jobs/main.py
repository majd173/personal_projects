from oop_projects.hurfiesh_jobs.jobs import Job
from oop_projects.hurfiesh_jobs.professional import Professional


def add_professional():
    while True:
        name = input("Enter professional name: ").lower()
        if not name:
            print("Name cannot be empty.")
            continue
        if not name.isalpha():
            print("Name must be alphabetic.")
            continue
        break
    while True:
        phone_input = input("Enter professional phone: ")
        # Check if the phone number is a digit and has the correct length
        if not phone_input.isdigit():
            print("Phone number must be a number.")
            continue
        phone_length = len(phone_input)
        if phone_length < 9 or phone_length > 11:
            print("Phone number must be 9-11 digits.")
            continue
        phone = int(phone_input)
        break
    while True:
        profession = input("Enter professional profession: ").lower()
        if not profession:
            print("Profession cannot be empty.")
            continue
        if not profession.isalpha():
            print("Profession must be alphabetic.")
            continue
        break
    new_professional = Professional(name, phone, profession)
    new_professional.add_professional()
    return new_professional.to_dict()


def main():
    while True:
        print("Welcome to Horfiesh Jobs App!")
        option = input("Please choose an option:\n1. Add a new job\n"
                       "2. Remove a job\n3. Add a professional\n4. Remove a professional\n5. Exit\n")
        if option == "1":
            while True:
                job_title = input("Enter job title: ").lower()
                if not job_title:
                    print("Job title cannot be empty.")
                    continue
                if not job_title.isalpha():
                    print("Job title must be alphabetic.")
                    continue
                break
            print("Would you like to add a new profession? (yes/no)")
            answer = input("Please insert your answer: ")
            professional_data = None
            if answer.lower() == "yes":
                professional_data = add_professional()
                new_job = Job(job_title)
                new_job.add_job(professional_data)
                print(f"Job: {job_title} was added successfully with a new professional: {professional_data['name']}.")
            elif answer.lower() == "no":
                new_job = Job(job_title)
                new_job.add_job(None)
                print(f"Job: {job_title} was added successfully.")
            else:
                print("Please insert a correct option.")
        elif option == "2":
            while True:
                job_title = input("Enter job title: ").lower()
                if not job_title:
                    print("Job title cannot be empty.")
                    continue
                if not job_title.isalpha():
                    print("Job title must be alphabetic.")
                    continue
                break
            job_to_remove = Job(job_title)
            job_to_remove.remove_job(job_title)
        elif option == "3":
            add_professional()
        elif option == "4":
            while True:

                name = input("Enter professional name: ").lower()
                if not name:
                    print("Name cannot be empty.")
                    continue
                if not name.isalpha():
                    print("Name must be alphabetic.")
                    continue
                break
            professional_to_remove = Professional(name, None, None)
            professional_to_remove.remove_professional(name)

        elif option == "5":
            print("Thank you for using Horfiesh Jobs App!")
            break
        else:
            print("Please insert a correct option.")


if __name__ == '__main__':
    main()
