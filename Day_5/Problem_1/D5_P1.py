from pathlib import Path

def main():
	counter = 0
	fresh_intervals = []
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		line = file.readline()
		while line != '\n':
			first, last = line.strip().split("-")
			fresh_intervals.append((int(first), int(last)))
			line = file.readline()
		line = file.readline()
		while line:
			ingredient = int(line.strip())
			for interval in fresh_intervals:
				if interval[0] <= ingredient <= interval[1]:
					counter += 1
					break
			line = file.readline()
	print(counter)

if __name__ == "__main__":
	main()
