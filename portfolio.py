import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ---------- #
st.set_page_config(page_title="Atishay Jain Portfolio", page_icon="📊", layout="wide")
custom_css = """
<style>
/* Body font and color */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #222222;
    background-color: #f9f9f9;
}

/* Sidebar background and text */
[data-testid="stSidebar"] {
    background-color: #1e1e2f;
    color: #ffffff;
    padding: 1rem 1.5rem;
}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: #ffcc00;
}

/* Sidebar radio buttons styling */
[data-testid="stSidebar"] .stRadio > label {
    color: #ffcc00;
    font-weight: 600;
}

/* Main page headers */
h1 {
    color: #003366;
    font-weight: 700;
    margin-bottom: 0.2rem;
}

h2, h3 {
    color: #004080;
    font-weight: 600;
    margin-top: 1.2rem;
    margin-bottom: 0.5rem;
}

/* Links style */
a {
    color: #0066cc;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

/* Horizontal rule styling */
hr {
    border: 1px solid #ddd;
    margin: 1.5rem 0;
}

/* Subheaders */
h4 {
    color: #333333;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

/* Columns spacing */
[data-testid="stVerticalBlock"] > div {
    padding-right: 1.5rem;
}

/* Contact section number styling */
.contact-number {
    font-size: 1.2rem;
    font-weight: 600;
    color: #003366;
}

/* Project list styling */
ul {
    list-style-type: square;
    margin-left: 1.2rem;
}

/* Code blocks */
code {
    background-color: #eee;
    padding: 2px 6px;
    border-radius: 4px;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
# ---------- SIDEBAR NAVIGATION ---------- #
with st.sidebar:
    st.title("👨‍💻 Navigation")
    page = st.radio("Go to", ["Home", "About Me", "Projects", "Resume", "Contact"])

# ---------- HOME PAGE ---------- #
if page == "Home":
    st.title("👋 Hi, I'm Atishay Jain")
    st.subheader("Data Science Student | ML Enthusiast | IIT Patna")

    st.write("""
    I'm a passionate data science student currently in my 2nd year at IIT Patna. I build practical ML projects, love solving problems with data, 
    and aim to contribute meaningfully to real-world AI solutions.
    """)

    st.markdown("---")
    
    col1, col2 = st.columns(2)

    with col1:
        st.header("🔧 Skills")
        st.write("""
        - Languages: Python, SQL, HTML, CSS
        - Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
        - Tools: Git, GitHub, Jupyter Notebook, Power BI
        - Concepts: EDA, Handling Imbalanced Data (SMOTE), Regression, Decision Trees, Hyperparameter Tuning
        - Deployment: Streamlit, Model Serialization (Pickle/Joblib)
        - Databases: MySQL (Joins, Aggregations, DDL/DML)
        """)

    with col2:
        st.header("🏆 Highlights")
        st.write("""
        - 📈 Led end-to-end ML pipeline in national-level hackathon (Devfolio)
        - � Built CEO-level Power BI dashboards for business decisions (TATA Forage)
        - 🚀 Deployed interactive Streamlit apps with real-time feedback <2s
        - 📚 CGPA: 8.47 | JEE Percentile: 91%ile | IIT Patna BSc DS
        """)

# ---------- ABOUT PAGE ---------- #
elif page == "About Me":
    st.title("📘 About Me")
    st.write("""
    I'm Atishay Jain, a B.Sc (Hons) Data Science student at IIT Patna (2024–2027).
    I'm passionate about solving real-world problems with machine learning and analytics.

    I've worked on projects that span ML model building, imbalanced classification, and business dashboarding.
    I'm a fast learner, able to independently lead projects end-to-end — from data cleaning to deployment.
    """)

    st.subheader("🎓 Education")
    st.write("""
    - **Indian Institute of Technology Patna**  
      B.Sc in Computer Science and Data Analytics (2024–2027)  
      CGPA: 8.47 / 10
    """)

    st.subheader("💼 Experience")
    st.write("""
    - **Devfolio Hackathon (Holboxathon)** – May 2025  
      • Led ML pipeline for imbalanced classification (SMOTE, GridSearchCV)  
      • Deployed Streamlit app with <2s response time, F1-score 0.82

    - **TATA Group – Forage Intern** – Jan 2025  
      • Created interactive Power BI dashboards simulating CEO decision-making  
      • Proposed business insights that modeled a 5% revenue lift
    """)

    st.subheader("📜 Certifications")
    st.write("""
    - SQL for Data Science – SQLBolt
    - Machine Learning Fundamentals – Krish Naik
    - Version Control with Git and GitHub
    - Data Visualization Virtual Experience – Tata Group (Forage)
    - Web Scraping – Coursevita
    - HTML/CSS & Python – Infosys & Great Learning
    """)


# ---------- PROJECTS PAGE ---------- #
elif page == "Projects":
    st.title("🛠 Projects")

    st.subheader("📌 Imbalanced Classification – Devfolio Hackathon")
    st.write("""
    - Built and deployed an ML model to tackle an imbalanced dataset (SMOTE + Random Forest)
    - Achieved **F1-score of 0.82**, improving baseline by 25%
    - Used **GridSearchCV** for hyperparameter tuning and deployed via **Streamlit** with <2s prediction time
    **GitHub:** [AtishayJain](https://github.com/Atishaygang/Coustmer-churn-predictor) 
    """)

    st.subheader("📌 Power BI Business Dashboard – TATA Forage")
    st.write("""
    - Created interactive dashboards using **Power BI** simulating CEO-level insights
    - Revealed a 15% drop in Q3 sales and proposed strategies for a 5% improvement in revenue
    """)

    st.subheader("📌 Titanic Survval Project – Linear Regression")
    st.write("""
    - Used **Scikit-learn** for regression modeling and evaluated with **R² and MSE**
    - Cleaned and visualized data using Pandas and Seaborn
    **GitHub:** [AtishayJain](https://github.com/Atishaygang/ML-Projects/tree/main/Linear_regression_titanic_project) 
    """)

    st.subheader("📌 Loan Approval Project – Logistic Regression")
    st.write("""
    - Applied **Logistic Regression** to predict survival with 79% accuracy
    - Used sklearn pipelines and preprocessing techniques
    **GitHub:** [AtishayJain](https://github.com/Atishaygang/ML-Projects/tree/main/Logistic_regression_Loan_approval_project) 
    """)

    st.subheader("📌 Bank Full dataset – Decision Tree (Pre-Pruning)")
    st.write("""
    - Built pre-pruned **Decision Tree Classifier** for health dataset analysis
    - Visualized patterns and risk factors with Seaborn and Matplotlib
    **GitHub:** [AtishayJain](https://github.com/Atishaygang/ML-Projects/tree/main/Decision_tree_pre_prunning)
    """)

    st.subheader("📌 Decision Tree Classifier – Post-Pruning")
    st.write("""
    - Implemented **Post-pruning** to reduce overfitting and improve accuracy
    - Reduced model complexity while maintaining strong evaluation scores
    **GitHub:** [AtishayJain](https://github.com/Atishaygang/ML-Projects)
    """)

    st.subheader("📌 NumPy and Pandas EDA Project")
    st.write("""
    - Performed deep exploratory data analysis on large datasets
    - Handled missing values and visualized insights through plots
    **GitHub:** [AtishayJain](https://github.com/Atishaygang/ML-Projects)
    """)

# ---------- RESUME PAGE ---------- #
elif page == "Resume":
    st.title("📄 Resume - Atishay Jain")
    st.markdown("---")
    
    # Contact Information
    st.header("📬 Contact Information")
    st.write("""
    **Email:** Atishay.jainn.1008@gmail.com  
    **Phone:** +91-9084907534  
    **Location:** New Delhi, INDIA  
    **GitHub:** [AtishayJain](https://github.com/Atishaygang)  
    **LinkedIn:** [Atishay Jain](https://www.linkedin.com/in/atishay-jain-718014313/)
    """)
    
    st.markdown("---")
    
    # Professional Summary
    st.header("👨‍💻 Professional Summary")
    st.write("""
    Aspiring Data Scientist with a BSc degree and strong hands-on experience in Python, machine learning, and data analysis. 
    Despite not holding an MSc or PhD, I have completed advanced projects and certifications demonstrating my ability to 
    deliver business value through data-driven insights.
    """)
    
    st.markdown("---")
    
    # Experience
    st.header("💼 Experience")
    
    # Devfolio Experience
    st.subheader("**Devfolio** | SOLO ML HACKATHON (HOLBOXATHON)")
    st.caption("May 2025 – May 2025 | Virtual")
    st.write("""
    - Led end-to-end ML pipeline for a highly imbalanced classification problem
    - Used **SMOTE** to balance the dataset and improve minority class performance
    - Achieved **F1-score of 0.82**, improving baseline by **25%**
    - Applied **GridSearchCV** for hyperparameter tuning to optimize model performance
    - Deployed solution using Streamlit with **real-time predictions (<2s response time)** and interactive UI
    """)
    
    # TATA Experience
    st.subheader("**TATA GROUP VIA FORAGE** | INTERN")
    st.caption("Jan 2025 – Jan 2025 | Virtual")
    st.write("""
    - Practiced framing business scenarios, choosing impactful visuals, and communicating insights clearly
    - Built dashboards that revealed a **15% decline in Q3 sales**, helping direct marketing attention
    - Used **Power BI** to analyze business data and create interactive dashboards and graphs
    - Interpreted data to support business decisions from a **CEO's perspective** in simulated scenarios
    - Proposed data-driven insights that simulated a **5% improvement in revenue projections**
    """)
    
    st.markdown("---")
    
    # Projects
    st.header("🛠 Projects")
    
    # Imbalanced Classification Project
    st.subheader("**IMBALANCED CLASSIFICATION** | PATH-PLANNING LEAD")
    st.caption("May 2025 – Present | Virtual")
    st.write("""
    - Tools: Scikit-learn, SMOTE, Random Forest, Streamlit
    - Deployed a Streamlit web app that could process **100+ inputs/hour with live feedback**
    - Achieved **recall improvement of 42%** on minority class
    - Applied **GridSearchCV** for hyperparameter tuning
    """)
    
    # Power BI Project
    st.subheader("**POWER BI BUSINESS DASHBOARD** | TATA FORAGE")
    st.caption("Jan 2025 – Jan 2025 | Virtual")
    st.write("""
    - Simulated CEO-level decision-making based on visual data interpretation
    - Improved business strategies through data-driven recommendations
    - Built dashboards to analyze business metrics, sales trends, and customer insights
    """)
    
    st.markdown("---")
    
    # Education
    st.header("🎓 Education")
    st.subheader("**IIT Patna**")
    st.write("""
    BACHELOR OF SCIENCE IN COMPUTER SCIENCE AND DATA ANALYTICS  
    Expected June 2027 | Patna, Bihar  
    Cum. CGPA: 8.47 / 10
    """)
    
    st.markdown("---")
    
    # Skills
    st.header("🛠 Skills")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("**Programming**")
        st.write("""
        - Python (NumPy, Pandas, Matplotlib, Seaborn)
        - SQL
        - HTML/CSS
        """)
        
        st.subheader("**Machine Learning**")
        st.write("""
        - Linear Regression, Logistic Regression
        - Decision Tree, Random Forest, KNN
        - Model Evaluation (Accuracy, Precision, Recall, F1-Score, ROC-AUC)
        - Hyperparameter Tuning
        """)
    
    with col2:
        st.subheader("**Technology**")
        st.write("""
        - Scikit-learn, Streamlit
        - Jupyter Notebook, Git & GitHub
        - PySpark (beginner)
        - Power BI
        """)
        
        st.subheader("**Data Handling**")
        st.write("""
        - Data Cleaning, EDA
        - Handling Imbalanced Data (SMOTE)
        - Data Visualization, Statistics
        - Model Deployment (Streamlit, Pickle/Joblib)
        """)
        
        st.subheader("**Databases**")
        st.write("""
        - MySQL (Joins, Subqueries, Aggregations, DDL, DML)
        """)

# ---------- CONTACT PAGE ---------- #
elif page == "Contact":
    st.title("📩 Contact Me")
    st.write("""
    Feel free to reach out for collaborations or opportunities!
    - Number: 9084907534
    """)
    
    
