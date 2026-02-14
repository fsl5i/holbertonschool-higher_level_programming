# 🚀 Everything is Object in Python

![Python Objects](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

> "In Python, **everything is an object**. Understanding this is key to mastering the language."

---

## 1️⃣ Introduction

Python is more than just a programming language; it's a world where **everything is an object** — integers, lists, strings, functions, even classes themselves.  
This project explores how Python handles objects, their identity, type, mutability, and how function arguments behave.  
Mastering these concepts ensures you write **efficient, bug-free, and professional code**.

---

## 2️⃣ `id` and `type`

Every object in Python has a **unique identity** (`id`) and a **type** (`type`).

```python
a = 10
print(f"id(a): {id(a)}")   # Memory address
print(f"type(a): {type(a)}") # <class 'int'>
