"""
Fahmi Taib - AI Engineer Portfolio
Professional Portfolio with Apple Design Language
Showcasing 3 Years of AI/ML Experience
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import random
import hashlib
import time

# Import configuration
from config import PROFILE, SUMMARY, SKILLS, PROJECTS, EXPERIENCE, CERTIFICATIONS, DEMO_CONFIG, EDUCATION

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Fahmi Taib | AI Engineer Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# APPLE-INSPIRED CSS STYLING
# ============================================================================

st.markdown("""
<style>
    /* Import SF Pro Font Alternative */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Root variables - Apple Design System */
    :root {
        --apple-blue: #007AFF;
        --apple-green: #34C759;
        --apple-orange: #FF9500;
        --apple-red: #FF3B30;
        --apple-purple: #AF52DE;
        --apple-pink: #FF2D55;
        --apple-gray: #8E8E93;
        --apple-gray-2: #AEAEB2;
        --apple-gray-3: #C7C7CC;
        --apple-gray-4: #D1D1D6;
        --apple-gray-5: #E5E5EA;
        --apple-gray-6: #F2F2F7;
        --apple-black: #1D1D1F;
        --apple-white: #FFFFFF;
        --glass-bg: rgba(255, 255, 255, 0.72);
        --glass-border: rgba(255, 255, 255, 0.18);
        --shadow-light: 0 4px 30px rgba(0, 0, 0, 0.1);
        --shadow-medium: 0 8px 40px rgba(0, 0, 0, 0.12);
        --shadow-heavy: 0 20px 60px rgba(0, 0, 0, 0.15);
    }
    
    /* Reset and Base */
    .block-container {
        padding: 2rem 3rem !important;
        max-width: 1400px !important;
    }
    
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    
    #MainMenu, footer, .stDeployButton {
        display: none !important;
    }
    
    /* Typography */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-weight: 600;
        letter-spacing: -0.02em;
        color: var(--apple-black);
    }
    
    /* Background */
    .stApp {
        background: linear-gradient(180deg, #FAFAFA 0%, #F5F5F7 100%);
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        border-radius: 24px;
        padding: 4rem;
        margin-bottom: 2rem;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 60%;
        height: 200%;
        background: radial-gradient(ellipse, rgba(255,255,255,0.15) 0%, transparent 60%);
        transform: rotate(-15deg);
    }
    
    .hero-name {
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.03em;
    }
    
    .hero-title {
        font-size: 1.5rem;
        font-weight: 400;
        opacity: 0.9;
        margin: 0.5rem 0;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        opacity: 0.8;
        margin-top: 1rem;
    }
    
    /* Glass Card */
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid var(--glass-border);
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--shadow-light);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-medium);
    }
    
    /* Project Card */
    .project-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        height: 100%;
        box-shadow: var(--shadow-light);
        border: 1px solid var(--apple-gray-5);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }
    
    .project-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-heavy);
    }
    
    .project-icon {
        width: 60px;
        height: 60px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        margin-bottom: 1rem;
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: var(--apple-black);
        margin-bottom: 0.5rem;
    }
    
    .project-desc {
        font-size: 0.95rem;
        color: var(--apple-gray);
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    /* Tech Tag */
    .tech-tag {
        display: inline-block;
        padding: 4px 12px;
        background: var(--apple-gray-6);
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 500;
        color: var(--apple-gray);
        margin: 2px;
    }
    
    /* Skill Progress */
    .skill-bar {
        height: 8px;
        background: var(--apple-gray-5);
        border-radius: 4px;
        overflow: hidden;
        margin-top: 0.5rem;
    }
    
    .skill-fill {
        height: 100%;
        border-radius: 4px;
        transition: width 1s ease-out;
    }
    
    /* Stats Card */
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--apple-blue), var(--apple-purple));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: var(--apple-gray);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 0.5rem;
    }
    
    /* Section Title */
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: var(--apple-black);
        margin-bottom: 1.5rem;
        letter-spacing: -0.02em;
    }
    
    .section-subtitle {
        font-size: 1.1rem;
        color: var(--apple-gray);
        margin-bottom: 2rem;
    }
    
    /* Navigation Pills */
    .nav-pills {
        display: flex;
        gap: 0.5rem;
        padding: 0.5rem;
        background: var(--apple-gray-6);
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    
    .nav-pill {
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .nav-pill.active {
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Metric Card */
    .metric-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        border: 1px solid var(--apple-gray-5);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--apple-black);
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: var(--apple-gray);
        margin-top: 0.25rem;
    }
    
    /* Live Demo Badge */
    .live-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 12px;
        background: linear-gradient(135deg, var(--apple-green), #2FB344);
        color: white;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .live-dot {
        width: 8px;
        height: 8px;
        background: white;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Hide Streamlit elements */
    div[data-testid="stDecoration"] {
        display: none !important;
    }
    
    /* Custom Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: var(--apple-gray-6);
        padding: 6px;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: white !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--apple-blue), #0056CC);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 20px rgba(0,122,255,0.3);
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        border-radius: 12px;
        border-color: var(--apple-gray-4);
    }
    
    /* Dataframe */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA MASKING UTILITIES
# ============================================================================

def mask_name(name):
    """Mask personal names while keeping structure"""
    first_names = ["Alex", "Jordan", "Sam", "Casey", "Morgan", "Riley", "Quinn", "Avery", "Taylor", "Drew"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Wilson", "Lee"]
    hash_val = int(hashlib.md5(str(name).encode()).hexdigest()[:8], 16)
    return f"{first_names[hash_val % len(first_names)]} {last_names[(hash_val // 10) % len(last_names)]}"

def mask_bus_id(bus_id):
    """Mask bus IDs"""
    return f"BUS-{hashlib.md5(str(bus_id).encode()).hexdigest()[:6].upper()}"

def mask_route(route):
    """Mask route names"""
    prefixes = ["Route", "Line", "Express", "Metro"]
    hash_val = int(hashlib.md5(str(route).encode()).hexdigest()[:8], 16)
    return f"{prefixes[hash_val % len(prefixes)]}-{hash_val % 999:03d}"

def mask_user_id(user_id):
    """Generate random SAP user IDs"""
    prefixes = ["JSMITH", "MJONES", "ABROWN", "KWILSON", "RGARCIA", "TLEE", "DCHEN", "PKIM", "NWANG", "SZHOU"]
    return f"{random.choice(prefixes)}{random.randint(100, 999)}"

# ============================================================================
# SAMPLE DATA GENERATORS FOR DEMOS
# ============================================================================

def generate_anomaly_detection_data():
    """
    Generate sample IoT sensor data for anomaly detection demo - 10 months of data
    
    Model Architecture (Autoencoder):
    - Input: 51 engineered features (17 sensors × 3 features: trend, std, residual)
    - Encoder: 51 → 32 → 16 → 8 (latent space)
    - Decoder: 8 → 16 → 32 → 51
    - Activation: ReLU (encoder), Linear (decoder)
    - Loss: Mean Squared Error (MSE)
    - Training: 50 epochs, batch size 32
    
    Note: Idling state (RPM < 700) is filtered out for cleaner trend analysis
    """
    np.random.seed(42)
    # Generate 10 months of data (like the reference: 2024-11 to 2025-09)
    # Generate more points initially to account for filtering
    dates = pd.date_range(start='2024-11-01', end='2025-09-15', freq='4h')
    n_points = len(dates)
    
    # 17 IoT Sensors monitored
    sensor_names = [
        'Engine Temperature', 'Engine Load', 'Fuel Rate', 'Vibration X', 'Vibration Y', 
        'Vibration Z', 'Board Voltage', 'RPM', 'Oil Pressure', 'Coolant Temp',
        'Intake Air Temp', 'Exhaust Temp', 'Throttle Position', 'Battery Voltage',
        'Transmission Temp', 'Brake Pressure', 'Wheel Speed'
    ]
    
    # Generate base anomaly scores (reconstruction errors) with realistic patterns
    base_scores = np.random.exponential(0.15, n_points)
    
    # Add some periodic patterns and drift
    time_idx = np.arange(n_points)
    seasonal = 0.1 * np.sin(2 * np.pi * time_idx / (24 * 7))  # Weekly pattern
    base_scores = base_scores + seasonal + 0.1
    
    # Inject anomaly periods with maintenance type indicators
    # Period 1: Jan 2025 - Mechanical issues (vibration-related)
    jan_start = int(n_points * 0.25)
    jan_end = int(n_points * 0.35)
    for i in range(jan_start, jan_end):
        if random.random() > 0.7:
            base_scores[i] = random.uniform(1.0, 1.5)
    
    # Period 2: Feb-Mar 2025 - Engine Performance issues
    feb_start = int(n_points * 0.38)
    feb_end = int(n_points * 0.55)
    for i in range(feb_start, feb_end):
        if random.random() > 0.5:
            base_scores[i] = random.uniform(0.9, 2.5)
    spike_idx = int(n_points * 0.45)
    base_scores[spike_idx] = 3.75
    
    # Period 3: Mar-Apr 2025 - Electrical issues
    mar_start = int(n_points * 0.50)
    mar_end = int(n_points * 0.62)
    for i in range(mar_start, mar_end):
        if random.random() > 0.6:
            base_scores[i] = random.uniform(0.9, 2.2)
    
    # Quiet period: May-Jul 2025
    quiet_start = int(n_points * 0.65)
    quiet_end = int(n_points * 0.82)
    base_scores[quiet_start:quiet_end] = np.random.uniform(0.02, 0.15, quiet_end - quiet_start)
    
    # Period 4: Aug-Sep 2025 - Mixed issues
    aug_start = int(n_points * 0.85)
    for i in range(aug_start, n_points):
        if random.random() > 0.4:
            base_scores[i] = random.uniform(0.9, 2.0)
    
    base_scores[-1] = 1.2732
    base_scores = np.clip(base_scores, 0, 4)
    
    # Generate RPM with operating state simulation
    # Normal operating RPM: 800-2500, Idling: 400-700
    rpm_base = np.random.normal(1500, 300, n_points)
    # Add some idling periods (about 15% of data)
    idling_mask = np.random.random(n_points) < 0.15
    rpm_base[idling_mask] = np.random.uniform(400, 650, idling_mask.sum())
    rpm = rpm_base + base_scores * 200
    
    # Generate raw sensor data (17 sensors)
    data = {
        'timestamp': dates,
        'Anomaly Score': base_scores,
        'RPM': rpm,
    }
    
    # Add sensor readings with anomaly type signatures
    sensor_configs = {
        'Engine Temperature': (75, 8, 15),
        'Engine Load': (45, 15, 20),
        'Fuel Rate': (25, 5, 8),
        'Vibration X': (0.5, 0.2, 0.8),
        'Vibration Y': (0.4, 0.15, 0.6),
        'Vibration Z': (0.3, 0.1, 0.5),
        'Board Voltage': (26, 1.5, -2),
        'Oil Pressure': (45, 8, 10),
        'Coolant Temp': (85, 5, 12),
        'Intake Air Temp': (35, 8, 5),
        'Exhaust Temp': (450, 50, 80),
        'Throttle Position': (30, 15, 10),
        'Battery Voltage': (12.6, 0.3, -0.5),
        'Transmission Temp': (80, 10, 15),
        'Brake Pressure': (100, 20, 25),
        'Wheel Speed': (45, 15, 10),
    }
    
    for sensor, (mean, std, anomaly_factor) in sensor_configs.items():
        data[sensor] = mean + base_scores * anomaly_factor + np.random.normal(0, std, n_points)
    
    df = pd.DataFrame(data)
    
    # Filter out idling state (RPM < 700) for cleaner trend analysis
    df = df[df['RPM'] >= 700].reset_index(drop=True)
    
    # Determine maintenance type based on sensor patterns for anomalies
    def get_maintenance_type(row):
        if row['Anomaly Score'] < 0.5:
            return 'Normal'
        
        # Calculate deviation scores for each category
        vibration_score = (abs(row['Vibration X'] - 0.5) + abs(row['Vibration Y'] - 0.4) + abs(row['Vibration Z'] - 0.3)) / 3
        electrical_score = abs(row['Board Voltage'] - 26) / 3 + abs(row['Battery Voltage'] - 12.6) / 1
        engine_score = (abs(row['Engine Temperature'] - 75) / 20 + abs(row['Engine Load'] - 45) / 30 + 
                       abs(row['Exhaust Temp'] - 450) / 100 + abs(row['Oil Pressure'] - 45) / 15) / 4
        
        scores = {
            '🔧 Mechanical': vibration_score,
            '⚡ Electrical': electrical_score,
            '🔥 Engine Performance': engine_score
        }
        return max(scores, key=scores.get)
    
    df['Maintenance Type'] = df.apply(get_maintenance_type, axis=1)
    
    # Calculate 95th percentile threshold on filtered data
    threshold_95 = np.percentile(df['Anomaly Score'], 95)
    df['Is Anomaly'] = df['Anomaly Score'] > threshold_95
    df['Threshold_95'] = threshold_95
    
    return df

def generate_sod_data():
    """Generate sample SoD violation data with random user IDs"""
    # Generate truly random user IDs
    first_initials = ["J", "M", "A", "K", "R", "T", "D", "P", "N", "S", "L", "C", "B", "E", "W"]
    last_names = ["SMITH", "JONES", "BROWN", "WILSON", "GARCIA", "LEE", "CHEN", "KIM", "WANG", "ZHOU", 
                  "DAVIS", "MILLER", "TAYLOR", "ANDERSON", "THOMAS"]
    
    users = []
    for _ in range(50):
        user_id = f"{random.choice(first_initials)}{random.choice(last_names)}{random.randint(10, 99)}"
        users.append(user_id)
    
    violations = []
    
    sod_rules = [
        ("AP01", "Create Vendor vs Pay Vendor", "Critical"),
        ("GL01", "Create GL Account vs Post to GL", "High"),
        ("MM01", "Create PO vs Goods Receipt", "Medium"),
        ("SD01", "Create Customer vs Process Sales", "High"),
        ("HR01", "Maintain Employee vs Payroll Processing", "Critical"),
    ]
    
    for _ in range(100):
        user = random.choice(users)
        rule = random.choice(sod_rules)
        violations.append({
            'User ID': user,
            'Rule ID': rule[0],
            'Description': rule[1],
            'Risk Level': rule[2],
            'Function 1': rule[1].split(' vs ')[0],
            'Function 2': rule[1].split(' vs ')[1],
            'Detection Date': datetime.now() - timedelta(days=random.randint(0, 90))
        })
    
    return pd.DataFrame(violations)

def generate_ridership_data():
    """Generate sample ridership prediction data"""
    hours = list(range(24))
    routes = [mask_route(f"ROUTE{i}") for i in range(10)]
    
    data = []
    for route in routes:
        for hour in hours:
            # Simulate realistic ridership patterns
            base = random.randint(50, 200)
            if 7 <= hour <= 9 or 17 <= hour <= 19:  # Peak hours
                actual = base * random.uniform(1.5, 2.5)
            else:
                actual = base * random.uniform(0.5, 1.0)
            
            predicted = actual * random.uniform(0.9, 1.1)
            
            data.append({
                'Route': route,
                'Hour': hour,
                'Actual Ridership': int(actual),
                'Predicted Ridership': int(predicted),
                'Accuracy': min(100, 100 - abs(actual - predicted) / actual * 100)
            })
    
    return pd.DataFrame(data)

def generate_bus_speed_data():
    """Generate sample bus speed prediction data"""
    segments = [f"Segment {i+1}" for i in range(20)]
    
    data = []
    for seg in segments:
        actual_speed = random.uniform(15, 45)
        predicted_speed = actual_speed * random.uniform(0.92, 1.08)
        data.append({
            'Segment': seg,
            'Actual Speed (km/h)': round(actual_speed, 1),
            'Predicted Speed (km/h)': round(predicted_speed, 1),
            'Traffic Level': random.choice(['Light', 'Moderate', 'Heavy']),
            'Weather': random.choice(['Clear', 'Rainy', 'Cloudy']),
        })
    
    return pd.DataFrame(data)

# ============================================================================
# PORTFOLIO SECTIONS
# ============================================================================

def render_hero():
    """Render clean hero section"""
    hero_html = f'''
    <div class="hero-section" style="position: relative; overflow: hidden;">
        <div style="position: relative; z-index: 1;">
            <p style="font-size: 1rem; font-weight: 500; opacity: 0.9; margin-bottom: 0.5rem;">
                👋 Hello, I'm
            </p>
            <h1 class="hero-name">{PROFILE['name']}</h1>
            <p class="hero-title">{PROFILE['title']}</p>
            <p class="hero-subtitle">{SUMMARY}</p>
            <div style="margin-top: 2rem; display: flex; gap: 1rem; flex-wrap: wrap; align-items: center;">
                <span class="live-badge"><span class="live-dot"></span> {PROFILE['status']}</span>
                <span style="background: rgba(255,255,255,0.2); padding: 6px 16px; border-radius: 100px; font-size: 0.85rem;">📍 {PROFILE['location']}</span>
                <span style="background: rgba(255,255,255,0.2); padding: 6px 16px; border-radius: 100px; font-size: 0.85rem;">💼 {PROFILE['experience_years']}+ Years Experience</span>
                <span style="background: rgba(255,255,255,0.2); padding: 6px 16px; border-radius: 100px; font-size: 0.85rem;">🎓 {PROFILE.get('education', 'BSc Computer Science')}</span>
            </div>
        </div>
    </div>
    '''
    st.markdown(hero_html, unsafe_allow_html=True)

def render_stats():
    """Render statistics section"""
    col1, col2, col3, col4 = st.columns(4)
    
    stats = [
        ("4+", "AI Projects Delivered"),
        ("3+", "Years Experience"),
        ("10+", "ML Models Deployed"),
        ("90%", "Average Accuracy"),
    ]
    
    for col, (value, label) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="stat-number">{value}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

def render_skills():
    """Render skills section"""
    st.markdown('''
    <h2 class="section-title">🛠️ Technical Expertise</h2>
    ''', unsafe_allow_html=True)
    
    cols = st.columns(len(SKILLS))
    
    for col, (category, data) in zip(cols, SKILLS.items()):
        with col:
            st.markdown(f"""
            <div class="glass-card">
                <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -0.02em;">{category}</h3>
            </div>
            """, unsafe_allow_html=True)
            for skill, level in data['skills']:
                st.markdown(f"**{skill}**")
                st.progress(level / 100)

def render_projects():
    """Render projects section"""
    st.markdown('''
    <h2 class="section-title">🚀 Featured Projects</h2>
    ''', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Click on any project tab above to explore the interactive demo</p>', unsafe_allow_html=True)
    
    # Add custom CSS for equal gaps
    st.markdown("""
    <style>
    .project-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Use columns with gap specification
    col1, spacer, col2 = st.columns([1, 0.08, 1])
    
    for idx, project in enumerate(PROJECTS):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class="project-card" style="margin-bottom: 1.5rem;">
                <div class="project-icon" style="background: {project['color']};">
                    {project['icon']}
                </div>
                <h3 class="project-title">{project['title']}</h3>
                <p class="project-desc">{project['description']}</p>
                <div style="margin-bottom: 1rem;">
                    {''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['technologies'][:5]])}
                </div>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                    {''.join([f'<div style="text-align: center;"><div style="font-size: 1.2rem; font-weight: 700; color: #007AFF;">{v}</div><div style="font-size: 0.75rem; color: #8E8E93;">{k}</div></div>' for k, v in project['metrics'].items()])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Experience Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('''
    <h2 class="section-title">💼 Experience</h2>
    ''', unsafe_allow_html=True)
    
    for exp in EXPERIENCE:
        st.markdown(f"""
        <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                <div>
                    <h3 style="margin: 0; font-size: 1.2rem;">{exp['role']}</h3>
                    <p style="margin: 0.25rem 0 0 0; color: #8E8E93;">{exp['company']} · {exp.get('location', '')}</p>
                </div>
                <span style="background: var(--apple-gray-6); padding: 4px 12px; border-radius: 100px; font-size: 0.8rem; color: #8E8E93;">
                    {exp['duration']}
                </span>
            </div>
            <ul style="margin: 0; padding-left: 1.2rem; color: #3A3A3C;">
                {''.join([f'<li style="margin-bottom: 0.5rem;">{h}</li>' for h in exp['highlights']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Education Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('''
    <h2 class="section-title">🎓 Education</h2>
    ''', unsafe_allow_html=True)
    
    for edu in EDUCATION:
        st.markdown(f"""
        <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                <div>
                    <h3 style="margin: 0; font-size: 1.2rem;">{edu['degree']}</h3>
                    <p style="margin: 0.25rem 0 0 0; color: #8E8E93;">{edu['institution']}</p>
                    <p style="margin: 0.25rem 0 0 0; color: #007AFF; font-weight: 500;">{edu['grade']}</p>
                </div>
                <span style="background: var(--apple-gray-6); padding: 4px 12px; border-radius: 100px; font-size: 0.8rem; color: #8E8E93;">
                    {edu['duration']}
                </span>
            </div>
            <ul style="margin: 0; padding-left: 1.2rem; color: #3A3A3C;">
                {''.join([f'<li style="margin-bottom: 0.5rem;">{h}</li>' for h in edu['highlights']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('''
    <h2 class="section-title">🏅 Certifications</h2>
    ''', unsafe_allow_html=True)
    
    cert_cols = st.columns(len(CERTIFICATIONS))
    for col, cert in zip(cert_cols, CERTIFICATIONS):
        with col:
            skills_html = ""
            if 'skills' in cert:
                skills_html = f'''<div style="margin-top: 0.75rem; display: flex; flex-wrap: wrap; gap: 4px; justify-content: center;">
                    {''.join([f'<span style="background: #F2F2F7; padding: 2px 8px; border-radius: 12px; font-size: 0.7rem; color: #8E8E93;">{s}</span>' for s in cert['skills'][:3]])}
                </div>'''
            st.markdown(f"""
            <div class="metric-card" style="padding: 1.5rem;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🏆</div>
                <div style="font-weight: 600; color: #1D1D1F; font-size: 0.95rem;">{cert['name']}</div>
                <div style="font-size: 0.8rem; color: #007AFF; font-weight: 500; margin-top: 0.25rem;">{cert['issuer']} • {cert['year']}</div>
                {skills_html}
            </div>
            """, unsafe_allow_html=True)
    

# ============================================================================
# INTERACTIVE DEMOS
# ============================================================================

def demo_anomaly_detection():
    """Interactive Predictive Maintenance Demo with Autoencoder"""
    
    # Problem Statement Card
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #FF6B6B;">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div style="font-size: 2.5rem;">🔧</div>
            <div>
                <h3 style="font-size: 1.5rem; margin: 0 0 0.5rem 0; color: #1D1D1F;">Predictive Maintenance with Autoencoder</h3>
                <p style="color: #8E8E93; margin: 0;">Deep Learning-based anomaly detection for bus fleet health monitoring</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Problem & Solution Section
    col_prob, col_sol = st.columns(2)
    
    with col_prob:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF5F5, #FED7D7); padding: 1.5rem; border-radius: 16px; height: 100%;">
            <h4 style="color: #C53030; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                <span>⚠️</span> The Problem
            </h4>
            <ul style="color: #742A2A; margin: 0; padding-left: 1.2rem; line-height: 1.8;">
                <li><strong>Unexpected Breakdowns</strong> cause service disruptions</li>
                <li><strong>Long Passenger Wait Times</strong> due to vehicle failures</li>
                <li><strong>Reactive Maintenance</strong> leads to costly emergency repairs</li>
                <li><strong>No Early Warning System</strong> for component degradation</li>
                <li><strong>Revenue Loss</strong> from cancelled routes & unhappy passengers</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_sol:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #F0FFF4, #C6F6D5); padding: 1.5rem; border-radius: 16px; height: 100%;">
            <h4 style="color: #276749; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                <span>✅</span> The Solution
            </h4>
            <ul style="color: #22543D; margin: 0; padding-left: 1.2rem; line-height: 1.8;">
                <li><strong>Autoencoder Neural Network</strong> learns normal operating patterns</li>
                <li><strong>17 IoT Sensors × 3 Features</strong> = 51 input features</li>
                <li><strong>Early Anomaly Detection</strong> days before failure occurs</li>
                <li><strong>Proactive Maintenance</strong> scheduling during off-peak hours</li>
                <li><strong>30% Reduction</strong> in unplanned downtime</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Autoencoder Architecture Explanation
    with st.expander("🧠 How Autoencoder Anomaly Detection Works", expanded=False):
        st.markdown("""
        **Feature Engineering (per sensor):**
        - **Trend**: Rolling mean to capture gradual changes
        - **Std**: Rolling standard deviation for variability
        - **Residual**: Difference from trend to capture sudden shifts
        
        **Autoencoder Architecture:**
        ```
        Input Layer (51 features)  →  Encoder  →  Latent Space (8)  →  Decoder  →  Output Layer (51 features)
              ↓                         ↓              ↓                  ↓              ↓
        [17 sensors × 3 features]  [Dense 32]    [Compressed]       [Dense 32]    [Reconstructed
         trend, std, residual      [Dense 16]    [8-dim repr.]      [Dense 16]     Features]
                                   [Dense 8]     [ReLU act.]        [Linear act.]
        ```
        
        **Model Configuration:**
        - **Loss Function**: Mean Squared Error (MSE)
        - **Training**: 50 epochs, batch size 32
        - **Threshold**: 95th percentile of reconstruction error
        
        **Detection Method:**
        1. Train autoencoder on **normal operating data** only
        2. Model learns to compress 51 features into 8-dimensional latent space
        3. **Anomalies** = High reconstruction error (model can't recreate abnormal patterns)
        4. Alert when MSE exceeds the 95th percentile threshold
        
        **Why Autoencoders for PdM?**
        - Unsupervised learning (no need for labeled failure data)
        - Captures complex multivariate sensor relationships
        - 8-dim latent space captures essential operating states
        - Sensitive to subtle deviations from normal behavior
        """)
    
    # Interactive Demo
    st.markdown("### 📊 Anomaly Score Timeline")
    
    # Generate data
    df = generate_anomaly_detection_data()
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### 🎛️ Controls")
        
        # Bus selector with masked IDs like screenshot
        bus_options = ['WA7230M', 'WA9479M', 'WB8743F', 'WB915L', 'WB946L', 'WWB872U']
        selected_bus = st.selectbox("Select Vehicle", bus_options)
        
        # Reseed based on bus selection for variety
        bus_seed = hash(selected_bus) % 100
        np.random.seed(bus_seed)
        
        # Percentile threshold selector
        percentile = st.selectbox(
            "Threshold Percentile",
            [90, 95, 99],
            index=1,
            help="Percentile for anomaly threshold"
        )
        
        # Calculate threshold based on percentile
        threshold = np.percentile(df['Anomaly Score'], percentile)
        df['Is Anomaly'] = df['Anomaly Score'] > threshold
        
        st.markdown("---")
        st.markdown("### 📈 Statistics")
        
        alert_count = df['Is Anomaly'].sum()
        current_value = df['Anomaly Score'].iloc[-1]
        is_alert = current_value > threshold
        
        st.markdown(f"""
        <div style="background: #F0F7FF; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <div style="font-size: 0.85rem; color: #6B7280;">Threshold ({percentile}th %ile)</div>
            <div style="font-size: 1.3rem; font-weight: 700; color: #1D1D1F;">{threshold:.3f}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background: #FEF2F2; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <div style="font-size: 0.85rem; color: #6B7280;">Total Alerts</div>
            <div style="font-size: 1.3rem; font-weight: 700; color: #DC2626;">{alert_count}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 🧠 Autoencoder Model")
        st.markdown("""
        <div style="background: #F5F3FF; padding: 12px; border-radius: 8px; font-size: 0.8rem; line-height: 1.6;">
            <strong>Input Features:</strong><br>
            51 features (17 sensors × 3)<br>
            <span style="color: #6B7280;">trend, std, residual</span><br><br>
            <strong>Architecture:</strong><br>
            51 → 32 → 16 → <b>8</b> → 16 → 32 → 51<br><br>
            <strong>Latent Space:</strong> 8 dims<br>
            <strong>Activation:</strong> ReLU / Linear<br>
            <strong>Loss:</strong> MSE<br>
            <strong>Training:</strong> 50 epochs<br>
            <strong>Batch Size:</strong> 32
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 🚫 Data Filtering")
        st.markdown("""
        <div style="background: #FEF9C3; padding: 10px; border-radius: 8px; font-size: 0.8rem;">
            <strong>Idling Filtered:</strong><br>
            RPM < 700 excluded<br>
            <span style="color: #6B7280;">Cleaner trend analysis</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Main Anomaly Score Timeline Chart (like the screenshot)
        fig = go.Figure()
        
        # Anomaly score line (light blue)
        fig.add_trace(go.Scatter(
            x=df['timestamp'],
            y=df['Anomaly Score'],
            mode='lines',
            name='Anomaly Score',
            line=dict(color='#38BDF8', width=1.5),
            hovertemplate='<b>Date:</b> %{x}<br><b>Score:</b> %{y:.4f}<extra></extra>'
        ))
        
        # Threshold line (red dashed)
        fig.add_trace(go.Scatter(
            x=[df['timestamp'].min(), df['timestamp'].max()],
            y=[threshold, threshold],
            mode='lines',
            name=f'{percentile}th Percentile: {threshold:.3f}',
            line=dict(color='#EF4444', width=2, dash='dash'),
            hoverinfo='skip'
        ))
        
        # Alert points (red dots for anomalies)
        anomaly_df = df[df['Is Anomaly']]
        fig.add_trace(go.Scatter(
            x=anomaly_df['timestamp'],
            y=anomaly_df['Anomaly Score'],
            mode='markers',
            name=f'Alerts: {len(anomaly_df)}',
            marker=dict(color='#EF4444', size=8, symbol='circle',
                       line=dict(color='#DC2626', width=1)),
            hovertemplate='<b>🚨 ALERT</b><br>Date: %{x}<br>Score: %{y:.4f}<extra></extra>'
        ))
        
        # Add current status annotation (bottom right like screenshot)
        current_color = '#EF4444' if is_alert else '#10B981'
        alert_text = '🚨 ALERT' if is_alert else '✅ Normal'
        
        fig.add_annotation(
            x=df['timestamp'].iloc[-1],
            y=current_value,
            text=f"<b>Current: {current_value:.4f}</b><br>{alert_text}",
            showarrow=True,
            arrowhead=2,
            arrowcolor=current_color,
            bgcolor=current_color,
            font=dict(color='white', size=11),
            bordercolor=current_color,
            borderwidth=2,
            borderpad=6,
            ax=-80,
            ay=40
        )
        
        fig.update_layout(
            title=dict(
                text=f'Bus {selected_bus} - Anomaly Score Timeline ({percentile}th Percentile)',
                font=dict(size=18, color='#1D1D1F')
            ),
            xaxis_title='Date/Time',
            yaxis_title='Reconstruction Error (Anomaly Score)',
            template='plotly_white',
            height=450,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='left',
                x=0
            ),
            margin=dict(t=80, b=60, l=60, r=40),
            hovermode='x unified'
        )
        
        # Add range slider
        fig.update_xaxes(
            rangeslider_visible=False,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1M", step="month", stepmode="backward"),
                    dict(count=3, label="3M", step="month", stepmode="backward"),
                    dict(count=6, label="6M", step="month", stepmode="backward"),
                    dict(step="all", label="All")
                ]),
                bgcolor='#F3F4F6',
                activecolor='#007AFF'
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Summary metrics row
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Records", f"{len(df):,}", help="Idling (RPM<700) filtered out")
        m2.metric("Alerts Detected", f"{alert_count:,}", delta=f"{alert_count/len(df)*100:.1f}%")
        m3.metric("Max Score", f"{df['Anomaly Score'].max():.3f}")
        m4.metric("Current Status", alert_text)
        
        # Maintenance Type Breakdown
        if alert_count > 0:
            st.markdown("### 🔧 Recommended Maintenance Actions")
            
            # Get maintenance type distribution for anomalies
            maint_df = anomaly_df.groupby('Maintenance Type').size().reset_index(name='Count')
            maint_df = maint_df[maint_df['Maintenance Type'] != 'Normal']
            
            if len(maint_df) > 0:
                maint_cols = st.columns(3)
                
                maint_info = {
                    '🔧 Mechanical': {
                        'color': '#F59E0B',
                        'bg': '#FEF3C7',
                        'desc': 'Check vibration sensors, bearings, belt tension, suspension components'
                    },
                    '⚡ Electrical': {
                        'color': '#3B82F6',
                        'bg': '#DBEAFE',
                        'desc': 'Inspect battery, alternator, wiring harness, voltage regulators'
                    },
                    '🔥 Engine Performance': {
                        'color': '#EF4444',
                        'bg': '#FEE2E2',
                        'desc': 'Check fuel system, air filters, exhaust, cooling system, oil levels'
                    }
                }
                
                for idx, maint_type in enumerate(['🔧 Mechanical', '⚡ Electrical', '🔥 Engine Performance']):
                    with maint_cols[idx]:
                        count = maint_df[maint_df['Maintenance Type'] == maint_type]['Count'].sum() if maint_type in maint_df['Maintenance Type'].values else 0
                        info = maint_info[maint_type]
                        st.markdown(f"""
                        <div style="background: {info['bg']}; padding: 1rem; border-radius: 12px; border-left: 4px solid {info['color']};">
                            <div style="font-size: 1.1rem; font-weight: 600; color: {info['color']}; margin-bottom: 0.5rem;">
                                {maint_type}
                            </div>
                            <div style="font-size: 2rem; font-weight: 700; color: #1D1D1F;">{count}</div>
                            <div style="font-size: 0.75rem; color: #6B7280; margin-top: 0.5rem;">
                                {info['desc']}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Anomaly details table with maintenance type
            st.markdown("### 🚨 Recent High Reconstruction Error Events")
            anomaly_details = anomaly_df[['timestamp', 'Anomaly Score', 'Maintenance Type', 'RPM']].copy()
            anomaly_details['Severity'] = anomaly_details['Anomaly Score'].apply(
                lambda x: '🔴 Critical' if x > 2 else ('🟠 High' if x > 1.5 else '🟡 Medium')
            )
            anomaly_details = anomaly_details.sort_values('timestamp', ascending=False).head(10)
            anomaly_details.columns = ['Timestamp', 'Reconstruction Error', 'Maintenance Type', 'RPM', 'Severity']
            st.dataframe(anomaly_details, use_container_width=True)
            
            # Add note about filtering
            st.info("ℹ️ **Note:** Data filtered to exclude idling state (RPM < 700) for cleaner trend analysis. This removes noise from stationary periods and focuses on operational anomalies.")

def demo_sod_violations():
    """Interactive SoD Violations Demo"""
    
    # Problem Statement Card
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #4ECDC4;">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div style="font-size: 2.5rem;">🔐</div>
            <div>
                <h3 style="font-size: 1.5rem; margin: 0 0 0.5rem 0; color: #1D1D1F;">SAP Access Governance (IGA)</h3>
                <p style="color: #8E8E93; margin: 0;">AI-powered Identity Governance and Segregation of Duties detection</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Problem & Solution Section
    col_prob, col_sol = st.columns(2)
    
    with col_prob:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF5F5, #FED7D7); padding: 1.5rem; border-radius: 16px; height: 100%;">
            <h4 style="color: #C53030; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                <span>⚠️</span> The Problem
            </h4>
            <ul style="color: #742A2A; margin: 0; padding-left: 1.2rem; line-height: 1.8;">
                <li><strong>Manual Audit Process</strong> takes weeks to complete</li>
                <li><strong>SoD Violations</strong> go undetected, creating fraud risk</li>
                <li><strong>Excessive Access Rights</strong> accumulate over time</li>
                <li><strong>Compliance Failures</strong> in SOX & GDPR audits</li>
                <li><strong>No Visibility</strong> into user access patterns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_sol:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #F0FFF4, #C6F6D5); padding: 1.5rem; border-radius: 16px; height: 100%;">
            <h4 style="color: #276749; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                <span>✅</span> The Solution
            </h4>
            <ul style="color: #22543D; margin: 0; padding-left: 1.2rem; line-height: 1.8;">
                <li><strong>Automated SoD Detection</strong> with 19+ standard rules</li>
                <li><strong>ML Anomaly Detection</strong> identifies unusual access</li>
                <li><strong>Access Housekeeping</strong> flags inactive/excessive access</li>
                <li><strong>Audit-Ready Reports</strong> for compliance teams</li>
                <li><strong>80% Reduction</strong> in manual audit time</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Demo
    st.markdown("### 🎮 Interactive Demo: SoD Violation Analysis")
    
    df = generate_sod_data()
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### 🎛️ Filters")
        
        risk_filter = st.multiselect(
            "Risk Level",
            ['Critical', 'High', 'Medium'],
            default=['Critical', 'High', 'Medium']
        )
        
        rule_filter = st.multiselect(
            "Rule Category",
            df['Rule ID'].unique().tolist(),
            default=df['Rule ID'].unique().tolist()[:3]
        )
        
        st.markdown("---")
        st.markdown("### 📊 Risk Summary")
        
        for risk in ['Critical', 'High', 'Medium']:
            count = len(df[df['Risk Level'] == risk])
            color = {'Critical': '#FF3B30', 'High': '#FF9500', 'Medium': '#FFCC00'}[risk]
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; padding: 8px 12px; 
                        background: {color}22; border-radius: 8px; margin-bottom: 8px;">
                <span>{risk}</span>
                <span style="font-weight: 700;">{count}</span>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Filter data
        df_filtered = df[
            (df['Risk Level'].isin(risk_filter)) & 
            (df['Rule ID'].isin(rule_filter))
        ]
        
        # Risk distribution chart
        fig = px.sunburst(
            df_filtered,
            path=['Risk Level', 'Rule ID', 'User ID'],
            color='Risk Level',
            color_discrete_map={'Critical': '#FF3B30', 'High': '#FF9500', 'Medium': '#FFCC00'},
            title='SoD Violations by Risk Level and Rule'
        )
        fig.update_layout(height=400, margin=dict(t=50, b=20))
        st.plotly_chart(fig, use_container_width=True)
        
        # Violations table
        st.markdown("### 📋 Violation Details")
        display_df = df_filtered[['User ID', 'Rule ID', 'Description', 'Risk Level', 'Function 1', 'Function 2']].head(15)
        st.dataframe(display_df, use_container_width=True)
    
    # ML Anomaly Detection Section
    st.markdown("---")
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #8B5CF6;">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div style="font-size: 2rem;">🤖</div>
            <div>
                <h3 style="font-size: 1.3rem; margin: 0 0 0.5rem 0; color: #1D1D1F;">ML-Based Access Anomaly Detection</h3>
                <p style="color: #8E8E93; margin: 0;">Isolation Forest algorithm identifies unusual user access patterns</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate anomaly data
    np.random.seed(42)
    n_users = 50
    
    first_names = ['JOHN', 'JANE', 'MIKE', 'SARAH', 'DAVID', 'EMMA', 'CHRIS', 'LISA', 'JAMES', 'ANNA',
                   'ROBERT', 'MARIA', 'WILLIAM', 'JENNIFER', 'RICHARD', 'MICHELLE', 'JOSEPH', 'KAREN',
                   'THOMAS', 'NANCY', 'DANIEL', 'BETTY', 'PAUL', 'HELEN', 'MARK']
    last_names = ['SMITH', 'JOHNSON', 'WILLIAMS', 'BROWN', 'JONES', 'GARCIA', 'MILLER', 'DAVIS', 
                  'MARTINEZ', 'ANDERSON', 'TAYLOR', 'THOMAS', 'MOORE', 'JACKSON', 'MARTIN']
    
    user_ids = []
    for i in range(n_users):
        first = random.choice(first_names)
        last = random.choice(last_names)
        num = random.randint(10, 99)
        user_ids.append(f"{first[0]}{last[:5].upper()}{num}")
    
    # Normal users have consistent patterns
    login_count = np.random.normal(25, 5, n_users).clip(10, 50)
    transactions = np.random.normal(150, 30, n_users).clip(50, 300)
    failed_logins = np.random.exponential(1, n_users).clip(0, 5)
    access_hours = np.random.normal(8, 1, n_users).clip(6, 10)  # Normal business hours
    unique_tcodes = np.random.normal(15, 3, n_users).clip(5, 30)
    
    # Inject anomalies (10% of users)
    anomaly_indices = np.random.choice(n_users, size=5, replace=False)
    for idx in anomaly_indices:
        anomaly_type = random.choice(['high_activity', 'off_hours', 'suspicious'])
        if anomaly_type == 'high_activity':
            login_count[idx] = np.random.uniform(80, 150)
            transactions[idx] = np.random.uniform(500, 1000)
        elif anomaly_type == 'off_hours':
            access_hours[idx] = np.random.uniform(0, 4)  # Late night access
            failed_logins[idx] = np.random.uniform(5, 15)
        else:
            unique_tcodes[idx] = np.random.uniform(50, 80)  # Accessing too many tcodes
            failed_logins[idx] = np.random.uniform(8, 20)
    
    # Calculate anomaly scores (simulating Isolation Forest output)
    anomaly_scores = (
        (login_count - login_count.mean()) / login_count.std() * 0.3 +
        (transactions - transactions.mean()) / transactions.std() * 0.2 +
        (failed_logins - failed_logins.mean()) / failed_logins.std() * 0.25 +
        np.abs(access_hours - 8) / 2 * 0.15 +
        (unique_tcodes - unique_tcodes.mean()) / unique_tcodes.std() * 0.1
    )
    anomaly_scores = (anomaly_scores - anomaly_scores.min()) / (anomaly_scores.max() - anomaly_scores.min())
    
    is_anomaly = anomaly_scores > 0.7
    
    access_df = pd.DataFrame({
        'User ID': user_ids,
        'Login Count': login_count.astype(int),
        'Transactions': transactions.astype(int),
        'Failed Logins': failed_logins.astype(int),
        'Avg Access Hour': access_hours.round(1),
        'Unique T-Codes': unique_tcodes.astype(int),
        'Anomaly Score': anomaly_scores.round(3),
        'Status': ['🚨 Anomaly' if a else '✅ Normal' for a in is_anomaly]
    })
    
    col_ml1, col_ml2 = st.columns([1, 2])
    
    with col_ml1:
        st.markdown("### 🎛️ Detection Settings")
        
        sensitivity = st.slider("Anomaly Sensitivity", 0.5, 0.9, 0.7, 0.05,
                               help="Lower = more strict, flags more users")
        
        # Recalculate based on sensitivity
        access_df['Status'] = ['🚨 Anomaly' if s > sensitivity else '✅ Normal' for s in access_df['Anomaly Score']]
        
        anomaly_count = (access_df['Status'] == '🚨 Anomaly').sum()
        normal_count = (access_df['Status'] == '✅ Normal').sum()
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #FEE2E2, #FECACA); padding: 1rem; border-radius: 12px; margin-bottom: 1rem;">
            <div style="font-size: 2rem; font-weight: 700; color: #DC2626;">{anomaly_count}</div>
            <div style="font-size: 0.85rem; color: #991B1B;">Anomalous Users</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #D1FAE5, #A7F3D0); padding: 1rem; border-radius: 12px;">
            <div style="font-size: 2rem; font-weight: 700; color: #059669;">{normal_count}</div>
            <div style="font-size: 0.85rem; color: #065F46;">Normal Users</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 🧠 Model Info")
        st.markdown("""
        <div style="background: #F5F3FF; padding: 12px; border-radius: 8px; font-size: 0.85rem;">
            <strong>Algorithm:</strong> Isolation Forest<br>
            <strong>Features:</strong> 5 behavioral<br>
            <strong>Training:</strong> 30-day history<br>
            <strong>Contamination:</strong> 10%
        </div>
        """, unsafe_allow_html=True)
    
    with col_ml2:
        # Scatter plot showing anomalies
        fig = go.Figure()
        
        normal_df = access_df[access_df['Status'] == '✅ Normal']
        anomaly_df = access_df[access_df['Status'] == '🚨 Anomaly']
        
        fig.add_trace(go.Scatter(
            x=normal_df['Login Count'],
            y=normal_df['Transactions'],
            mode='markers',
            name='Normal',
            marker=dict(size=10, color='#10B981', opacity=0.6),
            text=normal_df['User ID'],
            hovertemplate='<b>%{text}</b><br>Logins: %{x}<br>Transactions: %{y}<extra></extra>'
        ))
        
        fig.add_trace(go.Scatter(
            x=anomaly_df['Login Count'],
            y=anomaly_df['Transactions'],
            mode='markers',
            name='Anomaly',
            marker=dict(size=14, color='#EF4444', symbol='x', line=dict(width=2)),
            text=anomaly_df['User ID'],
            hovertemplate='<b>%{text}</b><br>Logins: %{x}<br>Transactions: %{y}<br>⚠️ Anomaly Detected<extra></extra>'
        ))
        
        fig.update_layout(
            title='User Access Pattern Analysis',
            xaxis_title='Login Count (30 days)',
            yaxis_title='Transaction Count',
            height=350,
            legend=dict(orientation='h', yanchor='bottom', y=1.02),
            margin=dict(t=60, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Anomaly details table
        st.markdown("### 🚨 Flagged Users for Review")
        if anomaly_count > 0:
            flagged_df = access_df[access_df['Status'] == '🚨 Anomaly'][
                ['User ID', 'Login Count', 'Transactions', 'Failed Logins', 'Avg Access Hour', 'Anomaly Score']
            ].sort_values('Anomaly Score', ascending=False)
            flagged_df['Risk Reason'] = flagged_df.apply(
                lambda x: 'High Activity' if x['Transactions'] > 400 else (
                    'Off-Hours Access' if x['Avg Access Hour'] < 6 else (
                        'Multiple Failed Logins' if x['Failed Logins'] > 5 else 'Unusual Pattern'
                    )
                ), axis=1
            )
            st.dataframe(flagged_df, use_container_width=True)
        else:
            st.info("No anomalies detected at current sensitivity level.")

def demo_ridership():
    """Interactive Route Recommendation & Ridership Demo"""
    
    # Problem Statement Card
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #667eea;">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div style="font-size: 2.5rem;">🚌</div>
            <div>
                <h3 style="font-size: 1.5rem; margin: 0 0 0.5rem 0; color: #1D1D1F;">SwiftRoute - AI Route Recommendation</h3>
                <p style="color: #8E8E93; margin: 0;">Intelligent bus rerouting during service disruptions</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Problem & Solution Section
    col_prob, col_sol = st.columns(2)
    
    with col_prob:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF5F5, #FED7D7); padding: 1.5rem; border-radius: 16px; height: 100%;">
            <h4 style="color: #C53030; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                <span>⚠️</span> The Problem
            </h4>
            <ul style="color: #742A2A; margin: 0; padding-left: 1.2rem; line-height: 1.8;">
                <li><strong>Service Disruptions</strong> leave passengers stranded</li>
                <li><strong>Manual Decision Making</strong> causes delays in response</li>
                <li><strong>Suboptimal Rerouting</strong> leads to overcrowded replacement buses</li>
                <li><strong>No Real-time Visibility</strong> on nearby bus availability</li>
                <li><strong>Revenue Loss</strong> from poor passenger experience</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_sol:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #F0FFF4, #C6F6D5); padding: 1.5rem; border-radius: 16px; height: 100%;">
            <h4 style="color: #276749; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                <span>✅</span> The Solution
            </h4>
            <ul style="color: #22543D; margin: 0; padding-left: 1.2rem; line-height: 1.8;">
                <li><strong>AI-Powered Recommendation</strong> suggests optimal replacement routes</li>
                <li><strong>Real-time Ridership Analysis</strong> identifies low-occupancy buses nearby</li>
                <li><strong>Automated Rerouting</strong> minimizes passenger wait time</li>
                <li><strong>Smart Load Balancing</strong> prevents bus overcrowding</li>
                <li><strong>Sub-500ms Response</strong> for instant decision support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Demo
    st.markdown("### 🎮 Interactive Demo: Disruption Scenario")
    
    df = generate_ridership_data()
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### 🚨 Disruption Input")
        
        # Simulate disruption scenario
        disruption_type = st.selectbox(
            "Disruption Type",
            ["Vehicle Breakdown", "Accident", "Road Closure", "Weather"]
        )
        
        affected_route = st.selectbox("Affected Route", df['Route'].unique().tolist())
        
        passengers_affected = st.slider("Passengers Stranded", 10, 100, 45)
        
        st.markdown("---")
        st.markdown("### 🔍 Nearby Buses")
        
        # Simulated nearby buses with ridership
        nearby_buses = [
            {"bus": "BUS-A12", "route": "Express-042", "occupancy": 35, "distance": 1.2},
            {"bus": "BUS-B07", "route": "Line-118", "occupancy": 22, "distance": 2.1},
            {"bus": "BUS-C19", "route": "Metro-205", "occupancy": 68, "distance": 0.8},
        ]
        
        for bus in nearby_buses:
            occ_color = "#34C759" if bus['occupancy'] < 40 else ("#FF9500" if bus['occupancy'] < 60 else "#FF3B30")
            st.markdown(f"""
            <div style="background: white; padding: 10px; border-radius: 10px; margin-bottom: 8px; border: 1px solid #E5E5EA;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 600;">{bus['bus']}</span>
                    <span style="background: {occ_color}22; color: {occ_color}; padding: 2px 8px; border-radius: 20px; font-size: 0.75rem; font-weight: 600;">{bus['occupancy']}%</span>
                </div>
                <div style="font-size: 0.8rem; color: #8E8E93;">{bus['route']} • {bus['distance']} km away</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # AI Recommendation
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 1.5rem; border-radius: 16px; color: white; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 0.9rem; opacity: 0.9;">🤖 AI RECOMMENDATION</div>
                    <div style="font-size: 1.5rem; font-weight: 700; margin-top: 0.5rem;">Reroute BUS-B07 (Line-118)</div>
                    <div style="font-size: 0.9rem; opacity: 0.9; margin-top: 0.25rem;">Lowest occupancy (22%) • 2.1 km away • ETA: 4 min</div>
                </div>
                <div style="text-align: center; background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 12px;">
                    <div style="font-size: 2rem; font-weight: 700;">92%</div>
                    <div style="font-size: 0.75rem;">Confidence</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Ridership comparison chart
        st.markdown("### 📊 Route Ridership Analysis")
        
        selected_route = affected_route
        time_range = (6, 22)
        
        route_df = df[df['Route'] == selected_route]
        route_df = route_df[(route_df['Hour'] >= time_range[0]) & (route_df['Hour'] <= time_range[1])]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=route_df['Hour'],
            y=route_df['Actual Ridership'],
            name='Current Ridership',
            marker_color='#007AFF'
        ))
        
        fig.add_trace(go.Scatter(
            x=route_df['Hour'],
            y=route_df['Predicted Ridership'],
            name='Predicted Demand',
            mode='lines+markers',
            line=dict(color='#FF9500', width=3),
            marker=dict(size=8)
        ))
        
        # Add disruption marker
        fig.add_vline(x=12, line_dash="dash", line_color="#FF3B30",
                     annotation_text="⚠️ Disruption", annotation_position="top")
        
        fig.update_layout(
            title=f'Hourly Ridership - {selected_route}',
            xaxis_title='Hour of Day',
            yaxis_title='Passengers',
            template='plotly_white',
            height=350,
            legend=dict(orientation='h', yanchor='bottom', y=1.02),
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Summary metrics
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Peak Hour", f"{route_df.loc[route_df['Actual Ridership'].idxmax(), 'Hour']:02d}:00")
        m2.metric("Affected Passengers", f"{passengers_affected}")
        m3.metric("Response Time", "< 500ms")
        m4.metric("Model Accuracy", "92%")

def demo_speed_prediction():
    """Interactive Bus Speed Prediction Demo"""
    
    # Problem Statement Card
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #f093fb;">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div style="font-size: 2.5rem;">⏱️</div>
            <div>
                <h3 style="font-size: 1.5rem; margin: 0 0 0.5rem 0; color: #1D1D1F;">Optimal Speed Predictor</h3>
                <p style="color: #8E8E93; margin: 0;">AI-powered speed guidance for perfect schedule adherence</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Problem & Solution Section
    col_prob, col_sol = st.columns(2)
    
    with col_prob:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF5F5, #FED7D7); padding: 1.5rem; border-radius: 16px; height: 100%;">
            <h4 style="color: #C53030; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                <span>⚠️</span> The Problem
            </h4>
            <ul style="color: #742A2A; margin: 0; padding-left: 1.2rem; line-height: 1.8;">
                <li><strong>Inconsistent Arrivals</strong> - Buses arrive too early or too late</li>
                <li><strong>Passenger Frustration</strong> - Missed connections & long waits</li>
                <li><strong>Driver Guesswork</strong> - No guidance on optimal driving speed</li>
                <li><strong>Schedule Bunching</strong> - Multiple buses arriving together</li>
                <li><strong>Poor Service Reliability</strong> - Unpredictable service quality</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_sol:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #F0FFF4, #C6F6D5); padding: 1.5rem; border-radius: 16px; height: 100%;">
            <h4 style="color: #276749; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                <span>✅</span> The Solution
            </h4>
            <ul style="color: #22543D; margin: 0; padding-left: 1.2rem; line-height: 1.8;">
                <li><strong>Real-time Speed Guidance</strong> - Optimal speed for each segment</li>
                <li><strong>Arrive On-Time</strong> - Not early, not late, just right</li>
                <li><strong>Traffic-Aware</strong> - Adjusts for live traffic conditions</li>
                <li><strong>SHAP Explainability</strong> - Drivers understand the "why"</li>
                <li><strong>15% Punctuality Improvement</strong> - Measurable service enhancement</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Demo
    st.markdown("### 🎮 Interactive Demo: Speed Optimization")
    
    df = generate_bus_speed_data()
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### 🎛️ Current Conditions")
        
        traffic = st.select_slider(
            "Traffic Condition",
            options=['Light', 'Moderate', 'Heavy'],
            value='Moderate'
        )
        
        weather = st.selectbox("Weather", ['Clear', 'Rainy', 'Cloudy'])
        
        time_of_day = st.slider("Current Hour", 6, 22, 12)
        
        schedule_status = st.radio("Schedule Status", ["On Time", "Running Late", "Running Early"])
        
        st.markdown("---")
        
        # Dynamic speed recommendation
        base_speed = 35 if traffic == 'Light' else (28 if traffic == 'Moderate' else 22)
        if schedule_status == "Running Late":
            optimal_speed = min(base_speed + 5, 40)
            status_color = "#FF9500"
            status_msg = "Speed up slightly"
        elif schedule_status == "Running Early":
            optimal_speed = max(base_speed - 5, 20)
            status_color = "#007AFF"
            status_msg = "Slow down to match schedule"
        else:
            optimal_speed = base_speed
            status_color = "#34C759"
            status_msg = "Maintain current pace"
        
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #f093fb, #f5576c); 
                    border-radius: 16px; color: white; margin-bottom: 1rem;">
            <div style="font-size: 0.85rem; opacity: 0.9;">RECOMMENDED SPEED</div>
            <div style="font-size: 3rem; font-weight: 700;">{optimal_speed}</div>
            <div style="font-size: 1rem;">km/h</div>
        </div>
        <div style="text-align: center; padding: 0.75rem; background: {status_color}22; border-radius: 8px; color: {status_color}; font-weight: 600;">
            {status_msg}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Speed comparison chart
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=df['Segment'],
            y=df['Actual Speed (km/h)'],
            name='Current Speed',
            marker_color='#007AFF'
        ))
        
        fig.add_trace(go.Scatter(
            x=df['Segment'],
            y=df['Predicted Speed (km/h)'],
            name='Optimal Speed',
            mode='lines+markers',
            line=dict(color='#34C759', width=3),
            marker=dict(size=8)
        ))
        
        # Add threshold lines
        fig.add_hline(y=optimal_speed, line_dash="dash", line_color="#f093fb",
                     annotation_text=f"Target: {optimal_speed} km/h")
        
        fig.update_layout(
            title='Segment-wise Speed Analysis',
            xaxis_title='Route Segment',
            yaxis_title='Speed (km/h)',
            template='plotly_white',
            height=350,
            legend=dict(orientation='h', yanchor='bottom', y=1.02)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # SHAP-like feature importance
        st.markdown("### 🔍 Why This Speed? (SHAP Explainability)")
        
        features = ['Traffic Density', 'Time of Day', 'Weather Condition', 'Passenger Load', 'Road Segment Type']
        importance = [0.35, 0.25, 0.18, 0.12, 0.10]
        colors = ['#FF6B6B', '#FF9500', '#FFCC00', '#34C759', '#007AFF']
        
        fig2 = go.Figure(go.Bar(
            x=importance,
            y=features,
            orientation='h',
            marker=dict(color=colors),
            text=[f'{v:.0%}' for v in importance],
            textposition='outside'
        ))
        fig2.update_layout(
            title='Feature Impact on Speed Recommendation',
            xaxis_title='Contribution',
            template='plotly_white',
            height=280,
            margin=dict(l=150)
        )
        st.plotly_chart(fig2, use_container_width=True)

def render_contact():
    """Render contact section"""
    st.markdown(f"""
    <div class="hero-section" style="background: linear-gradient(135deg, #1D1D1F 0%, #3A3A3C 100%);">
        <div style="text-align: center; position: relative; z-index: 1;">
            <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">Let's Build Something Amazing</h2>
            <p style="font-size: 1.2rem; opacity: 0.9; max-width: 600px; margin: 0 auto 2rem;">
                I'm always interested in hearing about new projects and opportunities. 
                Feel free to reach out if you'd like to collaborate!
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="mailto:{PROFILE['email']}" style="background: #007AFF; padding: 12px 24px; border-radius: 12px; 
                   color: white; text-decoration: none; font-weight: 600;">📧 Email Me</a>
                <a href="{PROFILE['linkedin']}" target="_blank" style="background: rgba(255,255,255,0.1); padding: 12px 24px; 
                   border-radius: 12px; color: white; text-decoration: none; font-weight: 600;">💼 LinkedIn</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    # Hero Section
    render_hero()
    
    # Stats
    render_stats()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main Navigation Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Overview",
        "🔧 Predictive Maintenance", 
        "🔐 SAP Access Governance",
        "🚌 Route Recommendation",
        "⏱️ Speed Predictor"
    ])
    
    with tab1:
        render_skills()
        st.markdown("<br>", unsafe_allow_html=True)
        render_projects()
    
    with tab2:
        demo_anomaly_detection()
    
    with tab3:
        demo_sod_violations()
    
    with tab4:
        demo_ridership()
    
    with tab5:
        demo_speed_prediction()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Contact
    render_contact()
    
    # Footer
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; color: #8E8E93; font-size: 0.85rem;">
        <p>© {datetime.now().year} {PROFILE['name']}. All rights reserved.</p>
        <p style="opacity: 0.7;">Happy coding! ❤️</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
