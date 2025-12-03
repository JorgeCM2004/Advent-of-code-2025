from pathlib import Path

def main():
	actual_state = 50
	counter = 0
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file:
			direction, number = line[0], int(line[1:].strip())
			if direction == "L":
				number *= -1
			actual_state += number
			while actual_state < 0:
				actual_state += 100
			while actual_state > 99:
				actual_state -= 100
			if actual_state == 0:
				counter += 1
	print(counter)

if __name__ == "__main__":
	main()
