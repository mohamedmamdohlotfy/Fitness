# 🏋️ Fitness Data Explorer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.4-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.59-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Fitness-181717?style=for-the-badge&logo=github&logoColor=white)

### 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mohamedmamdohlotfy-fitness-app-8silmk.streamlit.app/)

**👉 [https://mohamedmamdohlotfy-fitness-app-8silmk.streamlit.app/](https://mohamedmamdohlotfy-fitness-app-8silmk.streamlit.app/)**

</div>

---

## 📌 Overview

**Fitness Data Explorer** is an interactive web dashboard built with **Python**, **NumPy**, and **Streamlit** that analyzes a 7-day fitness dataset. The project demonstrates core NumPy operations — array exploration, slicing, reshaping, filtering, and statistical analysis — all wrapped in a modern, visually-rich web interface.

---

## 📊 Dataset

The dataset tracks **7 days** of fitness metrics across **3 columns**:

| Column | Description |
|--------|-------------|
| `Steps` | Number of steps walked per day |
| `Calories Burned` | Total calories burned per day |
| `Sleep Hours` | Hours of sleep per night |

```python
fitness_data = np.array([
    [5000, 200, 6],
    [7000, 250, 7],
    [6500, 230, 6],
    [8000, 300, 8],
    [9000, 320, 7],
    [7500, 270, 6],
    [12000, 400, 5]
])
```

---

## ✨ Features

| # | Section | What it does |
|---|---------|--------------|
| 1 | **Array Exploration** | Shows `ndim`, `shape`, and total elements |
| 2 | **Data Slicing** | Interactive tabs for Steps, Calories, Sleep, and more |
| 3 | **Reshaping** | Visualizes `(7,1)` and `(3,7)` reshape operations |
| 4 | **Filtering** | Filters rows by Steps > 8000, Sleep < 6, Calories > 300 |
| 5 | **Statistics** | Avg, Max, Min, Std Dev, and Range metrics |
| 6 | **Insights** | Glassmorphism cards with data-driven analysis |

---

## 🗂️ Project Structure

```
Fitness/
├── app.py              # Streamlit web application
├── activity.py         # Pure NumPy solution (console output)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/mohamedmamdohlotfy/Fitness.git
cd Fitness
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit app**
```bash
streamlit run app.py
```

**4. Or run the console version**
```bash
python activity.py
```

---

## 📈 Key Insights

- 🔗 **Steps & Calories** are strongly correlated — more steps = more calories burned
- ⚠️ **Day 7** is the outlier — highest steps (12,000) but lowest sleep (5 hrs)
- ✅ **Day 4** is the most balanced — 8,000 steps with 8 hours of sleep
- 🎯 **Sweet spot** — 7,000–9,000 steps with 7+ hours of sleep

---

## 🛠️ Built With

- [Python 3.14](https://www.python.org/)
- [NumPy](https://numpy.org/) — Array operations & statistics
- [Streamlit](https://streamlit.io/) — Interactive web dashboard

---

## 👨‍💻 Author

**Mohamed Mamdoh Lotfy**

[![GitHub](https://img.shields.io/badge/GitHub-mohamedmamdohlotfy-181717?style=flat&logo=github)](https://github.com/mohamedmamdohlotfy)

---

<div align="center">
  <sub>Built with ❤️ as part of the NTI Python & NumPy Training</sub>
</div>
