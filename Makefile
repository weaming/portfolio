local: generate-md generate-html open

fetch:
	python fetch_user.py

generate-md:
	python generate_markdown.py

generate-html:
	md2png -m index.md -print -cssfile css/style.css -cssfile css/custom.css > index.html
	@rm index.png

open:
	open index.html


.PHONY: generate open fetch-generate local
