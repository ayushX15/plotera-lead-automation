# routes/leads.py

from flask import Blueprint, request, jsonify
from db.db_connection import get_db_connection
from datetime import date

leads_bp = Blueprint('leads', __name__)

# 🔸 Add new lead
@leads_bp.route('/add-lead', methods=['POST'])
def add_lead():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    interest = data.get('interest')
    visit_date = data.get('visit_date')  # format: YYYY-MM-DD

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO leads (name, phone, interest, visit_date)
            VALUES (%s, %s, %s, %s)
        """, (name, phone, interest, visit_date))
        conn.commit()
        conn.close()
        return jsonify({"message": "✅ Lead added successfully"}), 201
    return jsonify({"error": "❌ Failed to add lead"}), 500

# 🔸 Get all leads
@leads_bp.route('/get-leads', methods=['GET'])
def get_leads():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM leads")
        leads = cursor.fetchall()
        conn.close()
        return jsonify(leads), 200
    return jsonify({"error": "❌ Could not fetch leads"}), 500

# 🔸 Get today's visits
@leads_bp.route('/get-today-visits', methods=['GET'])
def get_today_visits():
    today = date.today().isoformat()
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM leads WHERE visit_date = %s", (today,))
        visits = cursor.fetchall()
        conn.close()
        return jsonify(visits), 200
    return jsonify({"error": "❌ Failed to fetch today's visits"}), 500

# 🔸 Update lead status
@leads_bp.route('/update-status', methods=['PUT'])
def update_status():
    data = request.get_json()
    lead_id = data.get('id')
    new_status = data.get('status')

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE leads SET status = %s WHERE id = %s", (new_status, lead_id))
        conn.commit()
        conn.close()
        return jsonify({"message": "✅ Status updated"}), 200
    return jsonify({"error": "❌ Failed to update status"}), 500

# 🔸 Assign salesperson
@leads_bp.route('/assign-salesperson', methods=['PUT'])
def assign_salesperson():
    data = request.get_json()
    lead_id = data.get('id')
    salesperson_id = data.get('assigned_to')

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE leads SET assigned_to = %s WHERE id = %s", (salesperson_id, lead_id))
        conn.commit()
        conn.close()
        return jsonify({"message": "✅ Salesperson assigned"}), 200
    return jsonify({"error": "❌ Failed to assign salesperson"}), 500
