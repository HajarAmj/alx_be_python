def main():
    task = input("Enter your task: ").strip()
    
    while True:
        priority = input("Priority (high/medium/low): ").lower().strip()
        if priority in ("high", "medium", "low"):
            break
        print("Invalid priority. Please enter high, medium, or low.")
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
        if time_bound in ("yes", "no"):
            break
        print("Please enter yes or no.")
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
    if time_bound == "yes":
        reminder = f"Reminder: {base_message} that requires immediate attention today!"
    else:
        reminder = f"Note: {base_message}. Consider completing it when you have free time."
    
    print("\n" + reminder)

if __name__ == "__main__":
    main()


