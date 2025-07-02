from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from config import load_config
from db.db_connection import get_db_connection

# ✅ New imports for blueprints
from routes.leads import leads_bp
from routes.sales import sales_bp

# ✅ Load .env file from current folder
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# ✅ Optional debug print
print("DB Name from .env:", os.getenv("DB_NAME"))

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Load custom config (like secret keys)
app.config.from_object(load_config())

# ✅ Register API route blueprints
app.register_blueprint(leads_bp)
app.register_blueprint(sales_bp)

# ✅ Health check route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200

# ✅ Test DB connection route
@app.route('/test-db', methods=['GET'])
def test_db():
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"message": "DB connection successful ✅"}), 200
    else:
        return jsonify({"error": "DB connection failed ❌"}), 500

# ✅ Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
