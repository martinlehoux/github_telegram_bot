- https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#issues

```bash
poetry export --without-hashes -o requirements.txt

zip -r gcp.zip src main.py requirements.txt
