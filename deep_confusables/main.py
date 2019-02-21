import argparse
import sys
import signal

from .domains import similar_domains, check_domains
from .utils.similarity import load_file
from .utils.printing import print_diff

DESCRIPTION = ('deep-confusables-cli: Visual Unicode attacks with Deep Learning - '
               'System based on the similarity of the characters unicode by '
               'means of Deep Learning. This provides a greater number of '
               'variations and a possible update over time')


def banner():
    print("""
 __   ___  ___  __      __   __        ___       __        __        ___  __
|  \ |__  |__  |__) __ /  ` /  \ |\ | |__  |  | /__`  /\  |__) |    |__  /__`
|__/ |___ |___ |       \__, \__/ | \| |    \__/ .__/ /~~\ |__) |___ |___ .__/

    Visual Unicode attacks with Deep Learning
    Version 1.1.1
    Created by:
      - José Ignacio Escribano Pablos (@jiep)
      - Miguel Hernández Boza (@Miguel000)
      - Alfonso Muñoz Muñoz (@mindcrypt)
""")


def main():
    banner()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-d', '--domain', action='store',
                        help='check similar domains to this one')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-c', '--check', action='store_true',
                        help='check if this domain is alive')
    parser.add_argument('-w', '--whois', action='store_true',
                        help='check whois')
    parser.add_argument('-vt', '--virustotal', action='store_true',
                        help='check Virus Total')
    parser.add_argument('-m', '--max', action='store',
                        default=10000, type=int,
                        help='maximum number of similar domains')
    parser.add_argument('-t', '--threshold', action='store',
                        default=75,
                        type=int,
                        choices=[75, 80, 85, 90, 95, 99],
                        metavar="75,80,85,90,95,99",
                        help='Similarity threshold')
    parser.add_argument('-key', '--api-key', dest='api',
                        help='VirusTotal API Key')
    parser.add_argument('-o', '--output', dest='output', help='Output file')
    parser.add_argument('-i', '--input', dest='fileinput',
                        help='List of targets. One input per line.')

    args = parser.parse_args()

    if (not args.domain and not args.fileinput):
        print("Need one type of input, -i --input or -d --domain")
        print(parser.print_help())
        sys.exit(-1)

    if(args.virustotal and not args.api):
        print('Please, enter a VirusTotal API Key with -api or --api-key')
        sys.exit(-1)

    confusables = load_file(args.threshold)

    idomains = list()
    write = False
    if args.fileinput:
        try:
            f = open(args.fileinput, 'r')
            for line in f:
                idomains.append(line.strip())
        except Exception:
            print("--------------")
            print("Wrong input file.\n\n")
            print("--------------")
            print(parser.print_help())
            sys.exit(-1)
    else:
        idomains.append(args.domain)
    if (args.output):
        f = open(args.output, 'w')
        write = True
    for dom in idomains:
        domains = set(similar_domains(dom, confusables, args.max))
        if len(domains) > 0:
            print('Similar domains to {}'.format(dom))
            domains.difference_update(set(dom))
            for d in domains:
                print_diff(dom, d)
                if write:
                    f.write(d + "\n")
            if (args.check):
                print('Checking if domains are up')
                check_domains(domains, t=5,
                              API_KEY=args.api,
                              verbose=args.verbose,
                              whois=args.whois,
                              vt=args.virustotal)
            print('Total similar domains to {}: {}'.format(dom, len(domains)))
    if write:
        f.close()


if __name__ == 'main':
    main()
