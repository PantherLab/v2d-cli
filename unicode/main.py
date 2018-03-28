import argparse
import configparser
import signal

from .domains import similar_domains, check_domains
from .utils.similarity import load_file

config = configparser.ConfigParser()
config.read('config')

DESCRIPTION = config['APPLICATION_INFO']['DESCRIPTION']


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('domain', action='store',
                        help='check similar domains to this one')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-w', '--whois', action='store_true',
                        help='check whois')
    parser.add_argument('-m', '--max', action='store',
                        default=10000, type=int,
                        help='maximum number of similar domains')

    args = parser.parse_args()

    confusables = load_file()
    print(args.max)
    domains = similar_domains(args.domain, confusables, args.max)
    if len(domains) > 0:
        print('Similar domains to {}'.format(args.domain))
        for d in domains:
            print(d)
        print('Checking if domains are up')
        check_domains(domains, t=5, verbose=args.verbose, whois=args.whois)


if __name__ == 'main':
    main()
