export:
	poetry export --without-hashes -o requirements.txt

gcp:
	zip -r gcp.zip src main.py requirements.txt