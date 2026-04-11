import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file_path = Path("education_cleaned.csv")
df = pd.read_csv(file_path)
st.title("Parents Education Analysis")

# KPI Section
st.markdown("Key Insights")
col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Most Common Father Degree", df["Father_Degree"].mode()[0])
col3.metric("Most Common Mother Degree", df["Mother_Degree"].mode()[0])

st.divider()

# Row 1
st.subheader("Parents Education Comparison")
father = df["Father_Degree"].value_counts()
mother = df["Mother_Degree"].value_counts()

all_degrees = sorted(set(father.index).union(set(mother.index)))
father = father.reindex(all_degrees, fill_value=0)
mother = mother.reindex(all_degrees, fill_value=0)

comparison = pd.DataFrame({"Father": father, "Mother": mother})
fig1, ax1 = plt.subplots(figsize=(12,5))

comparison.plot(
    kind="bar",
    ax=ax1,
    color=[plt.cm.Set2(i) for i in range(len(comparison.columns))]
)

ax1.set_title("Comparison of Parents' Education Levels", fontsize=12, fontweight='bold')
ax1.set_xlabel("Education Level")
ax1.set_ylabel("Count")
ax1.tick_params(axis='x', rotation=45)
st.pyplot(fig1)
st.divider()

# Row 2
c1, c2 = st.columns(2)

# Father
with c1:
    st.subheader("Father Degree vs Education Type")
    counts_father = df.groupby(["Father_Degree", "Education_Type"]).size().unstack(fill_value=0)
    fig2, ax2 = plt.subplots(figsize=(7,5))

    counts_father.plot(
        kind="bar",
        ax=ax2,
        color=[plt.cm.tab10(i / (len(counts_father.columns)-1 if len(counts_father.columns)>1 else 1))
               for i in range(len(counts_father.columns))]
    )

    ax2.set_title("Father Impact", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Father Degree")
    ax2.set_ylabel("Count")
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)


# Mother
with c2:
    st.subheader("Mother Degree vs Education Type")
    counts_mother = df.groupby(["Mother_Degree", "Education_Type"]).size().unstack(fill_value=0)
    fig3, ax3 = plt.subplots(figsize=(7,5))

    counts_mother.plot(
        kind="bar",
        ax=ax3,
        color=[plt.cm.tab10(i / (len(counts_mother.columns)-1 if len(counts_mother.columns)>1 else 1))
               for i in range(len(counts_mother.columns))]
    )

    ax3.set_title("Mother Impact", fontsize=11, fontweight='bold')
    ax3.set_xlabel("Mother Degree")
    ax3.set_ylabel("Count")
    ax3.tick_params(axis='x', rotation=45)
    st.pyplot(fig3)

st.divider()

# Row 3
st.subheader("Student Year vs Education Type")
counts_year = df.groupby(["Student_Year", "Education_Type"]).size().unstack(fill_value=0)
fig4, ax4 = plt.subplots(figsize=(12,6))

counts_year.plot(
    kind="bar",
    ax=ax4,
    color=[plt.cm.tab10(i / (len(counts_year.columns)-1 if len(counts_year.columns)>1 else 1))
           for i in range(len(counts_year.columns))]
)

ax4.set_title("Student Year vs Education Type", fontsize=12, fontweight='bold')
ax4.set_xlabel("Student Year")
ax4.set_ylabel("Count")
ax4.tick_params(axis='x', rotation=0)

st.pyplot(fig4)
