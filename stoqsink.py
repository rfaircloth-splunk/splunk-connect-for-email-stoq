#!/usr/bin/python3
import sys
import json
import email
import hashlib
import traceback
import logging
import uuid
from datetime import datetime


OUTPUT_DIR = '/tmp/'

def create_filename(mime):
    return str(uuid.uuid4()).replace(' ', '_') + '.txt'

def on_error(stdin):
    with open(OUTPUT_DIR + '/var/log/stoqsink.err', 'a') as f:
        traceback.print_exc(file=f)

def main(stdin):
    msg = email.message_from_string(stdin)
    # out = {}
    # out['date'] = msg['Date']
    # out['id'] = msg['Message-Id']
    # out['from'] = msg['from']
    # out['body'] = msg.get_payload()
    # out['raw'] = str(msg)

    filename = create_filename(msg)
    newlines = str(msg).replace('\\n', '\n')

    with open(OUTPUT_DIR + filename, 'w') as f:
        f.write(str(msg).replace('\\n', '\n'))


if __name__ == '__main__':
    stdin = sys.stdin.read()
    try:
        main(stdin)
    except Exception as e:
        on_error(stdin)