from pathlib import Path

def main():
	counter = 0
	row = 0
	data = []
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file.readlines():
			data.append(line.strip())

	for row in range(len(data)):
		for col in range(len(data[0])):
			if data[row][col] == "@":
				neighbours = 0
				movements = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
				for movement in movements:
					if 0 <= row + movement[0] < len(data) and 0 <= col + movement[1] < len(data[0]):
						if data[row + movement[0]][col + movement[1]] == "@":
							neighbours += 1
				if neighbours < 4:
					counter += 1

	print(counter)

if __name__ == "__main__":
	main()
