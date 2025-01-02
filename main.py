import streamlit as st
from components import comparison, energy, problem_solving

st.set_page_config(
    page_title="Quantum vs Classical Computing",
    page_icon="🔄",
    layout="wide"
)

def main():
    st.title("Quantum vs Classical Computing: An Interactive Comparison")
    
    st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTabs {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["Overview", "Energy Consumption", "Problem Solving Capabilities"])
    
    with tabs[0]:
        comparison.render_comparison()
    
    with tabs[1]:
        energy.render_energy_comparison()
    
    with tabs[2]:
        problem_solving.render_problem_solving()

    st.sidebar.title("Navigation")
    st.sidebar.info("""
    This interactive platform helps you understand the key differences between quantum 
    and classical computers. Explore different sections using the tabs above.
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### About
    This educational platform provides:
    - Interactive visualizations
    - Energy consumption comparisons
    - Problem-solving capabilities analysis
    - Real-world applications
    """)

if __name__ == "__main__":
    main()
