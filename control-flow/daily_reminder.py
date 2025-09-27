task = input("Task Description: ")
priority = input("Tasks Priority (High/Medium/Low): ")
time_bound = input("Time Bound? (Yes/No) ")

match priority:
    case "high" if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
