import os

def StartUp():
	print("\nLoading modules... Please wait... \n")
	os.system("pip install turtle")

StartUp()

import turtle

List_Of_Drawables = []
List_Of_Pens = []

class Program:
	def __init__(self):
		self.main()

	def main(self):
		self.CreateWindow()
		self.Menu()
		self.UpdateWindow()

	def Undo(self):
		global List_Of_Drawables
		try:
			List_Of_Drawables = List_Of_Drawables[:-1]
		except Exception:
			os.system('cls')
			print("\nNo Object found! Press ENTER to RETURN to menu")
			input("")
		turtle.Screen().resetscreen()
		turtle.Screen().bgcolor("black")

	def DeleteObject(self, ID):
		os.system("cls")
		
		try:
			Y = str(input("\nAre you sure you want to delete this object? (Y/N): "))
		except Exception:
			pass
		
		if(Y.lower() == "y"):
			List_Of_Pens.pop(ID)
			List_Of_Drawables.pop(ID)
		else:
			pass

	def Menu(self):
		while True:
			os.system("cls")
			print("\n1. Add New Object")
			print("2. Draw Objects")
			print("3. Delete Object")
			print("4. UNDO")
			print("5. Exit\n")

			try:
				choice = int(input(">> "))
			except Exception:
				pass

			if(choice == 1):
				os.system("cls")
				try:
					StartX = float(input("\nThe start X coordonate: "))
					StartY = float(input("The start Y coordonate: "))
					Type = str(input("Type of the object (square/circle/triangle): "))
					Size = float(input("The size of the object (1 is default): "))

					self.CreateObj(StartX, StartY, Type, Size)

					os.system("cls")

					input("\nObject added, press ENTER to RETURN to menu.")
				except Exception:
					choice = 100

			elif(choice == 2):
				os.system("cls")
				print("\nDrawing RELIC... Please wait...")
				self.DrawObjects()
				os.system("cls")
				input("\nDrawing FINISHED, press ENTER to RETURN to menu.")
				turtle.Screen().resetscreen()
				turtle.Screen().bgcolor("black")

			elif(choice == 3):
				os.system("cls")

				ID = 0
				for Object in List_Of_Drawables:
					print("ID: " + str(ID) + " | TYPE: " + str(Object[2]) + " | START POSITION: " + str(Object[0]) + ", " + str(Object[1]) + " | SIZE: " + str(Object[3]) + " |")
					ID += 1

				try:
					Del = int(input("\nEnter the ID you want to delete: "))
					self.DeleteObject(Del)
				except Exception:
					pass

			elif(choice == 4):
				os.system("cls")

				try:
					Y = str(input("\nAre you sure you want to UNDO? (Y/N): "))
				except Exception:
					pass

				if(Y.lower() == "y"):
					self.Undo()
				else:
					pass

			elif(choice == 5):
				os.system("cls")
				quit()

			else:
				pass

	def DrawObjects(self):
		ID = 0
		for Object in List_Of_Drawables:

			pen = List_Of_Pens[ID]

			if(Object[2].lower() == "circle"):
				pen.goto(Object[0], Object[1]-57*Object[3])
				pen.color("white")
				pen.hideturtle()
				pen.pensize(2)
				pen.pendown()
				for i in range(360):
					pen.forward(1*Object[3])
					pen.left(1)

			if(Object[2].lower() == "square"):
				pen.goto(Object[0]+50*Object[3], Object[1]+50*Object[3])
				pen.color("white")
				pen.hideturtle()
				pen.pensize(2)
				pen.pendown()
				pen.goto(pen.xcor(), pen.ycor()-100*Object[3])
				pen.goto(pen.xcor()-100*Object[3], pen.ycor())
				pen.goto(pen.xcor(), pen.ycor()+100*Object[3])
				pen.goto(pen.xcor()+100*Object[3], pen.ycor())

			if(Object[2].lower() == "triangle"):
				pen.goto(Object[0], Object[1]+50*Object[3])
				pen.color("white")
				pen.hideturtle()
				pen.pensize(2)
				pen.pendown()
				pen.setheading(pen.towards(pen.xcor()-50*Object[3], pen.ycor()-100*Object[3])), pen.forward(pen.distance(pen.xcor()-50*Object[3], pen.ycor()-100*Object[3]))
				pen.setheading(pen.towards(pen.xcor()+100*Object[3], pen.ycor())), pen.forward(pen.distance(pen.xcor()+100*Object[3], pen.ycor()))
				pen.setheading(pen.towards(pen.xcor()-50*Object[3], pen.ycor()+100*Object[3])), pen.forward(pen.distance(pen.xcor()-50*Object[3], pen.ycor()+100*Object[3]))

			ID += 1

	def CreateObj(self, StartPosX, StartPosY, Type_Of_Drawing, size):
		pen = turtle.Turtle()
		pen.penup()
		pen.hideturtle()
		pen.color("white")
		pen.pensize(2)

		List_Of_Pens.append(pen)

		Object = []

		Object.append(StartPosX)
		Object.append(StartPosY)
		Object.append(Type_Of_Drawing)
		Object.append(size)

		List_Of_Drawables.append(Object)

	def CreateWindow(self):
		window = turtle.Screen()
		window.setup(0.99, 0.99)
		window.bgcolor("black")

	def UpdateWindow(self):
		while True:
			turtle.Screen().update()

if __name__ == "__main__":
	Program()