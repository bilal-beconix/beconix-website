# Deployment Guide - Beconix Website

## Step 1: Create GitHub Repository

### Option A: Using GitHub Web Interface (Easiest)

1. Go to [github.com/new](https://github.com/new)
2. **Repository name**: `beconix-website`
3. **Description**: "AI Voice Receptionist Website - Beconix"
4. **Privacy**: Public (free plan features; can change later)
5. **Initialize with**: Do NOT initialize (we'll push existing code)
6. Click "Create repository"

### Option B: Using GitHub CLI

```bash
gh repo create beconix-website --public --source=. --remote=origin --push
```

## Step 2: Push Code to GitHub (Local)

Open PowerShell in your project directory:

```powershell
cd "c:\Users\bilal\Downloads\AI VOICE WESBITE"

# Initialize git
git init

# Add your GitHub username and email
git config --global user.name "Your Name"
git config --global user.email "bilal@beconix.com"

# Add all files
git add .

# Commit
git commit -m "Initial commit: Beconix website with Flask backend"

# Add remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/beconix-website.git

# Push to GitHub
git branch -M main
git push -u origin main
```

After pushing, verify at `https://github.com/USERNAME/beconix-website`

---

## Step 3: Choose Deployment Platform

### ✅ RECOMMENDED: Render.com (Best Free Option)

**Why Render:**
- ✓ Completely free tier with no credit card required
- ✓ Supports Python/Flask natively
- ✓ Custom domain support
- ✓ Free SSL/HTTPS
- ✓ GitHub integration (auto-deploy on push)
- ✓ Suitable for production

**Price: $0/month** (Free tier)

### Alternative 1: Railway.app (Good Free Tier)

**Why Railway:**
- ✓ Free $5/month credits
- ✓ Auto-deploys from GitHub
- ✓ Python/Flask support
- ✓ Custom domain support
- ✓ Better performance than some free options

**Price: Free with $5 monthly credits**

### Alternative 2: PythonAnywhere (Python-Specific)

**Why PythonAnywhere:**
- ✓ Free tier available
- ✓ Python-specific (excellent support)
- ✓ No credit card needed
- ⚠ Custom domain requires paid plan ($5+/month)
- ✓ Good for learning

**Price: $0 or $5+/month for custom domain**

---

## DEPLOY TO RENDER.COM (Step-by-Step)

### 1. Sign Up

1. Go to [render.com](https://render.com)
2. Click "Get Started Free"
3. Connect GitHub account
4. Authorize Render to access your repositories

### 2. Create New Service

1. Dashboard → "New +" → "Web Service"
2. Select your `beconix-website` repository
3. Configure:
   - **Name**: `beconix-website`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free (perfect for this)

### 3. Environment Variables (Optional)

If you need to set environment variables:

1. Click "Advanced"
2. Add **Environment Variable**:
   - **Key**: `WEBHOOK_URL`
   - **Value**: `https://hook.us2.make.com/your-key` (if needed)
3. Click "Deploy"

**Note**: Your webhook URL is already hardcoded in `app.py`, so this is optional.

### 4. Deploy

- Click "Create Web Service"
- Render automatically deploys from your `main` branch
- Takes 2-5 minutes
- Live URL: `https://beconix-website.onrender.com` (or similar)

### 5. Setup Custom Domain (beconix.com)

1. **Service Dashboard** → Click "Settings"
2. **Custom Domain** → Add Domain
3. Enter: `www.beconix.com` or `beconix.com`
4. Render gives you DNS instructions
5. **Go to your domain registrar** (GoDaddy, Namecheap, etc.):
   - Update DNS CNAME record
   - **On Render's page, copy the CNAME value provided**
   - Add CNAME record: `CNAME www.beconix.com → render-cname-value`
   - Wait 24-48 hours for DNS propagation
6. Render auto-generates HTTPS certificate
7. Website now at `https://www.beconix.com`

---

## DEPLOY TO RAILWAY.APP (Alternative)

### 1. Sign Up & Connect

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Grant repository access

### 2. Create New Project

1. Dashboard → "New Project" → "Deploy from GitHub repo"
2. Select `beconix-website`
3. Railway auto-detects Python

### 3. Configure

1. The app deploys automatically
2. Railway detects `Procfile` and uses it
3. Live URL provided after deployment

### 4. Custom Domain

1. Project Settings → "Domains"
2. Add Domain: `beconix.com`
3. Railway provides CNAME target
4. Update DNS at registrar (same as Render)

---

## DEPLOY TO PYTHONANYWHERE (Free Tier)

### 1. Sign Up

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up (pick free account)
3. No credit card needed

### 2. Clone from GitHub

1. Files tab → Open SSH/terminal
2. Clone: `git clone https://github.com/USERNAME/beconix-website.git`
3. `cd beconix-website`
4. `mkvirtualenv --python=/usr/bin/python3.9 beconix`
5. `pip install -r requirements.txt`

### 3. Configure WSGI

1. Web tab → Add new web app
2. Choose Python 3.9
3. Framework: Flask
4. WSGI config file location: `/home/USERNAME/beconix-website/wsgi.py`

### 4. Create WSGI File

Create `/wsgi.py` in project root:

```python
from app import app as application
```

### 5. Reload & Test

1. Click "Reload" on Web tab
2. Website live at `https://USERNAME.pythonanywhere.com`

### 6. Custom Domain

- **Free tier**: Not available (would need paid plan)
- **Paid tier** ($5+/month): Supported via account settings

---

## Domain Configuration (All Platforms)

### For beconix.com:

**At your domain registrar** (GoDaddy, Namecheap, Bluehost, etc.):

1. Go to DNS settings
2. Add/Update CNAME record:
   ```
   Type: CNAME
   Name: www
   Value: [Platform-provided CNAME]
   TTL: 3600
   ```
3. Optional - Add root domain:
   ```
   Type: A
   Name: @
   Value: [Platform-provided IP, if available]
   ```
4. Wait 24-48 hours for DNS propagation

### Verify DNS:

```powershell
# In PowerShell, check if DNS is updated:
nslookup beconix.com
```

---

## Monitor Deployments

### Render.com
- Dashboard shows deployment logs
- Auto-redeploy on every GitHub push
- Monitor uptime and performance

### Railway.app
- Logs available in project dashboard
- Deployments tab shows history

### PythonAnywhere
- Web tab shows load and errors
- Logs available in console

---

## Troubleshooting

### Blank Page / 500 Error

**Check logs:**
- **Render**: Logs tab in dashboard
- **Railway**: Logs in project panel
- **PythonAnywhere**: Error log file

**Common issues:**
- Missing `gunicorn` in requirements.txt ✓ (Already added)
- Incorrect `static_folder` path
- WEBHOOK_URL not set (optional, already in app.py)

### Domain Not Working

1. Verify CNAME/A record added
2. Wait 24-48 hours
3. Clear browser cache (`Ctrl+Shift+Delete`)
4. Test with: `nslookup beconix.com`

### Form Submissions Not Working

1. Verify webhook URL in `app.py` (line 21)
2. Check leads_log.txt for local backups
3. Test Make.com webhook directly

---

## Next Steps After Deployment

1. ✅ Custom domain configured
2. Test form submissions on live site
3. Monitor Make.com Google Sheets integration
4. Share deployed link: `https://www.beconix.com`
5. Track analytics (optional: add Google Analytics)

---

## Quick Deployment Summary

| Platform | Cost | Setup Time | Custom Domain | Grade |
|----------|------|-----------|---|-------|
| **Render.com** | Free | 5 min | ✓ Yes | ⭐⭐⭐⭐⭐ |
| Railway.app | Free ($5 credits) | 5 min | ✓ Yes | ⭐⭐⭐⭐ |
| PythonAnywhere | Free | 10 min | Paid only | ⭐⭐⭐ |

**My Recommendation: Use Render.com** - Best free tier, easiest custom domain setup, perfect for production.
