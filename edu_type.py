import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/home/youssef/Desktop/Data_Projects/Egypt_Education/Data/education_cleaned.csv")

st.title("Education Type Analysis")

sns.set_style("whitegrid")

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 12
})

# KPI section
col1, col2, col3 = st.columns(3)

col1.metric("Total Types", df["Education_Type"].nunique())
col2.metric("Most Common Type", df["Education_Type"].mode()[0])
col3.metric("Avg Score", round(df["Average_Score"].mean(), 2))

st.divider()

# Row for charts
c1, c2 = st.columns(2)

# Pie chart for Education Types
with c1:
    st.subheader("Education Types Distribution")

    counts = df["Education_Type"].value_counts().sort_index()

    def func(pct, allvals):
        absolute = int(pct/100. * sum(allvals))
        return f"{pct:.1f}%\n({absolute})"

    colors = plt.cm.Set2.colors

    fig1, ax1 = plt.subplots(figsize=(6,6))

    ax1.pie(
        counts,
        labels=counts.index,
        autopct=lambda pct: func(pct, counts),
        startangle=90,
        colors=colors,
        textprops={'fontsize': 10, 'weight': 'bold'}
    )

    ax1.set_title("Distribution of Education Types", fontsize=12, fontweight='bold')
    ax1.axis('equal')

    st.pyplot(fig1)


# KDE plot for Average Score by Education Type
with c2:
    st.subheader("Average Score Density")

    fig2, ax2 = plt.subplots(figsize=(7,5))

    for etype in df["Education_Type"].unique():
        sns.kdeplot(
            df[df["Education_Type"] == etype]["Average_Score"],
            label=etype,
            fill=True,
            ax=ax2
        )

    ax2.set_title("Density of Average Score by Education Type", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Average Score")
    ax2.set_ylabel("Density")

    ax2.legend(title="Education Type")

    st.pyplot(fig2)