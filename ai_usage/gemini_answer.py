import pandas as pd
import altair as alt

# 1. Load Data
circuits = pd.read_csv('data/circuits.csv')
races = pd.read_csv('data/races.csv')

# Aggregate Data (Count races & find debut year)
stats = races.groupby('circuitId').agg(
    race_count=('raceId', 'count'),
    first_year=('year', 'min')
).reset_index()

map_data = pd.merge(circuits, stats, on='circuitId')

# 2. FILTERING: "The Rest of the World" (NOT Europe)
# We define the European box, and put a '~' (tilde) in front to invert it.
# Logic: Keep row IF NOT (Inside Europe Box)
non_europe_data = map_data[
    ~ ( # <--- The Tilde means "NOT"
        (map_data['lat'] > 35) & (map_data['lat'] < 70) & 
        (map_data['lng'] > -25) & (map_data['lng'] < 40)
    )
]

# 3. Create Map Background
world_url = "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json"
world = alt.topo_feature(world_url, 'countries')

background = alt.Chart(world).mark_geoshape(
    fill='#e0e0e0', stroke='white'
)

# 4. Create Points
points = alt.Chart(non_europe_data).mark_circle().encode(
    longitude='lng:Q',
    latitude='lat:Q',
    size=alt.Size('race_count:Q', scale=alt.Scale(range=[30, 400]), title='Races Hosted'),
    color=alt.Color('first_year:Q', scale=alt.Scale(scheme='turbo', reverse=True), title='Debut Year'),
    tooltip=['name', 'location', 'country', 'year']
)

# 5. Assemble Chart
# We use 'equalEarth' projection to show the whole world nicely without Europe dominating
chart = (background + points).project(
    type='equalEarth' 
).properties(
    title='Global Frontiers: F1 Outside of Europe',
    width=800,
    height=450
)

chart.save('f1_rest_of_world.json')
chart.display()