from pathlib import Path

def main():
	counter = 0
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file.readlines():
			numbers = [int(x) for x in line.strip()]
			final_number = ""
			for _ in range(12):
				for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
					if i in numbers:
						idx = numbers.index(i)
						if len(numbers) - idx >= 12 - len(final_number):
							final_number += str(i)
							break
				numbers = numbers[idx + 1:]
			counter += int(final_number)
	print(counter)


if __name__ == "__main__":
	main()
