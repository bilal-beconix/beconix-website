# Namecheap DNS Setup - Exact Steps for beconix.com

## 🎯 Your CNAME Values (from Render)

```
Record 1: www.beconix.com
Hostname: www
Target: beconix-website.onrender.com

Record 2: beconix.com (root domain)
Hostname: @ (at symbol)
Target: beconix-website.onrender.com
```

---

## 📍 LOGIN & NAVIGATE TO NAMECHEAP DNS

### Step 1: Open Namecheap
1. Go to [namecheap.com](https://namecheap.com)
2. Click **"Sign In"** (top right)
3. Login with your Namecheap account

### Step 2: Find Your Domain
1. After login, click your **Account** dropdown (top right)
2. Click **"Manage Domains"**
3. Find **beconix.com** in the list
4. Click **"Manage"**

### Step 3: Advanced DNS
1. You're on the domain management page
2. Click the **"Advanced DNS"** tab (should be 2nd from left)
3. Look for **"Host Records"** section

---

## ✍️ ADD TWO CNAME RECORDS

You need to add/modify TWO records:

### RECORD #1: www.beconix.com

In the Host Records section:

**Look for a record with Host = `www`**

If it exists:
- Click the **Edit** icon (pencil)
- Change **Type** to: `CNAME`
- Change **Value** to: `beconix-website.onrender.com`
- Keep **TTL**: 3600
- Click **Save** ✅

If it doesn't exist:
- Click **"Add Record"**
- **Type**: CNAME
- **Host**: www
- **Value**: beconix-website.onrender.com
- **TTL**: 3600
- Click checkmark ✅

---

### RECORD #2: beconix.com (root domain)

**Look for a record with Host = `@`**

If you see an A record with `@`:
- Click **Edit** (pencil)
- Change **Type** to: `CNAME`
- Change **Value** to: `beconix-website.onrender.com`
- Click **Save** ✅

If you see MX records with `@` (mail):
- **Leave those alone** (don't touch mail records)
- Click **"Add Record"** to add a new one
- **Type**: CNAME
- **Host**: @
- **Value**: beconix-website.onrender.com
- **TTL**: 3600
- Click checkmark ✅

**Note**: Some registrars don't allow CNAME on root domain (@). If Namecheap blocks it:
- Try **"Alias"** instead of CNAME (same thing)
- Or use **"A Record"** with value `216.24.57.1` (Render's IP for basic routing)

---

## 📋 EXPECTED RESULT

After adding both records, your Namecheap DNS should show:

```
Type   | Host | Value                         | TTL
-------|------|-------------------------------|-------
CNAME  | www  | beconix-website.onrender.com | 3600
CNAME  | @    | beconix-website.onrender.com | 3600
A      | @    | 75.*.*.* (old IP)            | 3600
MX     | @    | aspmx.l.google.com           | 3600
```

---

## ⏱️ WAIT FOR DNS PROPAGATION

**Namecheap might say:**
```
"DNS changes can take 24 hours or longer to propagate"
```

This is normal. While you wait:

### Option A: Test the Render URL (Works immediately)
- Visit: `https://beconix-website.onrender.com`
- Everything should work here RIGHT NOW
- Logo, forms, mobile - all tested

### Option B: Check DNS Status

**In PowerShell, check when DNS is ready:**

```powershell
# Check www subdomain
nslookup www.beconix.com

# Check root domain
nslookup beconix.com
```

**When ready, you'll see:**
```
Non-authoritative answer:
Name:    www.beconix.com
Address: 104.*.*.* (Render's server IP)
```

---

## 🌐 ONCE DNS PROPAGATES (24-48 hours)

Visit these and they should work:
- ✅ `https://www.beconix.com` (primary)
- ✅ `https://beconix.com` (redirects to www)
- ✅ `https://beconix-website.onrender.com` (always works)

All three point to your live website! 🎉

---

## 📷 SCREENSHOT GUIDE

### In Namecheap "Advanced DNS" tab:

```
╔════════════════════════════════════════════╗
║         HOST RECORDS (Important)           ║
╠════╦════════╦═══════════════════════╦═════╣
║Type║ Host   ║ Value                 ║ TTL ║
╠════╬════════╬═══════════════════════╬═════╣
║CNAME│ www   │beconix-website.onre..│3600 │
║CNAME│  @    │beconix-website.onre..│3600 │
║  A  │  @    │75.*.*.* (old IP)     │3600 │
║ MX  │  @    │aspmx.l.google...    │3600 │
╚════╩════════╩═══════════════════════╩═════╝
```

---

## 🔧 TROUBLESHOOTING

### "Namecheap says CNAME on @ is not allowed"

**Solution**: Use **Alias** instead (same thing, different name)
- Type: **Alias**
- Host: **@**
- Value: **beconix-website.onrender.com**

### "DNS still not working after 48 hours"

1. **Clear browser cache**: `Ctrl + Shift + Delete`
2. **Flush DNS cache**: 
   ```powershell
   ipconfig /flushdns
   ```
3. **Try different browser** (Chrome, Firefox, Edge)
4. **Check Namecheap records** - Make sure you saved the edits

### "HTTPS shows warning/error on custom domain"

1. Go back to Render dashboard
2. Click your **beconix-website** service
3. Go to **Settings** → **Custom Domains**
4. Wait for Render to auto-generate SSL certificate (up to 1 hour)
5. Try again

---

## ✅ FINAL CHECKLIST

- [ ] Opened Namecheap and logged in
- [ ] Went to Manage Domains → beconix.com
- [ ] Clicked Advanced DNS tab
- [ ] Added/edited CNAME record for `www` → `beconix-website.onrender.com`
- [ ] Added/edited CNAME record for `@` → `beconix-website.onrender.com`
- [ ] Saved all changes
- [ ] Tested Render URL: `https://beconix-website.onrender.com` ✅ (works now)
- [ ] Waiting for DNS to propagate (24-48 hours)
- [ ] Will test custom domain: `https://www.beconix.com` (wait for DNS)

---

## 🎯 SUMMARY

**What you just did:**
1. ✅ Created GitHub repo
2. ✅ Pushed code to GitHub
3. ✅ Deployed to Render.com (Running)
4. ✅ Added custom domain to Render
5. ⏳ Adding DNS records to Namecheap (THIS STEP)

**What's left:**
- Add 2 CNAME records in Namecheap DNS
- Wait 24-48 hours for DNS propagation
- Website live at `https://www.beconix.com` 🎉

---

## 📞 NEED HELP?

**Stuck on Namecheap DNS?**
- Namecheap Support: support@namecheap.com
- Docs: https://www.namecheap.com/support/knowledgebase/

**Render not working?**
- Test immediately at: https://beconix-website.onrender.com
- Check Render Logs tab for errors

**Let me know when DNS records are added!** ✅
