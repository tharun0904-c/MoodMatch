import random
from typing import Dict, List, Tuple, Any
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from langdetect import detect
from deep_translator import GoogleTranslator

try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

#data
MOODS = ["happy", "sad", "angry", "calm", "anxious", "motivated"]

EMOJI_TO_MOOD = {
    "😊": "happy",
    "😢": "sad",
    "😠": "angry",
    "😌": "calm",
    "😰": "anxious",
    "🔥": "motivated",
}
# playlist with title and urls.lang= "hindi"/"tamil"/"kannada"/"malayalam"
SPOTIFY_PLAYLISTS: Dict[str,List[Dict[str,str]]]={
    "happy":[
        # English
        {"title":"Have a Great Day!","url":"https://open.spotify.com/playlist/37i9dQZF1DX7KNKjOK0o75","lang":"English"},
        {"title":"Happy Hits","url":"https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC","lang":"English"},
        # Telugu
        {"title":"Good Mood Telugu","url":"https://open.spotify.com/playlist/5y0WU4I2apysRT5ZHqDSDy","lang": "Telugu"},
        {"title": "Telugu Happy Mood Songs","url": "https://open.spotify.com/playlist/4jW37umAGFKr2oQRAk5pAe","lang": "Telugu"},
        # Hindi
        {"title":"Hindi Mood Boosters","url":"https://open.spotify.com/playlist/01lkhFPwkcnP1HBNW3Qql2","lang":"Hindi" },
        {"title":"Bollywood Dance Hits","url":"https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM","lang":"Hindi"},
        # Tamil
        {"title":"Tamil Mood Boosters","url":"https://open.spotify.com/playlist/2uRSqaw3q6Cm4gSTLga5Kr","lang":"Tamil"},
        {"title":"Tamil Happy Mood Vibes","url":"https://open.spotify.com/playlist/5q8bruCWqDDoDiOMHKFg5M" ,"lang":"Tamil"},
    ],
    "sad": [
        # English
        {"title": "Life Sucks", "url": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1", "lang": "English"},
        {"title": "Sad Songs", "url": "https://open.spotify.com/playlist/37i9dQZF1DWVV27DiNWxkR", "lang": "English"},
        # Telugu
        {"title": "Telugu Heartbreak Hits", "url": "https://open.spotify.com/playlist/6JHVCce9p43tsyLCrN1F2N", "lang": "Telugu"},
        {"title": "Much Needed Comfort Songs", "url": "https://open.spotify.com/playlist/7uYBE9RgLZ8eMXzwnYfx6l", "lang": "Telugu"},
        # Hindi
        {"title": "Sad Hindi Songs", "url": "https://open.spotify.com/playlist/189Sow1xr7R94oSKs4kISc", "lang": "Hindi"},
        {"title": "Bollywood Sad Hits", "url": "https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT", "lang": "Hindi"},
        # Tamil
        {"title": "Tamil Sad Songs", "url": "https://open.spotify.com/playlist/0AyOLKzLZZmlliok7bu1mp", "lang": "Tamil"},
        {"title": "Tamil Heartbreak Hits", "url": "https://open.spotify.com/playlist/1WenBZNin1R4hAQz2qgzOl", "lang": "Tamil"},
    ],
    "angry":[
        # English
        {"title":"Rock Hard", "url":"https://open.spotify.com/playlist/37i9dQZF1DX1rVvRgjX59F","lang":"English"},
        {"title":"Beast Mode","url":"https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP","lang":"English"},
        # Telugu
        {"title":"Telugu Mass Beats","url":"https://open.spotify.com/playlist/5ZaV213C0aSoPEENQOPpGb","lang":"Telugu"},
        {"title":"Vintage Thaman","url":"https://open.spotify.com/playlist/5WBVluKblqOvgtQrBKk9PP","lang":"Telugu"},
        # Hindi
        {"tamil":"Bollywood Workout Hits","url":"https://open.spotify.com/playlist/37i9dQZF1DX3wwp27Epwn5","lang":"Hindi"},
        {"title":"Hindi pump Up","url":"https://open.spotify.com/playlist/5cwtgqs4L1fX8IKoQebfjJ","lang":"Hindi" },
        # Tamil
        {"title":"Tamil Mass Hits","url":"https://open.spotify.com/playlist/3p8ejB7BscAVmEdyK7AtXx","lang":"Tamil"},
        {"tamil":"Tamil Workout Anthems","url":"https://open.spotify.com/playlist/3TCmVKURNBtXWEsdu9iEwC","lang":"Tamil"},
    ],
    "calm":[
        # English
        {"title":"Peaceful Piano","url":"https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO","lang":"English"},
        {"title":"Lo-Fi Beats","url":"https://open.spotify.com/playlist/37i9dQZF1DXdbkmlag2h7b","lang":"English"},
        # Telugu
        {"title":"Soothing Telugu Melodies","url":"https://open.spotify.com/playlist/1UF6QgQcJAerQ6C8q7qLUb","lang":"Telugu"},
        {"title":"Carnatic & Relaxation","url":"https://open.spotify.com/playlist/37i9dQZF1DXdMUUSqm9tTc","lang":"Telugu"},
        # Hindi
        {"title":"Hindi Chill Vibes","url":"https://open.spotify.com/playlist/02uXGKglrYZD67gcyxkvTd","lang":"Hindi"},
        {"title":"Bollywood Acoustic","url":"https://open.spotify.com/playlist/37i9dQZF1DWSwxyU5zGZYe","lang":"Hindi"},
        # Tamil
        {"title":"Tamil Chill Vibes","url":"https://open.spotify.com/playlist/5nG3U5u6Q7Zcl8mjkrqHpX","lang":"Tamil"},
        {"title":"Tamil Acoustic","url":"https://open.spotify.com/playlist/37i9dQZF1DX3SAjV5mzFIB","lang":"Tamil"},
    ],
    "anxious":[
        # English
        {"title":"Deep Foucus","url":"https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ","lang":"English"},
        {"title":"calm Vibes","url":"https://open.spotify.com/playlist/37i9dQZF1DX9sIqqvKsjG8","lang":"English"},
        # Telugu
        {"title":" calm Your Mind","url":"https://open.spotify.com/playlist/5q8sllODnbXCWJyha3cL5n","lang":"Telugu"},
        {"title":"Carnatic Fusion Instrumental","url":"https://open.spotify.com/playlist/4A41E4xm9VLjUbVPG32Cuy","lang":"Telugu"},
        # Hindi
        {"title":"Hindi Meditation","url":"https://open.spotify.com/playlist/0uZcnijuXOQrH9kxCGjJdk","lang":"Hindi"},
        {"title":"Bollywood Relaxation","url":"https://open.spotify.com/playlist/37i9dQZF1DWX76Z8XDsZzF","lang":"Hindi"},
        # tamil
        {"title":"Tamil Meditation","url":"https://open.spotify.com/playlist/37i9dQZF1DWZqd5JICZI0u","lang":"Tamil"},
        {"title":"Tamil Relaxation","url":"https://open.spotify.com/playlist/37i9dQZF1DWX5ZkTCLvHmi","lang":"Tamil"},

    ],
    "motivated":[
        # English
        {"title":"Power Workout","url":"https://open.spotify.com/playlist/37i9dQZF1DX70RN3TfWWJh","lang":"English"},
        {"title":"Confidence Boost", "url": "https://open.spotify.com/playlist/37i9dQZF1DX4fpCWaHOned","lang":"English"},
        # Telugu
        {"title":"Workout Beats Telugu","url":"https://open.spotify.com/playlist/0i0B2twRW5Bf627kHtZiYY","lang":"Telugu"},
        {"title":"Dha Bandekku Road Trip Songs","url":"https://open.spotify.com/playlist/2pRRvJqWla6AJFcQXOc572", "lang": "Telugu"},
        # Hindi
        {"title":"Hindi motivation","url":"https://open.spotify.com/playlist/7zNvXEjgmE1110slXAuZie", "lang": "Hindi"},
        {"title":"Bollywood Workout", "url": "https://open.spotify.com/playlist/37i9dQZF1DX3wwp27Epwn5", "lang": "Hindi"},
        # Tamil
        {"title":"Tamil motivation","url":"https://open.spotify.com/playlist/4Ky4vveGq77DAgV3Z2Lk4e", "lang": "Tamil"},
        {"title":"Tamil Workout", "url": "https://open.spotify.com/playlist/4VWF0TcCYet7z1RpgLjAaY", "lang": "Tamil"},
    ],
}
QUOTES: Dict[str,List[str]] = {
    "happy": [ 
        "Happy is not by chance, but by choice.",
        "Wherever you go, no matter what the weather, always bring your own sunshine.",
    ],
    "sad":[
        "Tears are words that need to be written.",
        "Stars can't shine without darkness.",
    ],
    "angry":[
        "For every minute you remain angry, you give up sixty seconds of peace of mind.",
        "Speak when you are angry and you will make the best speech you will ever regret.",
    ],
    "calm":[
        "Calm is a superpower.",
        "Within you, there is a stillness and a sanctuary.",

    ],
    "anxious":[
        "Do what you can, with what you have, where you are.",
        "This too shall pass.",
    ],
    "motivated":[
        "Dreams dont work unless you do.",
        "Success is the sum of small efforts, repeated day in and day out.",

    ],
}
COLORS = {
    "happy":"#FFD166",
    "sad":"#7EB6FF",
    "angry":"#FF6B6B",
    "Calm":"#A8C6EF",
    "anxious":"#CDB4DB"
    "motivated""#B9FBC0",
}
GRADIENTS = {
    "happy":"linear-gradient(90deg,#FFD166,#FFB347)",
    "sad":"linear-gradient(90deg,#7EB6FF,5A8DEE)",
    "angry":"linear-gradient(90deg,#FF6B6B,#D64545)",
    "Calm":"linear-gradient(90deg,#A8C6EF,#56C596)",
    "anxious":"linear-gradient(90deg,#CDB4DB,#A78EB2)",
    "motivated":"linear-gradient(90deg,#B9FBC0,#4CAF50)",
}
#____Helpers__

def analyze_text_mood(text: str)->Tuple[str,Dict[str,float]]:
    try:
        lang=detect(text)
    except Exception:
        lang='en'
    if lang !="en":
        try:
            translated=GoogleTranslator(source=lang,target='en').translate(text)
            text = translated
            st.caption(f"Detected language:{lang.upper()}->translatedto Englishfor analysis.")
        except Exception:
            st.warning("Translation failed, analyzing original text.")

    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    compound = scores["compumd"]
    lowered = text.lower()
    if any(k in lowered for k in ["angry","mad","furious","annoyed","rage"]):
        return "angry",scores
    if any(k in lowered for k in ["nervous","anxious","worried","stressed","panic"]):
        return"anxious", scores
    if any(k in lowered for k in ["calm","Peaceful","relaxed","chill","serene"]):
        return"calm", scores
    if any(k in lowered for k in["motivate","hustle","grind","Foucus","ambitious"]):
        return "motivated", scores
    if compound>=0.4:
        return "happy",scores
    elif compound<= -0.4:
        return "sad",scores
    else:
        return"calm",scores
def get_recommendations(mood: str) -> Tuple[List[Dict[str,str]],List[str]]:
    return SPOTIFY_PLAYLISTS.get(mood, []),QUOTES.get(mood,[])
def section_title(title:str,color:str):
    st.markdown(
        f"<h3 style='margin-top:0.75rem;color:{color};'>{title}</h3>",
        unsafe_allow_html=True
    )

def ensure_session():
    if "favorites" not in st.session_state:
        st.session_state["favorites"]=[]

def save_favorite(item:Dict[str,Any]):
    ensure_session()
    st.session_state["favorites".append(item)]

#UI
st.set_page_config(page_title="MoodMatch | Music + Quotes", page_icon="🎧",layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #f9f9f9; font-family: 'Segoe UI', sans-serif; }
    h3 { font-weight: 600; margin-top: 1rem; }
    .card { background: white; padding: 12px; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.05); margin-bottom: 10px; }
    .mood-banner { padding: 14px; border-radius: 12px; color: white; font-weight: bold; text-align: center; margin-bottom: 20px; }
    a { text-decoration: none; }
    </style>
""", unsafe_allow_html=True)
st.title("MoodMatch 🎧 ✨")
st.caption("Your mood, your Vibe instantly matched.")

with st.expander("How it works",expanded=False):
    st.markdown(
        "-Enter how you feel or tap an emoji.\n"
        "- We detect your mood and recommend playlists and quotes.\n"
        "- Use language filter to switch between Telugu and English.\n"
        "- Save favorites while you browse."
    )
# input area 
col1,col2 = st.columns([3,2])
with col1:
    user_text=st.text_area(
        "Describe your mood in a sentence (optional if you use emojis)",
        placeholder="Example: ఈ రోజు నాకు చాలా సంతోషంగా ఉంది 🙂 / I'm feeling a bit stressed but hopeful.",
        height=100,
    )
with col2:
    st.write("Quick pick:")
    emoji_choice = st.radio(
        "choose mood emoji",
        options=[""]+list(EMOJI_TO_MOOD.keys()),
        index=0,
        horizontal=True

    )
    if emoji_choice=="":
        emoji_choice=None
#Mood determine
detected_mood=None
scores={}
if emoji_choice:
    detected_mood = EMOJI_TO_MOOD[emoji_choice]
elif user_text and user_text.strip():
    detected_mood,scores=analyze_text_mood(user_text.strip())
# overriding the mood
st.write("")
override = st.selectbox("Or pick a mood directly", MOODS, index=MOODS.index(detected_mood) if detected_mood else 0)
active_mood = override if override else (detected_mood or "calm")

#mood-shift
st.write("")
shift_mode = st.checkbox("🎯 Mood‑Shift Mode", value=False, help="Recommend content for a different mood than your current one")
target_mood = active_mood
if shift_mode:
    target_mood= st.selectbox(
        "Choose the mood you want to shift to ",
        MOODS,
        index=moods.index("happy") if active_mood!="happy" else 0 

    )
#Mood banner with gradient 
st.markdown(
    f"""
    <div class="mood-banner" style="background: {GRADIENTS.get(target_mood, '#EEE')};">
      {'Target mood' if shift_mode else 'Current mood'}: {target_mood.capitalize()}
    </div>
    """,
    unsafe_allow_html=True,
)
#recomndations
playlists,quotes = get_recommendations(target_mood)

#language Filter 
available_langs = sorted(set(p.get("lang","English") for p in playlists))
language_choice = st.selectbox(
    "Filter playlists by language",
    ["All"]+available_langs,
    index=0
)
filtered_playlists = playlists if language_choice=="All" else [p for p in playlists if p.get("lang")==language_choice]
section_title("Playlists",COLORS.get(target_mood,"#000"))
if not filtered_playlists:
    st.info("No playlists for this language yet. Choose another language or add more links to SPOTIFY_PLAYLISTS.")
else:
    for p in filtered_playlists:
        with st.container():
            st.markdown(f"""
                <div class="card">
                    <b>🎵 {p['title']}</b> <span style="color:#888;">({p.get('lang','')})</span><br>
                    <a href="{p['url']}" target="_blank">Open in Spotify</a>
                </div>
            """, unsafe_allow_html=True)
            c1,c2 =st.columns(2)
            with c1:
                if st.button(f"❤️ Save '{p['title']}'", key=f"fav_pl_{target_mood}_{p['title']}"):
                    save_favorite({"type": "playlist", "title": p["title"], "url": p["url"], "lang": p.get("lang","")})
                    st.success("Saved to favorites!")

section_title("Quotes", COLORS.get(target_mood, "#000"))
for q in quotes:
     with st.container():
        st.markdown(f"""
            <div class="card">
                📝 {q}
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"💾 Save quote {abs(hash(q)) % 9999}", key=f"fav_q_{target_mood}_{abs(hash(q))}"):
            save_favorite({"type": "quote", "text": q, "mood": target_mood})
            st.success("Saved to favorites!")

# Favorite section
st.markdown("<hr style='border:0.5px solid #ddd; margin: 20px 0;'>", unsafe_allow_html=True)
section_title("Your favorites (session)", "#555")
favs = st.session_state.get("favorites", [])
if not favs:
    st.caption("No favorite at. Save a playlist or quote you like.")
else:
    for item in favs:
        if item["typw"]=="playlist":
            st.markdown(f"- 🎵 **{item['title']}** ({item.get('lang','')}) — [Open]({item['url']})")
        else:
            st.markdown(f"- 📝 {item['text']}")
#optional debud
with st.expander("Debug:sentiment scores",expanded=False):
    if scores:
        st.json(scores)
    else:
        st.caption("No sentiment yet - eneter text to analyze.")
st.caption("Tip: Add more languages by appending entries to SPOTIFY_PLAYLISTS with a 'lang' field (e.g., 'Hindi', 'Tamil', 'Kannada', 'Malayalam'). They’ll automatically appear in the filter.")