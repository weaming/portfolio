#!/usr/bin/env python
# coding: utf-8
"""
Author       : weaming
Created Time : 2018-05-01 02:20:27

File Name    : fetch_user.py
Description  :

"""
import json
from datetime import date, datetime
import github
from github import Github

with open("config.json") as f:
    cfg = json.load(f)

g = Github(cfg["token"])


def repo_data(repo):
    keys = [
        "id",
        "name",
        "full_name",
        "html_url",
        "ssh_url",
        "description",
        "forks_count",
        "stargazers_count",
        "watchers_count",
        "updated_at",
        "created_at",
        "pushed_at",
        "topics",
        "size",
        "fork",
        "private",
        "license",
        "homepage",
        "owner",
    ]
    data = {k: getattr(repo, k, None) for k in keys}
    # print(data)
    return data


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.strftime("%Y-%m-%d")
    if isinstance(obj, github.NamedUser.NamedUser):
        keys = ["login", "bio", "blog", "avatar_url", "company"]
        return {k: getattr(obj, k, None) for k in keys}
    raise TypeError("Type %s not serializable" % type(obj))


repos = list(map(repo_data, g.get_user().get_repos()))
repos = sorted(repos, key=lambda x: x["created_at"], reverse=True)

with open("repos.json", "w") as f:
    ss = json.dumps(repos, ensure_ascii=False, default=json_serial, indent=4)
    f.write(ss)

with open("projects.txt", "w") as f:
    f.write("\n".join(x["name"] for x in repos))
