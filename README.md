# 🔐 Python Secure Login System

A Python-based login and registration system built with **Tkinter**, designed to demonstrate secure user authentication and credential handling.

## ✦ Features

- 🔑 User registration and login
- 🛡️ Password hashing instead of storing plaintext passwords
- 📁 Local text-file storage for account data
- 👤 Username-based account identification
- 🔒 Password verification using stored hashes
- 🖥️ Tkinter graphical user interface
- ✨ Modernised login and registration interface
- ⚠️ Invalid-login and registration error handling
- 🚫 Prevents duplicate usernames
- 💾 Persistent account storage between program launches

## 🔐 Password Security

Passwords are **not stored directly**. When a user creates an account, their password is processed through a hashing algorithm before being stored.

During login, the entered password is hashed and compared against the stored hash rather than comparing or storing the original password.

```text
User enters password
        ↓
   Password hashing
        ↓
   Hash stored locally
        ↓
      Login
        ↓
Entered password → hash → compare with stored hash
```

This means the account file does not contain users' original passwords.

## 🧩 Technologies

- 🐍 Python
- 🖼️ Tkinter
- 🔐 Password hashing
- 📄 Local file storage

## 🎯 Purpose

This project was created to practise Python GUI development, file handling, authentication logic, and basic cybersecurity principles while building a functional desktop login system.
