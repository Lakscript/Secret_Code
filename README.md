# 🔐 Secret Code Encoder/Decoder

This Python project allows users to **encode** and **decode secret messages** using a simple scrambling algorithm. It offers an interactive command-line interface where users can choose to create secret codes or decode them.

## 🚀 Features

- Encode a message with a random obfuscation pattern
- Decode a previously encoded message back to readable text
- Looping menu system so users can repeat actions as needed
- Simple and beginner-friendly code structure

## 💡 How It Works

- **Encoding logic**:
  - For 2-letter words: reverse the letters.
  - For longer words:
    - Move the first letter to the end.
    - Add 3 random letters at the end.
    - Add 3 random letters at the beginning.

- **Decoding logic**:
  - For 2-letter words: reverse them back.
  - For longer words:
    - Remove the first 3 and last 3 random letters.
    - Move the last letter (original first letter) to the front.



