from pathlib import Path

def main():
	counter = 0
	coords = []
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file.readlines():
			coords.append(tuple(int(x) for x in line.strip().split(",")))
	max_size = 0
	for i in range(len(coords)):
		for j in range(i + 1, len(coords)):
			tile1 = coords[i]
			tile2 = coords[j]
			size = abs(tile1[0] - tile2[0] + 1) * abs(tile1[1] - tile2[1] + 1)
			if size > max_size:
				max_size = size
	print(max_size)

if __name__ == "__main__":
	main()
