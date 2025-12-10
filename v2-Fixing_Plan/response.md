# **📘 Game Design Document (GDD) – Hero vs. Boss Arena (Updated Version)**

## **1. Overview**

This project is a beginner-friendly **2D action survival game** built with **Pygame**.
The player controls a hero who defeats incoming enemies to build up score. When the score reaches **30**, a powerful boss spawns and performs a sequence of four unique attacks. The player's goal is to **survive all four boss attacks** to win the game.

Playfield size: **800 × 800 px**

---

## **2. Core Gameplay Loop**

1. Move the hero around the arena.
2. Defeat enemies to earn score.
3. When score reaches **30**, the boss appears.
4. Survive **four distinct boss attacks**.
5. If the hero survives all attacks → **Victory**.
6. If the hero is hit by certain attacks or the boss itself → **Game Over**.

---

## **3. Game Mechanics**

### **3.1 Hero**

* Controlled with WASD or arrow keys.
* Can shoot projectiles/bullets.
* Defeats basic enemies and avoids boss attacks.
* **Collision with boss = instant death.**

---

### **3.2 Regular Enemies**

* Move toward the hero.
* Deal contact damage (or instant kill depending on design).
* Defeatable using hero’s bullets.
* Each enemy kill = **+1 score**.

---

## **4. Boss Encounter**

### **Boss Spawn Condition**

* The boss appears **exactly when the player reaches 30 points**.

### **Boss Win Condition**

* The player must **survive all four boss attacks** in sequence.
* After surviving all four attacks → **The boss is defeated**.

### **Boss Player Collision**

* If the hero touches the boss at any time:

  * **Instant game over.**

---

## **5. Boss Attacks (Detailed)**

The boss performs four unique attacks **in order**.
The player must survive each one without dying.

---

### **Attack 1 – Ground Danger**

**Description:**

* Dangerous squares/tiles appear from the **ground (bottom) and rise upward**.
* If the hero touches any of these tiles → **Instant death**.
* If the hero's bullets hit these squares:

  * The bullets **disappear**.
  * They **do not damage the boss**.

**Goal for the player:**
Survive without touching the rising danger.

---

### **Attack 2 – Thunder Nightmare**

**Description:**

* Vertical or horizontal **lightning lines** spawn at fixed positions.
* The attack happens **twice**.
* Each wave lasts **5 seconds**.
* Touching a lightning line = **Instant death**.

**Goal for the player:**
Memorize or react to the pattern and avoid all lightning strikes.

---

### **Attack 3 – Gauntlet Death**

**Description:**

* A dangerous projectile/object moves like a classic **DVD screensaver logo**, bouncing off the arena corners.
* It never leaves the screen.
* Its movement is continuous during the attack phase.

**Goal for the player:**
Avoid the bouncing object until the attack ends.

---

### **Attack 4 – Dodge Fight**

**Description:**

* Asteroids fall from the top of the screen in random positions.
* The hero must dodge falling obstacles.
* Each asteroid avoided earns points or contributes toward success.

**Win Requirement:**
Survive and earn **+20 score during this phase** to successfully clear Attack 4.

---

## **6. Win & Lose Conditions**

### ✔ **Victory**

The player wins when:

* Score reaches 30 → boss spawns.
* The hero **successfully survives all 4 boss attacks**, including gaining 20 points during Attack 4.

### ✘ **Failure (Game Over)**

Any of the following cause loss:

* Hero touches the boss.
* Hero touches a danger zone in Attack 1.
* Hero is hit by Thunder Nightmare lines.
* Hero is hit by the Gauntlet Death bouncing projectile.
* Hero collides with a falling asteroid.
* (Optional) Hero loses all health if a health system is included.

---

## **7. Suggested Code Structure (Optional but Helpful)**

| Class                                    | Purpose                                         |
| ---------------------------------------- | ----------------------------------------------- |
| `Hero`                                   | Movement, shooting, collision detection         |
| `Enemy`                                  | Basic enemy behavior, tracking player           |
| `Boss`                                   | Handles attack phases, state machine            |
| `AttackPhase` or multiple attack classes | Implement Attack 1–4 logic separately           |
| `Projectile`                             | Hero bullets                                    |
| `Asteroid`                               | Falling objects for Attack 4                    |
| `GameManager`                            | Tracks score, state transitions, victory/defeat |
| `UI`                                     | Score display, boss phase info                  |