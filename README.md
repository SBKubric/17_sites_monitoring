# Sites Monitoring Utility

## Description

The script helps you to track your sites. It takes a path to the file with links to sources and returns if its response
code is 200 and if domain is paid for next month.

##Installation

The script is written with Python3.

Install the packages from requirements.txt using pip:

```
pip install -r requirements.txt
```

**IMPORTANT**: best practice is to use virtualenv. See here: [Link](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

##File format

The line format in file should be like this: `schema:url\n`.

For example:

**FILE:**

```
http://www.google.com
http://www.yandex.com
http://www.rambler.com
http://www.azaza.ru
```

##Example

**INPUT:**

```
python3 check_sites_health.py urls -o result
```

**OUTPUT:**

It will be located at `./result.log`

```
http://www.google.com
  response_code_200: True
  is_paid_for_next_month: True


http://www.yandex.com
  response_code_200: True
  is_paid_for_next_month: True


http://www.rambler.com
  response_code_200: True
  is_paid_for_next_month: True


http://www.azaza.ru
  response_code_200: True
  is_paid_for_next_month: True

```

Use `-h` or `--help` argument for HELP.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
