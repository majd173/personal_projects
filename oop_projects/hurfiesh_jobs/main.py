from oop_projects.hurfiesh_jobs.jobs import Job
from oop_projects.hurfiesh_jobs.professional import Professional


def main():
    while True:
        print("Welcome to Horfiesh Jobs App!")
        option = input("Please choose an option:\n1. Add a new job\n2. Add a new professional\n3. Exit\n")
        if option == "1":
            job_title = input("Enter job title: ")
            new_job = Job(job_title)
            new_job.add_job()
        elif option == "2":
            name = input("Enter professional name: ")
            phone = input("Enter professional phone: ")
            profession = input("Enter professional profession: ")
            new_professional = Professional(name, phone, profession)
            new_professional.add_professional()
        elif option == "3":
            print("Thank you for using Horfiesh Jobs App!")
            break
        else:
            print("Please insert a correct option.")


if __name__ == '__main__':
    main()
