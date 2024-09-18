from dotenv import dotenv_values
from QiSpaceSdkLib import SequrUtil


config = dotenv_values(".env")

#########
# Initialize two different devices
device_1_sequr_util = SequrUtil(
  config["QISPACE_ENTERPRISE_URL"],
  config["DEVICE_1_TOKEN"],
)
device_2_sequr_util = SequrUtil(
  config["QISPACE_ENTERPRISE_URL"],
  config["DEVICE_2_TOKEN"],
)
#########


#########
# Device 1 generates new QK
key_id, qk_device_1 = device_1_sequr_util.key_gen(1024)
print(f"--- Device 1 generates QK with key_id {key_id} of length {len(qk_device_1)}")
#########


######### `key_id` can be safely shared with device 2 over the network or any manner in plain text
print(f"--- Device 1 shares key_id {key_id} in plaintext with Device 2")
#########


#########
# Device 2 queries for QK using key_id given to Device 1
_, qk_device_2 = device_2_sequr_util.query_key(key_id)
print(f"--- Device 2 queries for QK with key_id {key_id}, received key of length {len(qk_device_1)}")
#########

print(f"Key contents are the same? {qk_device_1 == qk_device_2}")
