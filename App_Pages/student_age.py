import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

file_path = Path("education_cleaned.csv")
df = pd.read_csv(file_path)
st.title("Student Age Analysis")
sns.set_style("whitegrid")

# KPI section
col1, col2, col3 = st.columns(3)

col1.metric("Average Age", round(df["Student_Age"].mean(), 2))
col2.metric("Total Students", len(df))
col3.metric("Age Range", f"{df['Student_Age'].min()} - {df['Student_Age'].max()}")

st.divider()

# Row for main analysis
c1, c2 = st.columns(2)

# Boxplot: Age vs Average Score
with c1:
    st.subheader("Age vs Average Score")

    fig1, ax1 = plt.subplots(figsize=(7,5))

    sns.boxplot(
        x="Student_Age",
        y="Average_Score",
        data=df,
        palette="Set2",
        ax=ax1
    )

    ax1.set_title("Average Score by Student Age", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Student Age")
    ax1.set_ylabel("Average Score")

    st.pyplot(fig1)


# Age distribution
with c2:
    st.subheader("Student Age Distribution")

    counts = df["Student_Age"].value_counts().sort_index()

    fig2, ax2 = plt.subplots(figsize=(7,5))

    counts.plot(
        kind="bar",
        ax=ax2,
        color=[plt.cm.tab10(i / (len(counts)-1 if len(counts)>1 else 1))
               for i in range(len(counts))]
    )

    ax2.set_title("Distribution of Student Ages", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Student Age")
    ax2.set_ylabel("Count")

    ax2.tick_params(axis='x', rotation=0)

    # value labels
    for i, v in enumerate(counts):
        ax2.text(i, v + 1, str(v), ha='center', fontsize=9)

    st.pyplot(fig2)
