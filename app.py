import streamlit as st
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Happy Birthday Saloni ❤️",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Image URLs - Replace these with your actual image URLs
IMAGE_URL_1 = "https://ibb.co/j9bLq9ct"  # Replace with your first image URL
IMAGE_URL_2 = "https://ibb.co/TqN3fXqh"  # Replace with your second image URL  
IMAGE_URL_3 = "https://ibb.co/Z1xhBDnh"  # Replace with your third image URL

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;400;700&family=Inter:wght@300;400;500&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd9 50%, #f48fb1 100%);
        background-attachment: fixed;
    }
    
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 4.5rem;
        font-weight: 900;
        color: white !important;
        text-align: center;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.3), 0 0 20px rgba(255,255,255,0.5);
        margin-bottom: 20px;
        letter-spacing: 2px;
        transform: scale(1.05);
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: white !important;
    }
    
    .subtitle {
        font-size: 1.8rem;
        color: white;
        text-align: center;
        font-weight: 700;
        margin-bottom: 30px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3), 0 0 15px rgba(255,255,255,0.4);
        letter-spacing: 1px;
    }
    
    .love-message {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .message-text {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        line-height: 1.8;
        color: white;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .photo-frame {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        border: 3px solid rgba(255, 255, 255, 0.3);
        transition: transform 0.3s ease;
    }
    
    .photo-frame:hover {
        transform: scale(1.05);
    }
    
    .memory-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    }
    
    .memory-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        color: white;
        margin-bottom: 10px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3), 0 0 12px rgba(255,255,255,0.4);
        font-weight: 800;
        letter-spacing: 1px;
    }
    
    .memory-text {
        color: white;
        font-size: 1rem;
        line-height: 1.6;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1000;
    }
    
    .heart {
        position: absolute;
        font-size: 20px;
        color: rgba(255, 255, 255, 0.7);
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { 
            transform: translateY(0px) rotate(0deg); 
            opacity: 0.7; 
        }
        50% { 
            transform: translateY(-20px) rotate(10deg); 
            opacity: 1; 
        }
    }
    
    .countdown-box {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .countdown-number {
        font-size: 3rem;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .countdown-label {
        font-size: 1rem;
        color: white;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Hide Streamlit elements */
    .stDeployButton {display: none;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# Floating hearts animation
st.markdown("""
<div class="floating-hearts">
    <div class="heart" style="left: 10%; animation-delay: 0s;">💖</div>
    <div class="heart" style="left: 20%; animation-delay: 1s;">💕</div>
    <div class="heart" style="left: 80%; animation-delay: 2s;">💖</div>
    <div class="heart" style="left: 90%; animation-delay: 3s;">💕</div>
    <div class="heart" style="left: 60%; animation-delay: 4s;">💖</div>
</div>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-title">Happy Birthday Saloni 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Today is all about celebrating the amazing person you are ✨</p>', unsafe_allow_html=True)

# Add some space
st.markdown("<br>", unsafe_allow_html=True)

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Main love message
    st.markdown('''
    <div class="love-message">
        <p class="message-text">
            My dearest Saloni,

On this special day, I just want to pause and let you know how much you truly mean to me. You bring sunshine into my darkest days and somehow make even the ordinary moments feel extraordinary just by being in my life. Every time I look at you, I see the most beautiful soul, inside and out, and I cannot help but feel grateful that I get to call you mine.

Your smile lights up my world in ways words could never fully describe, and your laughter—oh, your laughter—is my favorite sound. It has this magic that can instantly melt away all my worries and replace them with joy. You are not just my girlfriend; you are my best friend, my safe place, my inspiration, and my greatest blessing.

I admire the way you love, the way you care, and the way you make life so much brighter for everyone around you. With you, I’ve learned what it means to be truly happy, and I can’t imagine my journey without you by my side.

 May this year bring you endless love, laughter, and everything your heart desires, because you deserve nothing less than the absolute best.

Happy Birthday, my love. Thank you for being the reason behind my happiest days and for making life so beautifully worth living. 💕
        </p>
    </div>
    ''', unsafe_allow_html=True)

# Photo gallery section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: white; font-family: Playfair Display; font-size: 3rem; font-weight: 900; text-shadow: 3px 3px 8px rgba(0,0,0,0.3), 0 0 20px rgba(255,255,255,0.5); letter-spacing: 2px;">Our Beautiful Memories 📸</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    try:
        st.image(IMAGE_URL_1, use_column_width=True, caption="Our Beautiful Memory ❤️")
    except:
        st.markdown('''
        <div style="height: 200px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 15px;">
            <p style="color: white; text-align: center;">Replace IMAGE_URL_1<br>with your photo URL ❤️</p>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    try:
        st.image(IMAGE_URL_2, use_column_width=True, caption="Another Special Moment 📷")
    except:
        st.markdown('''
        <div style="height: 200px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 15px;">
            <p style="color: white; text-align: center;">Replace IMAGE_URL_2<br>with your photo URL 📷</p>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    try:
        st.image(IMAGE_URL_3, use_column_width=True, caption="A Precious Memory 💕")
    except:
        st.markdown('''
        <div style="height: 200px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 15px;">
            <p style="color: white; text-align: center;">Replace IMAGE_URL_3<br>with your photo URL 💕</p>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Reasons why I love you section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: white; font-family: Playfair Display; font-size: 3rem; font-weight: 900; text-shadow: 3px 3px 8px rgba(0,0,0,0.3), 0 0 20px rgba(255,255,255,0.5); letter-spacing: 2px;">Reasons Why I Love You 💖</h2>', unsafe_allow_html=True)

reasons = [
    ("Your Beautiful Smile", "Your smile has the power to brighten even my darkest days and makes everything feel perfect."),
    ("Your Kind Heart", "The way you care for others and show compassion makes me fall in love with you more every day."),
    ("Your Amazing Laugh", "Your laughter is music to my ears and fills my heart with pure joy."),
    ("Your Strong Spirit", "Your determination and strength inspire me to be a better person every day."),
    ("Your Love for Life", "The way you embrace life and find beauty in small moments makes every day an adventure."),
    ("Simply Being You", "You are perfect just the way you are, and I wouldn't change a single thing about you.")
]

col1, col2 = st.columns(2)

for i, (title, reason) in enumerate(reasons):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f'''
        <div class="memory-card">
            <h3 class="memory-title">{title}</h3>
            <p class="memory-text">{reason}</p>
        </div>
        ''', unsafe_allow_html=True)

# Birthday countdown or celebration
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: white; font-family: Playfair Display; font-size: 3rem; font-weight: 900; text-shadow: 3px 3px 8px rgba(0,0,0,0.3), 0 0 20px rgba(255,255,255,0.5); letter-spacing: 2px;">Birthday Celebration 🎉</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Get current year for birthday
    current_year = datetime.now().year
    
    # Birthday wish button
    if st.button("🎂 Make a Birthday Wish! 🎂", key="birthday_wish"):
        st.balloons()
        st.markdown('''
        <div class="love-message" style="text-align: center;">
            <p class="message-text">
                🌟 Happy Birthday, Beautiful! 🌟<br><br>
                May all your dreams come true, just like you made all of mine come true 
                by being in my life. Here's to another year of love, laughter, and 
                countless beautiful memories together! 💕🎂✨
            </p>
        </div>
        ''', unsafe_allow_html=True)
        time.sleep(2)
        st.snow()

# Personal message section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: white; font-family: Playfair Display; font-size: 3rem; font-weight: 900; text-shadow: 3px 3px 8px rgba(0,0,0,0.3), 0 0 20px rgba(255,255,255,0.5); letter-spacing: 2px;">A Special Message Just for You 💌</h2>', unsafe_allow_html=True)

# Text area for personal message (you can pre-fill this)
personal_message = st.text_area(
    "Add your personal birthday message here:",
    value="My love, as you celebrate another year of your incredible life, I want you to know that loving you has been the greatest adventure of my life. You make every day feel like a celebration, and today, we celebrate YOU! Thank you for being the amazing, beautiful, strong, and loving person that you are. I can't wait to create many more memories with you. Happy Birthday babe! 💕",
    height=150,
    key="personal_message"
)

if personal_message:
    st.markdown(f'''
    <div class="love-message">
        <p class="message-text">{personal_message}</p>
    </div>
    ''', unsafe_allow_html=True)

# Footer message
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('''
<div style="text-align: center; padding: 40px 0;">
    <p style="color: white; font-size: 1.2rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
        Made with 💖 by someone who loves you more than words can express
    </p>
    <p style="color: white; font-size: 1rem; margin-top: 10px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
        Happy Birthday, My Love! 🎂✨💕
    </p>
</div>
''', unsafe_allow_html=True)

# Add a sidebar with additional options
with st.sidebar:
    st.markdown("### 🎨 Customize Your Site")
    if st.button("🎆 Celebration Mode"):
        st.balloons()
        st.snow()
    
    st.markdown("### 💕 Quick Actions")
    if st.button("💌 Send Love"):
        st.success("Love sent! 💕")
    
    if st.button("🎵 Birthday Song"):
        st.info("🎵 Happy Birthday to You! 🎵")
