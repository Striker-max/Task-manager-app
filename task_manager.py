#=====Importing libraries===========
from datetime import date

#====Functions Section====
# Validate username and password inputs
def login_details(username, password):
    while True:
        new_username = input('Please enter the username: ')
        if new_username in username:
            while True:
                new_password = input('Please enter the corresponding password: ')
                if new_password in password:
                    print('Valid username and password entered.')
                    return new_username
                else:
                    print('Incorrect password for the given username.')
        else:
            print('No such username in the database.')


# Check whether passwords match for 'r' section
def password_check():
    new_password = input("Please enter a new password: ") 
    conf_password = input("Please confirm new password: ")
    if new_password == conf_password:
        return new_password
    else:
        print("Passwords do not match. Please try again.")
        return password_check()


# Verify whether task is being added to a valid username
def user_check():
    with open('user.txt', 'r+', encoding='utf-8') as f:
        username = []
        for line in f:
            user = line.split(", ", 2)
            username.append(user[0])
        while True:
            name = input("Please enter username of task owner: ")
            if name in username:
                return name
            else:
                print('Sorry, that username is not registered in the database.')
                return user_check()
            

# Write new task to tasks.txt
def add_task(name, task, desc, day):
    with open('tasks.txt', 'r+', encoding='utf-8') as w:
        w.seek(0, 2)
        today = date.today()
        task_entry = ('\n' + name + 
                      ', ' + task + 
                      ', ' + desc + 
                      ', ' + day + 
                      ', ' + str(today) + 
                      ', ' + 'No')
        w.write(task_entry)


# Display each task in tasks.txt
def display_tasks(list):
    print('Task:\t\t\t' + list[1])
    print('Assigned to:\t\t' + list[0])
    print('Date addigned:\t\t' + list[4])
    print('Due date:\t\t' + list[3])
    print('Task Complete?\t\t' + list[5].strip('\n'))
    print('Task description?\t' + list[2])
        

# Lines for 'va' section        
def lines(length):
    line = length * '-'
    print(line)


# Task counter
def num_tasks():
    task_counter = []
    with open('tasks.txt', 'r+', encoding='utf-8') as y:
        for line in y:
            tasks = line.split(", ", 6)
            task_counter.append(tasks[1])
    return len(task_counter)

    
#====Login Section====
with open('user.txt', 'r+', encoding='utf-8') as f:
    username = []
    password = []
    for line in f:
        user = line.split(", ", 2)
        username.append(user[0])
        if '\n' in user[1]:
            user[1] = user[1].strip('\n')
            password.append(user[1])
        else:
            password.append(user[1])

    name_entered = login_details(username, password)

#====Menu Execution Section====
    while True:
        if name_entered == 'admin':
            menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - statistics
e - exit
''').lower()
            
        else:
            menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
''').lower()
            
        if menu == 'r':
            if name_entered == 'admin':
                new_username = input("Please enter a new username: ")
                new_password = password_check()
                f.seek(0, 2)  # Moves pointer to end of last line
                f.write('\n' + new_username + ', ' + new_password)
                print("New username and password added to database.")   
            else:
                print('Sorry. Only user "admin" is allowed to add new users.')
            continue
    
        elif menu == 'a':
            t_username = user_check() 
            t_title = input("Please enter task title: ")
            t_descr = input("Please enter task description: ")
            t_date = input("Please enter task due date: ")
            add_task(t_username, t_title, t_descr, t_date)
            continue

        elif menu == 'va':
            with open('tasks.txt', 'r+', encoding='utf-8') as v:
                for line in v:
                    entries = line.split(', ', 6)
                    lines(120)
                    display_tasks(entries)
                    lines(120)
            continue

        elif menu == 'vm':  
            task_avail = False  # Tracker to check if there is a task for given username
            with open('tasks.txt', 'r+', encoding='utf-8') as x:
                for line in x:
                    entries2 = line.split(', ', 6)
                    if entries2[0] == name_entered:
                        lines(120)
                        display_tasks(entries2)
                        lines(120)
                        task_avail = True
            if not task_avail:
                print('No tasks in database for this user.')
            continue

        elif menu == 's':
            if name_entered == 'admin':
                lines(120)
                print(f'Number of users in database:\t\t {len(username)}')
                print(f'Number of tasks in database:\t\t {num_tasks()}')
                lines(120)
            else:
                print("You have entered an invalid input. Please try again.")
            continue

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again.")


