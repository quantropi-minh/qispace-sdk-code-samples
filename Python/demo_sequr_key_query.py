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
    "--key_id",
    dest="key_id",
    help="Key ID to query",
    type=str
)
args = parser.parse_args()


#########
# Initialize device
device_2_sequr_util = SequrUtil({
  "url": args.url,
  "device_token": args.token,
})
#########

print("")

#########
# Device 2 queries for QK using key_id given to Device 1
_, qk_device_2 = device_2_sequr_util.query_key(args.key_id)
print(f"--- Device 2 queries for QK with key_id {args.key_id}, received key ")
print(f"------ key hex: { hexlify(qk_device_2).decode('utf-8')[0:10] }...{ hexlify(qk_device_2).decode('utf-8')[len(qk_device_2)-10:len(qk_device_2)] }")
#########

print("")
