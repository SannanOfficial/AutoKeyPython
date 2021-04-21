from pynput.keyboard import Key, Controller
import time


# Autoclicker Functionality
def AutoClick(inputClickKey, inputClickAmount, inputClickDelay):
	keyboard = Controller();

	clickAmount = 1;

	while clickAmount <= inputClickAmount:
		clickAmount += 1;

		keyboard.press(inputClickKey)
		keyboard.release(inputClickKey)

		time.sleep(inputClickDelay)

# User Input
KeyInput = input("Key to be autoclicked: ");
ClickAmountInput = int(input("Number of autoclicks (integer): "))
ClickDelayInput = int(input("Delay between each autoclick in seconds (integer): "))

# Code Execution
AutoClick(KeyInput, ClickAmountInput, ClickDelayInput);
