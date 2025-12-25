import streamlit as st
from fetcher import fetch_text
from analyzer import analyze
from formatter import clean_output

st.set_page_config(page_title="PULSE-ASSIGNMENT3", layout="wide")

st.title("PULSE-ASSIGNMENT3")
st.write("AI-Driven Documentation Structure Analyzer")

urls = st.text_area(
    "Enter Documentation URLs (comma separated)",
    value="https://wordpress.org/documentation/"
)

if st.button("Analyze"):
    final_result = []

    for url in urls.split(","):
        url = url.strip()
        texts = fetch_text(url)
        modules = analyze(texts)
        final_result.extend(modules)

    output = clean_output(final_result)

    if output:
        st.success("Extraction Successful")
        st.json(output)
    else:
        st.warning("No modules detected")
