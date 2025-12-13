# 🏎️ The Historical Evolution & Geography of Formula 1
### Data Visualization Portfolio

**Author:** [Your Name]  
**Course:** [Course Name/Number]  
**Date:** [Date]

---

## 📖 Project Overview
This portfolio explores the 74-year history of Formula 1, analyzing how the sport has evolved from a niche European championship into a global spectacle. Through five interactive visualizations, we examine the **geographical expansion** of the circuits and the **dynastic battles** between the sport's greatest constructors.

The project demonstrates the "Eras of Dominance" in F1, showing how teams like Ferrari, McLaren, and Mercedes have risen and fallen over decades.

**🔗 [Link to Video Presentation (YouTube/Drive)](Put_Your_Link_Here)**

---

## 📊 The Visualizations

### 1. 🌍 The Global Expansion of Formula 1 (Interactive Map)
* **Type:** Geospatial Map (Mercator Projection)
* **Question:** How has the geography of F1 expanded since 1950?
* **Insight:** Visualizes the shift from a Euro-centric calendar to a global tour, with recent expansions into the Middle East and Americas (colored by Debut Year).

### 2. 📈 The Race to History: Cumulative Wins (Line Chart)
* **Type:** Multi-Line Chart
* **Question:** Which constructor is the greatest of all time?
* **Insight:** Tracks the cumulative victory count of the Top 8 teams, highlighting Ferrari's consistent rise and Mercedes' rapid ascent in the hybrid era.

### 3. 🏔️ The Eras of Dominance: Share of Wins (Stacked Area)
* **Type:** Normalized Stacked Area Chart (Streamgraph)
* **Question:** How has the balance of power shifted between manufacturers?
* **Insight:** Shows the "Market Share" of wins per season. It clearly defines the specific eras of dominance (e.g., the "Williams Era" of the 90s, the "Red Bull Era" of today).

### 4. 🏆 All-Time Constructor Leaderboard (Bar Chart)
* **Type:** Horizontal Bar Chart
* **Question:** Who are the giants of the sport?
* **Insight:** A clean ranking of the Top 15 teams by total Grand Prix victories.

### 5. 🏛️ The Temples of Speed: Top Host Countries (Bar Chart)
* **Type:** Bar Chart
* **Question:** Which nations are the pillars of F1 history?
* **Insight:** Demonstrates that despite global expansion, Italy, Germany, and the UK remain the historical core of the sport.

---

## 🛠️ Tools & Technologies
* **Language:** Python 3.9+
* **Libraries:**
    * `pandas` (Data Manipulation & Cleaning)
    * `geopandas` (extends the datatypes used by pandas to allow spatial operations on geometric types)
    * `altair` (Declarative Statistical Visualization)
    * `matplotlib` (plotting and data visualization library)

---

## 📂 Repository Structure

```text
├── data/                 # Raw CSV datasets
│   ├── circuits.csv
│   ├── constructor_results.csv
│   ├── cinstructor_standings.csv
│   ├── costructors.csv
│   ├── driver_standings.csv
│   ├── drivers.csv
│   ├── lap_times.csv
│   ├── pit_stops.csv
│   ├── qualifying.csv
│   ├── races.csv
|   ├── results.csv
│   ├── seasons.csv
│   ├── sprint_results.csv
│   └── status.csv
|   
├── main.ipynb           # Jupyter Notebooks containing the Python code
└── README.md             # Project Documentation
