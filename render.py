#!/usr/bin/env python3

import subprocess
import yaml
from pathlib import Path
from dateutil import parser

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

                # Useful for sorting based on time
                self.epoch = parser.parse(self.data["publish-date"]).timestamp()
            except yaml.YAMLError as e:
                raise ValueError("   Error in parsing yaml:\n\n" + str(e))
            except KeyError as e:
                raise ValueError("   Title not listed for article")

    def thumbnail(self):
        # Ex.
        # <div class="thumbnail" onclick="location.href='/articles/first-article/index.html';">
        #     <h3>First Article</h3>
        #     <div class="info-holder">
        #         <span class="info-value"><b>Author:</b> Rushil Surti</span>
        #         <span class="info-value"><b>Date:</b> July 24, 2024</span>
        #         <span class="info-value"><b>Tags:</b>  <a href="/tags.html#meta"><span class="info-tag">meta</span></a>  <a href="/tags.html#website"><span class="info-tag">website</span></a> </span>
        #     </div>
        #     <p>The first (and hopefully not the last) article for this website, created mainly for testing purposes.</p>
        # </div>
        heading_tag = f"<h3>{self.name}</h3>"
        description_tag = f"<p>{self.data['description'].strip()}</p>"

        tags = " ".join(f'<a href="/tags.html#{tag}"><span class="info-tag">{tag}</span></a>' for tag in self.data["tags"])

        info_tag = '<div class="info-holder">\n'

        info_tag += f'        <span class="info-value"><b>Author:</b> Rushil</span>\n'
        info_tag += f'        <span class="info-value"><b>Date:</b> {self.data["publish-date"]}</span>\n'
        info_tag += f'        <span class="info-value"><b>Tags:</b> {tags}</span>\n'

        info_tag += "    </div>"

        thumbnail_tag = f"""<div class="thumbnail" onclick="location.href='{"/" + str(self.result)}';">\n    {heading_tag}\n    {info_tag}\n    {description_tag}\n</div>"""

        return thumbnail_tag

    def render(self, log):
        # Tweaking the options to get the correct arrangement for Katex to actually render
        # the correct stuff while also using the \( \) and \[ \] characters for latex in 
        # markdown instead of the not very nice $ $ and $$ $$ delimiters actually took
        # really long (like O(2^n) time :sob:).

        # Yeah unfortunately even though we're using Katex to do the actual rendering,
        # if you use the katex flag instead of the mathjax flag, it won't work :(
        # Thank you pandoc, very cool
        cmd = ["pandoc", "-f", "markdown-smart+tex_math_single_backslash", "--standalone", "--toc", "--mathjax", "--template=templates/article.html", "--metadata-file=" + str(self.metadata), "-o", str(self.result), str(self.article)]
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
articles = []

with open("log.txt", "w") as log:
    for d in articles_dir.iterdir():
        if not d.is_dir():
            continue

        print(f"-> Retrieving article at '{d}'")

        try:
            article = Article(d)
            articles.append(article)
        except ValueError as e:
            print(e)
            print("   Skipping..")
            continue

        print(f"   Rendering article '{article.name}' to '{article.result}'")

        log.write(f"Rendering article at '{d}'\n")
        article.render(log)

        print()

    print("Rendering index.html")

    articles.sort(key = lambda a: a.epoch, reverse=True)

    index_body = ""
    for article in articles:
        index_body += article.thumbnail()
        index_body += "\n"

    with open("templates/index.html") as ind:
        index_template = ind.read()

    with open("index.html", "w") as ind:
        ind.write(index_template.format(body=index_body))

    print("Finished rendering index.html")

    print()

    print("Rendering tags.html")

    tagged_articles = {}

    for article in articles:
        for tag in article.data["tags"]:
            if tag in tagged_articles:
                tagged_articles[tag].append(article)
            else:
                tagged_articles[tag] = [article]

    tags_body = ""

    for tag in tagged_articles:
        tags_body += f'<h2 id="{tag}">{tag}</h2>\n'

        for article in tagged_articles[tag]:
            tags_body += article.thumbnail()
            tags_body += "\n"

    with open("templates/tags.html") as tags:
        tags_template = tags.read()

    with open("tags.html", "w") as tags:
        tags.write(tags_template.format(body=tags_body))

    print("Finished rendering tags.html")
    
    print()
