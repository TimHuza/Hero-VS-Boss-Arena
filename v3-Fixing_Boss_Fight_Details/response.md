# **📘 Game Design Document (GDD) – Hero vs. Boss Arena (Final Updated Version)**

## **1. Overview**

This project is a beginner-friendly **2D action survival game** created using **Pygame**.
The player controls a hero who defeats enemies to gain score. When the score reaches **30**, a boss spawns on the right side of the screen and begins a sequence of four powerful attacks.

The player must survive all four boss attacks to win the game.

Playfield size: **800 × 800 px**.

---

## **2. Core Gameplay Loop**

1. Move the hero around the arena.
2. Defeat enemies to earn score (+1 per enemy).
3. When score reaches **30**, the boss appears.
4. The boss stays on the **right side** of the arena.
5. The hero is restricted to the **left side**.
6. All four boss attacks occur **only on the left side** where the hero stands.
7. Survive all boss attacks → Victory.
8. Colliding with boss or an attack → Game Over.

---

## **3. Player and Arena Restrictions**

### **Player Positioning**

* The player occupies the **left side** of the screen.
* A **vertical boundary** prevents the hero from entering the right side.
* This prevents the player from reaching or damaging the boss directly (no cheating).

### **Boss Positioning**

* The boss stays on the **right side** of the arena.
* It does not move to the left side.
* Only the boss’s **attacks** reach the hero.

---

## **4. Game Mechanics**

### **Hero**

* Moves freely within the **left half** of the arena.
* Can shoot projectiles (during enemy phase and boss fight).
* During Attack 1, bullets are blocked by ground spikes.
* Colliding with boss (if touching boundary) = **instant death**.

---

### **Enemies**

* Move toward the hero.
* Die on bullet hit.
* Each kill = **+1 score**.
* When score reaches **30**, enemies stop spawning and the boss appears.

---

## **5. Boss Encounter**

### **Boss Spawn Condition**

* Boss appears at **exactly 30 score**.

### **Boss Location**

* Fixed on the **right side** of the arena.
* Does not move toward the player.

### **Boss Attacks**

All four attacks spawn **only in the left half**, where the hero stands.

### **Boss Win Condition**

* The player must **survive all four attacks**.
* During Attack 4, the player must earn **+20 score** by surviving asteroid waves.

### **Player-Boss Collision**

* If the hero crosses the boundary into the boss area (or touches the boss hitbox):
  **Game Over.**

---

## **6. Boss Attack Phases (Detailed)**

The boss performs four attacks **in order**.
Player must survive each without dying.

---

### **Attack 1 – Ground Danger**

**Area:** Left side only.

**Description:**

* Dangerous red squares rise from the **bottom** of the left side.
* If hero touches any squares → **Instant death**.
* If bullets hit a square:

  * Bullets **disappear**.
  * Bullets **cannot reach the boss** during this attack.

**Objective:**
Avoid all ground danger regions.

---

### **Attack 2 – Thunder Nightmare**

**Area:** Left side only.

**Description:**

* Lightning lines appear (vertical or horizontal).
* Attack triggers **two times**.
* Each wave lasts **5 seconds**.
* Touching lightning = **Instant death**.

**Objective:**
Avoid lightning zones for the duration.

---

### **Attack 3 – Gauntlet Death**

**Area:** Left side only.

**Description:**

* A single large projectile moves like a **DVD logo**, bouncing off walls.
* It never leaves the left side.
* Movement speed may increase over time.

**Objective:**
Dodge the bouncing object until the attack ends.

---

### **Attack 4 – Dodge Fight**

**Area:** Left side only.

**Description:**

* Asteroids fall from the top in random lanes.
* The hero gains **+1 point per asteroid survived** or per time interval.
* Player must earn **+20 score during this phase** to clear the boss.

**Objective:**
Survive and accumulate enough points to win the fight.

---

## **7. Win & Lose Conditions**

### ✔ **Victory**

Player wins when:

* Score reaches 30 → Boss spawns.
* All four boss attacks are survived.
* During Attack 4, score increases by +20.
* After Attack 4 ends → **Boss defeated** → Victory screen.

### ✘ **Game Over**

* Hero touches the boss.
* Hero crosses the boundary into boss area.
* Hero gets hit by:

  * Ground Danger tiles
  * Thunder Nightmare lightning
  * Gauntlet Death bouncing projectile
  * Falling asteroids

---

## **8. Suggested Code Structure**

| Class                             | Responsibility                                                |
| --------------------------------- | ------------------------------------------------------------- |
| `Hero`                            | Movement, shooting, collision detection, boundary restriction |
| `Enemy`                           | Movement, scoring on death                                    |
| `Boss`                            | Handles attack phases, position, animations                   |
| `BossAttackPhase` or 4 subclasses | Logic for each attack                                         |
| `Projectile`                      | Hero bullets                                                  |
| `Asteroid`                        | Attack 4 falling hazards                                      |
| `GameManager`                     | States: normal → boss → victory/defeat                        |
| `UI`                              | Score, boss phase indicator                                   |