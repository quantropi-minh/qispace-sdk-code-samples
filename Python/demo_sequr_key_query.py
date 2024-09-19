#!/usr/bin/env python3

from QiSpaceSdkLib import SequrUtil
from binascii import hexlify
import argparse

parser = argparse.ArgumentParser("demo_sequr_key_gen.py")
parser.add_argument(
  "--url",
  required=True,
  dest="url",
  help="URL for QiSpace Enterprise API. ex: https://enterprise.staging.qispace.info/kds/api/v1",
  type=str
)
parser.add_argument(
  "--token",
  required=True,
  dest="token",
  help="Device token generated from QiSpace Enterprise",
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
sequr_util = SequrUtil({
  "url": args.url,
  "device_token": args.token,
})
#########

print("")

#########
# Device 2 queries for QK using key_id given to Device 1
_, key_content = sequr_util.query_key(args.key_id)
key_hex_string = hexlify(key_content).decode('utf-8')
print(f"--- Queried QK with key_id {args.key_id}")
print(f"------ key hex: { key_hex_string[0:10] }...{ key_hex_string[len(key_hex_string)-10:len(key_hex_string)] }")
#########

print("")
