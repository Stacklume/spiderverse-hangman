import random
import streamlit as st

st.set_page_config(page_title="Spider-Verse Hangman", page_icon="🕷️")

spiderman_words = {
    "easy": [
        "web", "suit", "mask", "hero", "bite", "aunt", "city",
        "gwen", "mary", "jane", "otto", "sand", "bugle", "peter",
        "venom", "stark", "happy", "power", "sense", "swing",
        "climb", "flash", "uncle", "harry", "brock"
    ],
    "medium": [
        "spider", "parker", "goblin", "norman", "osborn", "queens",
        "lizard", "shield", "marvel", "rescue", "danger", "mutant",
        "vulture", "octopus", "electro", "sandman", "carnage",
        "morbius", "avenger", "costume", "nylon", "pendulum"
    ],
    "hard": [
        "symbiote", "mysterio", "oscorp", "brooklyn", "multiverse",
        "chameleon", "hobgoblin", "scorpion", "kingpin", "blackcat",
        "spiderverse", "radioactive", "responsibility", "ironspider",
        "dailybugle", "docock", "milesmorales", "greengoblin"
    ]
}

def start_new_game(difficulty):
    st.session_state.word = random.choice(spiderman_words[difficulty]).lower()
    st.session_state.guessed = set()
    st.session_state.lives = 6
    st.session_state.game_over = False

def on_difficulty_change():
    start_new_game(st.session_state.difficulty_selector)

# Initialize default game on first load (starts on "easy" with a playable word ready)
if "difficulty_selector" not in st.session_state:
    st.session_state.difficulty_selector = "easy"
if "word" not in st.session_state:
    start_new_game(st.session_state.difficulty_selector)

# Header & Difficulty Selector
st.title("🕷️ Spider-Verse Hangman")
col1, col2 = st.columns([2, 1])

with col1:
    st.selectbox(
        "Select Difficulty",
        ["easy", "medium", "hard"],
        key="difficulty_selector",
        on_change=on_difficulty_change
    )

with col2:
    st.write("")
    st.write("")
    if st.button("New Word", use_container_width=True):
        start_new_game(st.session_state.difficulty_selector)
        st.rerun()

# Display Lives & Word Progress (Blank spaces update automatically to match word length)
st.subheader(f"Web Fluid Remaining: {'🕸️ ' * st.session_state.lives} ({st.session_state.lives}/6)")
display_word = " ".join(
    [letter.upper() if letter in st.session_state.guessed else "_" for letter in st.session_state.word]
)
st.markdown(f"## `{display_word}`")


# Win / Loss Check
if "_" not in display_word:
    st.success(f"🎉 You saved the multiverse! The word was **{st.session_state.word.upper()}**.")
    st.session_state.game_over = True
elif st.session_state.lives <= 0:
    st.error(f"💀 Out of web fluid! The word was **{st.session_state.word.upper()}**.")
    st.session_state.game_over = True

# Interactive On-Screen Keyboard
if not st.session_state.game_over:
    st.write("### Guess a Letter:")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cols = st.columns(9)
    for idx, letter in enumerate(alphabet):
        with cols[idx % 9]:
            disabled = letter in st.session_state.guessed
            if st.button(letter.upper(), key=letter, disabled=disabled, use_container_width=True):
                st.session_state.guessed.add(letter)
                if letter not in st.session_state.word:
                    st.session_state.lives -= 1
                st.rerun()