from setuptools import setup, find_packages

setup(
    name="nostr_ln_bot",
    version="1.0.0-beta",
    description="Nostr bot for Lightning Network channel recommendations",
    author="22388o",
    url="https://github.com/AreaLayer/nostr-ln-bot-channel",
    packages=find_packages(),
    install_requires=[
        "python-nostr",
        "lnd-grpc"
    ],
    entry_points={
        "console_scripts": [
            "nostr_ln_bot=nostr_ln_bot:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
