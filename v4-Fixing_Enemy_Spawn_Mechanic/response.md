# **📘 Game Design Document (GDD) – Hero vs. Boss Arena (Updated With Enemy Spawn Rule)**

## **1. Overview**

This project is a beginner-friendly **2D action survival game** made with **Pygame**.
The player defeats waves of enemies to build a score. When the score reaches **30**, the boss appears on the right side of the screen and unleashes four powerful attacks, all targeting the left side where the hero is restricted.

To win the game, the player must **survive all four boss attacks**.

Playfield: **800 × 800 px**.

---

## **2. Core Gameplay Loop**

1. Move the hero around the **left half** of the arena.
2. Defeat enemies → earn score (+1 per enemy).
3. Enemy phase always maintains **at least 6 enemies** on the screen.
4. At **30 score**, enemy spawning stops and the boss appears.
5. Survive four boss attacks.
6. Win the game, or die from a boss attack.

---

## **3. Arena & Movement Restrictions**

### **Player Position**

* The hero can move **only on the left side** of the screen (left half).
* A vertical barrier prevents the hero from entering the right side.

### **Boss Position**

* Boss remains fixed on the **right side**.
* Player cannot reach or touch the boss directly.
* All boss attacks occur **on the left side only**.

---

## **4. Enemies & Scoring System**

### **Enemy Behavior**

* All regular enemies move toward the hero.
* They spawn continuously until the boss appears.
* Killing an enemy gives:

  * **+1 score**
  * **Instant enemy replacement**

### **Minimum Enemy Count Rule**

**There must always be at least 6 enemies on screen:**

* If the hero kills 1 enemy → 1 new enemy spawns.
* If the hero kills 2 enemies quickly → 2 new enemies spawn.
* If the hero kills 6 enemies (wipes them all) → 6 spawn instantly to restore the minimum.

This keeps gameplay active and prevents the player from camping or stalling.

### **Boss Trigger**

* When total score reaches **30**, enemies stop spawning and the boss encounter begins.

---

## **5. Boss Encounter**

### **Boss Spawn Condition**

* Score reaches 30 → Boss appears on the right side.

### **Boss Behavior**

* Does not move toward the hero.
* Performs four attacks in sequence.
* If the hero touches the boss or crosses into the boss side → **instant death**.

### **Boss Victory Requirement**

* Player must survive all four attacks.
* In Attack 4: player must gain +20 survival score.

---

## **6. Boss Attack Phases**

### **Attack 1 – Ground Danger**

* Dangerous squares rise from the **bottom** of the left side.
* Hero collision = **instant death**.
* Bullets are destroyed on impact and **cannot reach the boss** during this attack.

### **Attack 2 – Thunder Nightmare**

* Lightning lines appear on the left side.
* Happens **twice**, each lasting **5 seconds**.
* Touching any lightning = **instant death**.

### **Attack 3 – Gauntlet Death**

* A large projectile bounces around the left side like a **DVD logo**.
* Never leaves the left half.
* Hitting the hero = **instant death**.

### **Attack 4 – Dodge Fight**

* Asteroids fall randomly from the top.
* Player gains survival score (e.g., time-based or per asteroid dodged).
* Must gain **+20 score** during this phase to clear the boss fight.

---

## **7. Win & Lose Conditions**

### ✔ **Victory**

Player wins if:

* Score reaches 30 (boss spawns).
* Hero survives all 4 boss attacks.
* During Attack 4, score increases by at least +20.
* Boss is defeated after Attack 4 ends.

### ✘ **Game Over**

* Player touches:

  * Boss
  * Boundary into boss area
  * Ground Danger squares
  * Thunder Nightmare lightning lines
  * Gauntlet Death bouncing projectile
  * Falling asteroids

---

## **8. Recommended Code Architecture**

| Class                      | Responsibility                                              |
| -------------------------- | ----------------------------------------------------------- |
| `Hero`                     | Movement, shooting, collision checks, left-side restriction |
| `Enemy`                    | Basic enemy movement & behavior                             |
| `EnemySpawner`             | Maintains 6+ enemies, controls respawn logic                |
| `Boss`                     | Manages attack order and transitions                        |
| `BossAttackPhase`          | Base class for the four attacks                             |
| `Attack1_GroundDanger`     | Rising danger zones                                         |
| `Attack2_ThunderNightmare` | Lightning strikes                                           |
| `Attack3_GauntletDeath`    | Bouncing projectile logic                                   |
| `Attack4_DodgeFight`       | Falling asteroid system                                     |
| `Projectile`               | Hero’s bullets                                              |
| `GameManager`              | Game state: enemy phase → boss → win/lose                   |
| `UI`                       | Score display, boss phase indicators                        |