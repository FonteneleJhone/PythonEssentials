"""
This class is in charge of handle information from .xlsx files

Author: Jhone Fontenele

Year: 2024
"""
__author__="Jhone Fontenele"
__year__="2024"

class ReadFile:

	def __init__(self, company, products):
		self.company = company
		self.products = products

	def find(self):
		print(self.company, self.products)
