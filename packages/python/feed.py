import urllib.request
import os
print("Feed; a Food updater. Now downloading/updating food...")
urllib.request.urlretrieve(
    "https://food.freakybob.site/src/food.py", "food.py"
)
urllib.request.urlretrieve(
    "https://food.freakybob.site/src/eat.py", "eat.py"
)
print("Downloaded Food and Eat! Thanks for using Feed.")