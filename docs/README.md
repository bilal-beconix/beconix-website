# Documentation

This project now runs as a static website.

## Files

- DEPLOY_STATIC.md: Static hosting deployment steps
- DNS_NAMECHEAP.md: Namecheap DNS records for custom domain
- TROUBLESHOOTING.md: Common issues and fixes

## Architecture

- Static page: /index.html
- Static assets: /static
- Form submit target: Make webhook (direct browser POST)

## Important

The old Flask backend flow was removed from this repository.
If you need hidden webhook URLs in the future, add an edge proxy (for example Cloudflare Worker).
