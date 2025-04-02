# SteganoX: Hidden Messages in Images

A simple Python script for encoding and decoding secret messages in images using **Least Significant Bit (LSB) steganography**.

## Features
- Hide text messages inside images without altering visual appearance.
- Extract hidden messages from encoded images.
- Works with any RGB image format.
- Lossless encoding using PNG format.

## Installation
Ensure you have Python installed, then install the required library:
```bash
pip install pillow
```

or simply run
```bash
pip install -r requirements.txt
```

## Clone the Repository
```bash
git clone https://github.com/AdityaBhatt3010/SteganoX.git
cd SteganoX
```

## Usage
### Encoding a Message into an Image
```bash
python steganography.py
```
1. Enter 'e' when prompted.
2. Provide the image path, the secret message, and the output image path.

### Decoding a Message from an Image
```bash
python steganography.py
```
1. Enter 'd' when prompted.
2. Provide the image path containing the hidden message.

## Example
### Encoding
```bash
Enter 'e' to encode or 'd' to decode: e
Enter image path: input.png
Enter the message to hide: Hello, World!
Enter output image path: output.png
```
### Decoding
```bash
Enter 'e' to encode or 'd' to decode: d
Enter image path to decode: output.png
Decoded message: Hello, World!
```

## License
This project is licensed under the MIT License.
