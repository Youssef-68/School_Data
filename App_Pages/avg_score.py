import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data/education_cleaned.csv")
st.title("Average Score Analysis")
sns.set_style("whitegrid")

# KPI section
col1, col2 = st.columns(2)

col1.metric("Average Score", round(df["Average_Score"].mean(), 2))
col2.metric("Total Students", len(df))

st.divider()

# Row for main charts
c1, c2 = st.columns(2)

# KDE plot for Average Score distribution
with c1:
    st.subheader("Average Score Distribution")

    fig1, ax1 = plt.subplots(figsize=(7,5))

    sns.kdeplot(
        df["Average_Score"],
        fill=True,
        color="steelblue",
        linewidth=2,
        ax=ax1
    )

    ax1.set_title("Distribution of Average Score", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Average Score")
    ax1.set_ylabel("Density")
    ax1.tick_params(labelsize=9)

    st.pyplot(fig1)


# Bar chart for average score per subject
with c2:
    st.subheader("Average Score per Subject")

    subjects = [col for col in df.columns if "Subject" in col]
    means = df[subjects].mean().sort_index()

    fig2, ax2 = plt.subplots(figsize=(7,5))

    means.plot(
        kind="bar",
        ax=ax2,
        color=[plt.cm.tab10(i / (len(means)-1 if len(means)>1 else 1))
               for i in range(len(means))]
    )

    ax2.set_title("Average Score per Subject", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Subjects")
    ax2.set_ylabel("Average Score")
    ax2.tick_params(axis='x', rotation=45, labelsize=9)

    # add value labels on bars
    for i, v in enumerate(means):
        ax2.text(i, v + 0.2, f"{v:.1f}", ha='center', fontsize=8)

    st.pyplot(fig2)
