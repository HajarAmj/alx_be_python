task = input("Enter your task: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

match priority.lower():
    case "high":
        message = f"Reminder: {task} [High Priority]"
    case "medium":
        message = f"Reminder: {task} [Medium Priority]"
    case "low":
        message = f"Reminder: {task} [Low Priority]"
    case _:
        message = f"Reminder: {task} [Unknown Priority]"

if time_bound.lower() == "yes":
    message += " that requires immediate attention today!"

print(message)
