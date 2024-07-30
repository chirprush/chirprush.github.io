#!/usr/bin/env python3

import subprocess
import yaml
from pathlib import Path

# TODO: Allow for specifying templates within the yaml file
# (doesn't take long at all to implement; this is just a note)
class Article:
    def __init__(self, base):
        self.base = base
        self.article = base / "article.md"
        self.metadata = base / "meta.yaml"
        self.result = base / "index.html"

        if not self.article.exists():
            raise ValueError(f"   Could not find article markdown file at '{self.article}'")

        if not self.metadata.exists():
            raise ValueError(f"   Could not find yaml metadata file at '{self.metadata}'")

        with open(str(self.metadata.absolute())) as stream:
            try:
                self.data = yaml.safe_load(stream)

                self.name = self.data["title"]
            except yaml.YAMLError as e:
                raise ValueError("   Error in parsing yaml:\n\n" + str(e))
            except KeyError as e:
                raise ValueError("   Title not listed for article")


    def render(self, log):
        # Tweaking the options to get the correct arrangement for Katex to actually render
        # the correct stuff while also using the \( \) and \[ \] characters for latex in 
        # markdown instead of the not very nice $ $ and $$ $$ delimiters actually took
        # really long (like O(2^n) time :sob:).

        # Yeah unfortunately even though we're using Katex to do the actual rendering,
        # if you use the katex flag instead of the mathjax flag, it won't work :(
        # Thank you pandoc, very cool
        cmd = ["pandoc", "-f", "markdown-smart+tex_math_single_backslash", "--standalone", "--toc", "--mathjax", "--template=templates/template.html", "--metadata-file=" + str(self.metadata), "-o", str(self.result), str(self.article)]
        print()
        print("   " + " ".join(cmd[:3]))
        print("   " + " ".join(cmd[3:]))

        log.write(f"Command: {' '.join(cmd)}\n")

        result = subprocess.run(cmd, text=True, capture_output=True)

        log.write(f"Return code: {result.returncode}\n")
        log.write(f"Stdout:\n")
        log.write(result.stdout + "\n")

        log.write(f"Stderr:\n")
        log.write(result.stderr + "\n")

        if result.returncode != 0:
            print(f"   Failed with return code {result.returncode}, see log for more details")
        else:
            print(f"   Succeeded")

# Main pipeline:
# - Run pandoc for the main pages -> index.html, articles.html, about.html (to be decided I guess), resume.html
#   - Overall I'm kinda iffy on whether or not I really want to render the main pages since I might want to hardcode stuff for those
#     on one hand it's more extendable and there's repetition if I ever want to change something (which honestly could happen a lot),
#     but if I want to customize stuff with like say a p5 canvas or something I have to hardcode that in which is like awkward.
#     I guess articles.html should be generated though.
# - Run pandoc on each of the articles and stuff
# - Throughout the proper variables should be given for each thing (variables for like the selection bar and stuff)

# Eventually I'll have to deal with fixing the css and making things responsive
# as well, but I'll work on that once I actually get content and can see how
# things look I suppose

articles_dir = Path("./articles")
articles = [Article(d) for d in articles_dir.iterdir() if d.is_dir()]

with open("log.txt", "w") as log:
    for d in articles_dir.iterdir():
        if not d.is_dir():
            continue

        print(f"-> Retrieving article at '{d}'")

        try:
            article = Article(d)
        except ValueError as e:
            print(e)
            print("   Skipping..")
            continue

        print(f"   Rendering article '{article.name}' to '{article.result}'")

        log.write(f"Rendering article at '{d}'\n")
        article.render(log)

        print()
