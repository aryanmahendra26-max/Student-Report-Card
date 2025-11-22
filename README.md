# Student Report Card Manager 

### Project Title
Student Report Card Manager

### Overview of the project
This is a small **Python program** that runs in the command line in python. I built it to manage a class roster and all the marks they get in their subjects. It uses a built-in Python tool (`pickle`) to save and load student data (names, roll numbers, and marks) to a local file, so all the records are stored safely.

### Features
The program is focused on basic record keeping and retrieval:

1.  **Full Data Control (CRUD):**
    * **ADD:** Easily add a new student and all marks for the 7 subjects.
    * **MODIFY:** Change a student's name or any of their marks.
    * **DELETE:** Remove an entire student record using their Roll Number.

2.  **Searching & Viewing:**
    * **SEARCH:** Quickly find and display all the details for one specific student using their Roll Number.
    * **READ:** View a list of all the student records currently saved in the system.

3.  **Data Persistence:**
    * All records are saved securely in a file called `student.st`.

### Technologies/tools used
* **Language:** Standard **Python 3.x**.
* **Data Storage:** Python's built-in **`pickle` module** for saving Python dictionaries to a local binary file.

### Steps to install & run the project
It uses standard Python, so it's very simple to start.

1.  **Get the Files:** Download the Python file (`student report card.py`) from this repository.
2.  **Open Terminal:** Use the terminal/command line and go to the folder where you saved the file.
3.  **Run the Main Script:**
    ```bash
    python student report card.py
    ```

### Instructions for testing
To test the program, follow the main menu options (1-6):

1.  **Test Saving:** Use **ADD** (Option 2) to put in a new record. Then select **Exit** (Option 6). Run the program again and use **READ** (Option 4) to check the record was saved correctly.
2.  **Test Reliability:** Try typing letters (e.g., "hello") when the program asks for a Roll Number or Marks in the **ADD** or **SEARCH** options. The program should show an error and let you try again.
3.  **Test Deletion:** Use **ADD** to create a test record, and then use **DELETE** (Option 5) to remove it. Check **READ** again to confirm it's gone.

### Screenshots 
Screenshot 2025-11-23 002557.png
Screenshot 2025-11-23 002656.png



