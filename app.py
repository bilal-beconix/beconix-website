"""
Beconix - AI Receptionist Web Application
Flask backend for handling demo requests and webhook integration with Make/n8n
"""

from flask import Flask, render_template, request, jsonify
import os
import requests
from datetime import datetime

# ===== FLASK APP INITIALIZATION =====
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'beconix-ai-secret-key-2026')

# Configuration
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Webhook Configuration - Get from environment variable or use actual URL
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', 'https://hook.us2.make.com/5zii1syjfkdyjkja664p2j73qjgb8ekm')


# ===== ROUTES =====

@app.route('/')
def index():
    """Render the main homepage"""
    return render_template('index.html')


@app.route('/api/demo-request', methods=['POST'])
def demo_request():
    """
    Handle Demo form submissions
    Sends data to Google Sheets via Make/n8n webhook and logs locally
    
    Expected fields in request JSON:
    - name (required)
    - company (required)
    - position (optional)
    - email (required)
    - phone (required)
    """
    try:
        data = request.get_json()
        
        # ===== VALIDATION =====
        # Check required fields
        required_fields = ['name', 'company', 'email', 'phone']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False,
                    'message': f'Missing required field: {field}'
                }), 400
        
        # Validate email format
        email = data.get('email', '').strip()
        if '@' not in email:
            return jsonify({
                'success': False,
                'message': 'Invalid email address'
            }), 400
        
        # ===== WEBHOOK FORWARDING (Non-Blocking) =====
        # Forward to Make/n8n webhook to push to Google Sheets
        # Wrapping in try-except so form still succeeds even if webhook is slow/down
        webhook_sent = False
        try:
            if WEBHOOK_URL != 'https://hook.us1.make.com/YOUR_WEBHOOK_ID':
                response = requests.post(WEBHOOK_URL, json=data, timeout=5)
                webhook_sent = response.status_code < 400
                print(f"✓ Webhook sent (Status: {response.status_code})")
            else:
                print("⚠ Webhook URL not configured - using local logging only")
        except requests.exceptions.RequestException as e:
            print(f"⚠ Webhook error (non-blocking): {e}")
        
        # ===== LOCAL BACKUP LOGGING =====
        # Save to local log file as backup
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = (
            f"{timestamp} | "
            f"Name: {data.get('name')} | "
            f"Company: {data.get('company')} | "
            f"Position: {data.get('position', 'N/A')} | "
            f"Email: {email} | "
            f"Phone: {data.get('phone')}\n"
        )
        
        with open('leads_log.txt', 'a') as f:
            f.write(log_entry)
        
        print(f"✓ Lead logged: {email}")
        
        # ===== RESPONSE =====
        return jsonify({
            'success': True,
            'message': 'Thank you! Connecting to Amelia...',
            'data': {
                'email': email,
                'name': data.get('name'),
                'company': data.get('company')
            }
        }), 200
    
    except Exception as e:
        print(f"❌ Error in demo_request: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Beconix AI Receptionist',
        'webhook_configured': WEBHOOK_URL != 'https://hook.us1.make.com/YOUR_WEBHOOK_ID'
    }), 200


# ===== ERROR HANDLERS =====

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found', 'status': 404}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error', 'status': 500}), 500


# ===== MAIN ENTRY POINT =====

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 BECONIX - AI RECEPTIONIST")
    print("="*70)
    print(f"  🌐 Server: http://127.0.0.1:5000")
    print(f"  🔗 Webhook: {'✅ Configured' if WEBHOOK_URL != 'https://hook.us1.make.com/YOUR_WEBHOOK_ID' else '❌ Not Configured (using local logging)'}")
    print(f"  📧 Logs saved to: leads_log.txt")
    print("="*70)
    print("\n  Press CTRL+C to stop server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
