from pathlib import Path

def main():
	counter = 0
	data = []
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file.readlines():
			try:
				line_data = list(map(int, line.strip().split()))
				data.append(line_data)
			except ValueError:
				operations = list(line.strip().split())
				data.append(operations)
	for col in range(len(data[0])):
		operation = data[-1][col]
		aux = 1 if operation == "*" else 0
		for row in range(len(data) - 1):
			if operation == "*":
				aux *= data[row][col]
			else:
				aux += data[row][col]
		counter += aux
	print(counter)

if __name__ == "__main__":
	main()
