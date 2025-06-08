task = input("Enter the task description: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        reminder = f"Task: {task} is HIGH priority."
    case "medium":
        reminder = f"Task: {task} is medium priority."
    case "low":
        reminder = f"Task: {task} is low priority."
    case _:
        reminder = f"Task: {task} has unknown priority."

if time_bound.lower() == "yes":
    reminder += " This task requires immediate attention today!"

print(reminder)
