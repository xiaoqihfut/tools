# import re

# log = "id:12 f_id:123,o_if:43"

# def check_log():

import re
import logging

string = "id:12 f_id:123,o_if:43"
pattern = r'\bid\b.*?\d+'

def parse_digit(strs):
    return re.findall(r"\d+", strs)

def parse_key(key, string):
    matches = re.findall(pattern, string)
    if matches:
        for match in matches:
            logging.warning(int(parse_digit(match)[0]))
    else:
        logging.warning("not match  {}".format(key))
        return None

parse_key(pattern, string)