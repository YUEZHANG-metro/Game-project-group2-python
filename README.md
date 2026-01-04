# Carbon Code: The Spy Energy Race 🌍

> **A Full-Stack Strategy Game regarding Sustainability, Global Travel, and Resource Management.**

![Project Status](https://img.shields.io/badge/Status-Demo_Ready-success)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![Python](https://img.shields.io/badge/Backend-Python_Flask-yellow)
![React](https://img.shields.io/badge/Frontend-Next.js_TypeScript-blueviolet)

## 📖 Project Overview
**Carbon Code** is an interactive strategy game set in the year 2200. It simulates a high-stakes race between nations to secure clean energy technologies while managing carbon footprints.

This project demonstrates a complete **System Integration** of a Python-based logic engine, a persistent MySQL database, and a modern React frontend with 3D geospatial visualization.

### 🛠️ Tech Stack
| Component | Technologies |
|-----------|--------------|
| **Backend** | Python 3, Flask, RESTful APIs, GeoPy (Distance/Carbon Calculation) |
| **Frontend** | TypeScript, Next.js, Tailwind CSS, **Cesium (3D Maps)**, Radix UI |
| **Database** | MySQL / MariaDB |
| **DevOps** | Docker, Docker Compose |

---

## 🚀 Quick Start (Recommended)
The application is fully containerized for easy deployment and testing.

**Prerequisites:** Docker Desktop installed.

1. **Clone the repository**

        git clone [https://github.com/SuzyZhang-Dev/FullStack-Spygame-CarbonCode.git](https://github.com/SuzyZhang-Dev/FullStack-Spygame-CarbonCode.git)
        cd FullStack-Spygame-CarbonCode

2. **Run with Docker Compose**
   This command sets up the Backend, Frontend, and Database automatically.

        docker-compose up --build

3. **Access the Application**
   * **Frontend (Game UI):** Open `http://localhost:3000`
   * **Backend API:** Running at `http://localhost:8080`

---

## 🌏 Worldview & Story
**The Year 2200:** The world is depleted of non-renewable resources. A "War without Smoke" has divided humanity into three roles:

1.  **🔬 The Inventors:** Brilliant geniuses moving secretly across continents. Their goal is to research clean energy technologies to save the dying planet without being beholden to any government.
2.  **🕵️‍♀️ The Spies (You):** Intelligence agents tasked by their nations to track down Inventors, steal their technology, and transport it back home—all while managing the "Carbon Budget."
3.  **Ordinary People:** The bystanders in this global race.

### 🎯 Player Mission
As a spy, you must:
1.  **Select a starting nation** (Each has different Initial Inventive Capabilities).
2.  **Travel globally** to find clues about the Inventor's location.
3.  **Manage Carbon Emissions:** Every flight costs carbon credits. Exceeding the limit results in mission failure (Game Over).
4.  **Win:** Secure enough Invention Points (200+) to save your country's future.

---

## ✨ Key Features
* **Carbon Emission Simulation:** Real-time calculation of flight distances and environmental impact using geodesic algorithms.
* **Global Navigation:** Interactive map interface for selecting travel destinations.
* **Competitor AI:** NPC spies that compete against the player in real-time.
* **Dynamic Event System:** Randomized clues and inventor locations to ensure unique gameplay every session.
* **Data Persistence:** Game state and player history are stored securely in a relational database.

### ✅ Development Checklist
- [x] **Core Game Loop:** Select country -> Travel -> Get Clues -> Find Inventor.
- [x] **Algorithm:** Carbon footprint calculation based on real-world airport coordinates.
- [x] **API Integration:** REST endpoints connecting Python logic with Next.js frontend.
- [x] **Win/Loss Conditions:** Logic for Invention Score victory and Carbon Limit failure.
- [x] **Dockerization:** Containerized environment for consistent deployment.

---

## 🛠️ Manual Setup (For Development)
If you wish to run the components individually without Docker:

### 1. Database Setup
Ensure you have a local MySQL instance running. Create a database named `spy_game` and import `backend/game_spy_database.sql`.

### 2. Backend (Python)

    cd backend
    # Create and activate virtual environment
    python -m venv .venv
    source .venv/bin/activate  # Windows: .\.venv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt

    # Configure Environment (Rename .env.template and update DB_PASSWORD)
    mv .env.template .env

    # Run Server
    python spy.py

### 3. Frontend (Node.js)

    cd frontend
    npm install
    npm run dev

---

## 🤝 Contribution
1. Create a new branch for your feature.
2. Commit your changes with clear messages.
3. Open a Pull Request (PR) to the `main` branch.
4. **Warning:** Do not commit directly to `main`.

---

*Developed for the Python Development Project Course.*