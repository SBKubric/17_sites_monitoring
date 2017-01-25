import pythonwhois
import requests
import argparse
from urllib.parse import urlparse
from datetime import datetime
from calendar import monthrange
import tldextract


def parse_args():
    parser = argparse.ArgumentParser(description='SMUS (Sites Monitoring Utility Script)\n'
                                                 'The script helps you to control your sites.'
                                                 'It can return their if their response is 200 and check their'
                                                 'domain expiration date.')
    parser.add_argument('source', help='The path to the url list file')
    parser.add_argument('-nr', '--no_redirects', action='store_true', help='Forbid redirection from sites')
    args = parser.parse_args()
    return args


def load_urls4check(path):
    with open(path) as urls_source:
        while True:
            url_string = urls_source.readline()
            if not url_string:
                break
            if '\n' in url_string:
                url_string = url_string[:-1]
            url_parts = urlparse(url_string)
            yield '{}://{}'.format(url_parts.scheme, url_parts.netloc)


def is_server_respond_with_200(url, forbid_redirects=False):
    response = requests.get(url, allow_redirects=not forbid_redirects)
    return response.status_code == 200


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
    return dt_exp >= due_date


if __name__ == '__main__':
    args = parse_args()
    for url in load_urls4check(args.source):
        print('{}\n  response_code_200: {}\n  is_paid_for_next_month: {}\n\n'.format(
            url, is_server_respond_with_200(url, args.no_redirects), is_paid_for_next_month(url)
        ))

