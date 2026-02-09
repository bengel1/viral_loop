
import streamlit as st
import numpy as np

st.set_page_config(page_title="The Viral Architect", layout="wide")

st.title("The Viral Architect: Absorbing Markov Chains")
st.caption("Growth Architecture Dashboard")

states = [
    "Newbie",
    "Casual",
    "Power User",
    "Community Leader",
    "Verified Legend",
    "Deleted Account"
]

st.header("1. Transition Matrix (P)")
st.markdown("Enter **any value between 0 and 1**. Absorbing states may include **1.0** on the diagonal.")

P = np.zeros((6, 6))

for i in range(6):
    st.subheader(states[i])
    cols = st.columns(6)
    for j in range(6):
        with cols[j]:
            P[i, j] = st.number_input(
                label=f"→ {states[j]}",
                min_value=0.0,
                max_value=1.0,
                value=0.0,
                step=0.01,
                format="%.2f",
                key=f"{i}-{j}"
            )

st.header("2. Transient and Absorbing States")
st.write("**Transient States:** Newbie, Casual, Power User, Community Leader")
st.write("**Absorbing States:** Verified Legend, Deleted Account")

Q = P[:4, :4]
R = P[:4, 4:]

st.header("3. Q and R Matrices")
st.subheader("Q Matrix (Transient → Transient)")
st.dataframe(Q)

st.subheader("R Matrix (Transient → Absorbing)")
st.dataframe(R)

st.header("4. Fundamental Matrix and Absorption Probabilities")

I = np.eye(4)

try:
    F = np.linalg.inv(I - Q)
    B = F @ R

    st.subheader("Fundamental Matrix F = (I − Q)⁻¹")
    st.dataframe(F)

    st.subheader("Absorption Matrix B = F × R")
    st.dataframe(B)

    st.metric(
        "Probability a Newbie becomes a Verified Legend",
        f"{B[0, 0]:.3f}"
    )

except np.linalg.LinAlgError:
    st.error("Matrix (I − Q) is not invertible. Check transient-state probabilities.")

st.header("5. What‑If Analysis: Reduce Newbie Dropout")

reduction = st.slider(
    "Reduce Newbie → Deleted probability",
    min_value=0.0,
    max_value=0.30,
    value=0.0,
    step=0.01
)

P_adj = P.copy()
P_adj[0, 5] = max(P_adj[0, 5] - reduction, 0)
P_adj[0, 0] += reduction

Q_adj = P_adj[:4, :4]
R_adj = P_adj[:4, 4:]

try:
    F_adj = np.linalg.inv(I - Q_adj)
    B_adj = F_adj @ R_adj

    st.metric(
        "New Probability of Verified Legend",
        f"{B_adj[0, 0]:.3f}",
        delta=f"{B_adj[0, 0] - B[0, 0]:.3f}"
    )
except:
    pass
