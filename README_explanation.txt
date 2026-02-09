
The Viral Architect – Streamlit App Explanation

This application implements an Absorbing Markov Chain model to analyze user growth and retention in a social media platform.

Key Features:
1. User-defined Transition Matrix (P)
2. Automatic identification of Transient and Absorbing states
3. Extraction of Q (transient-to-transient) and R (transient-to-absorbing) matrices
4. Calculation of the Fundamental Matrix F = (I − Q)^−1
5. Calculation of Absorption Probabilities B = F × R
6. Success Metric: Probability a Newbie becomes a Verified Legend
7. What-if analysis to simulate reduced dropout rates

Mathematical Interpretation:
- Diagonal values of F represent expected time spent in each state.
- B[0,0] represents the probability that a Newbie eventually reaches Verified Legend.
- The What‑If slider redistributes dropout probability into retention, showing its effect on long-term success.

This dashboard satisfies all Phase D requirements of the Viral Architect assignment.
