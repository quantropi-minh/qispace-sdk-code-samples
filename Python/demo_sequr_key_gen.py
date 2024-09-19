#!/usr/bin/env python3

from QiSpaceSdkLib import SequrUtil
from binascii import hexlify
import argparse

parser = argparse.ArgumentParser("demo_sequr_key_gen.py")
parser.add_argument(
  "--url", 
  dest="url",
  help="URL for QiSpace Enterprise API. ex: https://enterprise.staging.qispace.info/kds/api/v1",
  type=str
)
parser.add_argument(
  "--token", 
  dest="token",
  help="Device token generated from QiSpace Enterprise",
  type=str
)
parser.add_argument(
  "--key_size", 
  dest="key_size",
  help="Key size to generate",
  default=1024,
  type=int
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
# Generates new QK
key_id, key_content = sequr_util.key_gen(1024)
key_hex_string = hexlify(key_content).decode('utf-8')
print(f"--- Generated QK with key_id {key_id}")
print(f"------ key hex: { key_hex_string[0:10] }...{ key_hex_string[len(key_hex_string)-10:len(key_hex_string)] }")
#########

print("")
