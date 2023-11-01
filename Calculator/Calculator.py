def calculator():
	def add(x, y):
		return x + y

	def subtract(x, y):
		return x - y

	def multiply(x, y):
		return x * y

	def divide(x, y):
		if y == 0:
			return "Error! Division by zero is not allowed."
		return x / y

	print("\n🧮 Welcome to the Python Calculator 🧮")
	print("=====================================")
	print("Select operation:")
	print("1. Addition ➕")
	print("2. Subtraction ➖")
	print("3. Multiplication ✖️")
	print("4. Division ➗")
	print("5. Exit calculator 🚪")

	while True:
		choice = input("\nEnter choice (1/2/3/4/5): ")

		if choice == '5':
			print("\n👋 Exiting the calculator. See you next time!")
			break

		num1 = float(input("\nEnter first number: "))
		num2 = float(input("Enter second number: "))

		if choice == '1':
			print(f"\n{num1} ➕ {num2} = {add(num1, num2)}")

		elif choice == '2':
			print(f"\n{num1} ➖ {num2} = {subtract(num1, num2)}")

		elif choice == '3':
			print(f"\n{num1} ✖️ {num2} = {multiply(num1, num2)}")

		elif choice == '4':
			result = divide(num1, num2)
			if isinstance(result, str):
				print(f"\n{result}")
			else:
				print(f"\n{num1} ➗ {num2} = {result}")

		else:
			print("\n❌ Invalid input. Please enter a number between 1 and 5.")

calculator()