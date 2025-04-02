# 🌟 SteganoX: Hidden Messages in Images 🕵️‍♂️

SteganoX is a powerful steganography tool that lets you **hide and extract secret messages** from images effortlessly. Whether you're a cybersecurity enthusiast, privacy advocate, or just having fun with hidden messages, **SteganoX has you covered!** 🔒✨

---
## 🚀 Features
✅ **Encode** secret messages into images
✅ **Decode** hidden messages from images
✅ **Command-line interface** for seamless automation
✅ **Interactive mode** for quick and easy usage
✅ **Lightweight & Efficient** – No unnecessary bloat!

---
## 📥 Installation

Clone the repository and install dependencies:
```sh
git clone https://github.com/AdityaBhatt3010/SteganoX.git
cd SteganoX
pip install -r requirements.txt
```

---
## 🎯 Usage

### 🔹 Command-Line Mode

#### 🔐 Encoding a Message:
```sh
python SteganoX.py -e <image_path> "<secret_message>" <output_image_path>
```
**Example:**
```sh
python SteganoX.py -e input.png "This is a secret!" output.png
```

#### 🔎 Decoding a Message:
```sh
python SteganoX.py -d <image_path>
```
**Example:**
```sh
python SteganoX.py -d output.png
```

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

---
## 📜 License
This project is licensed under the **GNU GPL V3 License**.

---
## 👨‍💻 Author
Developed with ❤️ by **Aditya Bhatt**

🔗 Connect with me on [LinkedIn](https://www.linkedin.com/) | 🛡️ Explore more on [GitHub](https://github.com/)
