import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# Greetings--Slots can be used for receiving signals,
@Slot()
def say_hello():
    print("Button clicked, Hello!")

# Create the Qt Application
app = QApplication(sys.argv)

# Create a button
button = QPushButton("Click me")

# Connect the button to the function---this is the singal---control the slot
button.clicked.connect(say_hello)

# Show the button
button.show()

# Run the main Qt loop
app.exec()

