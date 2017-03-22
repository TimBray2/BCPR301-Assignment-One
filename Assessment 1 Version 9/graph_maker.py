import plotly


def create_graph(stored_data):
    male_count = 0
    female_count = 0
    for item in stored_data:
        if item[1] in ["M", "Male"]:
            male_count += 1
        elif item[1] in ["F", "Female"]:
            female_count += 1
    fig = {
        'data': [{'labels': ['Male', 'Female'],
                  'values': [male_count, female_count],
                  'type': 'pie'}],
        'layout': {
            'title': 'Number of Males vs Females Saved'}
    }

    plotly.offline.plot(fig)
