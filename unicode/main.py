import argparse
import configparser
import signal

from domains import similar_domains, check_domains
from utils.similarity import load_file

config = configparser.ConfigParser()
config.read('config')

DESCRIPTION = config['APPLICATION_INFO']['DESCRIPTION']


def banner():
    print("""

.########..##.....##..######...######..
.##.....##.##.....##.##....##.##....##.
.##.....##.##.....##.##.......##.......
.##.....##.##.....##.##.......##...####
.##.....##.##.....##.##.......##....##.
.##.....##.##.....##.##....##.##....##.
.########...#######...######...######..

Domain Unicode Confusables Generator
""")


def main():
    banner()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('domain', action='store',
                        help='check similar domains to this one')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-c', '--check', action='store_true',
                        help='check if this domain is alive')
    parser.add_argument('-w', '--whois', action='store_true',
                        help='check whois')
    parser.add_argument('-m', '--max', action='store',
                        default=10000, type=int,
                        help='maximum number of similar domains')
    parser.add_argument('-t', '--threshold', action='store',
                        default=75, type=int, choices=[75, 80, 85, 90, 95, 99], metavar="75,80,85,90,95,99",
                        help='Similarity threshold')
    parser.add_argument('-o', '--output', dest='output', help='Output file')

    args = parser.parse_args()

    confusables = load_file(args.threshold)

    domains = set(similar_domains(args.domain, confusables, args.max))
    write = False
    if len(domains) > 0:
        print('Similar domains to {}'.format(args.domain))
        if (args.output):
            f = open(args.output, 'w')
            write = True
        for d in domains:
            print(d)
            if write:
                f.write(d + "\n")
        if (args.check):
            print('Checking if domains are up')
            check_domains(domains, t=5, verbose=args.verbose, whois=args.whois)

        if write:
            f.close()
        print('Total similar domains to {}: {}'.format(args.domain, len(domains)))


if __name__ == 'main':
    main()
