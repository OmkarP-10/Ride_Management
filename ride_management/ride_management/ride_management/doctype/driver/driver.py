# Copyright (c) 2024, os and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		self.set_full_name()

	def set_full_name(self):
		self.full_name  = self.first_name + " " + self.last_name
