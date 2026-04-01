# Beconix - AI Voice Receptionist

A modern web application showcasing Beconix AI phone agents for medical practices and service businesses.

## Features

- **AI Phone Agent Demo** - Live demonstration of voice capabilities
- **Responsive Design** - Mobile-optimized for all devices (iPhone, iPad, Desktop)
- **Lead Management** - Contact forms integrated with Make.com webhook
- **HIPAA Compliance** - Security-focused design
- **Multi-specialty Solutions** - Dental, MedSpa, Aesthetics, Concierge Medicine
- **Real-time Webhook Integration** - Automatic data sync with Google Sheets

## Tech Stack

- **Backend**: Python 3.13 + Flask 2.3.3
- **Frontend**: HTML5 + Tailwind CSS (CDN)
- **Integration**: Make.com webhook for lead capture
- **Deployment**: Render.com (recommended) or Railway.app

## Local Setup

### Prerequisites
- Python 3.8+
- pip or virtual environment manager

### Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/beconix-website.git
cd beconix-website

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

The website will be available at `http://localhost:5000`

## Deployment

### Option 1: Render.com (Recommended - Free Tier)

1. Push code to GitHub
2. Sign up at [render.com](https://render.com)
3. Create new Web Service → Connect GitHub repo
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Add environment variables if needed
7. Connect custom domain in settings

### Option 2: Railway.app (Free Credits)

1. Sign up at [railway.app](https://railway.app)
2. Connect GitHub repository
3. Automatic Python detection and deployment
4. Custom domain configuration available

### Option 3: PythonAnywhere (Free Tier)

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload code or clone from GitHub
3. Configure WSGI application
4. Free tier includes subdomain; custom domain requires paid plan

## Custom Domain Setup

1. Update DNS records at your domain registrar (beconix.com)
2. Point to deployment platform's nameservers or CNAME
3. Enable HTTPS (all platforms provide free SSL)
4. Platform-specific instructions:
   - **Render**: Add CNAME in DNS settings
   - **Railway**: Configure domain in project settings
   - **PythonAnywhere**: Available in account settings

## Environment Variables

Create `.env` file (not committed to git):

```
FLASK_ENV=production
WEBHOOK_URL=https://hook.us2.make.com/your-webhook-key
```

## API Endpoints

- `GET /` - Homepage
- `POST /api/demo-request` - Form submission (forwards to webhook + local logging)
- `GET /api/health` - Health check

## File Structure

```
beconix-website/
├── app.py                      # Flask application (main backend)
├── requirements.txt            # Python dependencies
├── Procfile                    # Deployment configuration
├── render.yaml                 # Render-specific config
├── README.md                   # This file
├── docs/                       # Documentation
│   ├── DEPLOYMENT_GUIDE.md    # All deployment options
│   ├── DEPLOY_NOW.md          # Step-by-step deployment
│   ├── QUICK_START.md         # Quick overview
│   ├── NAMECHEAP_DNS_SETUP.md # DNS configuration
│   └── FIX_REPORT.md          # Bug fixes and improvements
├── tests/                      # Test files
│   ├── test_fixed_app.py      # Flask app tests
│   ├── test_logo.py           # Logo display tests
│   ├── test_mobile.py         # Mobile responsiveness tests
│   └── test_webhook.py        # Webhook integration tests
├── templates/
│   └── index.html             # Main website (HTML + Tailwind)
└── static/
    └── logo.svg               # Brand logo (SVG)
```

## Contact

- Email: bilal@beconix.com
- Address: 75 Franklin Square, Elmont, NY 11001

## License

Proprietary - Beconix 2026
