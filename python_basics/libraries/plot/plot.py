import plotly.express as px

# Sample data for a scatter plot
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [50, 60, 65, 75, 85]
}

# Create a scatter plot
fig = px.scatter(data, x='Height', y='Weight', title='Height vs. Weight')
fig.show()
