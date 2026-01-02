import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
from datetime import datetime
import base64
import os
import textwrap

# --- CONFIGURATION & ASSETS ---
st.set_page_config(
    page_title="Muhammad Muzammil | Data Science",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (Flattened to prevent Markdown parsing errors) ---
CUSTOM_CSS = """
/* FONTS */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=Inter:wght@300;400;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* GLOBAL VARIABLES */
:root {
    --bg: #0b0c10;
    --bg-secondary: #1a1d23;
    --card-bg: #1f2833;
    --accent: #66fcf1;
    --accent-secondary: #45a29e;
    --text: #c5c6c7;
    --text-highlight: #ffffff;
    --text-muted: #8a8d93;
    --success: #4ade80;
    --warning: #fbbf24;
    --error: #ef4444;
}

/* RESET & BASICS */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: var(--text);
    background-color: var(--bg);
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--text-highlight);
    letter-spacing: -1px;
}

/* REMOVE STREAMLIT CHROME */
#MainMenu, footer, header {visibility: hidden;}

/* CUSTOM SCROLLBAR */
::-webkit-scrollbar {width: 8px;}
::-webkit-scrollbar-track {background: var(--bg);}
::-webkit-scrollbar-thumb {background: #45a29e; border-radius: 4px;}
::-webkit-scrollbar-thumb:hover {background: #66fcf1;}

/* MAGNETIC ELEMENTS */
.magnetic-element {
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.magnetic-element:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(102, 252, 241, 0.3);
}

/* HERO SECTION STYLING */
.hero-container {
    padding: 4rem 0 2rem 0;
    animation: slideInFromBottom 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    position: relative;
    z-index: 1;
}
.big-title {
    font-size: 4.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 0%, #66fcf1 50%, #45a29e 100%);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 4s ease-in-out infinite;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 30px rgba(102, 252, 241, 0.3);
}
.subtitle {
    font-size: 1.5rem;
    color: #45a29e;
    margin-bottom: 2rem;
    animation: fadeInUp 1.5s ease-out 0.3s both;
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}
@keyframes slideInFromBottom {
    from { transform: translateY(50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
@keyframes fadeInUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

/* DYNAMIC PROFILE IMAGE */
.profile-img-container {
    display: flex !important;
    justify-content: center;
    margin-bottom: 20px;
    visibility: visible !important;
}
.profile-img {
    width: 220px;
    height: 220px;
    object-fit: cover;
    border: 2px solid var(--accent);
    box-shadow: 0 0 30px rgba(102, 252, 241, 0.3);
    /* The "Morphing" Shape */
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
    animation: morph 8s ease-in-out infinite;
    transition: all 0.5s ease-in-out;
}
.profile-img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 50px rgba(102, 252, 241, 0.6);
}

/* MOBILE-ONLY PROFILE IMAGE (appears before name on small screens) */
.profile-img-mobile {
    display: none;
}

@keyframes morph {
    0% {border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;}
    50% {border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;}
    100% {border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;}
}

/* ENHANCED BENTO BOX CARD DESIGN */
div[data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlock"] {
    gap: 1.5rem;
}

.project-card {
    background: rgba(31, 40, 51, 0.8) !important;
    border: 1px solid rgba(102, 252, 241, 0.15) !important;
    border-radius: 20px;
    padding: 28px !important;
    transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
    height: 100%;
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    box-shadow:
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg,
        transparent,
        rgba(102, 252, 241, 0.2),
        rgba(102, 252, 241, 0.1),
        transparent);
    transition: left 0.8s ease;
}

.project-card::after {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(102, 252, 241, 0.03) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.5s ease;
    pointer-events: none;
}

.project-card:hover::before {
    left: 100%;
    width: 200%;
}

.project-card:hover::after {
    opacity: 1;
}

.project-card:hover {
    transform: translateY(-12px) scale(1.03);
    border-color: var(--accent);
    box-shadow:
        0 20px 40px -10px rgba(102, 252, 241, 0.4),
        0 0 60px rgba(102, 252, 241, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

/* ENHANCED METRIC HIGHLIGHT */
.metric-pill {
    display: inline-block;
    background: linear-gradient(135deg, rgba(102, 252, 241, 0.15) 0%, rgba(102, 252, 241, 0.05) 100%);
    color: var(--accent);
    padding: 6px 16px;
    border-radius: 25px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 12px;
    border: 1px solid rgba(102, 252, 241, 0.3);
    box-shadow: 0 2px 10px rgba(102, 252, 241, 0.1);
    position: relative;
    overflow: hidden;
}

.metric-pill::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(102, 252, 241, 0.2), transparent);
    transition: left 0.5s ease;
}

.metric-pill:hover::before {
    left: 100%;
}

/* TESTIMONIAL CARD */
.testimonial-card {
    background: rgba(31, 40, 51, 0.3);
    border-left: 4px solid var(--accent);
    padding: 20px;
    border-radius: 0 12px 12px 0;
    margin-bottom: 10px;
}

/* ENHANCED BUTTONS OVERRIDE */
.stButton > button {
    background: linear-gradient(135deg, rgba(102, 252, 241, 0.1) 0%, rgba(102, 252, 241, 0.05) 100%);
    border: 1px solid var(--accent);
    color: var(--accent);
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    width: 100%;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(102, 252, 241, 0.2), transparent);
    transition: left 0.5s ease;
}

.stButton > button:hover::before {
    left: 100%;
}

.stButton > button:hover {
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent-secondary) 100%);
    color: #0b0c10;
    box-shadow:
        0 8px 25px rgba(102, 252, 241, 0.4),
        0 0 40px rgba(102, 252, 241, 0.3);
    transform: translateY(-2px);
}

/* DOWNLOAD BUTTON (Primary) */
.stDownloadButton > button {
    background: var(--accent);
    color: #0b0c10;
    border: none;
    font-weight: 700;
}
.stDownloadButton > button:hover {
    background: #45a29e;
    box-shadow: 0 0 20px rgba(102, 252, 241, 0.7);
}

/* ADVANCED ANIMATIONS */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes slideInFromLeft {
    from {opacity: 0; transform: translateX(-50px);}
    to {opacity: 1; transform: translateX(0);}
}

@keyframes slideInFromRight {
    from {opacity: 0; transform: translateX(50px);}
    to {opacity: 1; transform: translateX(0);}
}

@keyframes scaleIn {
    from {opacity: 0; transform: scale(0.8);}
    to {opacity: 1; transform: scale(1);}
}

@keyframes glowPulse {
    0%, 100% {
        box-shadow: 0 0 20px rgba(102, 252, 241, 0.3);
    }
    50% {
        box-shadow: 0 0 40px rgba(102, 252, 241, 0.6), 0 0 60px rgba(102, 252, 241, 0.4);
    }
}

/* SKILLS PROGRESS BARS */
.skill-bar {
    width: 100%;
    height: 8px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 4px;
    overflow: hidden;
    margin: 8px 0 16px 0;
}
.skill-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--accent), var(--accent-secondary));
    border-radius: 4px;
    width: 0%;
}

/* INTERACTIVE ELEMENTS */
.glow-button {
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}
.glow-button::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    background: radial-gradient(circle, rgba(102, 252, 241, 0.3) 0%, transparent 70%);
    transition: width 0.6s, height 0.6s;
    transform: translate(-50%, -50%);
    border-radius: 50%;
}
.glow-button:hover::after {
    width: 300px;
    height: 300px;
}

/* TYPING ANIMATION */
.typing-animation {
    border-right: 2px solid var(--accent);
    animation: blink 1s infinite;
}
@keyframes blink {
    0%, 50% { border-color: var(--accent); }
    51%, 100% { border-color: transparent; }
}

/* SCROLL-TRIGGERED ANIMATIONS */
.project-card, .testimonial-card {
    opacity: 1 !important;
    transform: translateY(0) !important;
    visibility: visible !important;
    display: block !important;
}

.project-card:nth-child(odd) {
    animation: slideInFromLeft 0.8s ease-out;
}

.project-card:nth-child(even) {
    animation: slideInFromRight 0.8s ease-out;
}

.animate-in {
    opacity: 1 !important;
    transform: translateY(0) !important;
}

/* ENHANCED SKILL BARS */
.skill-bar {
    width: 100%;
    height: 8px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 4px;
    overflow: hidden;
    margin: 8px 0 16px 0;
    position: relative;
}

.skill-bar::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, rgba(102, 252, 241, 0.2) 0%, rgba(102, 252, 241, 0.1) 100%);
    border-radius: 4px;
}

.skill-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--accent), var(--accent-secondary));
    border-radius: 4px;
    width: 0%;
    position: relative;
    box-shadow: 0 0 10px rgba(102, 252, 241, 0.5);
}

/* MOBILE TWEAKS */
@media (max-width: 768px) {
    .big-title {
        font-size: 2.5rem;
        line-height: 1.2;
    }
    .subtitle { font-size: 1.2rem; }
    .hero-container { padding: 2rem 0 1rem 0; }
    .project-card {
        padding: 16px;
        margin-bottom: 16px;
    }
    .profile-img { width: 180px; height: 180px; }

    /* On mobile show mobile image inside hero and hide desktop column image */
    .profile-img-mobile {
        display: block !important;
        width: 180px;
        height: 180px;
        object-fit: cover;
        border: 2px solid var(--accent);
        box-shadow: 0 0 30px rgba(102, 252, 241, 0.3);
        border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
        margin: 0 auto 14px auto;
    }

    .profile-img-container { display: none !important; }
}

@media (max-width: 480px) {
    .big-title { font-size: 2rem; }
    .project-card { padding: 12px; }
    .profile-img { width: 150px; height: 150px; }

    /* slightly smaller mobile-only image */
    .profile-img-mobile {
        width: 150px !important;
        height: 150px !important;
    }
}

/* TABLET OPTIMIZATIONS */
@media (min-width: 769px) and (max-width: 1024px) {
    .big-title { font-size: 3.5rem; }
    .project-card { padding: 20px; }
}

/* ACCESSIBILITY */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
"""

# Inject CSS properly using st.html instead of st.markdown
st.html(f"<style>{CUSTOM_CSS}</style>")


# --- UTILITY: GENERIC ASSET LOADER ---
def load_image(path):
    """
    Handles both web URLs and local file paths.
    Converts local files to base64 for embedding in HTML/CSS.
    """
    if path.startswith(("http://", "https://")):
        return path
    
    if os.path.exists(path):
        try:
            with open(path, "rb") as file:
                data = file.read()
                encoded = base64.b64encode(data).decode()
                # Guess mime type based on extension
                ext = path.split('.')[-1].lower()
                mime_type = "image/png" if ext == "png" else "image/jpeg"
                return f"data:{mime_type};base64,{encoded}"
        except Exception as e:
            st.error(f"Error loading image: {e}")
            return "https://placehold.co/800x600/1f2833/66fcf1?text=Image+Error"
            
    # Return placeholder if file not found
    return "https://placehold.co/400x400/1f2833/66fcf1?text=Profile+Image"

def load_pdf(file_path):
    """
    Reads a local PDF file and returns the binary data for the download button.
    Returns None if file not found to prevent errors.
    """
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return f.read()
    return None

# --- DATA: STRUCTURED & MINIMALIST ---
PROFILE = {
    "name": "Muhammad Muzammil",
    "title": "Data Scientist & ML Engineer",
    "tagline": "Turning Entropy into ROI.",
    "image": r"Assets/Profile image/Muzammil.jpg", 
    "resume_path": "D:/Muzammil/PROJECT/Portfolio/Muzammil_Resume.pdf",
    "about": "I don't just train models; I deploy scalable intelligence. Specializing in high-performance predictive engines and explainable AI for FinTech and Healthcare sectors.",
    "socials": {
        "LinkedIn": "https://www.linkedin.com/in/muhammad-muzammil444",
        "GitHub": "https://www.github.com/Muzammil444",
        "Email": "mailto:muzamilshahid444@gmail.com"
    }
}

PROJECTS = [
    {
        "id": 1,
        "title": "AI Symptom Detection & Triage",
        "client": "HealthTech / Telemedicine",
        "stack": ["XGBoost", "SHAP", "Scikit-Learn", "Streamlit"],
        "metric": "98% Accuracy",
        "desc": "Developed a clinical diagnostic engine predicting 41 diseases from 132+ distinct symptoms. Unlike standard black-box classifiers, this system utilizes SHAP waterfall plots to visualize *why* a diagnosis was made (e.g., 'Yellowing Skin + High Fever → Hepatitis'). Integrated with a precaution mapping system to suggest immediate medical actions.",
        "type": "Classification / Healthcare",
        "github": "https://github.com/yourusername/symptom-checker",
        "gallery": [
            "Assets/AI Symptom Detection/symptom detection 1.png",
            "Assets/AI Symptom Detection/symptom 2.png"
        ]
    },
    {
        "id": 2,
        "title": "Loan Approval Prediction System",
        "client": "FinTech / Compliance",
        "stack": ["XGBoost", "SHAP", "SMOTE", "Scikit-Learn"],
        "metric": "95% Accuracy",
        "desc": "Advanced credit risk assessment system using explainable AI techniques. The model handles class imbalance with SMOTE and provides SHAP-based explanations for loan approval decisions, ensuring regulatory compliance and transparency in lending decisions.",
        "type": "Regression / XAI",
        "github": "https://github.com/yourusername/loan-approval-project",
        "gallery": [
            "Assets/Loan Approval/Loan Approval 1.png",
            "Assets/Loan Approval/loan approval 2.png"
        ]
    },
    {
        "id": 3,
        "title": "Stock Management & Recommendation Engine",
        "client": "Retail Analytics / E-Commerce",
        "stack": ["StatsForecast", "MLxtend", "Scikit-Learn", "Streamlit"],
        "metric": "$250k/yr Revenue Boost",
        "desc": "A comprehensive retail analytics powerhouse combining AI-powered sales forecasting, market basket analysis, and customer segmentation. The system uses AutoARIMA for demand prediction, Apriori algorithm for product bundling insights, and K-Means clustering for customer profiling. Features real-time KPI dashboards, stock optimization algorithms, and actionable business intelligence that directly impacts bottom-line performance.",
        "type": "Retail Analytics / Forecasting",
        "github": "https://github.com/yourusername/retail-analytics-system",
        "gallery": [
            "Assets/Stock Management and Recommendation/1.png",
            "Assets/Stock Management and Recommendation/2.png",
            "Assets/Stock Management and Recommendation/3.png",
            "Assets/Stock Management and Recommendation/4.png"
        ]
    },
    {
        "id": 4,
        "title": "CLIP-Powered Fake News Detection",
        "client": "MediaTech / Content Moderation",
        "stack": ["OpenAI CLIP", "Scikit-Learn", "MLPClassifier", "Streamlit"],
        "metric": "94.2% Detection Rate",
        "desc": "Advanced misinformation detection system using OpenAI's CLIP vision-language model for semantic text analysis. Trained on 72K+ news samples, the system extracts rich 768-dimensional embeddings to understand linguistic nuance and contextual patterns that traditional methods miss. Features offline operation, GPU acceleration, and real-time verification through an intuitive web interface.",
        "type": "NLP / Classification",
        "github": "https://github.com/yourusername/fake-news-detector",
        "gallery": [
            "Assets/Fake News Prediction/1.png",
            "Assets/Fake News Prediction/2.png",
            "Assets/Fake News Prediction/3.png",
            "Assets/Fake News Prediction/4.png"
        ]
    }
]

EXPERIENCE = [
    {"role": "Data Science Freelancer", "company": "Global Clients", "year": "2024 - Present", "impact": "Delivered 15+ End-to-End ML pipelines."},
    {"role": "ML Researcher", "company": "University of Central Punjab", "year": "2023 - 2024", "impact": "Published paper on transformer efficiency."},
]

TESTIMONIALS = [
    {
        "quote": "Muzammil's model didn't just work; it saved us six figures in the first quarter. His understanding of business context is rare.",
        "author": "CTO, FinTech Corp"
    },
    {
        "quote": "Fast, clean code, and highly communicative. The deployment to our edge devices was seamless.",
        "author": "Product Lead, AutoMfgr"
    }
]

# --- SESSION STATE MANAGEMENT ---
if 'view' not in st.session_state:
    st.session_state.view = 'portfolio'
if 'selected_id' not in st.session_state:
    st.session_state.selected_id = None

def view_project(p_id):
    st.session_state.view = 'detail'
    st.session_state.selected_id = p_id

def go_home():
    st.session_state.view = 'portfolio'
    st.session_state.selected_id = None

# --- UI COMPONENTS ---

def draw_hero():
    col1, col2 = st.columns([1.5, 1], gap="large")
    with col1:
        st.markdown('<div class="hero-container">', unsafe_allow_html=True)

        # Mobile-only profile image (hidden on desktop; shown on small screens)
        image_src_mobile = load_image(PROFILE['image'])
        st.markdown(f'<div style="text-align:center;"><img src="{image_src_mobile}" class="profile-img-mobile magnetic-element"></div>', unsafe_allow_html=True)

        st.markdown(f'<div class="big-title">{PROFILE["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="subtitle">{PROFILE["title"]}</div>', unsafe_allow_html=True)

        # Enhanced about section with typing effect
        st.markdown(f"""
        <div style="font-size: 1.1rem; line-height: 1.6; color: var(--text); margin-bottom: 2rem;">
            {PROFILE['about']}
        </div>
        """, unsafe_allow_html=True)

        # Skills section with progress bars
        st.markdown("### Core Competencies")
        skills = {
            "Machine Learning": 95,
            "Data Engineering": 90,
            "Computer Vision": 85,
            "NLP & Text Analytics": 88,
            "Business Intelligence": 92
        }

        for skill, level in skills.items():
            # Inject CSS separately to ensure no indentation issues
            # Using st.markdown with unsafe_allow_html=True for the style block
            # No indentation at all inside the style block to be 100% safe
            st.markdown(f"""
<style>
@keyframes progressAnimation-{level} {{
    from {{ width: 0%; }}
    to {{ width: {level}%; }}
}}
</style>
""", unsafe_allow_html=True)

            # Inject the HTML structure
            st.markdown(textwrap.dedent(f"""
            <div style="margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 600; color: var(--text);">{skill}</span>
                    <span style="color: var(--accent); font-weight: 600;">{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill" style="animation: progressAnimation-{level} 2s ease-in-out forwards;"></div>
                </div>
            </div>
            """), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Enhanced buttons and socials
        c_resume, c_social = st.columns([1, 2])
        with c_resume:
            pdf_data = load_pdf(PROFILE["resume_path"])
            if pdf_data:
                st.markdown('<div class="glow-button">', unsafe_allow_html=True)
                st.download_button(
                    label="📄 Download CV",
                    data=pdf_data,
                    file_name="Muzammil_Resume.pdf",
                    mime="application/pdf"
                )
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.button("📄 CV Not Found", disabled=True)

        with c_social:
            # Build social links with proper escaping
            social_links = []
            for platform, link in PROFILE['socials'].items():
                social_links.append(f'<a href="{link}" style="color:#66fcf1; text-decoration:none; font-weight:600; transition: all 0.3s ease;" onmouseover="this.style.color=\'#45a29e\'; this.style.transform=\'scale(1.1)\';" onmouseout="this.style.color=\'#66fcf1\'; this.style.transform=\'scale(1)\';">{platform} ↗</a>')
            social_html = ' &nbsp; • &nbsp; '.join(social_links)

            st.markdown(f"""
            <div style="padding-top:10px;">
                {social_html}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        image_src = load_image(PROFILE['image'])
        st.markdown(f"""
        <div class="profile-img-container">
            <img src="{image_src}" class="profile-img magnetic-element" style="cursor: pointer;">
        </div>
        """, unsafe_allow_html=True)

        categories = ['Modelling', 'Data Eng', 'Visualization', 'Business Strategy', 'Math/Stats']
        r = [5, 4, 4, 3, 5]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=r,
            theta=categories,
            fill='toself',
            name='Skills',
            line_color='#66fcf1',
            fillcolor='rgba(102, 252, 241, 0.2)'
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 5], showticklabels=False, linecolor='#333'),
                angularaxis=dict(tickfont=dict(color='#c5c6c7', size=10)),
                bgcolor='rgba(0,0,0,0)'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            margin=dict(l=40, r=40, t=10, b=40),
            height=300
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def draw_project_grid():
    st.markdown("### Featured Projects")
    st.markdown("---")

    # Filter options
    col_filter, col_empty = st.columns([3, 1])
    with col_filter:
        project_types = list(set([p['type'].split(' / ')[0] for p in PROJECTS]))
        selected_type = st.selectbox(
            "Filter by Category:",
            ["All"] + project_types,
            help="Filter projects by their primary technology category"
        )

    # Filter projects based on selection
    filtered_projects = PROJECTS if selected_type == "All" else [
        p for p in PROJECTS if p['type'].startswith(selected_type)
    ]

    if not filtered_projects:
        st.info("No projects found in this category. Try selecting 'All' to see all projects.")
        filtered_projects = PROJECTS

    rows = [filtered_projects[i:i+2] for i in range(0, len(filtered_projects), 2)]

    for row in rows:
        cols = st.columns(2)
        for idx, proj in enumerate(row):
            with cols[idx]:
                # Build tech badges safely
                tech_badges = []
                for tech in proj['stack'][:3]:
                    # Escape any special characters in tech name
                    safe_tech = str(tech).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                    badge_html = (
                        f'<span style="background: rgba(102, 252, 241, 0.1); '
                        f'color: #66fcf1; padding: 2px 8px; border-radius: 10px; '
                        f'font-size: 0.7rem; font-weight: 500;">{safe_tech}</span>'
                    )
                    tech_badges.append(badge_html)

                tech_badges_html = "".join(tech_badges)

                # Construct enhanced card HTML safely
                card_html = f"""
                <div class="project-card magnetic-element" onclick="this.style.transform='scale(0.98)'; setTimeout(() => this.style.transform='', 150)">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom: 16px;">
                        <span class="metric-pill">{proj['metric']}</span>
                        <div style="text-align: right;">
                            <span style="font-size:0.75rem; opacity:0.7; display: block;">{proj['type']}</span>
                            <span style="font-size:0.7rem; opacity:0.5; display: block;">{proj['client']}</span>
                        </div>
                    </div>
                    <h3 style="margin: 0 0 12px 0; font-size: 1.3rem; line-height: 1.3; color: var(--text-highlight);">{proj['title']}</h3>
                    <p style="font-size:0.9rem; color:#a0a0a0; margin: 0 0 16px 0; line-height: 1.5;">{proj['desc'][:120]}...</p>

                    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px;">
                        {tech_badges_html}
                    </div>

                    <!-- Subtle shine effect -->
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent 0%, var(--accent) 50%, transparent 100%); opacity: 0.3;"></div>
                </div>
                """

                st.html(card_html)

                # Buttons below card
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button(f"View Details", key=f"btn_{proj['id']}", help=f"Learn more about {proj['title']}"):
                        view_project(proj['id'])
                        st.rerun()

                with col_btn2:
                    if "github" in proj and proj["github"] != "#":
                        github_html = f"""
                        <a href='{proj['github']}' target='_blank' style='text-decoration: none;'>
                            <button style='width: 100%; background: rgba(102, 252, 241, 0.1); border: 1px solid rgba(102, 252, 241, 0.3); color: #66fcf1; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease;' onmouseover='this.style.background=\"rgba(102, 252, 241, 0.2)\"; this.style.borderColor=\"#66fcf1\";' onmouseout='this.style.background=\"rgba(102, 252, 241, 0.1)\"; this.style.borderColor=\"rgba(102, 252, 241, 0.3)\";'>Code ↗</button>
                        </a>
                        """
                        st.html(github_html)
                    else:
                        st.button("Demo", key=f"demo_{proj['id']}", disabled=True, help="Demo not available")

def draw_detail_view():
    proj = next(p for p in PROJECTS if p['id'] == st.session_state.selected_id)
    # Ensure the page is scrolled to top when opening the detail view
    try:
        components.html("""<script>window.scrollTo({top:0,left:0,behavior:'auto'});</script>""", height=1)
    except Exception:
        # Fallback: no-op if components rendering fails in older Streamlit versions
        pass
    
    # Back and Source Code Buttons
    c_btn1, c_btn2, c_spacer = st.columns([1, 1, 4])
    with c_btn1:
        if st.button("← Back"):
            go_home()
            st.rerun()
    with c_btn2:
        if "github" in proj and proj["github"] != "#":
            st.markdown(f"<a href='{proj['github']}' target='_blank'><button style='background:rgba(102, 252, 241, 0.1); color:#66fcf1; border:1px solid #66fcf1; border-radius:6px; font-weight:600; padding:6px 12px; cursor:pointer; width:100%;'>View Code ↗</button></a>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown(f"<h1 style='font-size:3.5rem;'>{proj['title']}</h1>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#66fcf1; font-size:1.2rem; font-family:Space Grotesk;'>{proj['client']}</span>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div style="text-align:right; border-left:2px solid #66fcf1; padding-left:20px;">
            <div style="font-size:2.5rem; font-weight:bold; color:#fff;">{proj['metric'].split(' ')[0]}</div>
            <div style="color:#aaa;">{ ' '.join(proj['metric'].split(' ')[1:]) }</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    col_desc, col_stack = st.columns([2, 1], gap="large")
    
    with col_desc:
        st.markdown("### The Problem & Solution")
        st.write(proj['desc'])
        
        if 'gallery' in proj:
            st.markdown("<br>### Visual Evidence", unsafe_allow_html=True)
            for img_path in proj['gallery']:
                img_src = load_image(img_path)
                img_html = f"""
                <div style="border-radius:12px; overflow:hidden; border:1px solid rgba(102, 252, 241, 0.2); margin-bottom:20px;">
                    <img src="{img_src}" style="width:100%; display:block; transition: transform 0.3s ease;">
                </div>
                """
                st.html(img_html)

    with col_stack:
        st.markdown("### Technology Stack")
        for tool in proj['stack']:
            tool_html = f"""
            <div style="background:rgba(255,255,255,0.05); padding:10px; margin-bottom:8px; border-radius:5px; border-left:3px solid #66fcf1;">
                {tool}
            </div>
            """
            st.html(tool_html)
        
        # Performance graph removed (identical across projects)


def draw_timeline():
    st.markdown("### Journey")
    st.markdown("---")
    for role in EXPERIENCE:
        col_date, col_info = st.columns([1, 4])
        with col_date:
            st.markdown(f"<div style='color:#66fcf1; font-weight:bold; margin-top:5px;'>{role['year']}</div>", unsafe_allow_html=True)
        with col_info:
            st.markdown(f"<div style='font-size:1.1rem; font-weight:bold; color:#fff;'>{role['role']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:0.9rem; color:#aaa; margin-bottom:5px;'>{role['company']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:0.9rem; color:#c5c6c7; font-style:italic;'>{role['impact']}</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

def draw_testimonials():
    st.markdown("### What People Say")
    st.markdown("---")
    
    cols = st.columns(2)
    for idx, item in enumerate(TESTIMONIALS):
        with cols[idx]:
            st.markdown(f"""
            <div class="testimonial-card">
                <div style="font-size:1.1rem; color:#fff; font-style:italic;">"{item['quote']}"</div>
                <div style="margin-top:10px; color:#66fcf1; font-weight:bold;">— {item['author']}</div>
            </div>
            """, unsafe_allow_html=True)

def draw_contact():
    st.markdown("### Let's Work Together")
    st.markdown("---")
    
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.write("Ready to transform your data strategy? Fill out the form or reach out directly via email.")
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Project Details")
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                st.error("Form unavailable right now!. Please contact via email.")
    
    with c2:
        st.markdown(f"""
        <div style="background:rgba(31,40,51,0.5); padding:30px; border-radius:12px; text-align:center;">
            <h4>Prefer Email?</h4>
            <p>I typically respond within 24 hours.</p>
            <br>
            <a href="{PROFILE['socials']['Email']}" style="background:#66fcf1; color:#0b0c10; padding:12px 24px; border-radius:6px; text-decoration:none; font-weight:bold;">Send Email ✉</a>
        </div>
        """, unsafe_allow_html=True)

# --- MAIN RENDER LOGIC ---

if st.session_state.view == 'portfolio':
    draw_hero()
    st.markdown("<br><br>", unsafe_allow_html=True)
    draw_project_grid()
    st.markdown("<br><br>", unsafe_allow_html=True)
    draw_timeline()
    st.markdown("<br><br>", unsafe_allow_html=True)
    draw_testimonials()
    st.markdown("<br><br>", unsafe_allow_html=True)
    draw_contact()
    
    # Enhanced Footer with interactive elements
    st.markdown(textwrap.dedent("""
    <br><hr>
    <div style="text-align: center; padding: 2rem 0; position: relative;">
        <div style="margin-bottom: 1rem;">
            <span style="color: var(--accent); font-size: 1.2rem; font-weight: 600;">🚀</span>
            <span style="color: var(--text); font-size: 0.9rem; margin-left: 8px;">Built with Streamlit & Advanced CSS</span>
        </div>
        <div style="color: var(--text-muted); font-size: 0.8rem; line-height: 1.6;">
            <p>Transforming complex data challenges into elegant, scalable solutions.</p>
            <p style="margin-top: 8px;">
                <span style="color: var(--accent);">✨</span> Last updated: January 2026
                <span style="margin: 0 12px;">•</span>
                <span style="color: var(--accent);">🎯</span> Open to new opportunities
            </p>
        </div>
        <div style="margin-top: 1rem;">
            <button onclick="document.body.scrollTop = 0; document.documentElement.scrollTop = 0;"
                    style="background: rgba(102, 252, 241, 0.1); border: 1px solid rgba(102, 252, 241, 0.3); color: var(--accent); padding: 8px 16px; border-radius: 20px; font-size: 0.8rem; cursor: pointer; transition: all 0.3s ease;"
                    onmouseover="this.style.background='rgba(102, 252, 241, 0.2)'; this.style.transform='translateY(-2px)';"
                    onmouseout="this.style.background='rgba(102, 252, 241, 0.1)'; this.style.transform='translateY(0)';">
                ↑ Back to Top
            </button>
        </div>
    </div>
    """), unsafe_allow_html=True)

elif st.session_state.view == 'detail':
    draw_detail_view()
