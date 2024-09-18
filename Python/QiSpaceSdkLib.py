import requests
import base64
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

    self.qeep = QeepQSC()
    self.qeep.qk_load(response.sub_key)

    return self

  def sequr_key_gen(self, key_size):
    response = requests.post(
      f"{self.url}/qk",
      headers={"Authorization": f"Bearer {self.device_token}"},
      json={"key_length": key_size}
    ).json()

    key_id = response.id
    decryptedQk = self.__qeepDecrypt__(response.payload, response.iv)

    return (key_id, decryptedQk)

  def sequr_query_key(self, key_id):
    response = requests.get(
      f"{self.url}/qk/{key_id}",
      headers={"Authorization": f"Bearer {self.device_token}"},
    ).json()

    decryptedQk = self.__qeepDecrypt__(response.payload, response.iv)

    return (key_id, decryptedQk)

  def __qeepDecrypt__(self, base64_cipher, iv):
    self.qeep.set_iv(iv)
    cipher = base64.b64decode(base64_cipher)
    plaintext = self.qeep.decrypt(cipher)
    return plaintext
