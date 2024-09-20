#!/usr/bin/env python3

from QiSpaceSdkLib import SequrUtil
from binascii import hexlify
import argparse
import json

parser = argparse.ArgumentParser("demo_sequr_key_gen.py")
parser.add_argument(
  "--qispace_meta",
  required=True,
  dest="qispace_meta",
  help="path to qispace meta .json file, provided by Quantropi",
  type=str
)
parser.add_argument(
  "--key_id",
  required=True,
  dest="key_id",
  help="Key ID to query",
  type=str
)
args = parser.parse_args()

#########
# Initialize device
qispace_meta_content = json.load(open(args.qispace_meta))
sequr_util = SequrUtil(qispace_meta_content)
#########

#########
# Queries for key using key_id
_, raw_key = sequr_util.query_key(args.key_id)
key_hex_string = hexlify(raw_key, " ").decode('utf-8')
print("------------------------")
print(f"Key query successful")
if len(key_hex_string) > 10*3:
  print(
      f"Key: {key_hex_string[0:5*3]} ... {key_hex_string[len(key_hex_string)-5*3:len(key_hex_string)]}")
else:
  print(f"Key: {key_hex_string}")
print("------------------------")
#########
