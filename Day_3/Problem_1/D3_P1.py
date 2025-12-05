from pathlib import Path


def main():
	counter = 0
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file.readlines():
			numbers = [int(x) for x in line.strip()]
			first_digit = max(numbers)
			idx = numbers.index(first_digit)
			if idx == len(numbers) - 1:
				numbers.pop(-1)
				aux = max(numbers)
				numbers.append(first_digit)
				first_digit = aux
				idx = numbers.index(first_digit)
			last_digit = -1
			for new_digit in numbers[idx + 1:]:
				if new_digit > last_digit:
					last_digit = new_digit
				if last_digit == 9:
					break
			counter += int(str(first_digit) + str(last_digit))

	print(counter)


if __name__ == "__main__":
	main()
