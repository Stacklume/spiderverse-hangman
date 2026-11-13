# 🕷️ Spider-Verse Hangman

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://spiderverse-hangman.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)

An interactive, browser-based word-guessing game inspired by the Spider-Man universe, built with **Python** and **Streamlit**.

## 🚀 Live Demo
👉 **[Play Spider-Verse Hangman Live](https://spiderverse-hangman.streamlit.app)** 

---

## ✨ Key Features
- **Instant Gameplay:** Launches immediately with a playable default word and blank progress spaces ready for guessing.
- **Dynamic Difficulty Scaling:** Switch seamlessly between **Easy**, **Medium**, and **Hard** word tiers using Streamlit `on_change` callbacks that automatically reset the board and adjust the target word length.
- **Persistent State Management:** Uses `st.session_state` to track guessed letters, remaining web-fluid lives (`6/6`), and win/loss states across interactive UI reruns.
- **Responsive On-Screen Keyboard:** Features a 9-column alphabet button grid that dynamically disables already-guessed letters in real time.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Web Framework:** Streamlit
- **Hosting & CI/CD:** Streamlit Community Cloud (auto-deployed from GitHub)

---

## 📂 Project Structure
```text
├── app.py              # Main Streamlit application & game state logic
├── requirements.txt    # Python dependencies for cloud deployment
├── .gitignore          # Excludes local virtual environments and cache files
└── README.md           # Project documentation
