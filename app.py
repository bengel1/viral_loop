
import streamlit as st
import numpy as np

st.set_page_config(page_title="The Viral Architect", layout="wide")

st.title("📈 The Viral Architect: Absorbing Markov Funnel")
st.caption("Growth Architecture • Absorbing Markov Chains • Viral Loops")

states = [
    "Newbie (S1)",
    "Casual (S2)",
    "Power User (S3)",
    "Community Leader (S4)",
    "Verified Legend (S5)",
    "Deleted Account (S6)"
]

st.markdown("### 1️⃣ Define the Transition Matrix P")
P = np.zeros((6, 6))

for i, state in enumerate(states):
    cols = st.columns(6)
    for j in range(6):
        with cols[j]:
            P[i, j] = st.number_input(
                f"{state} → {states[j]}",
                min_value=0.0,
                max_value=1.0,
                value=0.0,
                step=0.05,
                key=f"{i}-{j}"
            )

st.markdown("### 2️⃣ Transient and Absorbing States")
st.success("Transient States: Newbie, Casual, Power User, Community Leader")
st.info("Absorbing States: Verified Legend, Deleted Account")

Q = P[:4, :4]
R = P[:4, 4:]

st.markdown("### 3️⃣ Q and R Matrices")
st.write("Q Matrix")
st.dataframe(Q)
st.write("R Matrix")
st.dataframe(R)

st.markdown("### 4️⃣ Fundamental Matrix and Absorption Probabilities")
I = np.eye(4)

try:
    F = np.linalg.inv(I - Q)
    B = F @ R

    st.write("Fundamental Matrix F")
    st.dataframe(F)

    st.write("Absorption Matrix B")
    st.dataframe(B)

    st.metric(
        "Probability Newbie → Verified Legend",
        f"{B[0,0]:.3f}"
    )

except np.linalg.LinAlgError:
    st.error("Matrix (I − Q) is not invertible.")

st.markdown("### 5️⃣ What‑If Analysis")
reduction = st.slider("Reduce Newbie Dropout", 0.0, 0.30, 0.0, 0.05)

P_adj = P.copy()
P_adj[0,5] = max(P_adj[0,5] - reduction, 0)
P_adj[0,0] += reduction

Q_adj = P_adj[:4,:4]
R_adj = P_adj[:4,4:]

try:
    F_adj = np.linalg.inv(I - Q_adj)
    B_adj = F_adj @ R_adj

    st.metric(
        "New Legend Probability After Change",
        f"{B_adj[0,0]:.3f}",
        delta=f"{B_adj[0,0] - B[0,0]:.3f}"
    )
except:
    pass
