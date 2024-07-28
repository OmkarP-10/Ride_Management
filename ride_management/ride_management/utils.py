import frappe

from twilio.rest import Client
from frappe.utils.password import get_decrypted_password

def get_twilio_client():
    account_sid = frappe.db.get_single_value("Twilio Settings", "account_sid")
    auth_token = get_decrypted_password("Twilio Settings", "Twilio Settings", "auth_token")

    if not account_sid or not auth_token:
        frappe.throw("Please enter your Twilio Account SID and Auth Token in Appointments Twilio Settings")

    return Client(account_sid, auth_token)

# From -> "+18149047351"

def send_message(body, from_, to):
    client = get_twilio_client()
    message = client.messages.create(
        body=body,
        from_=from_,
        to=to
    )

    return message.sid