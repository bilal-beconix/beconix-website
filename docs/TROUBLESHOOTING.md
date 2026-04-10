# Troubleshooting

## Site loads on www but not root

Cause: missing @ record or redirect.
Fix: add root redirect/ALIAS in Namecheap.

## Form submit fails in browser

Check:
- Make scenario is enabled.
- Webhook URL in index.html is correct.
- Browser console for network errors.

## Form returns CORS error

Direct Make webhook should allow CORS for this setup.
If CORS becomes restricted, place a proxy in front (Cloudflare Worker).

## Changes are not visible

- Wait for DNS propagation.
- Hard refresh browser (Ctrl + F5).
- Check you deployed latest Git commit.
