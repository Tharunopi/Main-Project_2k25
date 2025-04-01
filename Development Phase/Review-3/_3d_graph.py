import streamlit as st
import plotly.graph_objects as go

st.title("3D Dot/Sphere Visualization")

# Dot parameters
radius = st.slider("Dot Size", 0.1, 2.0, 0.5)
center_x = st.slider("X Position", -3.0, 3.0, 0.0)
center_y = st.slider("Y Position", -3.0, 3.0, 0.0)
center_z = st.slider("Z Position", -3.0, 3.0, 0.0)
color = st.color_picker("Dot Color", "#FF4B4B")

# Create the 3D plot with a single marker (dot)
fig = go.Figure(data=[go.Scatter3d(
    x=[center_x],
    y=[center_y],
    z=[center_z],
    mode='markers',
    marker=dict(
        size=radius*20,  # Scale up the size for visibility
        color=color,
        opacity=0.8,
        symbol='circle'
    )
)])

# Set layout options
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube'
    ),
    width=600,
    height=600,
    margin=dict(l=0, r=0, b=0, t=40),
    title="3D Dot"
)

st.plotly_chart(fig)