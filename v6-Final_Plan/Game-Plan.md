# **📘 Game Design Document (GDD) – Hero vs. Boss Arena (Updated)**

## **1. Overview**

This is a beginner-friendly 2D action game made with **Pygame**.
The player defeats waves of enemies to earn score. Once the player reaches **30 score**, a boss appears on the right side and executes a sequence of four unique attacks on the left side.
The player must survive all attacks to win.

Arena size: **800 × 800 px**

---

## **2. Core Gameplay Loop**

1. **Move the hero around the arena** during the enemy phase (full movement allowed).
2. **Defeat enemies to earn score** (+1 per kill).
3. Maintain **at least 6 enemies on screen**; killed enemies instantly respawn.
4. When score reaches **30**, enemies stop spawning and **the boss appears**.
5. Movement becomes restricted to the **left side only** during the boss phase.
6. **Survive four distinct boss attacks**, each with unique hazards.
7. During Attack 4, gain **+20 bonus score** by surviving falling asteroids.
8. If the hero survives all attacks → **Victory**.
9. If the hero is hit by certain attacks or the boss itself → **Game Over**.

---

## **3. Game Phases**

### **Enemy Phase**

* Hero can move **everywhere** in the arena.
* At least **6 enemies** remain on the field at all times.
* Each kill = **+1 score** + instant enemy respawn.
* Reaching **30 score** triggers the Boss Phase.

### **Boss Phase**

* Hero becomes locked to the **left side** of the arena.
* Boss appears on the **right side**, stationary.
* All attacks occur **only on the left side**.
* Touching the boss or crossing the boundary = **instant death**.
* Survive 4 attacks to win.

---

## **4. Enemies & Scoring**

**Enemy behavior:**

* Enemies chase the hero.
* Die from hero bullets.

**Scoring:**

* +1 score per enemy killed.
* When score reaches 30, boss spawns and enemies stop spawning.

**Spawn System:**

* Always maintain **minimum 6 enemies**.
* Killing 1 spawns 1 new enemy.
* Killing 3 spawns 3 new enemies, and so on.

---

## **5. Boss Encounter**

### **Boss Positioning**

* Boss stays on the **right half**.
* Hero stays on the **left half**.
* Boundary prevents crossing into boss territory.

### **Win Requirement**

* Survive all four attacks.
* During Attack 4, gain **+20 survival score**.

### **Lose Conditions**

* Touching boss.
* Crossing into boss side.
* Getting hit by any attack.

---

## **6. Boss Attack Phases**

### **Attack 1 – Ground Danger**

* Rising danger tiles from bottom-left.
* Touch = instant death.
* Hero bullets are destroyed on contact (no boss damage).

### **Attack 2 – Thunder Nightmare**

* Lightning lines appear on the left side.
* Happens **twice**, each for **5 seconds**.
* Touch = instant death.

### **Attack 3 – Gauntlet Death**

* A large projectile bounces like a **DVD screen** inside the left side.
* Touch = instant death.

### **Attack 4 – Dodge Fight**

* Asteroids fall from top-left.
* Hero must survive while gaining **+20 score**.
* Each dodge/time survived contributes to this score.

---

## **7. Win & Lose Conditions**

### ✔ Victory

* Score reaches 30, boss appears.
* Hero survives all 4 attacks.
* Hero gains +20 score during Attack 4.
* Boss defeated → **Player wins**.

### ✘ Game Over

* Hero touches boss.
* Hero crosses boundary into boss area.
* Hero is hit by:

  * Ground Danger
  * Thunder Nightmare
  * Gauntlet Death
  * Falling asteroids

---

## **8. Recommended Code Architecture**

| **Class** | **Purpose** |
|----------|-------------|
| **`Hero`** | Movement, shooting, collision detection, boundary lock during boss phase |
| **`Enemy`** | Basic behavior, pathfinding toward hero |
| **`EnemySpawner`** | Maintains minimum 6 enemies, respawns instantly after kills |
| **`Boss`** | Handles boss state, triggers attacks in sequence, enforces boundary |
| **`AttackPhase`** | Base class for all boss attacks (update(), start(), end()) |
| **`Attack1_GroundDanger`** | Logic for rising danger tiles from bottom |
| **`Attack2_ThunderNightmare`** | Spawning and timing lightning lines |
| **`Attack3_GauntletDeath`** | Bouncing projectile logic (DVD-style movement) |
| **`Attack4_DodgeFight`** | Asteroid spawning, survival scoring system |
| **`Projectile`** | Hero bullets, collision logic with enemies and attack tiles |
| **`GameManager`** | Controls phase switching, score logic, game states |
| **`UI`** | Score display, boss warnings, phase indicators |
| **`BoundaryWall`** | Prevents hero from entering boss side |