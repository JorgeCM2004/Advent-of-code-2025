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
				new_beams = []
				for beam in beams:
					if line[beam] == "^":
						to_remove.append(beam)
						new_beams.append(beam - 1)
						new_beams.append(beam + 1)
						counter += 1
				for beam in to_remove:
					beams.remove(beam)
				for beam in new_beams:
					if beam not in beams:
						beams.append(beam)
	print(counter)

if __name__ == "__main__":
	main()
