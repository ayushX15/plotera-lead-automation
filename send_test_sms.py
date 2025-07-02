# send_test_sms.py

from utils.sms import send_sms

if __name__ == "__main__":
    receiver = "+919119272180"
    message = "Hello Ayush! 🚀 This is a live test SMS from your backend. If your received this message then your PLOTERA PROJECT IS WORKING."

    print("🔄 Trying to send SMS...")
    result = send_sms(receiver, message)

    if result:
        print("✅ SMS sent successfully!")
    else:
        print("❌ SMS sending failed.")
