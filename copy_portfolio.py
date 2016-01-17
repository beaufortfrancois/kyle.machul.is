import os
import json
import shutil

HEADER = """title: %s
slug: %s
template: project

"""

# Build portfolio links

BLOG_PF_DIR = os.path.join("/home/qdot/code/git-projects/kyle.machul.is", "content", "portfolio")
PORTFOLIO_DIR = "/share/qdot-projects/"
DESC_DIR = os.path.join(BLOG_PF_DIR, "desc")
INFO_DIR = os.path.join(BLOG_PF_DIR, "info")
IMG_DIR = os.path.join(BLOG_PF_DIR, "img")
projects = filter(os.path.isdir,
                  [os.path.join(PORTFOLIO_DIR, d)
                   for d in os.listdir(PORTFOLIO_DIR)])
os.chdir(PORTFOLIO_DIR)
for p in os.listdir(PORTFOLIO_DIR):
    if not os.path.isdir(os.path.join(PORTFOLIO_DIR, p)):
        continue
    ignore_file = os.path.join(p, "noportfolio")
    if os.path.isfile(ignore_file):
        print "* CANCELLED Ignoring %s" % (ignore_file)
        continue
    info_file = os.path.join(p, p + ".json")
    if not os.path.isfile(info_file):
        print "* TODO NO INFO FILE %s" % (info_file)
        continue
    desc_file = os.path.join(p, p + ".md")
    if not os.path.isfile(desc_file):
        print "* TODO NO DESC FILE %s" % (desc_file)
        continue
    img_small_file = os.path.join(p, "web", p + "-small.jpg")
    if not os.path.isfile(img_small_file):
        print "* TODO NO SMALL IMAGE FILE %s" % (img_small_file)
        continue
    img_file = os.path.join(p, "web", p + ".jpg")
    if not os.path.isfile(img_file):
        print "* TODO NO REGULAR IMAGE FILE %s" % (img_file)
        continue

    # Attach header to all description files
    with open(info_file) as info:
        try:
            post_info = json.load(info)
        except:
            print "* TODO INVALID JSON %s" % (p)
            continue
    print "* DONE %s" % (p)
    shutil.copy(info_file, INFO_DIR)
    img_path = os.path.join(IMG_DIR, post_info["slug"])
    try:
        os.makedirs(img_path, 0755)
    except:
        pass
    shutil.copy(img_small_file, img_path)
    shutil.copy(img_file, img_path)
    with open(desc_file) as desc:
        new_header = HEADER % (post_info["title"], post_info["slug"])
        fn = os.path.basename(desc_file)
        with open(os.path.join(DESC_DIR, fn), "w+") as new_desc:
            new_desc.write(new_header)
            new_desc.write(desc.read())
