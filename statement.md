### Problem statement
It takes too long and is too easy to make mistakes when manually calculating grades and creating report cards. I built this to make grading faster and more accurate by automating the calculations and report generation.

### Scope of the project
* **What it does:** It manages student records and their marks for a set number of subjects. It performs calculations and prints a final report.
* **What it doesn't do:** It is strictly a **command-line application**, and it saves data only to a local file.

### Target users
This tool is for **teachers or teaching assistants** who need a quick and straightforward way to manage grades for a single class or small group of students.

### High-level features
My implementation focused on making the code clean and reliable.

1.  **Clean Structure (Modularity):** I kept the code organized by separating different jobs (like saving data versus calculating grades) into different parts. This makes it easier to manage and update.
2.  **Reliability:** I added specific checks to the code to prevent crashes. If a user types a wrong value (like a letter instead of a number for a mark), the program handles the mistake and asks them to fix it, instead of stopping completely.
3.  **Simple Design:** I used basic Object-Oriented Programming (OOP) to create a "Student" object in the code to keep all of a student's information (ID, name, and marks) organized together.
