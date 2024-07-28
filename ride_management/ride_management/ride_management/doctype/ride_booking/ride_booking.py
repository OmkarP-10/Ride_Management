import frappe
from frappe.model.document import Document

class RideBooking(Document):
    def validate(self):
        # Validate the phone_number to be a valid 10-digit phone number, except the country code.
        # If it does not have a country code, prepend +91.
        if not self.phone_number:
            frappe.throw("Please enter a valid contact number")
        if len(self.phone_number) == 10:
            self.phone_number = f"+91{self.phone_number}"
        elif len(self.phone_number) == 13 and self.phone_number.startswith("+91"):
            pass
        else:
            frappe.throw("Please enter a valid contact number")

    def after_insert(self):
        self.set_ride_order()
        
    def on_cancel(self):
        self.cancel_doc()

    def set_ride_order(self):
        ride = frappe.get_doc({
            "doctype": "Ride Order",
            "vehicle": self.vehicle,
            "customer_name": self.customer_name,
            "phone": self.phone_number,
            "pickup_address": self.pickup_location
        })
        ride.insert()
        
    def cancel_doc(self):
        # Assuming phone_number is a unique identifier for the Ride Order
        ride_orders = frappe.get_all("Ride Order", filters={"phone": self.phone_number}, fields=["name"])
        for order in ride_orders:
            frappe.delete_doc("Ride Order", order["name"])
        
        # Properly delete the current Ride Booking document
        if self.name:
            frappe.delete_doc("Ride Booking", self.name)
