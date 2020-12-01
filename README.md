- https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#issues

```bash
poetry export --without-hashes -o requirements.txt
pip install -r requirements.txt --target ./package
zip -r function.zip src package
serverless offline
```
