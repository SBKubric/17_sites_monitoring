import pythonwhois
import requests
import argparse
from datetime import datetime
from calendar import monthrange
import tldextract
import logging


def parse_args():
    parser = argparse.ArgumentParser(description='SMUS (Sites Monitoring Utility Script)\n'
                                                 'The script helps you to control your sites.'
                                                 'It can return their if their response is 200 and check their'
                                                 'domain expiration date.')
    parser.add_argument('source', help='The path to the url list file')
    parser.add_argument('-nr', '--no_redirects', action='store_true', help='Forbid redirection from sites')
    parser.add_argument('-o', '--output', default='logfile', help='The name of file with results')
    args = parser.parse_args()
    return args


def get_logger(logfile_path):
    logging.basicConfig(format='%(message)s', filename='{}.log'.format(logfile_path), level=logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    logger = logging.getLogger()
    logger.addHandler(ch)
    return logger


def load_urls4check(path):
    file = open(path)
    while True:
        url = file.readline()
        if not url:
            break
        if '\n' in url:
            url = url[:-1]
        yield url


def is_server_respond_with_200(url, forbid_redirects=False):
    response = requests.get(url, allow_redirects=not forbid_redirects)
    if response.status_code == 200:
        return True
    return False


def get_domain_expiration_date(domain_name):
    status = pythonwhois.get_whois(domain_name)
    return status['expiration_date'][0]


def get_major_domain(url):
    tld_info = tldextract.extract(url)
    domain = '{}.{}'.format(tld_info.domain, tld_info.suffix)
    return domain


def is_paid_for_next_month(url):
    domain = get_major_domain(url)
    dt_exp = get_domain_expiration_date(domain)
    now_date = datetime.now()
    if now_date.month == 12:
        due_date = datetime(now_date.year+1, 1, 31, 23, 0, 0)
    else:
        first_day, last_day = monthrange(now_date.year, now_date.month+1)
        due_date = datetime(now_date.year, now_date.month+1, last_day, 23, 0, 0)
    if dt_exp < due_date:
        return False
    return True


if __name__ == '__main__':
    args = parse_args()
    logger = get_logger(args.output)
    for url in load_urls4check(args.source):
        logger.info('{}\n  response_code_200: {}\n  is_paid_for_next_month: {}\n\n'.format(
            url, is_server_respond_with_200(url, args.no_redirects), is_paid_for_next_month(url)
        ))

