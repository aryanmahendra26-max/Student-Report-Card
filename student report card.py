import pickle


# SEARCH FUNCTION
def search():
	try:
		x = open("student.st", "rb")
	except FileNotFoundError:
		print("No student records found.")
		return

	try:
		r = int(input("Enter roll no.: "))
	except ValueError:
		print("Invalid roll number.")
		x.close()
		return

	found = False
	try:
		while True:
			z = pickle.load(x)
			if z.get("Roll no") == r:
				print("Name:", z.get("Name"))
				print("Roll no:", z.get("Roll no"))
				print("Marks of Hindi:", z.get("Marks of Hindi"))
				print("Marks of English:", z.get("Marks of English"))
				print("Marks of Maths:", z.get("Marks of Maths"))
				print("Marks of Physics:", z.get("Marks of Physics"))
				print("Marks of Chemistry:", z.get("Marks of Chemistry"))
				print("Marks of Computer Sci.:", z.get("Marks of Computer Sci."))
				print("Marks of Physical Edu.:", z.get("Marks of Physical Edu."))
				found = True
				break
	except EOFError:
		pass
	finally:
		x.close()

	if not found:
		print("!!! Roll no does not exist !!!")
	print("-_- Program Ended -_-")


# ADD FUNCTION
def add():
	ans = "y"
	while ans.lower() == "y":
		s = {}
		s["Name"] = input("Enter name of student: ").strip()
		try:
			s["Roll no"] = int(input("Enter roll no.: "))
		except ValueError:
			print("Invalid roll number; skipping add.")
			return
		try:
			s["Marks of Hindi"] = float(input("Enter marks Hindi: "))
			s["Marks of English"] = float(input("Enter marks English: "))
			s["Marks of Maths"] = float(input("Enter marks Maths: "))
			s["Marks of Physics"] = float(input("Enter marks Physics: "))
			s["Marks of Chemistry"] = float(input("Enter marks Chemistry: "))
			s["Marks of Computer Sci."] = float(input("Enter marks Computer Sci.: "))
			s["Marks of Physical Edu."] = float(input("Enter marks Physical Edu.: "))
		except ValueError:
			print("Invalid marks entered; please try again.")
			return

		with open("student.st", "ab") as x:
			pickle.dump(s, x)

		print("Added Successfully")
		ans = input("Do you want to add more y/n: ")

	print("-_- Program Ended -_-")


# MODIFY FUNCTION
def modify():
	try:
		r = int(input("Enter roll no: "))
	except ValueError:
		print("Invalid roll number.")
		return

	try:
		x = open("student.st", "rb")
	except FileNotFoundError:
		print("No student records found.")
		return

	l = []
	found = False
	try:
		while True:
			z = pickle.load(x)
			if z.get("Roll no") == r:
				z["Name"] = input("Enter new name: ")
				try:
					z["Marks of Hindi"] = float(input("Enter new marks Hindi: "))
					z["Marks of English"] = float(input("Enter new marks English: "))
					z["Marks of Maths"] = float(input("Enter new marks Maths: "))
					z["Marks of Physics"] = float(input("Enter new marks Physics: "))
					z["Marks of Chemistry"] = float(input("Enter new marks Chemistry: "))
					z["Marks of Computer Sci."] = float(input("Enter new marks Computer Sci.: "))
					z["Marks of Physical Edu."] = float(input("Enter new marks Physical Edu.: "))
				except ValueError:
					print("Invalid marks entered; modification aborted for this record.")
				found = True
			l.append(z)
	except EOFError:
		x.close()

	if not found:
		print("!!! Roll no. not exist !!!")
	else:
		with open("student.st", "wb") as x:
			for i in l:
				pickle.dump(i, x)
		print("Record modified Successfully")

	print("-_- Program Ended -_-")


# READ FUNCTION
def reed():
	try:
		x = open("student.st", "rb")
	except FileNotFoundError:
		print("No student records found.")
		return

	print("------ Data Showing --------------------------------------------------")
	try:
		while True:
			y = pickle.load(x)
			print(y)
	except EOFError:
		pass
	finally:
		x.close()

	print("------ Data Ended ----------------------------------------------------")
	print("-_- Program Ended -_-")


# DELETE FUNCTION
def delete():
	try:
		r = int(input("Enter roll no: "))
	except ValueError:
		print("Invalid roll number.")
		return

	try:
		x = open("student.st", "rb")
	except FileNotFoundError:
		print("No student records found.")
		return

	l = []
	found = False
	try:
		while True:
			z = pickle.load(x)
			if z.get("Roll no") == r:
				found = True
				print("Deleted Successfully")
				# skip adding this record to the list
			else:
				l.append(z)
	except EOFError:
		x.close()

	if not found:
		print("!!! Roll no. not exist !!!")
	else:
		with open("student.st", "wb") as x:
			for i in l:
				pickle.dump(i, x)

	print("-_- Program Ended -_-")


# INTERFACE PROGRAM
def main():
	print("---------- STUDENT REPORT CARD ----------")
	print("Available Options Are:")
	print("""1. SEARCH
2. ADD/APPEND
3. MODIFY
4. READ
5. DELETE
6. Exit""")

	p = "y"
	while p.lower() == "y":
		try:
			c = int(input("Enter Your Choice: "))
		except ValueError:
			print("----- Invalid Choice ----- Try Again -----")
			continue

		if c == 1:
			search()
		elif c == 2:
			add()
		elif c == 3:
			modify()
		elif c == 4:
			reed()
		elif c == 5:
			delete()
		elif c == 6:
			print("----- Exiting ------------------------------------------------------------")
			break
		else:
			print("----- Invalid Choice ----- Try Again -----")
			continue

		p = input("Do you want to use software again y/n: ")

	print("(; Software Ended ;)")


if __name__ == "__main__":
	main()