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
keyId, qk_device_1 = device_1_sequr_util.key_gen(1024)
print("Device 1 generated qk of length: ", len(qk_device_1))
#########


#########
# Device 2 queries for QK using keyId given to Device 1
_, qk_device_2 = device_2_sequr_util.query_key(keyId)
print("Device 2 received qk of length: ", len(qk_device_2))
#########

print(f"Key contents are the same? {qk_device_1 == qk_device_2}")
