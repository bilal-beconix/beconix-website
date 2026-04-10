# Namecheap DNS Setup

## Required Records

Use the target hostname provided by your static host.

- CNAME | Host: www | Value: <your-static-host-target> | TTL: Automatic
- URL Redirect (301) or ALIAS for root:
  - Host: @
  - Value: https://www.beconix.com

## Keep Existing Non-Website Records

Do not remove records used by email or MailerLite verification unless they conflict with host @ or host www.

## Validation

Run in PowerShell:

```powershell
nslookup www.beconix.com
nslookup beconix.com
```

Expected:
- www resolves to your static host
- root resolves or redirects to www
