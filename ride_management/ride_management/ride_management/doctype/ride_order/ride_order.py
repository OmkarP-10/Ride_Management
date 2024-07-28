# Copyright (c) 2024, os and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideOrder(Document):
	def on_update(self):
		if self.status == "Accepted":
			self.send_confirmation_message()


	def send_confirmation_message(self):
		
		message = f"Hi {self.customer_name}, your booking for {self.vehicle} confirmed"

		frappe.enqueue(
			"ride_management.utils.send_message",
			body=message,
			from_=frappe.db.get_single_value("Twilio Settings","from_phone_number"),
			to=self.phone,
		)




		

