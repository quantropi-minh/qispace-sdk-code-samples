from QiSpaceSdkLib import SequrUtil

sequr = SequrUtil(
  "https://enterprise.staging.qispace.info/kds/api/v1",
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOjY5MTgsImRldmljZV9pZCI6NjkxOCwidG9rZW5faWQiOjExNDYxLCJpYXQiOjE3MjY2NzMxMzZ9.mJa_W0ImHepc_Z3paio4TzF-CFWzRB0TiMGsNZnZksQ"
)

keyId, key = sequr.key_gen()
_, queried_key = sequr.query_key(keyId)

print(key == queried_key)
