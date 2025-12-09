from pathlib import Path

def main():
	counter = 0
	lines = []
	max_lines = 0
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file.readlines():
			max_lines = max(max_lines, len(line))
			lines.append(line)
	for i in range(len(lines)):
		lines[i] = lines[i] + " " * (max_lines - len(lines[i]))
		lines[i] = lines[i].replace("\n", "")
	last_line = set([" "])
	aux = None
	for chars in zip(*lines):
		if last_line == {" "}:
			op = chars[-1]
			counter += aux if aux else 0
			aux = 1 if op == "*" else 0
		num = 0
		for i in range(len(chars) - 1):
			if chars[i] != " ":
				num = num * 10 + int(chars[i])
		if op == "+":
			aux += num
		else:
			if not set(chars) == {" "}:
				aux *= num
		last_line = set(chars)
	counter += aux
	print(counter)

if __name__ == "__main__":
	main()
