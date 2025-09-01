import urllib.request
import os
import json
import sys

def python(args):
    with urllib.request.urlopen("https://food.freakybob.site/autumn/food.json") as url:
        data = json.load(url)
        print("Packages fetched! [autumn]")
    if (args.i in data["pypackages"]):
        print("Package found!")
        urllib.request.urlretrieve(
            "https://food.freakybob.site/packages/python/" + args.i + ".py", args.i + ".py"
        )
        print("Package downloaded!")
        print("The package will now run.")
        print("-----")
        with open(args.i + ".py") as file:
            exec(file.read())
    else:
        sys.exit("Package not found. Food will now exit.")
def txt(args):
    with urllib.request.urlopen("https://food.freakybob.site/autumn/food.json") as url:
        data = json.load(url)
        print("Packages fetched! [autumn]")
    if (args.i in data["txt"]):
        print("Package found!")
        urllib.request.urlretrieve(
            "https://food.freakybob.site/packages/txt/" + args.i + ".py", args.i + ".py"
        )
        print("Package downloaded!")
        print("The package will now run.")
        print("-----")
        with open(args.i + ".py") as file:
            exec(file.read())
    else:
        sys.exit("Package not found. Food will now exit.")