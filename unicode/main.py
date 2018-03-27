import argparse
import configparser

from .domains import similar_domain
from .utils.similarity import load_file

config = configparser.ConfigParser()
config.read('config')

DESCRIPTION = config['APPLICATION_INFO']['DESCRIPTION']


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('domain', action='store',
                        help='check similar domains to this one')
    args = parser.parse_args()

    confusables = load_file()

    print('Similar domain to {}: {}'.format(args.domain,
          similar_domain(args.domain, confusables)))


if __name__ == 'main':
    main()
