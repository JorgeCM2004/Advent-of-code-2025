from pathlib import Path

def main():
	counter = 0
	beams = {}
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		line = file.readline()
		beam = line.index("S")
		beams.update({beam: 1})
		for line in file.readlines():
			if set(line.strip()) == {"."}:
				continue
			else:
				to_remove = []
				new_beams = {}
				for beam, value in beams.items():
					if line[beam] == "^":
						to_remove.append(beam)
						try:
							new_beams[beam - 1] += value
						except:
							new_beams[beam - 1] = value
						try:
							new_beams[beam + 1] += value
						except:
							new_beams[beam + 1] = value
				for beam in to_remove:
					beams.pop(beam)
				for beam, value in new_beams.items():
					if beam not in beams:
						beams.update({beam: value})
					else:
						beams[beam] += value
	counter += sum(beams.values())
	print(counter)

if __name__ == "__main__":
	main()
