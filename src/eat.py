import urllib.request
import os
import json
import sys
import difflib

def python(args):
    with urllib.request.urlopen("https://food.freakybob.site/autumn/food.json") as url:
        data = json.load(url)
        print("Packages fetched! [autumn, food.json]")
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
        suggestions = difflib.get_close_matches(args.i, data['pypackages'], n=3, cutoff=0.6)
        if suggestions:
            print(f"Package not found. Did you mean: {', '.join(suggestions)}?")
        else:
            print("Package not found. No similar packages detected.")