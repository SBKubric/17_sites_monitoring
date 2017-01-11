import pythonwhois
import requests
import argparse
from datetime import datetime, timedelta
import tldextract
import logging


def parse_args():
    parser = argparse.ArgumentParser(description='')


def load_urls4check(path):
    file = open(path)
    while True:
        url = file.readline()
        if not url:
            break
        yield url


def is_server_respond_with_200(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    return False


def get_domain_expiration_date(domain_name):
    status = pythonwhois.get_whois(domain_name)
    return status['expiration_date'][0]


def get_major_domain(url):
    tld_info = tldextract.extract('www.rambler.ru')
    domain = '{}.{}'.format(tld_info.domain, tld_info.suffix)
    return domain


def is_paid_for_next_month(url):
    domain = get_major_domain(url)
    exp_date = get_domain_expiration_date(domain)
    now_date = datetime.now()
    if exp_date - now_date <= timedelta(months=1):
        return False
    return True


if __name__ == '__main__':
    args = parse_args()
    logger = logging.getLogger()
    for url in load_urls4check(args.path):
        logger.info('{}\n  response_code_200: {}\n  is_paid_for_next_month: {}\n\n'.format(
            url, is_server_respond_with_200(url), is_paid_for_next_month(url)
        ))

