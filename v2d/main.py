import argparse
import sys
import signal
from tld import get_tld

from .domains import similar_domains, check_domains
from .utils.similarity import load_file
from .utils.printing import print_diff

DESCRIPTION = ('v2d-cli: Visual Unicode attacks with Deep Learning - '
               'System based on the similarity of the characters unicode by '
               'means of Deep Learning. This provides a greater number of '
               'variations and a possible update over time')

def generate_flipper_domains(dom):

    url = get_tld(dom, as_object=True, fix_protocol=True)
    domain = url.domain
    new_urls_without_letter = []
    n = 0
    m = len(domain)

    if m == 1:
        new_urls_without_letter.append(domain)
    elif m == 2:
        new_domain = domain[1] + domain[0]
        new_urls_without_letter.append(new_domain)

    else:

        while n < m and m > 2:

            if n == 0 :
                new_domain = domain[n + 1] + domain[n] + domain[n + 2:m]

            elif n == 1:
                new_domain = domain[0] + domain[n + 1] + domain[n] + domain[n + 2:m]

            elif 1 < n < m - 1:
                new_domain = domain[0:n] + domain[n + 1] + domain[n] + domain[n + 2:m]

            n = n + 1
            new_urls_without_letter.append(new_domain+"."+url.tld)
    new_urls_list = list(set(new_urls_without_letter))
    return new_urls_list

def generate_substitution_domains(dom):
    url = get_tld(dom, as_object=True, fix_protocol=True)
    domain = url.domain

    new_urls_with_double_letter = []
    n = 0
    m = len(domain)
    while n < m:
        new_domain = domain[0:n] + domain[n] + domain[n] + domain[n+1:m]
        new_urls_with_double_letter.append(new_domain+"."+url.tld)
        new_domain = domain[0:n] + domain[n+1:m]
        new_urls_with_double_letter.append(new_domain+"."+url.tld)
        n = n + 1
    new_urls_list = list(set(new_urls_with_double_letter))
    return new_urls_list

def banner():
    print("""

oooooo     oooo   .oooo.   oooooooooo.
 `888.     .8'  .dP""Y88b  `888'   `Y8b
  `888.   .8'         ]8P'  888      888
   `888. .8'        .d8P'   888      888
    `888.8'       .dP'      888      888
     `888'      .oP     .o  888     d88'
      `8'       8888888888 o888bood8P'


    Visual Unicode attacks with Deep Learning
    Version 1.1.0
    Authors: José Ignacio Escribano
    Miguel Hernández (MiguelHzBz)
    Alfonso Muñoz (@mindcrypt)


""")


def main():
    banner()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('domain', action='store',
                        help='check similar domains to this one')

    parser.add_argument('-F','--flipper', dest='flipper',default=False, nargs='?', const=True, type=bool, help='Execute flipping attack')
    parser.add_argument('-H','--homoglyph', dest='homoglyph',default=False, nargs='?',const=True, type=bool,help="Execute homoglyph attack")
    parser.add_argument('-S','--substitution', dest='substitution',default=False, nargs='?', const=True, type=bool, help="Execute substitution attack")


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

    if not (args.homoglyph or args.substitution or args.flipper):
        print("Need one type of attack, -F -Hg or -S")
        print()
        sys.exit(-1)
    idomains = list()
    #domains = list()
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

    confusables = load_file(args.threshold)

    for dom in idomains:

        if args.homoglyph:
            print('Option selected: Homoglyph attack with a {}% threshold.'.format(args.threshold))
            print('Domain target: ' + dom)
            domains = set(similar_domains(dom, confusables, args.max))
        if args.flipper:
            print('Option selected: Flipping attack')
            print('Domain target: ' + dom)
            domains = set(generate_flipper_domains(dom))
        if args.substitution:
            print('Option selected: Substitution attack')
            print('Domain target: ' + dom)
            domains = set(generate_substitution_domains(dom))
        if len(domains) > 0:
            print('Similar domains to {}'.format(dom))
            if len(domains) > 0:
                domains.difference_update(set(dom))
            for d in domains:
                if not args.substitution:
                    print_diff(dom, d)
                else:
                    print (d)
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
