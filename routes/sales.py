# routes/sales.py

from flask import Blueprint, jsonify
from db.db_connection import get_db_connection

sales_bp = Blueprint('sales', __name__)

# 🔸 Get all salespersons
@sales_bp.route('/get-salespersons', methods=['GET'])
def get_salespersons():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM salespersons")
        sales = cursor.fetchall()
        conn.close()
        return jsonify(sales), 200
    return jsonify({"error": "❌ Failed to fetch salespersons"}), 500
