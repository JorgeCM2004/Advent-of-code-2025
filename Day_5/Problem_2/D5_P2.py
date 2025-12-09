from pathlib import Path

def main():
	counter = 0
	intervals: list[list[int]] = []
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		line = file.readline()
		while line != '\n':
			first, last = map(int, line.strip().split("-"))
			# Modify existing intervals
			if intervals:
				for interval in intervals:
					if first >= interval[0] and last <= interval[1]:
						continue
					elif first <= interval[1] and first >= interval[0]:
						interval[1] = last
					elif last >= interval[0] and last <= interval[1]:
						interval[0] = first
				if [first, last] not in intervals:
					intervals.append([first, last])
				intervals.sort()
				i = 0
				# Join intervals
				while i < len(intervals) - 1:
					if intervals[i][1] >= intervals[i + 1][0]:
						intervals[i] = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]
						intervals.pop(i + 1)
					else:
						i += 1
			else:
				intervals.append([first, last])

			line = file.readline()
	for interval in intervals:
		counter += interval[1] - interval[0] + 1
	print(counter)

if __name__ == "__main__":
	main()
