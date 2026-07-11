import numpy as np

fitness_data = np.array([
    [5000, 200, 6],
    [7000, 250, 7],
    [6500, 230, 6],
    [8000, 300, 8],
    [9000, 320, 7],
    [7500, 270, 6],
    [12000, 400, 5]
])

# ─────────────────────────────────────────────
# 1. EXPLORE THE ARRAY
# ─────────────────────────────────────────────

print("=" * 50)
print("1. ARRAY EXPLORATION")
print("=" * 50)

print(f"Number of dimensions : {fitness_data.ndim}")
print(f"Shape                : {fitness_data.shape}")
print(f"Total elements       : {fitness_data.size}")

# ─────────────────────────────────────────────
# 2. SLICE THE DATA
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("2. SLICING")
print("=" * 50)

steps       = fitness_data[:, 0]
calories    = fitness_data[:, 1]
sleep       = fitness_data[:, 2]
first_3     = fitness_data[:3]
steps_cal   = fitness_data[:, :2]

print(f"All Steps            : {steps}")
print(f"All Calories         : {calories}")
print(f"All Sleep Hours      : {sleep}")
print(f"\nFirst 3 Days:\n{first_3}")
print(f"\nSteps & Calories:\n{steps_cal}")

# ─────────────────────────────────────────────
# 3. RESHAPE THE DATA
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("3. RESHAPING")
print("=" * 50)

steps_reshaped   = steps.reshape(7, 1)
full_reshaped    = fitness_data.reshape(3, 7)

print(f"Steps reshaped to (7,1):\n{steps_reshaped}")
print(f"\nFull dataset reshaped to (3,7):\n{full_reshaped}")

# ─────────────────────────────────────────────
# 4. FILTER THE DATA
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("4. FILTERING")
print("=" * 50)

high_steps      = fitness_data[fitness_data[:, 0] > 8000]
low_sleep       = fitness_data[fitness_data[:, 2] < 6]
high_calories   = fitness_data[fitness_data[:, 1] > 300]

print(f"Days where Steps > 8000:\n{high_steps}")
print(f"\nDays where Sleep < 6 hours:\n{low_sleep}")
print(f"\nDays where Calories > 300:\n{high_calories}")

# ─────────────────────────────────────────────
# 5. STATISTICS
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("5. STATISTICS")
print("=" * 50)

avg_steps       = np.mean(fitness_data[:, 0])
max_steps       = np.max(fitness_data[:, 0])
min_sleep       = np.min(fitness_data[:, 2])
std_calories    = np.std(fitness_data[:, 1])
range_steps     = np.max(fitness_data[:, 0]) - np.min(fitness_data[:, 0])

print(f"Average Steps             : {avg_steps:.2f}")
print(f"Maximum Steps             : {max_steps}")
print(f"Minimum Sleep Hours       : {min_sleep}")
print(f"Std Deviation (Calories)  : {std_calories:.2f}")
print(f"Range of Steps            : {range_steps}")

# ─────────────────────────────────────────────
# 6. INSIGHTS
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("6. INSIGHTS")
print("=" * 50)

print("""
Patterns Noticed:
  - Steps and Calories are strongly correlated:
    more steps consistently produce more calories burned.
  - Sleep hours are mostly stable (6-8 hrs) across days,
    with Day 7 being the only outlier at 5 hours.
  - Higher-activity days (steps > 8000) burn 320+ calories.

Unusual Days:
  - Day 7 (12000 steps, 400 cal, 5 hrs sleep) is a clear outlier:
    the highest activity level but the lowest sleep — suggesting
    fatigue or overexertion that night.
  - Day 4 (8000 steps, 300 cal, 8 hrs sleep) is the best-balanced
    day: solid activity and the most rest.

Key Learnings:
  - Physical activity (steps) is the strongest driver of
    calorie expenditure in this dataset.
  - Sleep does not scale with activity — the most active day
    had the worst sleep, which is a common burnout pattern.
  - A healthy target appears to be 7000-9000 steps with 7+
    hours of sleep for a balanced fitness routine.
""")
