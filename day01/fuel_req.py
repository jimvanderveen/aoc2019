#!/usr/bin/env python3

# Read from given filename or stdin.
# See https://unix.stackexchange.com/a/47543

import argparse, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()
    if args.filename:
        # print('opening file ' + args.filename)
        infile = open(args.filename, 'r')
    else:
        infile = sys.stdin

    fuel_total = 0
    for cnt, line in enumerate(infile):
        mass = int(line)
        fuel = Fuel_Needed(mass)
        # print("mass {} requires {} fuel units".format(mass, fuel))
        fuel_total += fuel

    print("Total fuel required is {} fuel units".format(fuel_total))
    
    # If a file was opened, close it now.
    if infile is not sys.stdin:
        infile.close()


def Fuel_Needed(mass):
    # To find the fuel required for a module, take its mass, divide by
    # three, round down, and subtract 2. But what if this results in a
    # negative number?
    # Aha! A recusion problem... The tyranny of the rocket equation!
    fuel_mass = int(mass/3)-2
    if fuel_mass > 0:
        return fuel_mass + Fuel_Needed(fuel_mass)
    else:
        return 0


if __name__ == '__main__':
   main()
