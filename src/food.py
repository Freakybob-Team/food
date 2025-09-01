import argparse
import eat

parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python')
parser.add_argument('--i')
#parser.add_argument('--t') - coming soon once again
args = parser.parse_args()

eat.python(args)