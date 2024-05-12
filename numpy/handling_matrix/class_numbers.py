"""
Jhone Fontenele
2024
"""
import timeit
import numpy as np
#
class Numbers:
	start_up_time = timeit.default_timer()
	def __init__(self, to_convert, column_size, line_size):
		self.to_convert = to_convert
		self.column_size = column_size
		self.line_size = line_size
		#

	def convert_bin2dec(self):
		dec = 0
		pot = 0
		for i in range(len(self.to_convert)-1, -1, -1):
			dec += self.to_convert[i]*2**pot
			pot =  pot + 1
		return dec
		#
	def random_numbers(self):
		numb_rand = np.random.randint(0, 2, [self.column_size, self.line_size])
		return numb_rand
