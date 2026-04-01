# Namecheap DNS Setup for beconix.com with Render.com

## 🎯 Quick Reference

After you deploy to Render, Render will give you:
```
CNAME: beconix-website.onrender.com
```

You need to add this to Namecheap. Here's exactly how:

---

## 📍 Navigate to Namecheap DNS Settings

### Step 1: Login to Namecheap
1. Go to [namecheap.com](https://namecheap.com)
2. Click **"Sign In"** (top right)
3. Enter your Namecheap credentials

### Step 2: Find Your Domain
1. After login, go to **"Account"** dropdown (top right)
2. Click **"Manage Domains"**
3. In the domain list, find **beconix.com**
4. Click **"Manage"**

### Step 3: Go to Advanced DNS
1. You're now on the domain details page
2. Click the **"Advanced DNS"** tab (usually second from left)
3. You should see **"Host Records"** section

---

## ✍️ Add CNAME Record

### Where You'll See Default Records:

```
+---------+---+---------+--------+
| Type    | Host | Value | TTL |
+---------+---+---------+--------+
| A       | @ | 75.*.*.*| 3600 |
| MX      | @ | aspmx.l...| 3600 |
+---------+---+---------+--------+
```

### Add New WWW CNAME Record:

**Click "Add Record"** (yellow button)

Fill in:
- **Type**: CNAME
- **Host**: `www`
- **Value**: `beconix-website.onrender.com`
- **TTL**: 3600 (or leave default)

Click ✅ **checkmark to save**

---

## 🏠 OPTIONAL: Root Domain Setup

If you want `beconix.com` (without www) to also work:

**Option A: Redirect**
- Type: Permanent Redirect (301)
- Host: `@`
- Value: `https://www.beconix.com`

**Option B: CNAME (Advanced)**
- Type: CNAME
- Host: `@`
- Value: `www.beconix.com`

(Namecheap's "Alias" is same as CNAME for this purpose)

⚠️ **Note**: Some registrars don't allow CNAME on root domain (@). Redirect works better.

---

## ✅ Complete DNS Record Example

After setup, your Namecheap should show:

```
Type    | Host      | Value                         | TTL
--------|-----------|-------------------------------|------
CNAME   | www       | beconix-website.onrender.com | 3600
Redirect| @         | https://www.beconix.com      | 3600
A       | @         | 75.*.*.*                     | 3600
MX      | @         | aspmx.l...                   | 3600
```

---

## 🔍 Verify DNS is Working

After you've updated Namecheap (5-10 minutes to apply):

**In PowerShell:**
```powershell
nslookup www.beconix.com
```

**Expected output:**
```
Non-authoritative answer:
Name:    www.beconix.com
Address: 104.*.*.* (Render's server)
```

If you see an address, DNS is working! ✅

**If still showing old address:**
- Wait another 24 hours
- Clear DNS cache: `ipconfig /flushdns` (PowerShell as Admin)
- Try incognito/private browser

---

## 🌐 Test Your Domain

Once DNS resolves (shows Render's address):

1. Open browser
2. Go to: `https://www.beconix.com`
3. You should see your website! 🎉

**Browser might show "SSL/TLS error"?** Don't worry:
- Render auto-generates certificate (takes up to 1 hour)
- Wait a bit, refresh browser
- Should work fine

---

## Common Namecheap Issues & Fixes

### Issue: Can't find "Advanced DNS" tab
**Solution**: Make sure you clicked **"Manage"** on the domain (not just viewing list)

### Issue: Host field requires selection from dropdown
**Solution**: Type `www` and it should appear as option - select it

### Issue: It says "Invalid CNAME"
**Solution**: Make sure Value is exactly: `beconix-website.onrender.com` (no https://)

### Issue: Domain redirects to Namecheap parked domain page
**Solution**: 
1. Check if "Parking" is enabled in Namecheap
2. Go to "Domain" tab (not Advanced DNS)
3. Make sure "Parking" is **Disabled** or **Forwarded** to your site

---

## 📌 Important: Order of Operations

1. ✅ Create GitHub repo
2. ✅ Push code to GitHub
3. ✅ Deploy to Render.com
4. ⏳ Get CNAME from Render: `beconix-website.onrender.com`
5. ⏳ Update DNS on Namecheap (add CNAME record)
6. ⏳ Wait 24-48 hours for propagation
7. 🎉 Website live at `https://www.beconix.com`

You can test the website at `https://beconix-website.onrender.com` while waiting for DNS!

---

## 💡 Pro Tip: Monitor Logs While Waiting

**While DNS propagates**, make sure everything else works:

1. Visit `https://beconix-website.onrender.com` (Render URL - works immediately)
2. Test all forms and click buttons
3. Check that logo displays
4. Mobile test (resize browser or use phone)

Once DNS works, same site appears at `https://www.beconix.com`

---

## Namecheap Support

If you get stuck:
- Email: support@namecheap.com
- Namecheap docs: [namecheap.com/dns](https://www.namecheap.com/support/knowledgebase/article.aspx/319/2176/how-do-i-set-up-host-records-for-a-domain)
- Free support chat on namecheap.com

---

## Next Steps

### Ready to Deploy?

1. **Go to GitHub** → Create `beconix-website` repository
2. **Run in PowerShell**:
   ```powershell
   cd "c:\Users\bilal\Downloads\AI VOICE WESBITE"
   git remote add origin https://github.com/bilal-beconix/beconix-website.git
   git branch -M main
   git push -u origin main
   ```
3. **Sign up at Render.com** with GitHub
4. **Render deploys automatically**
5. **Get CNAME from Render**
6. **Follow this guide to update Namecheap**
7. **Wait 24-48 hours** ☕
8. **Visit `https://www.beconix.com`** 🎉

Let me know when you're at the Render CNAME step - I can help with exact value!
