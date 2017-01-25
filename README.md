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

The urls in file schould be separated by `\n`.

For example:

**FILE:**

```
http://www.google.com
http://www.rambler.com
http://www.twitter.com
https://www.atlassian.com/git/tutorials/git-hooks
https://www.youtube.com/?gl=RU&hl=ru
```

##Example

**INPUT:**

```
python3 check_sites_health.py urls
```

**OUTPUT:**

```
http://www.google.com
  response_code_200: True
  is_paid_for_next_month: True


http://www.rambler.com
  response_code_200: True
  is_paid_for_next_month: True


http://www.twitter.com
  response_code_200: True
  is_paid_for_next_month: True


https://www.atlassian.com
  response_code_200: True
  is_paid_for_next_month: True


https://www.youtube.com
  response_code_200: True
  is_paid_for_next_month: True

```

Use `-h` or `--help` argument for HELP.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
