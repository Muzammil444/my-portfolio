import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for navigation and theming
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = None
if 'theme' not in st.session_state:
    # Default to 'light' mode
    st.session_state.theme = 'light' 

# --- Theme Toggle Function ---
def toggle_theme():
    """Switches the theme between light and dark."""
    # Modifying session state is enough to trigger a rerun automatically
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'

# --- Helper Function for Project Detail View ---

def render_project_detail(project):
    """Renders the detailed view of a selected project."""
    
    if st.button("⬅ Back to Projects List", key="back_btn_top"):
        st.session_state.selected_project = None

    st.markdown(f'<h1 style="color: var(--primary-color); font-size: 2rem; margin-top: 1rem;">{project["title"]} - Deep Dive</h1>', unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)
    
    st.subheader("Project Summary")
    st.info(project["description"])
    
    st.subheader("Key Performance Metrics")

    col_acc, col_roi, col_cred = st.columns(3)

    with col_acc:
        st.metric(label="Primary Metric", value=project.get("accuracy", "N/A"), delta="High Confidence")
    with col_roi:
        st.metric(label="Business Impact", value=project.get("roi", "N/A"), delta="+20%", delta_color="normal")
    with col_cred:
        st.metric(label="Credibility Score", value=f"{project.get('credibility_score', 'N/A')}/10", delta="Audit Ready")

    st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)

    st.subheader("Key Technologies & Stack")
    st.code(', '.join(project['technologies']), language='text')

    st.subheader("Analysis & Outcome")
    st.markdown(f"""
    This was a full-cycle project focusing on **{project['category']}**. 
    
    The implementation involved advanced data preprocessing, model selection (like XGboost or deep neural network ensembles), and **Explainable AI (XAI)** techniques like SHAP to ensure the decisions are transparent and trustworthy.
    
    #### Detailed Business Impact:
    * **Model Performance:** Achieved a definitive **{project.get('accuracy', 'AUPRC of 0.92')}** (as shown above) in a complex dataset.
    * **Budget/Resource Estimate:** Estimated cost of \$5,000 for cloud compute and development time.
    * **Impact Realized:** The project is currently yielding an estimated **{project.get('roi', '$100,000 annually')}** in savings/optimization, leading to high customer satisfaction and compliance.
    """)

    st.subheader("Visualizations & Screenshots")
    st.write("Below are key visualizations and snapshots from the project and dashboard. **(Remember to update these placeholder image URLs with your actual image paths!)**")
    
    placeholder_base = "https://placehold.co/800x400/2ecc71/fff?text="
    
    if "Loan Approval" in project['title']:
        # Corresponds to screenshots 202733, 202946/202843, and output.png
        st.image(placeholder_base + "App+Screenshot+1%3A+Input+Form+and+Sliders", 
                  caption="Screenshot 1: Applicant Input Form and Data Sliders", use_container_width=True)
        st.image(placeholder_base + "App+Screenshot+2%3A+Decision+with+XAI+Reasons", 
                  caption="Screenshot 2: Approved/Rejected Decision and Human-Readable XAI Reasons", use_container_width=True)
        st.image(placeholder_base + "EDA+Boxplots%3A+Feature+Distribution+vs+Default", 
                  caption="Screenshot 3: Exploratory Data Analysis (EDA) Boxplots", use_container_width=True)
        
    elif "Symptom Checker" in project['title']:
        # Corresponds to screenshots 203807 and 203930
        st.image(placeholder_base + "App+Screenshot+1%3A+Symptom+Input+Interface", 
                  caption="Screenshot 1: Symptom Input Interface (Initial State)", use_container_width=True)
        st.image(placeholder_base + "App+Screenshot+2%3A+Diagnosis%2C+Confidence%2C+and+XAI+Symptoms", 
                  caption="Screenshot 2: Predicted Condition, Confidence Score, and Key Influential Symptoms", use_container_width=True)
    else:
        # Default placeholders for other projects
        st.image(placeholder_base + f"{project['title']}+:+Feature+Importance", 
              caption="Screenshot A: Feature Importance Analysis", use_container_width=True)
        st.image(placeholder_base + f"{project['title']}+:+Model+Evaluation+Dashboard", 
                  caption="Screenshot B: Live Model Performance Dashboard", use_container_width=True)


    st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)

    st.subheader("Source & Demo")
    col_git, col_demo = st.columns(2) 
    with col_git:
        st.markdown(f"**🐙 [GitHub Repository]({project['github']})**", unsafe_allow_html=True)
    with col_demo:
        st.markdown(f"**🚀 [Live Demo / Application Link]({project['demo']})**", unsafe_allow_html=True)

    st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)
    
    if st.button("Back to Projects List", key="back_btn_bottom"):
        st.session_state.selected_project = None


# --- Main Application Code ---

# Set page configuration
st.set_page_config(
    page_title="Muhammad Muzammil | Data Scientist Portfolio",
    page_icon="📊",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Define CSS Variables based on the current theme
if st.session_state.theme == 'light':
    # Light Mode Colors
    bg_main = '#ffffff'
    bg_secondary = '#f0f2f6'
    text_color = '#262730'
    text_color_faded = '#6c757d'
    primary_color = '#4CAF50'
    mode_icon = '🌙'
    mode_text = 'Dark Mode'
    header_bg = '#e0e2e6' # Slightly different shade for header/sidebar
else:
    # Dark Mode Colors
    bg_main = '#0e1117'
    bg_secondary = '#262730'
    text_color = '#fafafa'
    text_color_faded = '#a0a0a0'
    primary_color = '#4CAF50' # Keeping primary green constant for recognition
    mode_icon = '☀️'
    mode_text = 'Light Mode'
    header_bg = '#1a1d23' # Slightly different shade for header/sidebar


# Custom CSS for styling and dynamic theme application
st.markdown(f"""
<style>
    /* Inject CSS variables for easy theme switching */
    :root {{
        --main-bg-color: {bg_main};
        --secondary-bg-color: {bg_secondary};
        --text-color: {text_color};
        --text-color-faded: {text_color_faded};
        --primary-color: {primary_color};
        --header-bg-color: {header_bg};
    }}

    /* Global Streamlit overrides using injected variables */
    .stApp {{
        background-color: var(--main-bg-color);
        color: var(--text-color);
    }}
    
    /* CRITICAL FIX: Target the Header Bar and Main Content Shell */
    header,
    .st-emotion-cache-1avcm0n {{ /* Target for the main content wrapper (may vary by Streamlit version) */
        background-color: var(--main-bg-color) !important;
    }}
    
    /* Target the persistent header bar (often an H-tag or specific Streamlit element) */
    header[data-testid="stHeader"] {{
        background-color: var(--header-bg-color) !important;
        border-bottom: 1px solid var(--text-color-faded);
    }}
    
    .stSidebar {{
        background-color: var(--secondary-bg-color);
    }}
    
    /* Ensure all text uses the correct color */
    .stText, h1, h2, h3, h4, h5, h6, label, p {{
        color: var(--text-color) !important;
    }}
    
    /* Overrides for specific Streamlit components */
    .stCodeBlock, .stTextInput, .stTextArea, .stSelectbox {{
        background-color: var(--secondary-bg-color) !important;
        border-color: var(--text-color-faded);
    }}
    
    /* Global Text and Header Styles */
    .main-header {{
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }}
    .section-header {{
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: var(--primary-color) !important;
    }}
    
    /* Project Card Style */
    .project-card {{
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid var(--primary-color);
        background-color: var(--secondary-bg-color);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    
    /* ENHANCED BUTTON STYLING (FOR ALL Streamlit Buttons) */
    .stButton>button {{
        background-color: var(--primary-color); 
        color: white !important; /* CRITICAL FIX: Added !important */
        border-radius: 12px; 
        font-weight: 700;
        padding: 0.75rem 1.5rem; 
        border: none;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
        transition: all 0.2s ease-in-out; 
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 0.5rem; 
        width: 100%; 
    }}

    @media (min-width: 600px) {{
        .stButton>button {{
            width: auto; 
            min-width: 250px; 
        }}
    }}

    .stButton>button:hover {{
        background-color: #45a049; 
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px); 
    }}
    
    /* Other sections */
    .experience-item {{
        margin-bottom: 1.5rem;
        padding: 1rem;
        border-left: 3px solid var(--primary-color);
        background-color: var(--main-bg-color); /* Use main background or secondary */
    }}
    .contact-form {{
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid var(--text-color-faded);
        background-color: var(--secondary-bg-color);
    }}
    .footer {{
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        color: var(--text-color-faded);
        border-top: 1px solid var(--text-color-faded);
    }}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Content ---
st.sidebar.title("Portfolio Navigation")

# Theme Toggle Button
st.sidebar.button(
    f"{mode_icon} {mode_text}", 
    on_click=toggle_theme, 
    use_container_width=True
)

page = st.sidebar.radio("Go to", ["Home", "Skills & Expertise", "Projects", "Experience", "Contact"])

# --- Content Sections ---

# Home/About Me Section
if page == "Home":
    st.markdown('<div class="main-header">Welcome to My Data Science Portfolio</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://placehold.co/250x250/4CAF50/fff?text=Your+Photo",
                  caption="Professional Photo", 
                  use_container_width=True
                 )
    
    with col2:
        st.header("Muhammad Muzammil")
        st.subheader("AI/ML Solutions for FinTech & Business Automation")
        
        st.markdown("""
        **About Me:**
        
        Passionate data scientist with expertise in machine learning, statistical analysis, and data visualization. 
        I transform complex data into actionable insights and build predictive models that drive business decisions.
        
        **Core Expertise:**
        - Explainable AI (XAI) and Model Interpretability
        - Financial Risk Modeling and Scoring
        - Natural Language Processing (NLP) for Diagnostics
        - Python, XGboost, SHAP, Streamlit, Pandas, Scikit-learn
        """)

        st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)
        st.subheader("Key Project Snapshots")
        
        placeholder_base = "https://placehold.co/600x300/2ecc71/fff?text=Project+Snapshot+" 
        
        st.image(placeholder_base + "XAI+Loan+Approval+Demo", caption="Explainable AI Loan Approval System", use_container_width=True)
        st.image(placeholder_base + "AI+Symptom+Checker+NLP", caption="AI Medical Symptom Checker (NLP Diagnosis)", use_container_width=True)
        st.image(placeholder_base + "Sales+Forecasting+Dashboard", caption="Sales Forecasting Model Dashboard", use_container_width=True)
        st.image(placeholder_base + "Image+Classification+System", caption="Image Classification System Overview", use_container_width=True)
        
        st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)
        
        st.info("👉 **Explore the full case studies, technical details, and performance metrics for all projects in the 'Projects' section!**")
        
        st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)
        
        st.markdown("**Connect with me:**")
        col_contact1, col_contact2, col_contact3 = st.columns(3)
        with col_contact1:
            st.markdown("🔗 [LinkedIn](https://linkedin.com)")
        with col_contact2:
            st.markdown("🐙 [GitHub](https://github.com)")
        with col_contact3:
            st.markdown("📧 [Email](mailto:your.email@example.com)")

# Skills & Expertise Section
elif page == "Skills & Expertise":
    st.markdown('<div class="section-header">Skills & Expertise</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="skill-category">', unsafe_allow_html=True)
    st.markdown('<div class="skill-header">Programming Languages</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2) 
    with col1:
        st.write("**Python**")
        st.progress(85)
    with col2:
        st.write("**C++**")
        st.progress(90)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="skill-category">', unsafe_allow_html=True)
    st.markdown('<div class="skill-header">Machine Learning & AI</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2) 
    with col1:
        st.write("**Scikit-learn**")
        st.progress(90)
        st.write("**TensorFlow/Keras**")
        st.progress(80)
        st.write("**PyTorch**")
        st.progress(70)
    with col2:
        st.write("**XGBoost**")
        st.progress(85)
        st.write("**SHAP / XAI**")
        st.progress(95) # High confidence on XAI based on project screenshots
        st.write("**NLP / Transformers**")
        st.progress(80)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="skill-category">', unsafe_allow_html=True)
    st.markdown('<div class="skill-header">Statistical & Analytical Proficiency</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2) 
    with col1:
        st.write("**A/B Testing & Causal Inference**")
        st.progress(80)
        st.write("**Bayesian Statistics**")
        st.progress(65)
    with col2:
        st.write("**Hypothesis Testing**")
        st.progress(90)
        st.write("**Data Modeling (ERD)**")
        st.progress(75)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="skill-category">', unsafe_allow_html=True)
    st.markdown('<div class="skill-header">Data Visualization</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2) 
    with col1:
        st.write("**Matplotlib**")
        st.progress(90)
        st.write("**Seaborn**")
        st.progress(85)
    with col2:
        st.write("**Plotly**")
        st.progress(80)
        st.write("**Streamlit**")
        st.progress(90)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="skill-category">', unsafe_allow_html=True)
    st.markdown('<div class="skill-header">Tools & Platforms</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2) 
    with col1:
        st.write("**Pandas / NumPy**")
        st.progress(95)
        st.write("**AWS**")
        st.progress(75)
    with col2:
        st.write("**Docker**")
        st.progress(65)
        st.write("**Git**")
        st.progress(85)
    st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
elif page == "Projects":

    projects = [
        {
            "title": "Explainable AI (XAI) Loan Approval System",
            "description": "Developed an Explainable AI (XAI) system for real-time loan approval/rejection. The tool uses a high-performance model (XGBoost) and SHAP values to provide human-readable reasons, risk estimation, and exportable reports.",
            "technologies": ["Python", "XGboost", "SHAP", "Streamlit", "Scikit-learn", "Docker"],
            "category": "FinTech / Explainable AI",
            "github": "https://github.com/loan-approval-xai",
            "demo": "https://demo.com/loan-xai",
            "accuracy": "AUC 0.95", 
            "roi": "15% Reduction in Default Rate", 
            "credibility_score": 10 
        },
        {
            "title": "AI Medical Symptom Checker (NLP Diagnosis)",
            "description": "Created a Natural Language Processing (NLP) tool to predict the most likely medical condition from user-input symptoms in plain English. Includes confidence scores and influential symptom analysis based on model interpretation.",
            "technologies": ["Python", "Transformers", "Streamlit", "NLP", "XAI", "HealthTech"],
            "category": "HealthTech / NLP",
            "github": "https://github.com/ai-symptom-checker",
            "demo": "https://demo.com/symptom-checker",
            "accuracy": "Top-3 Accuracy: 90%",
            "roi": "Faster Preliminary Screening",
            "credibility_score": 9
        },
        {
            "title": "Retail Sales Forecasting Model",
            "description": "Created a time series forecasting model using Prophet and TensorFlow to predict sales for retail business with high accuracy, optimizing inventory management and staffing.",
            "technologies": ["Python", "Prophet", "TensorFlow", "SQL", "Plotly"],
            "category": "Machine Learning",
            "github": "https://github.com/sales-forecasting",
            "demo": "https://demo.com/sales",
            "accuracy": "90.0%",
            "roi": "$95,000",
            "credibility_score": 9
        },
        {
            "title": "Image Classification System for Quality Control",
            "description": "Built a deep learning model for classifying images to automate quality control in manufacturing, significantly reducing manual inspection time and error rates.",
            "technologies": ["Python", "TensorFlow", "OpenCV", "Keras", "Azure"],
            "category": "Computer Vision",
            "github": "https://github.com/image-classifier",
            "demo": "https://demo.com/image",
            "accuracy": "94.8%",
            "roi": "$75,000",
            "credibility_score": 9
        }
    ]

    if st.session_state.selected_project:
        render_project_detail(st.session_state.selected_project)
        
    else:
        st.markdown('<div class="section-header">Projects Showcase</div>', unsafe_allow_html=True)
        
        project_filter = st.selectbox(
            "Filter by category:",
            ["All", "FinTech / Explainable AI", "HealthTech / NLP", "Machine Learning", "Computer Vision"]
        )
        
        if project_filter != "All":
            filtered_projects = [p for p in projects if p["category"] == project_filter]
        else:
            filtered_projects = projects
        
        for project in filtered_projects:
            with st.container():
                st.markdown(f"""
                <div class="project-card">
                    <h3>{project['title']} ({project['category']})</h3>
                    <p>{project['description']}</p>
                    <div style="margin-bottom: 0.5rem; font-size: 0.9rem;">
                        <strong style="color: var(--text-color);">Technologies:</strong> {', '.join(project['technologies'])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Modifying session state is enough; Streamlit reruns automatically
                if st.button(f"🔍 View Full Case Study", key=f"btn_view_details_{project['title']}"):
                    st.session_state.selected_project = project
                
                st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)


# Experience Section
elif page == "Experience":
    st.markdown('<div class="section-header">Experience & Education</div>', unsafe_allow_html=True)
    
    st.subheader("Work Experience")
    
    experiences = [
        {
            "title": "Freelance Data Scientist",
            "company": "Self-Employed",
            "period": "2024 - Present",
            "description": "Created 15+ machine learning solutions across finance, healthcare, and automation. Clients include startups and SMEs requiring predictive modeling, fraud detection, and document automation"
        },
        
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="experience-item">
            <h4>{exp['title']} - {exp['company']}</h4>
            <p><strong>{exp['period']}</strong></p>
            <p>{exp['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("Education")
    
    education = [
        {
            "degree": "B.S. in Data Science",
            "institution": "University Of Central Punjab",
            "year": "2024 - 2028"
        }
    ]
    
    for edu in education:
        st.markdown(f"""
        <div class="experience-item">
            <h4>{edu['degree']}</h4>
            <p><strong>{edu['institution']}</strong> - {edu['year']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("Certifications")
    
    certifications = [
        {"name": "Python Ka Chilla 2023",
         "issuer": "Codanics", 
         "year": "2023"}
        
    ]
    
    for cert in certifications:
        st.markdown(f"""
        <div class="experience-item">
            <h5>{cert['name']}</h5>
            <p><strong>{cert['issuer']}</strong> - {cert['year']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)
    st.download_button(
        label="📄 Download Resume",
        data="Sample Resume Content", 
        file_name="Your_Name_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# Contact Section
elif page == "Contact":
    st.markdown('<div class="section-header">Get In Touch</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="contact-form">', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message", height=150)
        
        submitted = st.form_submit_button("Send Message", use_container_width=True) 
        
        if submitted:
            if name and email and message:
                print(f"New message from {name} ({email}): {message}")
                st.success("Thank you for your message! I'll get back to you soon.")
            else:
                st.error("Please fill in all fields.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<hr style='border-top: 1px solid var(--text-color-faded);'>", unsafe_allow_html=True)
    st.subheader("Alternative Contact Methods")
    col1, col2, col3 = st.columns(3) 
    
    with col1:
        st.markdown("**Email**")
        st.write("your.email@example.com")
    
    with col2:
        st.markdown("**LinkedIn**")
        st.write("[Your LinkedIn Profile](https://linkedin.com)")
    
    with col3:
        st.markdown("**GitHub**")
        st.write("[Your GitHub Profile](https://github.com)")

# Footer
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.write(f"© {datetime.now().year} Muhammad Muzammil | Data Scientist Portfolio")
st.write("Built with Streamlit")
st.markdown('</div>', unsafe_allow_html=True)