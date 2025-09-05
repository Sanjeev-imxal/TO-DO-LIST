#TO-DO LIST

tasks = []

while True:
	
	print("\n1. Add task")
	print("2. remove task")
	print("3. list tasks")
	print("4. quit")
	
	choice=int(input("Enter your choice: "))
	
	if choice == 1:
		task = input("Enter task to add: ").lower()
		tasks.append(task)
	elif choice == 2:
		task = input("Enter task to remove: ").lower()
		if task in tasks:
			tasks.remove(task)
		else:
			print("task not found!")
	elif choice == 3:
		if tasks:
			for i , task in enumerate(tasks):
			  print(f"{i+1}. {task}")
		else:
			print("No tasks yet!")
	elif choice == 4:
		break
	else:
		print("Invalid choice! Try again.")
		
#code ends