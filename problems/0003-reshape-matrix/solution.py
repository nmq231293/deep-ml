import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	arr = np.array(a)
	sz = arr.size
	n, m = new_shape

	if n * m != sz:
		return []
	
	reshaped_matrix = arr.reshape(n, m).tolist()

	return reshaped_matrix