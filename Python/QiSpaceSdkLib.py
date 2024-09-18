import requests
import base64
import binascii
from qeep import QeepQSC

class SequrUtil:

  def __init__(self, url, device_token, pub_key = None):
    self.url = url
    self.device_token = device_token
    
    response = requests.post(
      f"{self.url}/sub_key",
      headers={"Authorization": f"Bearer {self.device_token}"},
      json={"pub_key": pub_key}
    ).json()

    self.qeepQSC = QeepQSC(response["key_index"])
    self.qeepQSC.qk_load(
      binascii.unhexlify(response["sub_key"].encode())
    )

  def key_gen(self, key_size = 1024):
    response = requests.post(
      f"{self.url}/qk",
      headers={"Authorization": f"Bearer {self.device_token}"},
      json={"key_length": key_size}
    ).json()

    key_id = response["id"]
    decryptedQk = self.__qeepDecrypt__(response["payload"], response["iv"])

    return (key_id, decryptedQk)

  def query_key(self, key_id):
    response = requests.get(
      f"{self.url}/qk/{key_id}",
      headers={"Authorization": f"Bearer {self.device_token}"},
    ).json()

    decryptedQk = self.__qeepDecrypt__(response["payload"], response["iv"])

    return (key_id, decryptedQk)

  def __qeepDecrypt__(self, base64_cipher, iv):
    self.qeepQSC.set_iv(
      base64.b64decode(iv.encode('utf-8'))
    )

    cipher = base64.b64decode(base64_cipher)
    result, decryptedMessage = self.qeepQSC.decrypt(cipher)
    if result != 1:
      raise Exception(f"failed to decrypt message: {result}")

    return decryptedMessage
