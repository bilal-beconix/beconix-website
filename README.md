# Beconix Website (Static)

High-performance static marketing website for Beconix with lead capture routed directly to Make.com.

## Current Architecture

- Frontend: Static HTML + Tailwind CDN + vanilla JavaScript
- Hosting: Static hosting (recommended: Render Static Site or Cloudflare Pages)
- Form handling: Browser POST to Make webhook
- Assets: Local static files in /static

## Why This Version

The previous Flask free-web-service deployment had cold starts after idle periods.
This repo is now configured for static hosting to provide fast and consistent page loads.

## Project Structure

- index.html: Main website page for static hosting
- static/logo.svg: Brand logo and favicon source
- docs/: Deployment and DNS guides (some legacy docs may reference old Flask flow)

## Lead Form Flow

1. User submits either form on index.html
2. Frontend sends JSON to Make webhook endpoint
3. Make scenario processes and stores lead (for example to Google Sheets)

## Local Preview

Open index.html directly in browser, or run any simple static server.

Windows PowerShell example:

```powershell
cd "c:\Users\bilal\Downloads\AI VOICE WESBITE"
python -m http.server 5500
```

Then open:

http://localhost:5500

## Deploy (Render Static Site)

1. Render dashboard -> New -> Static Site
2. Connect this GitHub repository
3. Build command: leave empty
4. Publish directory: .
5. Deploy

## Domain (Namecheap)

Use the static-site target given by your host.

Required records:

- CNAME: Host www -> host-provided static target
- Root domain @: ALIAS/ANAME to same target, or 301 redirect to https://www.beconix.com

## Notes

- The Make webhook URL is client-visible in the browser with this setup.
- If you want to hide webhook URLs, use an edge function proxy (for example Cloudflare Worker).

## Status

- Static-only mode: enabled
- Flask backend files: removed
- Legacy Python tests: removed
