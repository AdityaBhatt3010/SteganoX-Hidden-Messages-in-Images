from setuptools import setup, find_packages

# Read the contents of README.md for a detailed package description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SteganoX-Hidden-Messages-in-Images",
    version="1.0.0",
    author="Aditya Bhatt",
    author_email="info.adityabhatt3010@gmail.com",
    description="A powerful steganography tool for hiding and extracting messages in images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdityaBhatt3010/SteganoX-Hidden-Messages-in-Images",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
        "Topic :: Multimedia :: Graphics"
    ],
    python_requires=">=3.6",
    install_requires=[
        "pillow",
        "pyfiglet",
        "termcolor"
    ],
    entry_points={
        "console_scripts": [
            "steganox=SteganoX:main",
        ]
    },
)
