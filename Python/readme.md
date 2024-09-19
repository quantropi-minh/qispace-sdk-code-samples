# QiSpace Python Demos

## Sequr

### Setup
  1. Place your Qeep `.whl` library file under `lib` folder. If you do not have one, please contact Quantropi.
  1. Install demo dependencies and libraries: `./install.sh`

### Running the demo

  1. **Generate key demo:**
      - Execute the `demo_sequr_key_gen.py` with the bellow aruments:
      ```
      usage: demo_sequr_key_gen.py [-h] [--url URL] [--token TOKEN] [--key_size KEY_SIZE]

      options:
        -h, --help           show this help message and exit
        --url URL            URL for QiSpace Enterprise API. ex: https://enterprise.staging.qispace.info/kds/api/v1
        --token TOKEN        Device token generated from QiSpace Enterprise
        --key_size KEY_SIZE  Key size to generate
      ```
      - You might get an output as bellow:
      ```
      --- Generated QK with key_id 0d0ed476-6af7-49b3-a3c1-49de2ac98798
        ------ key hex: 71445a2843...0ca81bc043
      ```
  1. **Query key demo:**
      - Execute the `demo_sequr_key_query.py` with the bellow aruments:
      ```
      usage: demo_sequr_key_gen.py [-h] [--url URL] [--token TOKEN] [--key_id KEY_ID]

      options:
        -h, --help       show this help message and exit
        --url URL        URL for QiSpace Enterprise API. ex: https://enterprise.staging.qispace.info/kds/api/v1
        --token TOKEN    Device token generated from QiSpace Enterprise
        --key_id KEY_ID  Key ID to query
      ```
      - You might get an output as bellow:
      ```
      --- Queried for QK with key_id 0d0ed476-6af7-49b3-a3c1-49de2ac98798
        ------ key hex: 71445a2843...0ca81bc043
      ```
  1. **Compare results**

      Note that for the same `key_id`, we were able to retrieve the same key content.

### Implementation Note
A convenient `SequrUtil` class has been implemented in `QiSpaceSdkLib.py`. This class implements common encryption and decryption logic that can be used in any end-application.
