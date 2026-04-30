# 🧙‍♂️ Python OOP RPG System

A small object-oriented programming project built in Python to simulate a simple RPG-style system.  
This project is focused on practicing core OOP concepts rather than building a full game.

---

## 🎯 What this project does

This system includes:
- A player with health, stats, and inventory
- Items that can be used (Potions and Weapons)
- An abstract item system that forces all items to implement `use()`
- A health system using `@property` and setters
- Item counting using class variables

---

## 🧠 OOP Concepts Used

- Classes and Objects
- Inheritance
- Abstract Base Classes (ABC)
- Polymorphism (`use()` method)
- Encapsulation (`_health`)
- Properties and setters (`@property`)
- Class variables (`Item.count`)
- Magic methods (`__str__`)

---

## 📦 How it works

### Player
- Has a name
- Has health (controlled with property)
- Has an inventory of items

### Items
All items inherit from a base `Item` class and must implement:

```python
use(player)
