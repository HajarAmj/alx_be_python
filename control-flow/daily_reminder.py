task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder_message = ""

match priority:
    case "high":
        reminder_message = f"{task} is a high priority task"
    case "medium":
        reminder_message = f"{task} is a medium priority task"
    case "low":
        reminder_message = f"{task} is a low priority task"
    case _:
        reminder_message = f"{task} is a task"

if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"

print(f"\nReminder: {reminder_message}")


