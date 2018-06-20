.PHONY: local fetch generate-md generate-html open

local: generate-md generate-html open

fetch:
	python fetch_user.py

generate-md:
	python generate_markdown.py

generate-html:
	md2png -m Portfolio.md -print -cssfile css/style.css -cssfile css/custom.css > index.html
	@rm Portfolio.png

open:
	open index.html

