from pathlib import Path

def main():
	actual_state = 50
	l = []
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file:
			direction, number = line[0], int(line[1:].strip())
			for i in range(1, number + 1):
				actual_state += 1 if direction == "R" else -1
				if actual_state == 100:
					actual_state = 0
				elif actual_state == -1:
					actual_state = 99
				l.append(actual_state)
	print(l.count(0))

if __name__ == "__main__":
	main()
