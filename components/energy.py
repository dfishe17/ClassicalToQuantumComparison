import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils import create_comparison_chart
from data.computer_data import COMPUTER_COMPARISONS

def render_energy_comparison():
    st.header("Energy Consumption Analysis")

    st.markdown("""
    Explore detailed energy consumption patterns and environmental impact of quantum and classical computers
    across different computing tasks and operational scenarios. This analysis helps understand the energy
    trade-offs between quantum and classical computing approaches.
    """)

    # Tabs for different energy aspects
    tab1, tab2, tab3 = st.tabs(["Consumption Patterns", "Environmental Impact", "Cost Analysis"])

    with tab1:
        # Enhanced energy consumption data
        energy_data = {
            'categories': [
                'Basic Operation', 'Complex Calculation', 
                'Data Processing', 'Algorithm Execution',
                'Machine Learning', 'Quantum Simulation'
            ],
            'classical': [10, 45, 30, 60, 80, 100],
            'quantum': [50, 20, 15, 25, 40, 15]
        }

        # Create energy consumption chart
        fig = create_comparison_chart(
            energy_data,
            'Energy Consumption Comparison',
            'Computing Tasks',
            'Energy Usage (kWh)'
        )
        st.plotly_chart(fig, use_container_width=True)

        # Time-based energy consumption
        st.subheader("24-Hour Energy Profile")
        times = list(range(24))
        classical_profile = [COMPUTER_COMPARISONS['energy_baseline']['classical']['idle'] + 
                           (COMPUTER_COMPARISONS['energy_baseline']['classical']['peak'] - 
                            COMPUTER_COMPARISONS['energy_baseline']['classical']['idle']) * 
                           (0.5 + 0.5 * abs(12 - t)/12) for t in times]
        quantum_profile = [COMPUTER_COMPARISONS['energy_baseline']['quantum']['idle'] + 
                         (COMPUTER_COMPARISONS['energy_baseline']['quantum']['peak'] - 
                          COMPUTER_COMPARISONS['energy_baseline']['quantum']['idle']) * 
                         (0.3 + 0.7 * abs(12 - t)/12) for t in times]

        fig_profile = go.Figure()
        fig_profile.add_trace(go.Scatter(x=times, y=classical_profile, name='Classical Computer',
                                       mode='lines', line=dict(color='blue')))
        fig_profile.add_trace(go.Scatter(x=times, y=quantum_profile, name='Quantum Computer',
                                       mode='lines', line=dict(color='red')))
        fig_profile.update_layout(title='24-Hour Energy Consumption Profile',
                                xaxis_title='Hour of Day',
                                yaxis_title='Power Consumption (Watts)')
        st.plotly_chart(fig_profile, use_container_width=True)

    with tab2:
        st.subheader("Environmental Impact")

        # Carbon footprint calculator
        st.markdown("""
        #### Carbon Footprint Estimation
        Calculate the carbon footprint based on energy consumption and local energy mix.
        """)

        energy_source = st.selectbox(
            "Select Primary Energy Source",
            ["Coal", "Natural Gas", "Nuclear", "Renewable"]
        )

        carbon_factors = {
            "Coal": 0.995,  # kg CO2/kWh
            "Natural Gas": 0.535,
            "Nuclear": 0.029,
            "Renewable": 0.005
        }

        hours = st.slider("Daily Operation Hours", 1, 24, 8)

        # Calculate carbon footprint
        classical_energy = sum(classical_profile[:hours])/1000  # Convert W to kW
        quantum_energy = sum(quantum_profile[:hours])/1000

        classical_carbon = classical_energy * carbon_factors[energy_source]
        quantum_carbon = quantum_energy * carbon_factors[energy_source]

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Classical Computer CO₂ (kg/day)", f"{classical_carbon:.2f}")
        with col2:
            st.metric("Quantum Computer CO₂ (kg/day)", f"{quantum_carbon:.2f}")

    with tab3:
        st.subheader("Operational Cost Analysis")

        # Cost calculator
        electricity_rate = st.slider("Electricity Rate ($/kWh)", 0.05, 0.50, 0.12, 0.01)
        daily_cost_classical = classical_energy * electricity_rate
        daily_cost_quantum = quantum_energy * electricity_rate

        st.markdown("#### Daily Operating Costs")
        col3, col4 = st.columns(2)
        with col3:
            st.metric("Classical Computer Cost", f"${daily_cost_classical:.2f}")
        with col4:
            st.metric("Quantum Computer Cost", f"${daily_cost_quantum:.2f}")

        # ROI Calculator
        st.markdown("#### Return on Investment (ROI) Calculator")
        task_type = st.selectbox(
            "Select Computing Task",
            list(energy_data['categories'])
        )

        # Calculate time and cost savings
        task_index = energy_data['categories'].index(task_type)
        classical_time = 100  # baseline hours
        quantum_time = classical_time * (energy_data['classical'][task_index] / 
                                       energy_data['quantum'][task_index])

        st.markdown(f"""
        #### Estimated Time Savings
        - Classical Computing Time: {classical_time:.0f} hours
        - Quantum Computing Time: {quantum_time:.0f} hours
        - Time Saved: {classical_time - quantum_time:.0f} hours
        """)