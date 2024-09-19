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
key_id, qk_device_1 = sequr_util.key_gen(1024)
print(f"--- Generated QK with key_id {key_id}")
print(f"------ key hex: { hexlify(qk_device_1).decode('utf-8')[0:10] }...{ hexlify(qk_device_1).decode('utf-8')[len(qk_device_1)-10:len(qk_device_1)] }")
#########

print("")
