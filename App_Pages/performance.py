import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "education_cleaned.csv")
df = pd.read_csv(file_path)

st.title("Student Performance Analysis")
sns.set_style("whitegrid")

# KPI section
col1, col2, col3 = st.columns(3)

col1.metric("Avg Score", round(df["Average_Score"].mean(), 2))
col2.metric("Total Students", len(df))
col3.metric("Performance Levels", df["Performance"].nunique())

st.divider()

# Row for main distributions
c1, c2 = st.columns(2)

# Performance distribution
with c1:
    st.subheader("Performance Distribution")

    counts = df["Performance"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(7,5))

    counts.plot(
        kind="bar",
        ax=ax1,
        color=[plt.cm.tab10(i / (len(counts)-1 if len(counts)>1 else 1))
               for i in range(len(counts))]
    )

    ax1.set_title("Distribution of Student Performance", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Performance Level")
    ax1.set_ylabel("Count")
    ax1.tick_params(axis='x', rotation=0)

    # value labels
    for i, v in enumerate(counts):
        ax1.text(i, v + 1, str(v), ha='center', fontsize=9)

    st.pyplot(fig1)


# KDE score by performance
with c2:
    st.subheader("Score Density by Performance")

    fig2, ax2 = plt.subplots(figsize=(7,5))

    for p in df["Performance"].unique():
        sns.kdeplot(
            df[df["Performance"] == p]["Average_Score"],
            label=p,
            fill=True,
            ax=ax2
        )

    ax2.set_title("Density of Average Score by Performance", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Average Score")
    ax2.set_ylabel("Density")

    ax2.legend(title="Performance")

    st.pyplot(fig2)

st.divider()

# Row for relationship analysis
c3, c4 = st.columns(2)

# Year vs Performance
with c3:
    st.subheader("Year vs Performance")

    counts2 = df.groupby(["Student_Year", "Performance"]).size().unstack(fill_value=0)

    fig3, ax3 = plt.subplots(figsize=(7,5))

    counts2.plot(kind="bar", ax=ax3)

    ax3.set_title("Student Year vs Performance", fontsize=12, fontweight='bold')
    ax3.set_xlabel("Student Year")
    ax3.set_ylabel("Count")
    ax3.tick_params(axis='x', rotation=0)

    st.pyplot(fig3)


# Education Type vs Performance
with c4:
    st.subheader("Education Type vs Performance")

    counts3 = df.groupby(["Education_Type", "Performance"]).size().unstack(fill_value=0)

    fig4, ax4 = plt.subplots(figsize=(7,5))

    counts3.plot(kind="bar", ax=ax4)

    ax4.set_title("Education Type vs Performance", fontsize=12, fontweight='bold')
    ax4.set_xlabel("Education Type")
    ax4.set_ylabel("Count")
    ax4.tick_params(axis='x', rotation=0)

    st.pyplot(fig4)
