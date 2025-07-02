import os
import logging
from datetime import date
from dotenv import load_dotenv
from db.db_connection import get_db_connection
from utils.sms import send_sms

# Load environment variables
load_dotenv()

# Set up logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "app.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def send_daily_reminders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    today = date.today().isoformat()
    logging.info(f"🔍 Checking leads for visit today: {today}")

    try:
        cursor.execute("""
            SELECT l.id, l.name AS client_name, l.phone AS client_phone, l.visit_date,
                s.name AS salesperson_name, s.phone AS salesperson_phone
            FROM leads l
            JOIN salespersons s ON l.assigned_to = s.id
            WHERE l.visit_date = %s AND l.status = 'Scheduled'
        """, (today,))

        
        visits = cursor.fetchall()

        if not visits:
            logging.info("📭 No visits scheduled for today.")
            print("📭 No visits scheduled for today.")
            return

        for visit in visits:
            client_msg = f"Hello {visit['client_name']}, reminder: You have a site visit scheduled today. See you soon!"
            sales_msg = f"Reminder: Visit scheduled with {visit['client_name']} today."

            # Send SMS to client
            client_result = send_sms(visit['client_phone'], client_msg)

            # Send SMS to salesperson
            sales_result = send_sms(visit['salesperson_phone'], sales_msg)

            # Log results
            if client_result and sales_result:
                logging.info(f"✅ Reminder sent to {visit['client_name']} and {visit['salesperson_name']}")
                print(f"✅ SMS sent for lead ID {visit['id']}")
            else:
                logging.error(f"❌ Failed to send reminder for lead ID {visit['id']}")
                print(f"❌ SMS failed for lead ID {visit['id']}")

    except Exception as e:
        logging.error(f"❌ Error while sending reminders: {e}")
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    send_daily_reminders()
