# Gesture-Play: Hand Gesture Controlled Subway Surfers

Gesture-Play is a computer vision–based application that enables hands-free gameplay for Subway Surfers using real-time hand gestures. The system leverages webcam input to detect hand movements and translates them into keyboard actions, demonstrating practical applications of computer vision, human–computer interaction, and real-time systems.

This project highlights the use of AI-driven perception to create intuitive and accessible game controls without external hardware.

---

## Project Overview

- **Domain**: Computer Vision, Human–Computer Interaction (HCI)
- **Core Technologies**: Python, MediaPipe, OpenCV
- **Input**: Hand gestures via webcam
- **Output**: Keyboard control for gameplay

---

## Key Features

- **Real-Time Hand Tracking**  
  Uses MediaPipe’s hand landmark detection to accurately track hand movements through a standard webcam.

- **Gesture-Based Game Control**  
  - Swipe Up → Jump  
  - Swipe Down → Roll  
  - Move Left / Right → Change lanes  

- **Hands-Free Interaction**  
  No physical controllers required, improving accessibility and user experience.

- **Low Latency Execution**  
  Optimized gesture processing ensures smooth and responsive gameplay.

---

## Tech Stack

- **Python**
- **OpenCV** – Video capture and frame processing
- **MediaPipe** – Hand landmark detection
- **PyAutoGUI** – Simulated keyboard inputs
- **NumPy** – Numerical computations

---

Control Mapping

The application monitors your hand landmarks and translates specific postures into keyboard commands:

| Gesture | Game Action | Keyboard Trigger |
| :--- | :--- | :--- |
| **Index Finger Up** | **Idle** | None (Wait State) |
| **All Fingers Open** | **Jump** | `Up Arrow` |
| **Fist (All Closed)** | **Roll** | `Down Arrow` |
| **Pointing Index Left/Right** | **Move Lane** | `Left / Right Arrow` |


---

### 2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
## How to Run the Project
Start the application:

bash
Copy code
python main.py
Open Subway Surfers in your browser or desktop game window.

Position your hand clearly in front of the webcam.


---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/PratikAxis/Gesture-Play.git
cd Gesture-Play
