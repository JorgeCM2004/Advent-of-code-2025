from pathlib import Path
from math import sqrt

MAX_CONNECTIONS = 1000

def euclidean_distance_3d(point1, point2):
	return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)

def main():
	counter = 0
	boxes = []
	circuits: list[set[int]] = []
	with open(Path(__file__).parent.parent / "input.txt", "r") as file:
		for line in file.readlines():
			boxes.append(tuple(int(x) for x in line.strip().split(",")))
	order = []
	for id1, box1 in enumerate(boxes):
		for id2 in range(id1 + 1, len(boxes)):
			box2 = boxes[id2]
			value = euclidean_distance_3d(box1, box2)
			order.append((value, id1, id2))
	order.sort()
	i = 0
	for i in range(MAX_CONNECTIONS):
		min_distance, box1, box2 = order[i]
		box1_in_circuit = False
		box2_in_circuit = False
		for box1_circuit_id, circuit in enumerate(circuits):
			if box1 in circuit:
				box1_in_circuit = True
				break
		for box2_circuit_id, circuit in enumerate(circuits):
			if box2 in circuit:
				box2_in_circuit = True
				break
		if not box1_in_circuit and not box2_in_circuit:
			circuits.append({box1, box2})
		elif box1_in_circuit and box2_in_circuit:
			if box1_circuit_id != box2_circuit_id:
				for box in circuits[box2_circuit_id]:
					circuits[box1_circuit_id].add(box)
				circuits.pop(box2_circuit_id)
			else:
				pass
		elif box1_in_circuit and not box2_in_circuit:
			circuits[box1_circuit_id].add(box2)
		elif not box1_in_circuit and box2_in_circuit:
			circuits[box2_circuit_id].add(box1)
	len_circuits = [len(circuit) for circuit in circuits]
	len_circuits.sort(reverse=True)
	counter = len_circuits[0] * len_circuits[1] * len_circuits[2]
	print(counter)

if __name__ == "__main__":
	main()
