import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Fitness Data Explorer",
    page_icon="🏋️",
    layout="wide"
)

# ── Custom CSS ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.section-header {
    background: linear-gradient(90deg, #7f5af0, #2cb67d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.insight-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(127,90,240,0.3);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
    backdrop-filter: blur(8px);
}

.badge {
    display: inline-block;
    background: linear-gradient(90deg,#7f5af0,#2cb67d);
    color: white;
    border-radius: 20px;
    padding: 3px 14px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-right: 6px;
    margin-bottom: 4px;
}
</style>
""", unsafe_allow_html=True)


# ── Dataset ─────────────────────────────────────────────────
fitness_data = np.array([
    [5000, 200, 6],
    [7000, 250, 7],
    [6500, 230, 6],
    [8000, 300, 8],
    [9000, 320, 7],
    [7500, 270, 6],
    [12000, 400, 5]
])

days      = [f"Day {i+1}" for i in range(7)]
steps     = fitness_data[:, 0]
calories  = fitness_data[:, 1]
sleep     = fitness_data[:, 2]


# ── Hero Header ─────────────────────────────────────────────
st.markdown("## 🏋️ Fitness Data Explorer")
st.markdown("##### NumPy-powered analysis of a 7-day fitness dataset")
st.divider()


# ── 1. Array Exploration ────────────────────────────────────
st.markdown('<p class="section-header">1 · Array Exploration</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.metric("Dimensions (ndim)", fitness_data.ndim)
c2.metric("Shape", str(fitness_data.shape))
c3.metric("Total Elements (size)", fitness_data.size)

st.divider()


# ── 2. Slicing ──────────────────────────────────────────────
st.markdown('<p class="section-header">2 · Data Slices</p>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📶 Steps", "🔥 Calories", "😴 Sleep", "📅 First 3 Days", "⚡ Steps & Calories"]
)

with tab1:
    st.write("**All Steps** → `fitness_data[:, 0]`")
    st.bar_chart(dict(zip(days, steps)))

with tab2:
    st.write("**All Calories** → `fitness_data[:, 1]`")
    st.bar_chart(dict(zip(days, calories)))

with tab3:
    st.write("**All Sleep Hours** → `fitness_data[:, 2]`")
    st.bar_chart(dict(zip(days, sleep)))

with tab4:
    st.write("**First 3 Days** → `fitness_data[:3]`")
    st.dataframe(
        {"Day": days[:3], "Steps": steps[:3].tolist(), "Calories": calories[:3].tolist(), "Sleep": sleep[:3].tolist()},
        use_container_width=True, hide_index=True
    )

with tab5:
    st.write("**Steps & Calories** → `fitness_data[:, :2]`")
    st.dataframe(
        {"Day": days, "Steps": steps.tolist(), "Calories": calories.tolist()},
        use_container_width=True, hide_index=True
    )

st.divider()


# ── 3. Reshaping ────────────────────────────────────────────
st.markdown('<p class="section-header">3 · Reshaping</p>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    st.write("**Steps → (7, 1)** &nbsp; `steps.reshape(7, 1)`")
    st.dataframe(
        {"Steps (7×1)": steps.reshape(7, 1).flatten().tolist()},
        use_container_width=True, hide_index=False
    )

with col_b:
    st.write("**Full dataset → (3, 7)** &nbsp; `fitness_data.reshape(3, 7)`")
    reshaped = fitness_data.reshape(3, 7)
    st.dataframe(
        {f"Col {i}": reshaped[:, i].tolist() for i in range(7)},
        use_container_width=True, hide_index=False
    )

st.divider()


# ── 4. Filtering ────────────────────────────────────────────
st.markdown('<p class="section-header">4 · Filtered Data</p>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

high_steps_mask    = fitness_data[:, 0] > 8000
low_sleep_mask     = fitness_data[:, 2] < 6
high_calories_mask = fitness_data[:, 1] > 300

with f1:
    st.write("**Steps > 8,000**")
    matching = [days[i] for i in range(7) if high_steps_mask[i]]
    for d in matching:
        st.markdown(f'<span class="badge">{d}</span>', unsafe_allow_html=True)
    st.dataframe(
        {"Day": matching,
         "Steps": steps[high_steps_mask].tolist(),
         "Calories": calories[high_steps_mask].tolist(),
         "Sleep": sleep[high_steps_mask].tolist()},
        use_container_width=True, hide_index=True
    )

with f2:
    st.write("**Sleep < 6 hrs**")
    matching = [days[i] for i in range(7) if low_sleep_mask[i]]
    for d in matching:
        st.markdown(f'<span class="badge">{d}</span>', unsafe_allow_html=True)
    st.dataframe(
        {"Day": matching,
         "Steps": steps[low_sleep_mask].tolist(),
         "Calories": calories[low_sleep_mask].tolist(),
         "Sleep": sleep[low_sleep_mask].tolist()},
        use_container_width=True, hide_index=True
    )

with f3:
    st.write("**Calories > 300**")
    matching = [days[i] for i in range(7) if high_calories_mask[i]]
    for d in matching:
        st.markdown(f'<span class="badge">{d}</span>', unsafe_allow_html=True)
    st.dataframe(
        {"Day": matching,
         "Steps": steps[high_calories_mask].tolist(),
         "Calories": calories[high_calories_mask].tolist(),
         "Sleep": sleep[high_calories_mask].tolist()},
        use_container_width=True, hide_index=True
    )

st.divider()


# ── 5. Statistics ───────────────────────────────────────────
st.markdown('<p class="section-header">5 · Statistics</p>', unsafe_allow_html=True)

s1, s2, s3, s4, s5 = st.columns(5)
s1.metric("📊 Avg Steps",        f"{np.mean(steps):,.2f}")
s2.metric("🔝 Max Steps",        f"{np.max(steps):,}")
s3.metric("😴 Min Sleep",        f"{np.min(sleep)} hrs")
s4.metric("📉 Std Dev Calories", f"{np.std(calories):.2f}")
s5.metric("📐 Steps Range",      f"{np.max(steps) - np.min(steps):,}")

st.divider()


# ── 6. Insights ─────────────────────────────────────────────
st.markdown('<p class="section-header">6 · Insights</p>', unsafe_allow_html=True)

st.markdown("""
<div class="insight-card">
  <b>🔗 Steps & Calories are strongly correlated</b><br>
  Every increase in steps is matched by a proportional rise in calories burned.
  The relationship is nearly linear across all 7 days.
</div>
<div class="insight-card">
  <b>⚠️ Day 7 is the clear outlier</b><br>
  12,000 steps and 400 calories — the highest of any day — yet only 5 hours of sleep.
  This signals overexertion or burnout, and is flagged by all three filters above.
</div>
<div class="insight-card">
  <b>✅ Day 4 is the most balanced</b><br>
  8,000 steps with 8 hours of sleep — the best combination of activity and recovery.
</div>
<div class="insight-card">
  <b>🎯 Sweet spot for a healthy routine</b><br>
  7,000–9,000 steps with 7+ hours of sleep provides a sustainable balance between
  calorie burn and adequate rest.
</div>
""", unsafe_allow_html=True)

st.caption("Built with NumPy · Streamlit | NTI Fitness Activity")
