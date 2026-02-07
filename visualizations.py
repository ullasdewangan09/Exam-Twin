"""
Visualization components using Plotly.
"""

import random
import plotly.graph_objects as go


def create_readiness_gauge(readiness):
    """
    Create a gauge chart for exam readiness.
    
    Args:
        readiness: Readiness percentage (0-100)
    
    Returns:
        plotly.graph_objects.Figure: Gauge chart figure
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=readiness,
        title={'text': "Exam Readiness"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#4f46e5"},
            'steps': [
                {'range': [0, 50], 'color': '#fee2e2'},
                {'range': [50, 75], 'color': '#fef3c7'},
                {'range': [75, 100], 'color': '#dcfce7'}
            ],
        }
    ))
    return fig


def create_momentum_chart(readiness):
    """
    Create a line chart showing preparation momentum over time.
    
    Args:
        readiness: Current readiness percentage
    
    Returns:
        plotly.graph_objects.Figure: Line chart figure
    """
    weeks = ["Week 1", "Week 2", "Week 3", "Current"]
    trend = [
        max(20, readiness - random.randint(10, 20)),
        max(30, readiness - random.randint(5, 15)),
        max(40, readiness - random.randint(0, 10)),
        readiness
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=weeks,
        y=trend,
        mode='lines+markers',
        line=dict(width=4)
    ))

    fig.update_layout(
        yaxis_title="Readiness %",
        template="simple_white"
    )
    
    return fig
