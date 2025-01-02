import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def create_comparison_chart(data, title, x_label, y_label):
    """Create a comparative bar chart using Plotly"""
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data['categories'],
        y=data['classical'],
        name='Classical Computer',
        marker_color='#1f77b4'
    ))

    fig.add_trace(go.Bar(
        x=data['categories'],
        y=data['quantum'],
        name='Quantum Computer',
        marker_color='#ff7f0e'
    ))

    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        barmode='group',
        template='plotly_white'
    )

    return fig

def create_radar_chart(categories, classical_values, quantum_values):
    """Create a radar chart comparing classical and quantum computers"""
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=classical_values,
        theta=categories,
        fill='toself',
        name='Classical Computer'
    ))

    fig.add_trace(go.Scatterpolar(
        r=quantum_values,
        theta=categories,
        fill='toself',
        name='Quantum Computer'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=True
    )

    return fig

def create_3d_performance_surface(max_size=50, max_complexity=50):
    """Create a 3D surface plot comparing performance scaling"""
    problem_size = np.linspace(1, max_size, 50)
    problem_complexity = np.linspace(1, max_complexity, 50)
    size_grid, complexity_grid = np.meshgrid(problem_size, problem_complexity)

    # Classical computation time (exponential with both size and complexity)
    classical_time = np.exp(size_grid/max_size + complexity_grid/max_complexity)

    # Quantum computation time (polynomial with size, logarithmic with complexity)
    quantum_time = (size_grid/5)**2 * np.log2(complexity_grid + 1)

    fig = go.Figure()

    # Classical surface
    fig.add_trace(go.Surface(
        x=size_grid,
        y=complexity_grid,
        z=classical_time,
        name='Classical',
        colorscale='Blues',
        showscale=False,
        opacity=0.8
    ))

    # Quantum surface
    fig.add_trace(go.Surface(
        x=size_grid,
        y=complexity_grid,
        z=quantum_time,
        name='Quantum',
        colorscale='Oranges',
        showscale=False,
        opacity=0.8
    ))

    fig.update_layout(
        title='Performance Scaling: Quantum vs Classical',
        scene=dict(
            xaxis_title='Problem Size',
            yaxis_title='Problem Complexity',
            zaxis_title='Computation Time (log scale)',
            zaxis=dict(type='log')
        ),
        width=800,
        height=800
    )

    return fig

def create_energy_3d_bars():
    """Create a 3D visualization comparing energy consumption"""
    # Data from COMPUTER_COMPARISONS energy baseline
    operations = ['Idle', 'Basic', 'Medium', 'Complex']
    computers = ['Classical', 'Quantum']

    classical_energy = [65, 150, 250, 350]  # From DOE data
    quantum_energy = [1500, 15000, 21000, 27000]  # From Google Quantum AI Lab

    # Create coordinates for 3D bars
    x_classical = [0] * len(operations)
    x_quantum = [1] * len(operations)
    y_positions = list(range(len(operations)))

    fig = go.Figure()

    # Classical computer trace
    fig.add_trace(go.Scatter3d(
        x=x_classical,
        y=y_positions,
        z=classical_energy,
        mode='lines+markers',
        name='Classical',
        line=dict(color='blue', width=10),
        marker=dict(size=8, color='blue')
    ))

    # Quantum computer trace
    fig.add_trace(go.Scatter3d(
        x=x_quantum,
        y=y_positions,
        z=quantum_energy,
        mode='lines+markers',
        name='Quantum',
        line=dict(color='orange', width=10),
        marker=dict(size=8, color='orange')
    ))

    fig.update_layout(
        title='Energy Consumption Across Operation Types',
        scene=dict(
            xaxis=dict(
                title='Computer Type',
                ticktext=['Classical', 'Quantum'],
                tickvals=[0, 1],
                range=[-0.5, 1.5]
            ),
            yaxis=dict(
                title='Operation Complexity',
                ticktext=operations,
                tickvals=list(range(len(operations)))
            ),
            zaxis=dict(
                title='Energy (Watts)',
                type='log'
            ),
        ),
        width=800,
        height=800,
        showlegend=True
    )

    return fig

def create_interactive_scaling_animation(algorithm_type="Search"):
    """Create an animated 2D scatter plot showing computational scaling"""
    frames = []
    problem_sizes = np.linspace(1, 100, 50)

    scaling_functions = {
        "Search": {
            "classical": lambda n: n,  # O(n)
            "quantum": lambda n: np.sqrt(n)  # O(√n)
        },
        "Factoring": {
            "classical": lambda n: np.exp(np.sqrt(n)),  # Exponential
            "quantum": lambda n: np.log2(n)**2  # Polynomial
        }
    }

    # Create frames for animation
    for i in range(len(problem_sizes)):
        classical_times = scaling_functions[algorithm_type]["classical"](problem_sizes[:i+1])
        quantum_times = scaling_functions[algorithm_type]["quantum"](problem_sizes[:i+1])

        frame = go.Frame(
            data=[
                go.Scatter(
                    x=problem_sizes[:i+1],
                    y=classical_times,
                    mode='lines+markers',
                    name='Classical',
                    line=dict(color='blue')
                ),
                go.Scatter(
                    x=problem_sizes[:i+1],
                    y=quantum_times,
                    mode='lines+markers',
                    name='Quantum',
                    line=dict(color='orange')
                )
            ]
        )
        frames.append(frame)

    # Create the base figure
    fig = go.Figure(
        frames=frames,
        layout=go.Layout(
            title=f'Algorithm Scaling: {algorithm_type}',
            xaxis=dict(title='Problem Size', range=[0, 100]),
            yaxis=dict(title='Computation Time', type='log'),
            updatemenus=[dict(
                type='buttons',
                showactive=False,
                buttons=[
                    dict(label='Play',
                         method='animate',
                         args=[None, {'frame': {'duration': 50, 'redraw': True},
                                    'fromcurrent': True}]),
                    dict(label='Pause',
                         method='animate',
                         args=[[None], {'frame': {'duration': 0, 'redraw': False},
                                      'mode': 'immediate',
                                      'transition': {'duration': 0}}])
                ]
            )]
        )
    )

    # Add the initial data
    fig.add_trace(go.Scatter(
        x=[problem_sizes[0]],
        y=[scaling_functions[algorithm_type]["classical"](problem_sizes[0])],
        mode='lines+markers',
        name='Classical',
        line=dict(color='blue')
    ))

    fig.add_trace(go.Scatter(
        x=[problem_sizes[0]],
        y=[scaling_functions[algorithm_type]["quantum"](problem_sizes[0])],
        mode='lines+markers',
        name='Quantum',
        line=dict(color='orange')
    ))

    return fig