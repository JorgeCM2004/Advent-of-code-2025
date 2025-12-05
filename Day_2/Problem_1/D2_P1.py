from pathlib import Path

def invalid_until(number):
	i = 1
	invalids = []
	while int(str(i) + str(i)) <= number:
		invalids.append(int(str(i) + str(i)))
		i += 1
	return invalids

def main():
	counter = 0
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		file = file.readline()
		file = [x.strip() for x in file.split(",")]
		data = []
		for i in file:
			x, y = i.split("-")
			data.append((int(x), int(y)))

	for x, y in data:
		invalids = invalid_until(y)
		invalids = [inv for inv in invalids if inv >= x]
		counter += sum(invalids)
	print(counter)

if __name__ == "__main__":
	main()
