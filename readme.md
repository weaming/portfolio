## How to use

1. **config**: fill github token in `config.json`
1. **fetch**: `python3 fetch_user_data.py`
1. modify `projects-show.txt` to add project you want to show, one name per line
1. **generate**: `make generate-md`
1. modify `index.md` if you want
1. `go get github.com/weaming/md2png`
1. `make generate-html`
1. **publish**: commit & push
1. setup github pages
