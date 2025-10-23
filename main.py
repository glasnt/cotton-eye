from urllib.parse import urlparse

import github
from flask import Flask, render_template, request

app = Flask(__name__)

g = github.Github()


def get_context(github_url):
    """From a GitHub URL, return the elements required to use it in git"""
    url = urlparse(github_url)

    path_segments = list(filter(None, url.path.split("/")))
    repo_slug = "/".join(path_segments[0:2])

    repo = g.get_repo(repo_slug)

    if len(path_segments) > 3:
        branch = "/".join(path_segments[3:4])
        directory = "/".join(path_segments[4:])
    else:
        branch = repo.default_branch
        directory = " "

    context = {"repo": repo_slug, "branch": branch, "dir": directory}
    return context


@app.get("/")
def home():
    context = {}

    if "referer" in request.headers:
        if "https://github.com" in request.headers["referer"]:
            context = get_context(request.headers["referer"])

    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
