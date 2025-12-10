# **📘 Game Design Document (GDD) – Hero vs. Boss Arena (Updated Movement Rules)**

## **1. Overview**

This is a beginner-friendly 2D action game built using **Pygame**.
The player defeats waves of enemies to gain score. When the player reaches **30 points**, the boss appears and initiates four unique attack phases.

The player must survive all boss attacks to win.

Arena size: **800 × 800 px**

---

## **2. Game Phases**

The game has **two distinct phases**, each with different movement rules:

### **Phase 1 – Enemy Phase**

* Hero can **move freely anywhere** in the full 800×800 arena.
* A minimum of **6 enemies** must always be on the screen.
* Each kill = **+1 score**, and a new enemy instantly respawns.
* At **30 score**, enemies stop spawning → Boss Phase starts.

### **Phase 2 – Boss Phase**

* The boss appears on the **right side** of the arena.
* The hero becomes restricted to the **left side only** by a boundary wall.
* All boss attacks occur exclusively on the **left side**.
* Hero must survive four sequential boss attacks to win.

---

## **3. Movement Rules Summary**

| Phase       | Hero Movement                                    | Boss Movement                  |
| ----------- | ------------------------------------------------ | ------------------------------ |
| Enemy Phase | Full arena (left + right), unrestricted movement | No boss yet                    |
| Boss Phase  | Left side **only**, cannot cross into boss area  | Boss stays fixed on right side |

---

## **4. Enemy Mechanics**

### **Spawn Rules**

* Always maintain **at least 6 enemies**.
* When the hero kills an enemy:

  * Score increases by **+1**.
  * A new enemy spawns immediately.
* If the hero kills multiple enemies quickly:

  * Equal number of enemies respawn.

### **Behavior**

* Enemies move toward the hero.
* Colliding with an enemy damages or kills the hero (depends on your health system).
* Enemies stop spawning once the score reaches **30**.

---

## **5. Boss Encounter**

### **Boss Spawn Condition**

* Score reaches **30** → Enemy phase ends → Boss appears.

### **Boss Positioning**

* Boss stays fixed on the **right half** of the arena.
* The hero cannot enter the right side due to a collider/barrier.
* Hero touching the boss = **instant death**.

### **Boss Victory Condition**

* Survive all **four attacks**.
* During Attack 4, gain an additional **+20 survival score**.

---

## **6. Boss Attack Phases (Left-Side Only)**

All attacks occur **only on the left side**, where the hero is limited.

---

### **Attack 1 – Ground Danger**

* Dangerous squares rise from the bottom of the left side.
* Hero collision = **instant death**.
* Hero bullets disappear if they hit these squares (no damage to boss).

---

### **Attack 2 – Thunder Nightmare**

* Lightning lines appear on the left side.
* The attack happens **twice**, each lasting **5 seconds**.
* Touching lightning = **instant death**.

---

### **Attack 3 – Gauntlet Death**

* A large bouncing projectile moves like a **DVD screensaver logo**.
* It stays on the left side only.
* Hero collision = **instant death**.

---

### **Attack 4 – Dodge Fight**

* Asteroids fall from the top of the left side.
* The hero must dodge falling hazards.
* The hero earns “survival score” and must gain **+20** during this phase.

---

## **7. Win & Lose Conditions**

### ✔ **Victory**

* Score reaches 30 → Boss appears.
* Hero survives all 4 boss attacks.
* Hero earns +20 score during Attack 4.
* Boss is defeated → Player wins.

### ✘ **Game Over**

* Hero touches the boss.
* Hero crosses the boundary into boss area.
* Hero is hit by:

  * Ground Danger tiles
  * Thunder Nightmare lightning
  * Gauntlet Death projectile
  * Falling asteroids

---

## **8. Recommended Code Architecture**

| Class                      | Purpose                                             |
| -------------------------- | --------------------------------------------------- |
| `Hero`                     | Movement, shooting, collision detection             |
| `Enemy`                    | Behavior, tracking player                           |
| `EnemySpawner`             | Keeps minimum 6 enemies alive                       |
| `Boss`                     | Manages attack sequence and states                  |
| `AttackPhase`              | Base class for 4 boss attacks                       |
| `Attack1_GroundDanger`     | Rising hazard logic                                 |
| `Attack2_ThunderNightmare` | Lightning patterns                                  |
| `Attack3_GauntletDeath`    | Bouncing projectile                                 |
| `Attack4_DodgeFight`       | Falling asteroids                                   |
| `Projectile`               | Hero bullets                                        |
| `GameManager`              | Controls switching between Enemy Phase → Boss Phase |
| `UI`                       | Score, messages, boss phase indicators              |