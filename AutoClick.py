from pynput.keyboard import Controller
from time import sleep


def auto_click(key: str, n_clicks: int, delay: float):
	keyboard = Controller()

	for _ in range(n_clicks):
		keyboard.tap(key)
		sleep(delay)


def main():
	key = input("Key to be autopressed: ")

	try:
		n_clicks = int(input("Number of autopresses (integer): "))
	except ValueError:
		print("\n The number of autopresses should be an integer value, defaulting to 1. \n")
		n_clicks = 1

	try:
		delay = float(input("Delay between each autopress in seconds (integer/float): "))
	except ValueError:
		print("\n The delay between each autoclick should be an integer or a decimal value, defaulting to 1 (second). \n")
		delay = 1

	auto_click(key, n_clicks, delay)

if __name__ == '__main__':
    main()
