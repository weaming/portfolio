#!/usr/bin/env python
# coding: utf-8

import json

with open('repos.json') as f:
    repos = json.load(f)

with open('projects-show.txt') as f:
    included = list(l.strip() for l in f if l.strip()[0] not in '# \n')
    print(included)

with open('config.json') as f:
    cfg = json.load(f)

repos_map = {x['name'].lower(): x for x in repos if x['owner']['login'] == cfg['username']}
repos_filtered = [repos_map[x.lower()] for x in included if x.lower() in repos_map]

md_repo_template = u"""## {name} [source]({html_url})

- Star: {stargazers_count} Watch: {watchers_count} Fork: {forks_count}
- Created: {created_at}
- Updated: {pushed_at}

{description}
"""

md_template = u"""# Portfolio

These are my projects on github.

{}
"""

repo_text_list = [md_repo_template.format(**repo) for repo in sorted(
    repos_filtered,
    key=lambda x: sum(x[k] for k in [
        'stargazers_count',
        'watchers_count',
        'forks_count',
    ]),
    reverse=True)]

with open('Portfolio.md', 'wb') as f:
    f.write(md_template.format('\n'.join(repo_text_list)).encode('utf8'))
