# 🌟 SteganoX: Hidden Messages in Images 🕵️‍♂️

SteganoX is a powerful steganography tool that lets you **hide and extract secret messages** from images effortlessly. Whether you're a cybersecurity enthusiast, privacy advocate, or just having fun with hidden messages, **SteganoX has you covered!** 🔒✨

---
## 🚀 Features
✅ **Encode** secret messages into images. <br/>
✅ **Decode** hidden messages from images. <br/>
✅ **Command-line interface** for seamless automation. <br/>
✅ **Interactive mode** for quick and easy usage. <br/>
✅ **Lightweight & Efficient** – No unnecessary bloat! <br/>

---## 📥 Installation

### 🔹 Install via PyPI (Recommended)
SteganoX is now available on PyPI! Install it using:
```sh
pip install SteganoX-Hidden-Messages-in-Images
```

### 🔹 Manual Installation
Clone the repository and install dependencies:
```sh
git clone https://github.com/AdityaBhatt3010/SteganoX-Hidden-Messages-in-Images.git
cd SteganoX-Hidden-Messages-in-Images
python setup.py install
```
or simply run
```sh
git clone https://github.com/AdityaBhatt3010/SteganoX-Hidden-Messages-in-Images.git
cd SteganoX-Hidden-Messages-in-Images
pip install -r requirements.txt
```

---
## 🎯 Usage

### 🔹 Command-Line Mode

#### 🔎 Help Menu:
```sh
python SteganoX.py -h
```
![Image](https://github.com/user-attachments/assets/82eab841-d965-4925-b153-299d13306015) <br/>

#### 🔐 Encoding a Message:
```sh
python SteganoX.py -e <image_path> "<secret_message>" <output_image_path>
```
**Example:**
```sh
python SteganoX.py -e input.png "This is a secret!" output.png
```
![Image](https://github.com/user-attachments/assets/1c2975ea-465d-462c-920f-41052bb5cdae) <br/>

#### 🔎 Decoding a Message:
```sh
python SteganoX.py -d <image_path>
```
**Example:**
```sh
python SteganoX.py -d output.png
```
![Image](https://github.com/user-attachments/assets/2a846be8-3ad4-4f9a-a81e-9a8eb2f07a77) <br/>

---
### 🖥️ Minimal Interactive Mode
If you prefer a **guided experience**, run the interactive mode:
```sh
python SteganoX_Minimal.py
```
You'll be prompted to enter an image path, your message (if encoding), and an output file.

---
## 📌 Dependencies
- **Python 3.x** 🐍
- **Pillow** 🖼️ (Image processing)
- **pyfiglet** 🎭 (Cool ASCII banners)
- **termcolor** 🎨 (Stylish CLI output)

Install all dependencies with:
```sh
pip install -r requirements.txt
```

### 🎯 Sample Images:

#### 🔐 Imput Image:
![Image](https://github.com/user-attachments/assets/30ea5908-91c9-41c7-9012-05c8a0e7d975) <br/>

#### 🔎 Output Image:
![Image](https://github.com/user-attachments/assets/358c6782-6808-4f07-ade7-a45908b538c2) <br/>

Image Credit: [needpix](https://www.needpix.com/photo/29659/copyright-free-pd-cc0-free-music-license-symbol-free-vector-graphics-free-pictures-free-photos) <br/>
[Clker-Free-Vector-Images - pixabay.com, Copyright-Free PD CC0 Free Photo Available](https://www.needpix.com/photo/29659/copyright-free-pd-cc0-free-music-license-symbol)

---
## 👨‍💻 Author
Developed with ❤️ by **Aditya Bhatt**
