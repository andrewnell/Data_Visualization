import altair as alt
import pandas as pd
import numpy as np
import json
import os

# alt.renderers.enable('notebook')
def dataPull(zipcode):
    """
    Function to read in restaurant data per zip from
    Json file and convert to dataframe
    """

    # REad in Data
    #Set dynamic base path
    directory = os.path.dirname(__file__)
    #Load restaurant data
    data = json.load(open(os.path.join(directory, 'nyc_restaurants_by_cuisine.json'), 'r'))

    # Create empty array for storing data
    cuisinetype = []

    # Run function for specified zipcode to detrmine all cuisine types and number of restaurants
    for i in range(len(data)):

        # Try-except to ensure if the key does not exist for that zip a 0 value is pulled
        try:
            # Append array with actual value
            cuisinetype.append([data[i]['cuisine'], data[i]['perZip'][zipcode]])
        except KeyError:
            # Append array with 0
            cuisinetype.append([data[i]['cuisine'],0])


    # Store as dataframe
    zipdf = pd.DataFrame(cuisinetype, columns=['cuisine','restaurants']).sort_values('restaurants', ascending=False)[:15]

    # If incorrect zipcode, sum will be zero. To ensure empty plot is returned
    # if zipdf.restaurants.sum() == 0:
    #     zipdf = ''

    return zipdf

def createChart(data, zipcode):
    #color_expression    = "highlight._vgsid_==datum._vgsid_"
    #color_condition     = alt.ConditionalPredicateValueDef(color_expression, "SteelBlue")
    highlight_selection = alt.selection_single(name="highlight", empty="all", on="mouseover")
    rating_selection    = alt.selection_single(name="rating", empty="all", encodings=['y'])
    #maxCount            = int(data['restaurants'].max())

    barMean = alt.Chart() \
        .mark_bar(stroke="Black") \
        .encode(
            alt.X("mean(restaurants):Q", axis=alt.Axis(title="Restaurants")),
            alt.Y('cuisine:O', axis=alt.Axis(title="Cuisine"),
                  sort=alt.SortField(field="restaurants", op="mean", order='descending')),
            alt.ColorValue("LightGrey"),#, condition=color_condition), # Remove color condition
        ).properties(
            width=200,
            height=350,
            selection = highlight_selection+rating_selection,
        )

    return alt.hconcat(barMean,
        data=data,
        title="Cuisines in {}".format(zipcode)
    )