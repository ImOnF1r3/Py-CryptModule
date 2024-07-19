# PyCryptExecutor

This repository contains code for studying various types of encryption and decryption executable in Python. The provided scripts are intended for educational and experimental purposes only.

## Purpose

The purpose of this repository is to provide a framework for experimenting with and studying different encryption and decryption techniques. The scripts are designed to allow for the addition of multiple encryption layers.

## Usage

To use the scripts in this repository, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/pycryptexecutor.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd pycryptexecutor
    ```
3. Run the provided Python scripts:
    ```bash
    python inj-cry.py
    python out-cry.py
    ```

You can add additional encryption layers by modifying the scripts accordingly.

## How It Works

### inj-cry.py

This script is responsible for injecting or encrypting data. Here is a high-level overview of how it works:

1. **Input Data**: The script takes an input data string or file.
2. **Encryption**: It applies an encryption algorithm to the input data. The specific algorithm can be customized or replaced.
3. **Output**: The encrypted data is saved to a file or printed out.

### out-cry.py

This script is responsible for extracting or decrypting data. Here is a high-level overview of how it works:

1. **Input Data**: The script takes the encrypted data string or file.
2. **Decryption**: It applies a decryption algorithm to the encrypted data. This should correspond to the encryption algorithm used in `inj-cry.py`.
3. **Output**: The decrypted data is saved to a file or printed out.

### Adding Layers of Encryption

To add additional layers of encryption:

1. Open `inj-cry.py` and add your new encryption function.
2. Modify the script to apply the new encryption function in addition to the existing one.
3. Open `out-cry.py` and add the corresponding decryption function.
4. Modify the script to apply the new decryption function in the reverse order of the encryption functions.

## Disclaimer

This repository is for educational purposes only. The authors take no responsibility for any misuse of the provided code. Use it at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
