# QiSpace Python Demos

## Sequr
The `demo_sequr.py` file showcases a usecase of Sequr. 

### Setup
  1. Place your Qeep `.whl` library file under `lib` folder. If you do not have one, please contact Quantropi.
  1. Install demo dependencies and libraries: `./install.sh`
  1. Duplicate `.env_sample` file to `.env` and fill in content
  1. Run the demo: `python demo_sequr.py`

### Demo premise
- This demo simulates two separate devices sharing a secure **Quantum Key (QK)** with each other through **QiSpace Enterprise**.
- Each device is initialized using a unique **device token** retrieved from QiSpace Enterprise.
- **Device 1** generates a QK through Qispace Enterprise, receiving the raw QK and a `key_id`.
- `key_id` can be safely shared with **Device 2** 
- **Device 2** uses plaintext `key_id` to retrieve QK from QiSpace Enterprise
- QK from both sides are compared to confirm matching value

### Implementation Note
A convenient `SequrUtil` class has been implemented in `QiSpaceSdkLib.py`. This class implements common encryption and decryption logic that can be used in any end-application.