import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import base64
import os

# --- CONFIGURATION & ASSETS ---
st.set_page_config(
    page_title="Muzammil | Data Science",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed" # Collapsed for a cleaner initial look
)

# --- DATA: STRUCTURED & MINIMALIST ---
PROFILE = {
    "name": "Muzammil",
    "title": "Data Scientist & ML Engineer",
    "tagline": "Turning Entropy into ROI.",
    # UPDATE THIS PATH: Use forward slashes (/) even on Windows. 
    # Example: "C:/Users/Muzammil/Downloads/profile.jpg" or "./assets/me.png"
    "image": "Images\Muzammil.jpg", 
    "about": "I don't just train models; I deploy scalable intelligence. Specializing in high-performance predictive engines and explainable AI for FinTech and Healthcare sectors.",
    "socials": {
        "LinkedIn": "https://linkedin.com",
        "GitHub": "https://github.com",
        "Email": "mailto:email@example.com"
    }
}

PROJECTS = [
    {
        "id": 1,
        "title": "XAI Loan Approval",
        "client": "FinTech Corp",
        "stack": ["XGBoost", "SHAP", "Docker"],
        "metric": "15% ↓ Default Rate",
        "desc": "Black-box credit scoring is a compliance nightmare. I built a transparent boosting model integrated with SHAP values, allowing loan officers to explain rejections in plain English while maintaining 0.95 AUC.",
        "type": "Regression / XAI"
    },
    {
        "id": 2,
        "title": "Medi-NLP Triage",
        "client": "HealthPlus",
        "stack": ["Transformers", "FastAPI"],
        "metric": "200ms Inference",
        "desc": "Replaced manual triage with a BERT-based symptom classifier. Handles 50k+ daily queries, routing patients to specialists with 92% Top-3 accuracy.",
        "type": "NLP / Deploy"
    },
    {
        "id": 3,
        "title": "Inventory Prophet",
        "client": "Retail Giant",
        "stack": ["Prophet", "Snowflake"],
        "metric": "$95k/yr Saved",
        "desc": "Hybrid LSTM-Prophet pipeline detecting seasonal anomalies. Directly integrated into Snowflake warehouses for real-time dashboarding.",
        "type": "Time-Series"
    },
    {
        "id": 4,
        "title": "VisionQC Edge",
        "client": "AutoMfgr",
        "stack": ["OpenCV", "TensorRT"],
        "metric": "99.1% Accuracy",
        "desc": "Deployed quantized CNNs to Jetson Nano devices for real-time assembly line defect detection. Reduced manual QA load by 80%.",
        "type": "Computer Vision"
    }
]

EXPERIENCE = [
    {"role": "Data Science Freelancer", "company": "Global Clients", "year": "2024 - Present", "impact": "Delivered 15+ End-to-End ML pipelines."},
    {"role": "ML Researcher", "company": "University of Central Punjab", "year": "2023 - 2024", "impact": "Published paper on transformer efficiency."},
]

# --- UTILITY: IMAGE LOADER ---
def get_profile_image(path):
    """
    Handles both web URLs and local file paths for the image.
    If it's a local file, it converts it to base64 so HTML can render it.
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
            return "https://placehold.co/400x400/1f2833/66fcf1?text=Error"
            
    return path # Return path as is if it doesn't exist (browser will show broken icon)

# --- CUSTOM CSS (THE "MILLION DOLLAR" POLISH) ---
st.markdown("""
<style>
    /* FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=Inter:wght@300;400;600&display=swap');

    /* GLOBAL VARIABLES */
    :root {
        --bg: #0b0c10;
        --card-bg: #1f2833;
        --accent: #66fcf1;
        --text: #c5c6c7;
        --text-highlight: #ffffff;
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

    /* HERO SECTION STYLING */
    .hero-container {
        padding: 4rem 0 2rem 0;
        animation: fadeIn 1s ease-in;
    }
    .big-title {
        font-size: 4.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #ffffff, #66fcf1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #45a29e;
        margin-bottom: 2rem;
    }

    /* DYNAMIC PROFILE IMAGE */
    .profile-img-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
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
    
    @keyframes morph {
        0% {border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;}
        50% {border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;}
        100% {border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;}
    }

    /* BENTO BOX CARD DESIGN */
    div[data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlock"] {
        gap: 1rem;
    }
    
    .project-card {
        background: rgba(31, 40, 51, 0.6);
        border: 1px solid rgba(102, 252, 241, 0.1);
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        height: 100%;
        backdrop-filter: blur(10px);
    }
    .project-card:hover {
        transform: translateY(-5px);
        border-color: var(--accent);
        box-shadow: 0 10px 30px -10px rgba(102, 252, 241, 0.2);
    }
    
    /* METRIC HIGHLIGHT */
    .metric-pill {
        display: inline-block;
        background: rgba(102, 252, 241, 0.1);
        color: var(--accent);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 10px;
        border: 1px solid rgba(102, 252, 241, 0.2);
    }

    /* BUTTONS OVERRIDE */
    .stButton > button {
        background: transparent;
        border: 1px solid var(--accent);
        color: var(--accent);
        border-radius: 6px;
        font-weight: 600;
        transition: 0.3s;
        width: 100%;
    }
    .stButton > button:hover {
        background: var(--accent);
        color: #0b0c10;
        box-shadow: 0 0 15px rgba(102, 252, 241, 0.5);
    }

    /* ANIMATIONS */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    /* MOBILE TWEAKS */
    @media (max-width: 768px) {
        .big-title { font-size: 2.5rem; }
    }
</style>
""", unsafe_allow_html=True)

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
        st.markdown(f'<div class="big-title">{PROFILE["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="subtitle">{PROFILE["title"]}</div>', unsafe_allow_html=True)
        st.write(PROFILE['about'])
        
        # Social Row
        st.markdown("<br>", unsafe_allow_html=True)
        s_cols = st.columns(len(PROFILE['socials']) + 2)
        for i, (platform, link) in enumerate(PROFILE['socials'].items()):
            with s_cols[i]:
                st.markdown(f"<a href='{link}' style='color:#66fcf1; text-decoration:none; font-weight:600;'>{platform} ↗</a>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # 1. DYNAMIC PROFILE IMAGE (Safe Loading)
        image_src = get_profile_image(PROFILE['image'])
        st.markdown(f"""
        <div class="profile-img-container">
            <img src="{image_src}" class="profile-img">
        </div>
        """, unsafe_allow_html=True)

        # 2. DATA SCIENTIST "SIGNATURE" - THE RADAR CHART
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
            margin=dict(l=40, r=40, t=10, b=40), # Adjusted top margin since image is above
            height=300 # Slightly shorter to fit image
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def draw_project_grid():
    st.markdown("### Select Work")
    st.markdown("---")
    
    # Grid Logic (2 columns per row)
    rows = [PROJECTS[i:i+2] for i in range(0, len(PROJECTS), 2)]
    
    for row in rows:
        cols = st.columns(2)
        for idx, proj in enumerate(row):
            with cols[idx]:
                # CSS Card Container
                st.markdown(f"""
                <div class="project-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="metric-pill">{proj['metric']}</span>
                        <span style="font-size:0.8rem; opacity:0.7;">{proj['type']}</span>
                    </div>
                    <h3 style="margin-top:10px;">{proj['title']}</h3>
                    <p style="font-size:0.9rem; color:#a0a0a0; margin-bottom:15px;">{proj['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Invisible Interaction Layer
                if st.button(f"View Case Study", key=f"btn_{proj['id']}"):
                    view_project(proj['id'])
                    st.rerun()

def draw_detail_view():
    proj = next(p for p in PROJECTS if p['id'] == st.session_state.selected_id)
    
    if st.button("← Back to Dashboard"):
        go_home()
        st.rerun()
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Title Section
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
    
    # Content Grid
    col_desc, col_stack = st.columns([2, 1], gap="large")
    
    with col_desc:
        st.markdown("### The Problem & Solution")
        st.write(proj['desc'])
        st.info("Additional technical documentation, architectural diagrams, and code snippets would be displayed here in a real deployment, demonstrating the depth of the engineering process.")
        
        # Mock Graph for Visual Interest
        st.markdown("### Performance Analysis")
        x = list(range(10))
        y = [i**2 for i in x]
        fig_mock = go.Figure(data=go.Scatter(x=x, y=y, line=dict(color='#66fcf1', width=3)))
        fig_mock.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(31,40,51,0.5)', font=dict(color='#ccc'), height=250, margin=dict(l=0,r=0,t=0,b=0))
        st.plotly_chart(fig_mock, use_container_width=True)

    with col_stack:
        st.markdown("### Technology Stack")
        for tool in proj['stack']:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.05); padding:10px; margin-bottom:8px; border-radius:5px; border-left:3px solid #66fcf1;">
                {tool}
            </div>
            """, unsafe_allow_html=True)

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

# --- MAIN RENDER LOGIC ---

if st.session_state.view == 'portfolio':
    draw_hero()
    st.markdown("<br><br>", unsafe_allow_html=True)
    draw_project_grid()
    st.markdown("<br><br>", unsafe_allow_html=True)
    draw_timeline()
    
    # Footer
    st.markdown("<br><hr><center style='color:#555; font-size:0.8rem;'>Designed by Artificial Intelligence for Human Impact.</center>", unsafe_allow_html=True)

elif st.session_state.view == 'detail':
    draw_detail_view()

