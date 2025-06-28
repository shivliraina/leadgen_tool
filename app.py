import streamlit as st
import pandas as pd
from scraper import scrape_data, enrich_data
from utils import score_leads

st.title("SmartLead Profiler")

query = st.text_input("Enter a keyword (e.g. 'AI startup in India')")
if st.button("Generate Leads") and query:
    raw_data = scrape_data(query)
    enriched = enrich_data(raw_data)
    scored = score_leads(enriched)
    st.dataframe(scored)
    st.download_button("Download CSV", data=scored.to_csv(index=False), file_name="leads.csv")