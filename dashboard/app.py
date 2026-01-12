import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="DevOps Buddy Dashboard",
    layout="wide",
)

st.title("🚀 DevOps Buddy")
st.caption("GitHub Repository DevOps Insights")

st.markdown("---")

# Inputs
col_in_1, col_in_2 = st.columns(2)
with col_in_1:
    owner = st.text_input("GitHub Owner", placeholder="e.g. tiangolo")
with col_in_2:
    repo = st.text_input("Repository Name", placeholder="e.g. fastapi")

analyze = st.button("Analyze Repository")

def health_badge(value, good, warn):
    if value >= good:
        return "🟢 Healthy"
    if value >= warn:
        return "🟡 Attention"
    return "🔴 Needs work"

if analyze:
    if not owner or not repo:
        st.warning("Please enter both owner and repository name.")
    else:
        with st.spinner("Fetching insights..."):
            summary_res = requests.get(
                f"{API_BASE_URL}/github/repo/{owner}/{repo}/summary"
            )
            metrics_res = requests.get(
                f"{API_BASE_URL}/github/repo/{owner}/{repo}/metrics"
            )

        if summary_res.status_code != 200:
            st.error(summary_res.json().get("detail", "Error fetching summary"))
        elif metrics_res.status_code != 200:
            st.error(metrics_res.json().get("detail", "Error fetching metrics"))
        else:
            summary = summary_res.json()
            metrics = metrics_res.json()

            # --- Summary Card ---
            st.subheader(f"📦 {summary['full_name']}")
            if summary.get("description"):
                st.write(summary["description"])

            st.markdown("---")

            # --- KPI Cards ---
            k1, k2, k3, k4 = st.columns(4)
            k1.metric("⭐ Stars", summary["stars"])
            k2.metric("🍴 Forks", summary["forks"])
            k3.metric("👥 Contributors", summary["contributors"])
            k4.metric("🐛 Open Issues", summary["open_issues"])

            st.markdown("---")

            # --- Health Indicators ---
            h1, h2, h3 = st.columns(3)
            with h1:
                st.metric(
                    "🔥 Activity Score",
                    metrics["activity_score"],
                )
            with h2:
                st.write("Issue Health")
                st.write(health_badge(metrics["issue_health_score"], good=8, warn=5))
            with h3:
                st.write("Popularity")
                st.write(health_badge(metrics["popularity_score"], good=6, warn=3))

            st.markdown("---")

            # --- Breakdown ---
            b1, b2, b3, b4 = st.columns(4)
            b1.metric("Popularity", metrics["popularity_score"])
            b2.metric("Issues", metrics["issue_health_score"])
            b3.metric("Commits", metrics["commits_score"])
            b4.metric("Contributors", metrics["contributors_score"])

            st.markdown(
                f"[🔗 View on GitHub]({summary['html_url']})"
            )
