from pathlib import Path

def main():
	counter = 0
	beams = []
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		line = file.readline()
		beam = line.index("S")
		beams.append(beam)
		for line in file.readlines():
			if set(line.strip()) == {"."}:
				continue
			else:
				to_remove = []
				for beam in beams:
					if line[beam] == "^":
						counter += 1
						to_remove.append(beam)
						if beam - 1 not in beams:
							beams.append(beam - 1)
						if beam + 1 not in beams:
							beams.append(beam + 1)
				for beam in to_remove:
					beams.remove(beam)
	print(counter)

if __name__ == "__main__":
	main()
