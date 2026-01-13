# Hero VS Boss Arena

A **Python + Pygame** arcade-style game where you fight waves of enemies and survive multiple boss attack phases in an arena.

---

## Requirements

Make sure you have the following installed:

* **Python 3.9+** (Python 3 recommended)
* **Pygame** library

---

## Installation

1. **Clone or download** this repository:

```bash
git clone <repository-url>
cd Hero-VS-Boss-Arena
```

Or download the ZIP and extract it.

2. **Install Python**

Go to [Python.org](https://www.python.org/downloads/) and download the latest version of Python.

3. **Check if Python is installed**

```bash
python --version
```

If you see this

```bash
Python 3.x.x
```

then you have Python installed and you're good to go!

4. **Install Pygame**

```bash
pip install pygame
```

---

## Project Structure

`game-architecture` branch
```text
├── assets/
│   └── imgs/
│       ├── background.png
│       ├── shopbkrd.png
│       ├── coin.png
│       ├── startbtn.png
│       ├── shopbtn.png
│       ├── quitbtn.png
│       ├── leftbutton.png
│       ├── rightbutton.png
│       ├── backbtn.png
│       ├── returnbtn.png
│       └── win.png
├── attacks/
│   ├── attack_phase.py
│   ├── attack1.py
│   ├── attack2.py
│   ├── attack3.py
│   └── attack4.py
├── config/
│   └── settings.py
├── enemies/
│   └── enemies_spawner.py
├── enteties/
│   ├── enemy.py
│   ├── hero.py
│   └── projectile.py
├── game/
│   ├── boss.py
│   ├── boundary_wall.py
│   └── game_manager.py
├── ui/
│   └── ui.py
├── main.py
├── README.md
```

`main` branch
```text
├── assets/
│   └── imgs/
│       ├── background.png
│       ├── shopbkrd.png
│       ├── coin.png
│       ├── startbtn.png
│       ├── shopbtn.png
│       ├── quitbtn.png
│       ├── leftbutton.png
│       ├── rightbutton.png
│       ├── backbtn.png
│       ├── returnbtn.png
│       └── win.png
├── main.py
└── README.md
```

⚠️ **Important:** Do not move or rename the `assets/imgs` and `data/imgs` folders. The game loads images using relative paths.

---

## How to Run the Game

From the project root directory, run:

```bash
python main.py
```

The game window should open automatically.

---

## Controls

### Player Movement

* **W A S D** – Move the player

### Shooting

* **Arrow Keys** – Shoot projectiles

  * ⬅ Left
  * ➡ Right
  * ⬆ Up
  * ⬇ Down

### Menu Navigation

* **Mouse Click** – Navigate menus, shop, and buttons

---

## Gameplay Overview

* Defeat enemies to increase your score
* Collect coins for tracking progress
* Once your score reaches **15**, the **Boss Arena** is triggered
* Survive **4 boss attack phases**:

  1. Ground danger walls
  2. Thunder line attacks
  3. Moving gauntlet
  4. Falling dodge blocks

Survive all phases to **win the game** 🏆

---

## Common Issues

### Images not loading

* Make sure you are running `main.py` from the **project root folder**
* Verify the `assets/imgs` and `data/imgs` folders exist and contain all image files

### Pygame not found

Run:

```bash
pip install pygame
```

---

## Notes

* This game uses **Pygame** for rendering and input
* The game runs at **60 FPS**
* Designed for desktop (Windows / macOS / Linux)

---

## Author
Created as a learning project using Python and Pygame.


Enjoy the game! 🎮
