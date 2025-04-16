# Club and Nationality Viewing App

This is a simple and interactive Streamlit web application that allows users to filter and visualize football player data by Club and Nationality using dropdowns in the sidebar. The resulting subset of data is displayed as a table and a Plotly scatter plot.

---

## Features

- Load and cache a CSV file (`football_data.csv`) containing player statistics
- Sidebar multiselect filters for:
  - Club
  - Nationality
- Interactive scatter plot showing:
  - Player's Overall rating vs. Age
  - Points colored by player name

---

## Requirements

Make sure you have the following Python packages installed:

```bash
pip install streamlit pandas numpy plotly
```

---

## How to Run

1. Make sure you have a CSV file named `football_data.csv` in the same directory as the script.
2. Run the app using:

```bash
streamlit run Streamlit.py
```

---

## Notes

- The app uses `st.cache_data` to cache the loaded data for performance.
- The scatter plot updates dynamically based on your selections.

---

## File Structure

```
.
├── Streamlit.py
└── football_data.csv
```
