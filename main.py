import argparse
import passgen


parser = argparse.ArgumentParser()

# ARGUMENTS   
parser.add_argument('type', help="Enter the type of password you want")
parser.add_argument('--caps', help="Capitalize first letter of each word", action="store_true")
parser.add_argument('--sep', help="Separator of your liking")
parser.add_argument('--words', help='Number of words for the xk password')
# END OF ARGUMENTS

args = parser.parse_args()

if args.type == 'xk':
    options = ['-', 3]
    
    if args.sep:
        options[0] = args.sep
    
    if args.words:
        options[1] = args.words
    
    passgen.generate_password(args.caps, options[0], int(options[1]))
