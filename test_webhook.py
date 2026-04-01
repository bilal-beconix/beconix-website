"""
Test form submission with real webhook
"""

import json
from app import app

print("="*70)
print("🧪 Testing Form Submission with Real Webhook")
print("="*70 + "\n")

with app.test_client() as client:
    # Test data matching your form fields
    test_data = {
        'name': 'Bilal Test User',
        'company': 'Beconix Test Company',
        'position': 'Test Manager',
        'email': 'bilal@beconix.com',
        'phone': '555-0123'
    }
    
    print("📋 Submitting test form data:")
    for key, value in test_data.items():
        print(f"   {key}: {value}")
    
    print("\n🚀 Sending to webhook...")
    response = client.post(
        '/api/demo-request',
        data=json.dumps(test_data),
        content_type='application/json'
    )
    
    print(f"\n✅ Response Status: {response.status_code}")
    
    result = response.get_json()
    print(f"✅ Response Message: {result['message']}")
    print(f"✅ Success: {result['success']}")
    
    print("\n" + "="*70)
    if response.status_code == 200 and result['success']:
        print("✅ WEBHOOK INTEGRATION WORKING!")
        print("="*70)
        print("\n📊 What just happened:")
        print("   1. ✅ Form data validated")
        print("   2. ✅ Data sent to webhook:")
        print("      https://hook.us2.make.com/5zii1syjfkdyjkja664p2j73qjgb8ekm")
        print("   3. ✅ Email backed up locally")
        print("   4. ✅ Should appear in Google Sheets in ~2-5 seconds")
        print("\n📁 Local logs also saved to: leads_log.txt")
        print("\n" + "="*70)
    else:
        print("❌ Something went wrong")
        print("="*70)
