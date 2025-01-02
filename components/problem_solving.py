import streamlit as st
import plotly.graph_objects as go
import numpy as np
from utils import create_comparison_chart
from data.computer_data import COMPUTER_COMPARISONS

def render_problem_solving():
    st.header("Problem-Solving Capabilities")

    st.markdown("""
    Explore detailed comparisons of how quantum and classical computers approach and solve 
    different types of computational problems. Understand the strengths, limitations, and 
    optimal use cases for each computing paradigm.
    """)

    # Enhanced problem-solving comparison data
    problem_data = {
        'categories': [
            'Encryption', 'Database Search', 'Optimization', 
            'Machine Learning', 'Simulation', 'Integer Factoring',
            'Linear Systems'
        ],
        'classical': [60, 70, 50, 80, 40, 30, 75],
        'quantum': [95, 85, 90, 75, 95, 90, 85]
    }

    # Create problem-solving comparison chart
    fig = create_comparison_chart(
        problem_data,
        'Problem-Solving Capability Comparison',
        'Problem Types',
        'Efficiency Score'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Algorithm comparison section
    st.subheader("Algorithm Deep Dive")

    algorithm_type = st.selectbox(
        "Select Algorithm Category",
        ["Factorization", "Search", "Optimization", "Simulation"]
    )

    algorithm_details = {
        "Factorization": {
            "classical": {
                "name": "General Number Field Sieve",
                "complexity": "Sub-exponential time: L(n)[1/3, 1.923]",
                "example": "RSA-2048 factorization would take ~300 trillion years",
                "limitations": "Exponential scaling with number size"
            },
            "quantum": {
                "name": "Shor's Algorithm",
                "complexity": "O((log n)² × (log log n))",
                "example": "RSA-2048 factorization estimated in hours/days",
                "limitations": "Requires error-corrected quantum computer"
            }
        },
        "Search": {
            "classical": {
                "name": "Binary/Linear Search",
                "complexity": "O(log n) or O(n)",
                "example": "Finding item in sorted/unsorted database",
                "limitations": "Linear scaling with database size"
            },
            "quantum": {
                "name": "Grover's Algorithm",
                "complexity": "O(√n)",
                "example": "Quadratic speedup in unstructured search",
                "limitations": "Limited by quantum coherence time"
            }
        },
        "Optimization": {
            "classical": {
                "name": "Simulated Annealing",
                "complexity": "Problem-dependent, often exponential",
                "example": "Traveling Salesman Problem optimization",
                "limitations": "Can get stuck in local optima"
            },
            "quantum": {
                "name": "Quantum Annealing",
                "complexity": "Potentially polynomial for certain problems",
                "example": "Portfolio optimization, traffic routing",
                "limitations": "Limited by available quantum hardware"
            }
        },
        "Simulation": {
            "classical": {
                "name": "Molecular Dynamics",
                "complexity": "Exponential with particle count",
                "example": "Protein folding simulation",
                "limitations": "Exponential scaling with system size"
            },
            "quantum": {
                "name": "Quantum Phase Estimation",
                "complexity": "Polynomial in system size",
                "example": "Quantum chemistry simulation",
                "limitations": "Requires high qubit coherence"
            }
        }
    }

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Classical Algorithm")
        details = algorithm_details[algorithm_type]["classical"]
        st.markdown(f"""
        **Algorithm**: {details['name']}

        **Complexity**: {details['complexity']}

        **Example Application**: {details['example']}

        **Key Limitations**: {details['limitations']}
        """)

    with col2:
        st.markdown("### Quantum Algorithm")
        details = algorithm_details[algorithm_type]["quantum"]
        st.markdown(f"""
        **Algorithm**: {details['name']}

        **Complexity**: {details['complexity']}

        **Example Application**: {details['example']}

        **Key Limitations**: {details['limitations']}
        """)

    # Scaling visualization
    st.subheader("Algorithm Scaling Comparison")

    problem_size = np.linspace(1, 100, 100)
    scaling_data = {
        "Factorization": {
            "classical": np.exp(np.sqrt(problem_size)),
            "quantum": np.log(problem_size)**2
        },
        "Search": {
            "classical": problem_size,
            "quantum": np.sqrt(problem_size)
        },
        "Optimization": {
            "classical": 2**np.sqrt(problem_size),
            "quantum": problem_size**2
        },
        "Simulation": {
            "classical": 2**problem_size,
            "quantum": problem_size**3
        }
    }

    fig_scaling = go.Figure()
    fig_scaling.add_trace(go.Scatter(
        x=problem_size,
        y=scaling_data[algorithm_type]["classical"],
        name="Classical Algorithm",
        line=dict(color='blue')
    ))
    fig_scaling.add_trace(go.Scatter(
        x=problem_size,
        y=scaling_data[algorithm_type]["quantum"],
        name="Quantum Algorithm",
        line=dict(color='red')
    ))

    fig_scaling.update_layout(
        title=f"Algorithm Scaling: {algorithm_type}",
        xaxis_title="Problem Size",
        yaxis_title="Computational Resources Required",
        yaxis_type="log"
    )

    st.plotly_chart(fig_scaling, use_container_width=True)

    # Case studies section
    st.subheader("Real-World Case Studies")
    case_study = st.selectbox(
        "Select Case Study",
        ["Drug Discovery", "Financial Portfolio Optimization", "Climate Modeling", "Cryptography"]
    )

    case_studies = {
        "Drug Discovery": {
            "challenge": "Simulating molecular interactions for drug development",
            "classical_approach": "Approximate models, limited molecule size",
            "quantum_approach": "Direct quantum simulation of molecular behavior",
            "impact": "Potential 10-100x acceleration in drug discovery pipeline"
        },
        "Financial Portfolio Optimization": {
            "challenge": "Optimizing large portfolios with multiple constraints",
            "classical_approach": "Simplified models, local optimization",
            "quantum_approach": "Global optimization considering all variables",
            "impact": "More efficient portfolio management and risk assessment"
        },
        "Climate Modeling": {
            "challenge": "Simulating complex climate systems",
            "classical_approach": "Grid-based approximations, limited resolution",
            "quantum_approach": "Quantum-inspired algorithms for fluid dynamics",
            "impact": "More accurate long-term climate predictions"
        },
        "Cryptography": {
            "challenge": "Secure communication and data protection",
            "classical_approach": "RSA, elliptic curve cryptography",
            "quantum_approach": "Quantum key distribution, post-quantum cryptography",
            "impact": "Revolutionary changes in security infrastructure"
        }
    }

    st.markdown(f"""
    #### Challenge
    {case_studies[case_study]['challenge']}

    #### Classical Approach
    {case_studies[case_study]['classical_approach']}

    #### Quantum Approach
    {case_studies[case_study]['quantum_approach']}

    #### Potential Impact
    {case_studies[case_study]['impact']}
    """)