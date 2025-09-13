# 🎧 MoodMatch — Multi‑Language Mood Detection with Music & Quotes

MoodMatch is an interactive Streamlit app that understands your mood from text in multiple languages (English, Telugu, Hindi, Tamil) using sentiment analysis and translation.  
It instantly recommends curated Spotify playlists and uplifting quotes to either match your current mood or help you shift to a new one.

---

## ✨ Features

- **🎯 Multi‑Language Mood Detection** — Detects mood from text in English, Telugu, Hindi, and Tamil using `langdetect`, `deep‑translator`, and NLTK VADER sentiment analysis.
- **🔄 Mood‑Shift Mode** — Choose a *target mood* different from your detected mood to get recommendations that help you shift emotional state.
- **🎵 Verified Spotify Playlists** — Curated, working playlists for each mood in each supported language — no duplicates, all tested.
- **🌐 Language Filter** — Instantly filter playlists by language without re‑entering mood text.
- **❤️ Favorites System** — Save playlists and quotes you like during the session for quick access.
- **💬 Inspiring Quotes** — Mood‑specific quotes to match or improve your emotional state.
- **🎨 Polished UI** — Gradient mood banners, clean card layout, and emoji quick‑pick for instant mood selection.
- **🛠 Debug Mode (Optional)** — Expandable section showing raw sentiment scores for transparency and testing.

---

## 📹 Demo Video
[![Watch the demo](https://img.shields.io/badge/YouTube-Demo-red?logo=youtube)](YOUR_YOUTUBE_DEMO_LINK_HERE)

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** — Web app framework
- **NLTK (VADER)** — Sentiment analysis
- **langdetect** — Language detection
- **deep‑translator** — Translation to English for analysis
- **Spotify** — Curated playlist links

---

## 📦 Installation & Setup
 **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/MoodMatch.git
   cd MoodMatch
**Install dependencies**
pip install -r requirements.txt
 **How toRun the app**
streamlit run streamlit_app.py

Usage:
Enter your mood — Type a sentence in English, Telugu, Hindi, or Tamil, or pick an emoji.
View detected mood — The app detects your mood and shows matching playlists & quotes.
Use Mood‑Shift Mode — Switch to a different mood to change recommendations.
Filter by language — Show playlists only in your preferred language.
Save favorites — Keep playlists & quotes you like for quick access.

📂 Project Structure

MoodMatch/
│
├── streamlit_app.py       # Main app
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

Future Improvements:
Add Kannada & Malayalam playlists
AI‑generated quotes
User mood history tracking
More moods and playlist sources

Landing / Home Screen
<img width="1410" height="745" alt="image" src="https://github.com/user-attachments/assets/0bc7b918-1ad5-4e07-87fd-689cd032aac0" />

Mood Detection in Action
<img width="1416" height="996" alt="image" src="https://github.com/user-attachments/assets/d6f6842b-d984-4df9-b660-eaa26df73997" />
<img width="1392" height="986" alt="image" src="https://github.com/user-attachments/assets/9c632799-82af-49e2-ab6e-ee95dc4a97c4" />
