"""
Jhone  Fontenele
2024
"""
import numpy as np
from class_numbers import Numbers
#
to_conv = []
def start():
	obj = Numbers(to_conv, 3, 10)
	matrix = obj.random_numbers()
	print("\n The Matrix Dimension is:",matrix.shape)
	numb_row, numb_column = matrix.shape
	#
	print("--------------------------------")
	for i in range(numb_row):
		a = matrix[i][:]
		print(f"Vector {i} {a}")
	print("--------------------------------")
	#
	f=35
	while (f>30):
		for j in range(numb_row):
			for k in range(numb_row-1, -1, -1):
				if j!= k:
					print("-----------------------------")
					print(f"Likely Combinations{j} {k}")
					b = matrix[j][0:5]
					print(b)
					c = matrix[k][:5:10]
					print(c)
					to_convert = np.concatenate((b,c))
					print(to_convert)
					conv = Numbers(to_convert,3,10)
					e = conv.convert_bin2dec()
					print(e)
					f = np.abs(2*e+10-18)
					print("base 2:",to_convert,">> base 10:",e, "Fitness/FO:",f)



start()

