"""
Portfolio Configuration
Personal Information and Project Details
"""

# ============================================================================
# PERSONAL INFORMATION (Update with your details)
# ============================================================================

PROFILE = {
    "name": "Fahmi Taib",
    "title": "AI/ML Engineer",
    "tagline": "Transforming complex business challenges into intelligent solutions",
    "location": "Malaysia",
    "experience_years": 3,
    "email": "fahmi.taib@email.com",  # Update this
    "linkedin": "https://linkedin.com/in/fahmidev",
    "github": "https://github.com/yourprofile",  # Update this
    "status": "Open to Opportunities",
    "education": "BSc Computer Science, University of Malaya",
}

# ============================================================================
# PROFESSIONAL SUMMARY
# ============================================================================

SUMMARY = """
AI/ML Engineer with 3+ years of experience designing and deploying machine learning 
solutions that drive real business value. University of Malaya graduate with expertise in 
Predictive Maintenance, Telematics Analytics, and Enterprise AI Systems. Background in 
DevOps testing and automation. Proven track record of delivering production-ready ML models 
with measurable impact on operational efficiency.
"""

# ============================================================================
# SKILLS CONFIGURATION
# ============================================================================

SKILLS = {
    "Machine Learning": {
        "icon": "🤖",
        "skills": [
            ("Scikit-learn", 95),
            ("XGBoost / LightGBM", 90),
            ("TensorFlow / Keras", 85),
            ("PyTorch", 80),
            ("SHAP Explainability", 85),
        ]
    },
    "Data Engineering": {
        "icon": "📊",
        "skills": [
            ("Python / Pandas", 95),
            ("SQL / PostgreSQL", 90),
            ("Apache Spark", 75),
            ("ETL Pipelines", 85),
            ("Feature Engineering", 90),
        ]
    },
    "Cloud & Deployment": {
        "icon": "☁️",
        "skills": [
            ("Azure ML / AML", 90),
            ("Docker / Kubernetes", 80),
            ("FastAPI / Streamlit", 95),
            ("MLflow / MLOps", 85),
            ("CI/CD Pipelines", 80),
        ]
    }
}

# ============================================================================
# PROJECTS CONFIGURATION
# ============================================================================

PROJECTS = [
    {
        "id": "pdm",
        "icon": "🔧",
        "color": "linear-gradient(135deg, #FF6B6B, #FF8E53)",
        "title": "Predictive Maintenance System",
        "short_title": "PdM",
        "description": "Deep Learning-based anomaly detection for bus fleet using Autoencoders. Monitors 17+ IoT sensors in real-time to predict failures before they occur.",
        "detailed_description": """
        Built an end-to-end predictive maintenance system for Prasarana Malaysia's bus fleet:
        
        - **Autoencoder Neural Network** for unsupervised anomaly detection
        - **17+ IoT Sensors** monitored including engine temp, vibration, fuel rate
        - **MLflow Integration** for experiment tracking and model versioning
        - **Azure ML Deployment** for scalable inference
        - **Real-time Alerts** for maintenance team notifications
        """,
        "technologies": ["TensorFlow", "Autoencoder", "MLflow", "Azure ML", "Gradio", "Python"],
        "metrics": {
            "Accuracy": "94%",
            "F1 Score": "0.91",
            "Buses Monitored": "6+",
            "Sensors": "17+"
        },
        "impact": [
            "Reduced unplanned downtime by 30%",
            "Early detection of 89% of critical failures",
            "Cost savings of RM 200K annually"
        ]
    },
    {
        "id": "iga",
        "icon": "🔐",
        "color": "linear-gradient(135deg, #4ECDC4, #44A08D)",
        "title": "SAP Access Governance (IGA)",
        "short_title": "IGA",
        "description": "Enterprise Identity Governance system with ML-based anomaly detection and Segregation of Duties (SoD) violation detection for SAP environments.",
        "detailed_description": """
        Developed a comprehensive Identity Governance and Administration system similar to Saviynt:
        
        - **Isolation Forest** for anomaly detection in user access patterns
        - **19 SAP Standard SoD Rules** covering Finance, MM, SD, HR, and Basis
        - **Collaborative Filtering** for intelligent role recommendations
        - **Interactive Dashboard** with real-time risk visualization
        - **Audit-Ready Reports** for SOX, GDPR compliance
        """,
        "technologies": ["Isolation Forest", "Collaborative Filtering", "Streamlit", "Plotly", "Pandas"],
        "metrics": {
            "SoD Rules": "19+",
            "Users Analyzed": "1000+",
            "Risk Levels": "4",
            "T-codes Mapped": "100+"
        },
        "impact": [
            "Automated detection of 150+ SoD violations",
            "80% reduction in manual audit time",
            "Full compliance with SOX requirements"
        ]
    },
    {
        "id": "swiftroute",
        "icon": "🚌",
        "color": "linear-gradient(135deg, #667eea, #764ba2)",
        "title": "SwiftRoute AI Recommendation",
        "short_title": "SwiftRoute",
        "description": "AI-powered bus route recommendation system for disruption management. Predicts optimal replacement routes and ridership demand in real-time.",
        "detailed_description": """
        Enterprise-grade route recommendation system for Prasarana Malaysia:
        
        - **Multi-Model Ensemble** (XGBoost, KNN, Random Forest) for route prediction
        - **Real-time Ridership Forecasting** using time-series analysis
        - **FastAPI Backend** with sub-500ms response time
        - **Azure App Service** deployment with auto-scaling
        - **Apple-Inspired Dashboard** for operations control center
        """,
        "technologies": ["XGBoost", "KNN", "FastAPI", "Azure App Service", "Streamlit", "Folium"],
        "metrics": {
            "Routes": "200+",
            "Accuracy": "92%",
            "Response": "<500ms",
            "Daily Predictions": "5000+"
        },
        "impact": [
            "Improved disruption response time by 45%",
            "Optimized resource allocation during incidents",
            "Enhanced passenger experience during disruptions"
        ]
    },
    {
        "id": "punctuality",
        "icon": "⏱️",
        "color": "linear-gradient(135deg, #f093fb, #f5576c)",
        "title": "Bus Punctuality Predictor",
        "short_title": "Punctuality",
        "description": "Real-time optimal speed prediction for bus captains to maintain schedule adherence. Features interactive SHAP explanations for model transparency.",
        "detailed_description": """
        AI-powered speed recommendation system for bus schedule adherence:
        
        - **Random Forest Regressor** trained on historical GPS and traffic data
        - **SHAP Integration** for model explainability and transparency
        - **Real-time Traffic Integration** using live API data
        - **Interactive Map Interface** with PyDeck visualization
        - **Gamification Features** to engage bus captains
        """,
        "technologies": ["Random Forest", "SHAP", "Streamlit", "PyDeck", "Joblib"],
        "metrics": {
            "Segments": "20+",
            "RMSE": "2.3 km/h",
            "Captains": "100+",
            "Punctuality Improvement": "15%"
        },
        "impact": [
            "15% improvement in on-time performance",
            "Reduced passenger complaints by 25%",
            "Enhanced driver safety with optimal speed guidance"
        ]
    }
]

# ============================================================================
# EXPERIENCE TIMELINE
# ============================================================================

EXPERIENCE = [
    {
        "role": "Senior AI/ML Engineer",
        "company": "Prasarana Malaysia Berhad",
        "duration": "Nov 2024 - Present",
        "location": "Malaysia · Hybrid",
        "highlights": [
            "Developing predictive maintenance systems for bus fleet using Deep Learning",
            "Building anomaly detection models with Autoencoders for IoT sensor data",
            "Deploying ML models to production using Azure ML and MLflow",
            "Working on telematics analytics for transport optimization"
        ]
    },
    {
        "role": "Junior AI/ML Engineer",
        "company": "Pickles Asia Sdn Bhd",
        "duration": "Jan 2023 - Nov 2024",
        "location": "Kuala Lumpur · On-site",
        "highlights": [
            "Built and deployed machine learning models for business automation",
            "Developed data pipelines and ETL processes for ML workflows",
            "Implemented NLP solutions for text analysis and classification",
            "Collaborated with cross-functional teams on AI initiatives"
        ]
    },
    {
        "role": "DevOps Intern",
        "company": "RHB Banking Group",
        "duration": "Aug 2020 - Feb 2021",
        "location": "Kuala Lumpur · Hybrid",
        "highlights": [
            "Designed, developed and maintained automated scripts for black-box testing",
            "Designed QA and testing strategies for banking applications",
            "Executed test cases during development sprints",
            "Worked in cross-functional Agile Scrum team"
        ]
    },
]

# ============================================================================
# EDUCATION
# ============================================================================

EDUCATION = [
    {
        "degree": "Bachelor's Degree, Computer Science",
        "institution": "University of Malaya",
        "duration": "2018 - 2022",
        "grade": "CGPA: 3.67",
        "highlights": [
            "Algorithm, Mathematics and Statistics coursework",
            "Machine Learning & Data Structures coursework",
            "Fall Semester - IT Exchange Program to Zurich, Switzerland"
        ]
    },
    {
        "degree": "Foundation in Engineering",
        "institution": "Universiti Teknologi MARA (UiTM)",
        "duration": "2017 - 2018",
        "grade": "CGPA: 3.69",
        "highlights": ["Mathematics","Statistics","Python Programming Language"]
    }
]

# ============================================================================
# CERTIFICATIONS
# ============================================================================

CERTIFICATIONS = [
    {
        "name": "ASEAN AI Summit Kuala Lumpur 2025",
        "issuer": "Exhibitor & Participant",
        "year": 2025,
        "description": "Exhibited AI/ML solutions at Southeast Asia's premier AI conference",
        "skills": ["AI Innovation", "Industry Networking", "Tech Exhibition"]
    },
    {
        "name": "AI Hackathon for Public Sector",
        "issuer": "Microsoft",
        "year": 2025,
        "description": "Supercharging Malaysia Public Services with Microsoft AI Platform",
        "skills": ["Azure AI Foundry", "Azure ML", "Azure OpenAI", "Cosmos DB"]
    },
    {
        "name": "Certified AI Practitioner (CAIP)",
        "issuer": "CertNexus",
        "year": 2024,
        "description": "Professional certification in AI/ML methodologies",
        "skills": ["Machine Learning", "Data Engineering", "Model Training"]
    },
]

# ============================================================================
# DEMO DATA CONFIGURATION
# ============================================================================

DEMO_CONFIG = {
    "anomaly_detection": {
        "n_records": 1000,
        "n_buses": 6,
        "anomaly_rate": 0.05,
        "sensors": [
            'Engine Temperature (°C)',
            'Engine Load (%)',
            'Fuel Rate (L/h)',
            'Vibration',
            'Board Voltage (V)',
            'RPM'
        ]
    },
    "sod": {
        "n_users": 50,
        "n_violations": 100,
        "rules": [
            ("AP01", "Create Vendor vs Pay Vendor", "Critical"),
            ("GL01", "Create GL Account vs Post to GL", "High"),
            ("MM01", "Create PO vs Goods Receipt", "Medium"),
            ("SD01", "Create Customer vs Process Sales", "High"),
            ("HR01", "Maintain Employee vs Payroll Processing", "Critical"),
        ]
    },
    "ridership": {
        "n_routes": 10,
        "hours": list(range(24)),
        "peak_hours": [(7, 9), (17, 19)]
    },
    "speed": {
        "n_segments": 20,
        "traffic_levels": ['Light', 'Moderate', 'Heavy'],
        "weather_conditions": ['Clear', 'Rainy', 'Cloudy']
    }
}
