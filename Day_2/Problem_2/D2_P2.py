from pathlib import Path

def is_invalid(number):
	counter = 1
	sub_number = str(number)[:counter]
	while len(sub_number) <= len(str(number)) // 2:
		if sub_number * (len(str(number)) // counter) == str(number):
			return True
		counter += 1
		sub_number = str(number)[:counter]
	return False

def invalid_between(x, y):
	l = [i for i in range(x, y + 1) if is_invalid(i)]
	return l

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
		invalids = invalid_between(x, y)
		counter += sum(invalids)
	print(counter)

if __name__ == "__main__":
	main()
