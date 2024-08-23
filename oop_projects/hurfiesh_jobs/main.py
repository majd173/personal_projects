from oop_projects.hurfiesh_jobs.src.classes.jobs import Job
from oop_projects.hurfiesh_jobs.src.classes.professional import Professional


def add_professional():
    while True:
        name = input("Enter professional name: ").lower()
        if not name:
            print("Name cannot be empty.")
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
        services = input("Enter professional services: ").lower()
        if not services:
            print("Services cannot be empty.")
            continue
        break
    new_professional = Professional(name, phone, services)
    new_professional.add_a_professional()
    return new_professional.to_dict()


def main():
    while True:
        print("Welcome to Horfiesh Jobs App!")
        option = input("Please choose an option:\n1. Add a new job\n"
                       "2. Remove a job\n3. Add a professional\n"
                       "4. Remove a professional\n5. Show jobs\n6. Show professionals\n"
                       "7. Exit\n")
        if option == "1":
            while True:
                job_title = input("Enter job title: ").lower()
                if not job_title:
                    print("Job title cannot be empty.")
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
                break
            professional_to_remove = Professional(name, None, None)
            professional_to_remove.remove_professional(name)
        elif option == "5":
            Job.show_jobs()
            continue
        elif option == "6":
            Professional.show_professionals()
            continue
        elif option == "7":
            print("Thank you for using Horfiesh Jobs App!")
            break
        else:
            print("Please insert a correct option.")


if __name__ == '__main__':
    main()
