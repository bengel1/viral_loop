
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

P = np.zeros((6, 6))

for i in range(6):
    st.subheader(states[i])
    cols = st.columns(6)
    for j in range(6):
        with cols[j]:
            P[i, j] = st.number_input(
                label=f"to {states[j]}",
                min_value=0.0,
                max_value=1.0,
                value=0.0,
                step=0.05,
                key=f"{i}-{j}"
            )

st.header("2. Transient and Absorbing States")
st.write("**Transient:** Newbie, Casual, Power User, Community Leader")
st.write("**Absorbing:** Verified Legend, Deleted Account")

Q = P[:4, :4]
R = P[:4, 4:]

st.header("3. Q and R Matrices")
st.subheader("Q Matrix")
st.dataframe(Q)
st.subheader("R Matrix")
st.dataframe(R)

st.header("4. Fundamental Matrix and Absorption Probabilities")

I = np.eye(4)

try:
    F = np.linalg.inv(I - Q)
    B = F @ R

    st.subheader("Fundamental Matrix F")
    st.dataframe(F)

    st.subheader("Absorption Matrix B")
    st.dataframe(B)

    st.metric(
        "Probability a Newbie becomes a Verified Legend",
        f"{B[0, 0]:.3f}"
    )

except np.linalg.LinAlgError:
    st.error("Invalid matrix: (I − Q) is not invertible. Check probabilities.")

st.header("5. What‑If Analysis: Reduce Newbie Dropout")

reduction = st.slider(
    "Reduce Newbie → Deleted probability",
    0.0, 0.30, 0.0, 0.05
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
