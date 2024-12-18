import os

# Function to create folders and files
def create_day_folders_and_files(start_day, end_day):
    for day in range(start_day, end_day + 1):
        folder_name = f"Day{day}"
        file_name = f"{folder_name}-Tasks-and-Answers.md"
        
        # Create the folder
        os.makedirs(folder_name, exist_ok=True)
        
        # Create the README file inside the folder
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
            # Write a placeholder or a header
            file.write(f"# {folder_name} Tasks and Answers\n\n")
            file.write("Add tasks and answers here.\n")
        
        print(f"Created: {folder_name}/{file_name}")

# Call the function for Days 4 to 10
create_day_folders_and_files(1, 10)
