import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "education_cleaned.csv")
df = pd.read_csv(file_path)

st.title("Student Year Analysis")
sns.set_style("whitegrid")

# KPI section
col1, col2, col3 = st.columns(3)

col1.metric("Avg Score", round(df["Average_Score"].mean(), 2))
col2.metric("Total Students", len(df))
col3.metric("Total Years", df["Student_Year"].nunique())

st.divider()

# Row for boxplots
c1, c2 = st.columns(2)

# Boxplot for Average Score by Year
with c1:
    st.subheader("Year vs Average Score")

    fig1, ax1 = plt.subplots(figsize=(7,5))

    sns.boxplot(
        x="Student_Year",
        y="Average_Score",
        data=df,
        palette="coolwarm",
        ax=ax1
    )

    ax1.set_title("Average Score by Student Year", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Student Year")
    ax1.set_ylabel("Average Score")

    st.pyplot(fig1)


# Boxplot for Total Score by Year
with c2:
    st.subheader("Year vs Total Score")

    fig2, ax2 = plt.subplots(figsize=(7,5))

    sns.boxplot(
        x="Student_Year_num",
        y="Total_Score",
        data=df,
        palette="husl",
        ax=ax2
    )

    ax2.set_title("Total Score by Student Year", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Student Year")
    ax2.set_ylabel("Total Score")

    st.pyplot(fig2)

st.divider()

# Row for multi-dimensional analysis
st.subheader("Age Group + Education Type vs Student Year")

# Create Age Group
df["Age_Group"] = pd.cut(
    df["Student_Age"],
    bins=[13, 15, 17, 19],
    labels=["14-15", "16-17", "18-19"]
)

counts = df.groupby(["Age_Group", "Education_Type", "Student_Year"]).size()
counts = counts.unstack(fill_value=0)

fig3, ax3 = plt.subplots(figsize=(12,6))

counts.plot(
    kind="bar",
    ax=ax3,
    color=[plt.cm.tab10(i / (len(counts.columns)-1 if len(counts.columns)>1 else 1))
           for i in range(len(counts.columns))]
)

ax3.set_title("Age + Education Type vs Student Year", fontsize=12, fontweight='bold')
ax3.set_xlabel("Age Group + Education Type")
ax3.set_ylabel("Count")
ax3.tick_params(axis='x', rotation=45)

# value labels
for container in ax3.containers:
    for bar in container:
        h = bar.get_height()
        if h > 0:
            ax3.text(
                bar.get_x() + bar.get_width()/2,
                h + 1,
                int(h),
                ha='center',
                fontsize=8
            )

st.pyplot(fig3)
