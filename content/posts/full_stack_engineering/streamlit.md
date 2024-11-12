---
date: 2024-10-31
title: "Streamlit cheat sheet"
---

### Common Commands
- `pip install streamlit`
- `streamlit run <path>/<file_name>.py`
- `import streamlit as st`
- `streamlit docs` open docs in browser
- `streamlit config show` show meta config for streamlit (like hide menu)
- `streamlit cache clear` clear cache for updated display (debugging tool)

### Display Differnt Texts

#### Markdown
- Directly use markdown in python code
    ```markdown
    # Magic commands without explicit st.write()
    "_This_ is some **Markdown**"
    42  # Displays as "42" in the app
    "dataframe:", my_data_frame  # Displays both the text and the dataframe
    ```
- `st.title("Title")`
- `st.header("Header")`
- `st.subheader("Subheader")`

- `st.markdown("Markdown")`
- `st.latex(r"\alpha + \beta x^2 + \gamma x^3")`
- `st.code(code, language="python")`
- `st.html("Text")`
- `st.text("Text")`

#### Basic Writes
- `st.write("Text")`
- `st.write([1, 2, 3])`
- `st.write({"foo": "bar"})`
- `st.write_stream(my_generator())`
- `st.write_stream(my_llm_stream)`

#### Display Data
- `st.dataframe(df)`
- `st.table(df)`
- `st.json(my_json_dict)`
- `st.metric(label="Temperature", value="70.3 °F", delta="1.2 °F")`

#### Display Media
- `st.image("path/to/image.jpg")`
- `st.audio("path/to/audio.mp3")`
- `st.video("path/to/video.mp4", subtitles="path/to/subtitles.srt")`
- `st.logo("path/to/logo.png")`

#### Display Charts
- `st.line_chart(dataframe)`
- `st.area_chart(dataframe)`
- `st.bar_chart(dataframe, horizontal=True)`
- `st.scatter_chart(dataframe)`
- `st.pyplot(figure)`
- `st.map(dataframe)`

#### Display Charts with external libraries
- `st.altair_chart(chart)`
- `st.bokeh_chart(fig)`
- `st.graphviz_chart(fig)`
- `st.plotly_chart(fig)`
- `st.pydeck_chart(chart)`
- `st.pyplot(fig)`
- `st.vega_lite_chart(df, spec)`

#### Interact with user selections
- `event = st.plotly_chart(df,  on_select="rerun")`
- `event = st.altair_chart(chart, on_select="rerun")`
- `event = st.vega_lite_chart(df,  spec,  on_select="rerun")`

### Add stuff to sidebar
- `st.sidebar.<function>()`
- `with st.sidebar: st.<function>()`

### Containers: (Columns, Tabs, expanders, popover, etc.)
- Once created, use as st object (refer to sidebar)
- `col1, col2 = st.columns(2, vertical_align="bottom")`
- `tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])`
- `st.expander("Expand me")`
- `st.popover("Popove

### Control flow
