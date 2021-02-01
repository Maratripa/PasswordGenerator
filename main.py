import argparse
import passgen


parser = argparse.ArgumentParser()

# ARGUMENTS   
parser.add_argument('type', help="Enter the type of password you want")
parser.add_argument('--caps', help="Capitalize first letter of each word", action="store_true")
# END OF ARGUMENTS

args = parser.parse_args()

if args.type == 'xk':
    passgen.generate_password(args.caps, '-', 3)
