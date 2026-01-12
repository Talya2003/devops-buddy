import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="DevOps Buddy Dashboard",
    layout="centered",
)

st.title("🚀 DevOps Buddy")
st.subheader("GitHub Repository DevOps Insights")

st.markdown("---")

owner = st.text_input("GitHub Owner", placeholder="e.g. tiangolo")
repo = st.text_input("Repository Name", placeholder="e.g. fastapi")

if st.button("Analyze Repository"):
    if not owner or not repo:
        st.warning("Please enter both owner and repository name.")
    else:
        with st.spinner("Fetching insights..."):
            response = requests.get(
                f"{API_BASE_URL}/github/repo/{owner}/{repo}/metrics"
            )

            if response.status_code != 200:
                st.error(response.json().get("detail", "Error fetching data"))
            else:
                data = response.json()

                st.success("Analysis complete!")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("⭐ Popularity", data["popularity_score"])
                    st.metric("🐛 Issue Health", data["issue_health_score"])

                with col2:
                    st.metric("📦 Commits", data["commits_score"])
                    st.metric("👥 Contributors", data["contributors_score"])

                st.markdown("---")
                st.metric(
                    "🔥 Overall Activity Score",
                    data["activity_score"],
                )
