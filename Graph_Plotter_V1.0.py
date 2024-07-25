import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("GRAPH PLOTTER")
st.info("""
    The graph plotter is a program designed to plot data with 
    options for titles, line styles, widths, and colors. It is implemented
    in Python and augmented with Streamlit:  
    - Just load an Excel file where column A contains the x-axis data and column B the y-axis data.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# File Upload and Data Preview
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Choose an Excel File", type="xlsx")
    default_data = {'X': [1, 2, 3, 4, 5], 'Y': [10, 20, 30, 40, 50]}
    df_default = pd.DataFrame(default_data)
    df = pd.read_excel(uploaded_file) if uploaded_file else df_default
    graph_title = st.text_input("Graph Title:", "Graph Title")
    legend_name = st.text_input("Enter legend name:", "Data Series")

with col2:
    st.write("Partial data preview from Excel")
    st.write(df.head())
    columns = df.columns.tolist()
    x_axis = df.columns[0] if len(columns) > 0 else "No Data"
    y_axis = df.columns[1] if len(columns) > 0 else "No Data"

st.markdown("<hr>", unsafe_allow_html=True)

# Graph Type Selection
graph_type = st.radio("Select Graph Type", ('Line Graph', 'Bar Graph'))
st.markdown("<hr>", unsafe_allow_html=True)

# Line Graph Properties
if graph_type == 'Line Graph':
    with st.expander("Line Properties"):
        col1, col2, col3 = st.columns(3)
        with col1:
            line_type = st.selectbox("Line Style", ['solid', 'dashed', 'dashdot', 'dotted', 'None'])
        with col2:
            line_width = st.slider("Line Width", min_value=1, max_value=10, value=2)
        with col3:
            line_color = st.color_picker("Line Color", "#1f77b4")

    with st.expander("Marker Properties"):
        col1, col2, col3 = st.columns(3)
        with col1:
            marker_style = st.selectbox("Marker Style", ['o', 's', '^', 'D', '*', '+', 'x'])
        with col2:
            marker_size = st.slider("Marker Size", min_value=1, max_value=20, value=6)
        with col3:
            st.write("Marker Color")
            col1, col2 = st.columns(2)
            with col1:
                marker_edge_color = st.color_picker("Edge Color", "#000000")
            with col2:
                marker_face_color = st.color_picker("Face Color", "#1f77b4")

    plt.plot(df[x_axis], df[y_axis], linestyle=line_type, linewidth=line_width, color=line_color,
             marker=marker_style, markersize=marker_size,
             markeredgecolor=marker_edge_color, markerfacecolor=marker_face_color, label=legend_name)

# Bar Graph Properties
if graph_type == 'Bar Graph':
    with st.expander("Bar Graph Properties"):
        bar_color = st.color_picker("Bar Color", "#1f77b4")
        plt.bar(df[x_axis], df[y_axis], color=bar_color, label=legend_name)

# Axis Properties
with st.expander("Axis Properties"):
    st.text("Axis label rotation angle")
    col1, col2 = st.columns(2)
    with col1:
        xtick_rotation = st.slider("X-axis Rotation", min_value=-45, max_value=45, value=0)
    with col2:
        ytick_rotation = st.slider("Y-axis Rotation", min_value=-45, max_value=45, value=0)

# Gridline Properties
with st.expander("Gridline Properties"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        show_grid = st.checkbox("Show Gridlines", value=True)
    with col2:
        grid_line_style = st.selectbox("Gridline Style", ['-', '--', '-.', ':'])
    with col3:
        grid_line_width = st.slider("Gridline Width", min_value=0.1, max_value=2.0, value=0.5, step=0.1)
    with col4:
        grid_line_color = st.color_picker("Gridline Color", "#9A9090")

# Plotting the Graph
plt.title(graph_title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.xticks(rotation=xtick_rotation)
plt.yticks(rotation=ytick_rotation)
plt.legend()
if show_grid:
    plt.grid(True, linestyle=grid_line_style, linewidth=grid_line_width, color=grid_line_color)
else:
    plt.grid(False)
plt.tight_layout()
st.pyplot(plt)

st.markdown("<hr>", unsafe_allow_html=True)

# Disclaimer
st.markdown("""
    © Prakash Dulal | 
    [EMAIL](mailto:info@prakashd.com.np) | 
    [LINKEDIN](https://www.linkedin.com/in/prakasdulal/) | 
    [RESEARCHGATE](https://www.researchgate.net/profile/Prakash-Dulal)
""")
st.markdown("<hr>", unsafe_allow_html=True)
