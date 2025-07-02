# utils/sms.py

from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")

print("📡 Twilio SID:", TWILIO_SID)
print("📲 Twilio From Number:", TWILIO_PHONE)

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_sms(to, msg):
    try:
        print(f"📤 Sending SMS to {to}...")
        message = client.messages.create(
            body=msg,
            from_=TWILIO_PHONE,
            to=to
        )
        print(f"✅ SMS sent to {to}, SID: {message.sid}")
        return True
    except Exception as e:
        print(f"❌ Failed to send SMS to {to}. Error:\n{e}")
        return False
