from oop_projects.hurfiesh_jobs.jobs import Job
from oop_projects.hurfiesh_jobs.professional import Professional


def add_professional():
    name = input("Enter professional name: ")
    phone = input("Enter professional phone: ")
    profession = input("Enter professional profession: ")
    new_professional = Professional(name, phone, profession)
    new_professional.add_professional()
    return new_professional.to_dict()


def main():
    while True:
        print("Welcome to Horfiesh Jobs App!")
        option = input("Please choose an option:\n1. Add a new job\n2. Remove a job\n3. Exit\n")
        if option == "1":
            job_title = input("Enter job title: ")
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
            job_title = input("Enter job title: ")
            job_to_remove = Job(job_title)
            job_to_remove.remove_job(job_title)
            print(f"Job: {job_title} was removed successfully.")
        elif option == "3":
            print("Thank you for using Horfiesh Jobs App!")
            break
        else:
            print("Please insert a correct option.")


if __name__ == '__main__':
    main()
