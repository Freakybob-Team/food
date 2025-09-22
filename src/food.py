import argparse
import eat
import cook
helpstring = """
here's an example of downloading a python file: python3 food.py --i greg
formatting: [your python name, ex: python3 or py] food.py --i [packagename]"""
parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python', epilog=helpstring)
parser.add_argument('--i')
parser.add_argument('--t')
args = parser.parse_args()
if args.i:
    print("using python downloads")
    eat.python(args)
if args.t:
    print("using temp downloads; python")
    cook.cookpy(args)