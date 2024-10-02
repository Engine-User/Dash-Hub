import streamlit as st
import os
from PIL import Image

# Set page config
st.set_page_config(page_title="Dashboard Hub", layout="wide")

# Custom CSS for dark theme, color scheme, Graduate font, and stylish border
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Graduate&display=swap');

    * {
        font-family: 'Graduate', cursive;
    }
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }

    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #0066CC;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0052A3;
        transform: scale(1.05);
    }

    .project-title {
        color: #FF4B4B;
        font-size: 24px;
        font-weight: bold;
    }
    .project-description {
        font-size: 16px;
        margin-bottom: 20px;
    }
    .project-link {
        color: #0066CC;
        text-decoration: none;
    }
    .project-link:hover {
        text-decoration: underline;
    }
    
    }
    .about-me {
        background-color: #2D2D2D;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Graduate', cursive;
    }
    .title-border {
        border: none;
        height: 5px;
        background: linear-gradient(90deg, #FF4B4B, #0066CC);
        margin-bottom: 20px;
        position: relative;
    }
    .title-border::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #0066CC, #FF4B4B);
    }
</style>
""", unsafe_allow_html=True)

# Function to safely load an image
def load_image(image_path):
    try:
        return Image.open(image_path)
    except Exception as e:
        st.warning(f"Unable to load image: {image_path}")
        st.error(f"Error: {e}")
        return None

# Sidebar
with st.sidebar:
    st.markdown('<div class="about-me">', unsafe_allow_html=True)
    st.markdown("## About Me")
    st.markdown("""
    Hello! I am Archisman

    - <span style="color: red;">Passionate</span> Data Analyst and Engineer
    - <span style="color: red;">Expertise</span> in creating insightful dashboards and data-driven solutions
    - <span style="color: red;">Skills</span> include:
        - Data visualization
        - Statistical analysis
        - Machine learning
    - <span style="color: red;">Techinal & Analytical</span> Expertise in:
        - SQL
        - Power BI
        - Tableau
        - Python
        - Streamlit
        - PowerQuery
    - <span style="color: red;">Email:</span> [ggengineerco@gmail.com](mailto:ggengineerco@gmail.com)
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Main content
st.title("Dashboard Hub")
st.markdown('<div class="title-border"></div>', unsafe_allow_html=True)

# Function to create a project tile
def create_project_tile(title, images, description, tech_stack, project_link, github_repo):
    with st.container():
        st.markdown('<div class="project-tile">', unsafe_allow_html=True)
        st.markdown(f'<p class="project-title">{title}</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        for i, image_path in enumerate(images):
            image = load_image(image_path)
            if image:
                if i == 0:
                    col1.image(image, use_column_width=True, caption=f'{title} - A')
                else:
                    col2.image(image, use_column_width=True, caption=f'{title} - B')
        
        st.markdown(f'<p class="project-description">{description}</p>', unsafe_allow_html=True)
        st.markdown(f'<span style="color: red;">**Tech Stack:**</span> {tech_stack}', unsafe_allow_html=True)
        st.markdown(f'[View Project]({project_link})', unsafe_allow_html=True)
        st.markdown(f'[GitHub Repository]({github_repo})', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-border"></div>', unsafe_allow_html=True)

# Project 3: Indian Stocks Dashboard
create_project_tile(
    "Indian Stocks Dashboard",
    ["images/indian_stocks_1.png", "images/indian_stocks_2.png"],
    "A specialized dashboard focusing on the Indian stock market, providing insights into Nifty 50 and BSE Sensex.",
    "Python, Numpy, Pandas, Streamlit, Plotly, YFinance for data",
    "https://indianstocks.streamlit.app",
    "https://github.com/Engine-User/Stocks_Dashboard.git"
)

# Project 1: Crypto Dashboard
create_project_tile(
    "Crypto Dashboard",
    ["images/crypto_dashboard_1.png", "images/crypto_dashboard_2.png"],
    "A comprehensive cryptocurrency dashboard showcasing real-time market data, trends, and portfolio analytics.",
    "Power BI, Python, Streamlit, Plotly, YFinance for data",
    "https://github.com/Engine-User/Crypto-DB.git",
    "https://github.com/Engine-User/Crypto-DB.git"
)

# Project 4: Data Science Dashboard
create_project_tile(
    "Data Science Dashboard",
    ["images/data_science_1.png", "images/data_science_2.png"],
    "A multi-faceted dashboard showcasing how much Data science and related Job titles are in demand, across the globe.",
    "Tableau, Python",
    "https://public.tableau.com/app/profile/archisman.kundu/viz/DataScienceAcrossTheGlobe/Dashboard1",
    "https://github.com/Engine-User/DataSc-DB.git"
)
# Project 2: Stocks Dashboard
create_project_tile(
    "International Stocks Dashboard",
    ["images/stocks_dashboard_1.png", "images/stocks_dashboard_2.png"],
    "A comprehensive Stocks dashboard showcasing real-time market data, trends, and portfolio analytics.",
    "Power BI, Python, Streamlit, Plotly, YFinance for data",
    "https://github.com/Engine-User/Stocks-DB.git",
    "https://github.com/Engine-User/Stocks-DB.git"
)



