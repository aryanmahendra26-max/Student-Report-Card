
### Problem statement
I wanted a tool to quickly manage student data and keep track of all their marks in a structured way. Manually listing marks can be complicated. This program solves that by automating the basic storing, searching, and updating of these essential academic records.

### Scope of the project
* **What it does:** It handles all basic record keeping (adding, searching, modifying, and deleting student details) for 7 fixed subjects (Hindi, English, Maths, Physics, Chemistry, Computer Sci., and Physical Edu.).
* **What it doesn't do:** **It does not currently calculate Total Marks, Percentage, or Final Grade.** That is a planned feature for a later update.
* **Format:** It is a command-line application only.

### Target users
This tool is for **teachers or teaching assistants** who need a simple, fast, and stable way to manage and look up marks for students in their class.

### High-level features
My design focused on two things: clean code and reliable input.

1.  **Clean Structure (Modularity):** I kept the code organized by putting each main job (like `add`, `search`, `modify`) into its own function. This makes the code very easy to read and manage, which is a key requirement for a student project.
2.  **Reliability:** This was very important. I added specific safety checks (`try-except`) every time a user inputs a Roll Number or Marks. If a user types something wrong (like a letter instead of a number), the program catches the mistake and asks them to fix it, instead of crashing.
3.  **Simple Data Handling:** I used the standard Python `pickle` module. This makes saving and loading the student data (which is stored as simple Python dictionaries) extremely easy and secure.
