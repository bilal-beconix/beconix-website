# DEPLOYMENT - Step by Step (bilal-beconix)

## ✅ Status
- GitHub username: **bilal-beconix**
- Domain registrar: **Namecheap**
- Custom domain: **beconix.com**
- Ready to deploy: **YES**

---

## 🔴 STEP 1: Create GitHub Repository (DO THIS FIRST)

**Why?** The repository doesn't exist yet on GitHub.

### Option A: Using Web Browser (Easiest - RECOMMENDED)

1. Go to [github.com/new](https://github.com/new)
2. Fill in the form:
   - **Repository name**: `beconix-website`
   - **Description**: `AI Voice Receptionist Website - Beconix`
   - **Visibility**: Public
   - **Initialize with**: Do NOT check anything (we already have files)
3. Click **"Create repository"**

**After creating, GitHub shows you a page with commands. That's perfect!**

### Option B: Using GitHub CLI (If Installed)

```powershell
gh repo create beconix-website --public --source=. --remote=origin --push
```

---

## ✅ STEP 2: Push Code to GitHub

Once the repository exists, run this in PowerShell:

```powershell
cd "c:\Users\bilal\Downloads\AI VOICE WESBITE"

# Add your GitHub remote
git remote add origin https://github.com/bilal-beconix/beconix-website.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Expected output:**
```
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
...
 * [new branch]      main -> main
Branch 'main' is set up to track 'origin/main'.
```

✅ **Your code is now on GitHub!**
Visit: `https://github.com/bilal-beconix/beconix-website`

---

## 🟢 STEP 3: Deploy to Render.com (5 minutes)

### 3.1 Sign Up at Render

1. Go to [render.com](https://render.com)
2. Click **"Get Started Free"** (top right)
3. Click **"Sign up with GitHub"**
4. Authorize Render to access your GitHub account
5. It will ask which repository to connect → Select **beconix-website**

### 3.2 Create Web Service

1. In Render dashboard, click **"New +"** (top right)
2. Select **"Web Service"**
3. Find **beconix-website** in the list
4. Click **"Connect"**

### 3.3 Configure Service

Fill in these exact values:

- **Name**: `beconix-website`
- **Environment**: `Python 3`
- **Region**: `Oregon` (US) or closest to you
- **Branch**: `main`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Instance Type**: **Free** ← IMPORTANT!

**Click "Create Web Service"**

Render will start deploying. This takes 2-5 minutes. You'll see:
- Building... 🟡
- Running ✅ (Done!)

### 3.4 Get Your Live URL

Once deployment finishes (status = "Running"):
- Render shows you: `https://beconix-website.onrender.com`
- ✅ Your website is **LIVE**!

---

## 🟡 STEP 4: Connect Custom Domain (beconix.com) on Namecheap

### 4.1 Configure in Render

1. In Render dashboard, find your **beconix-website** service
2. Click **"Settings"** tab (bottom left)
3. Scroll to **"Custom Domains"** section
4. Click **"Add Custom Domain"**
5. Enter: `www.beconix.com`
6. Click **"Add"**

**Render shows you:**
```
CNAME: beconix-website.onrender.com
```

**✅ Copy this CNAME value** - you need it next!

---

### 4.2 Update DNS in Namecheap

**Login to Namecheap:**

1. Go to [namecheap.com](https://namecheap.com)
2. Login to your account
3. Go to **"Manage Domains"**
4. Find **beconix.com** in the list
5. Click **"Manage"**

**In the domain management page:**

1. Click **"Advanced DNS"** tab (should be second tab)
2. Look for **"Host Records"** section
3. **Find or Create CNAME record:**

   | Type | Host | Value | TTL |
   |------|------|-------|-----|
   | CNAME | www | beconix-website.onrender.com | 3600 |

**Steps:**
- If `www` record exists: Click **Edit** and replace the value
- If `www` record doesn't exist: Click **"Add Record"** and fill in above
- **TTL**: Set to 3600 (or leave as is)
- Click **"Save"** button

**Optional - Also add root domain:**

| Type | Host | Value | TTL |
|------|------|-------|-----|
| CNAME | @ | www.beconix.com | 3600 |

Or Namecheap might ask for "redirect" instead of CNAME. If you see that option, use:
- **Permanent Redirect (301)**: Redirect to `https://www.beconix.com`

---

### 4.3 Wait for DNS Propagation

DNS changes take **24-48 hours** to propagate globally.

**Check if it's working:**

Open PowerShell and run:
```powershell
nslookup www.beconix.com
```

You should see:
```
Non-authoritative answer:
Name:    www.beconix.com
Address: [Render's IP address]
```

Once resolved, visit:
- ✅ `https://www.beconix.com` 
- ✅ `https://beconix-website.onrender.com` (both work)

---

## 📋 CHECKLIST

### GitHub ✅
- [ ] Created repository: `beconix-website` on GitHub
- [ ] Pushed code to GitHub
- [ ] Visit `https://github.com/bilal-beconix/beconix-website` and see your code

### Render Deployment ✅
- [ ] Signed up at render.com with GitHub
- [ ] Created Web Service from beconix-website repo
- [ ] Set "Instance Type" to "Free"
- [ ] Deployment status shows "Running" ✅
- [ ] Website loads at `https://beconix-website.onrender.com`
- [ ] Logo displays correctly
- [ ] Forms work (select a field, type text)

### Namecheap DNS ✅
- [ ] Logged into Namecheap
- [ ] Found beconix.com domain
- [ ] Added CNAME record: `www → beconix-website.onrender.com`
- [ ] Waited 24-48 hours
- [ ] Verified with `nslookup www.beconix.com`
- [ ] Website loads at `https://www.beconix.com` ✅

---

## 🔧 Troubleshooting

### Website shows "Service Unavailable" or 502 Error

1. Check Render logs:
   - Render dashboard → Your service → "Logs" tab
   - Look for error messages
2. Common causes:
   - Missing `gunicorn` in requirements.txt ✓ (Already added)
   - Wrong start command ✓ (Correct)
   - Port not exposed ✓ (Flask defaults to port 5000, Render handles this)

### Domain not working after 48 hours

1. Clear browser cache: `Ctrl + Shift + Delete`
2. Try different browser (Chrome, Firefox, etc.)
3. Check DNS: `nslookup www.beconix.com`
4. If still failing, contact Namecheap support

### Forms not submitting

1. Check Make.com webhook is working
2. Look in project folder for `leads_log.txt` - shows backup logs
3. Try form on `https://beconix-website.onrender.com` first (before domain works)

---

## 🎉 After Deployment

**Your workflow becomes:**

1. **Make changes locally** in VS Code
2. **Test locally** at `http://localhost:5000`
3. **Push to GitHub**: `git add . && git commit -m "description" && git push`
4. **Render auto-deploys** (2-5 minutes)
5. **See live changes** at `https://www.beconix.com`

No manual redeploy needed! Automation FTW 🚀

---

## Summary Timeline

| Step | Time | When |
|------|------|------|
| 1. Create GitHub repo | 2 min | Now |
| 2. Push to GitHub | 1 min | Right after |
| 3. Deploy to Render | 5-10 min | Right after |
| 4. Setup DNS on Namecheap | 10 min | Right after |
| 5. Wait for DNS propagation | 24-48 hours | Happens automatically |

**Total active time: ~30 minutes**
**Total time to live domain: ~48 hours**

---

## Need Help?

Each step is independent. You can:
1. Create GitHub repo now
2. Push code now
3. Deploy to Render now
4. Update DNS now
5. Check back in 24-48 hours

No step blocks another! 🚀

**Ready to start Step 1?**
