## Find Coffee Shops in Populated Cities in US
--- Visualization Project CUSP

## Team members

Andrew Neil      NetID: adn323

Alex Shannon     NetID: acs882

Baoling Zhou     NetID: bz882

## Visualization Link: 
http://ando9.pythonanywhere.com/


![alt text](https://raw.githubusercontent.com/andrewnell/Data_Visualization/master/DataViz2018_adn323/Project/coffee_app_image.PNG)

- Instruction: 
1. After you get into the page, you can select a city and unchecked boxes to customize the filter
2. Then, you click the "update" buttom and a map with plots be shown on the right-hand side. 
3. Selection function: you can click the square box on the top right and then click the "selection" buttom. Doing this will enable the radius circle shown on the map. You can move the circle around and strech it in different sizes which displays coffee shops within the circle only. (This function will be activated automatically every time when you click the map).

## Objectives of the project
#### A brief context of the project, and what tasks you're aiming to solve using visualizations, domain(target user) and task abstraction.
We built a multifunctional web page which enables users to see all the available coffee shops in 25 cities around the United States under several filtering functions, such as price level, coffee shop types (as defined by us) and minimum rating.  Our target audience are coffee lovers and people looking for coffee shops with specific features, like bakeries and ice-cream. It's also a great tool for people who want to explore the coffee shop availability when deciding what area to move to, work in etc..


## Data set involves
Our project deals with data from coffee shops in 25 major American cities. This data did not exist in a clean format, so we wrote a script to interface with Yelp and Zillow APIs. The pulled data is then aggregated with a spatial join and concatenated to produce our final dataset. To perform initial exploratory analysis and to gain a better understanding of the 'coffee-shop-footprint' of different cities, we graphed location and plot data, as can be seen in our iPython Notebook. We used this analysis to inform our choice of relevant categories and to better anticipate what users may want to find on our web-visualization. 

## Descriptions on your visualization design choices. For example, why you're choosing the types of visualization, representations, and/or interactions in your project.

Visualization Representation:
- Dot points indicating coffee shops on the map show the location of coffeeshops in 25 cities. The size of the points indicates the number of reviews available in the yelp data for different coffee places. The more reviews there are, the bigger the points will be. This provides an easy to use way to identify coffee shops in a neigjbpurhood that can meet specific criteria of the user. One major shortcoming is the exclusion of tooltips which would make the visualization much more effective for a user who could see what specific coffee shop they are looking at.

- Graphical section on the bottom left contains three parts: all the charts created are based on coffee shops remained after UI filtering. This provides a quick and easy to see way of visualizing the distribution of coffee shops with the UI selection criteria. 

1. A bar chart representing the proportion of different types of coffee meeting selection criteria
2. A histogram showing distribution of coffee shops by rating.
3. A histogram showing distribution of coffee shops by price.

One major shortcoming is that it only updates on UI seelction croteria rather than what is shown in the map when using the circle selection or zooming in. However, it provides enough insights for the users to compare cities. However this feature should eb added in. 

Interactions:
- User Interface lets you selct coffee shops to show based on city, type of coffee shop, cost and rating according to yelp. The user can then seleect the update button and the charts and map will update. 
- selection function: you can click the square box on the top right and then click the "selection". Doing this will enable the radias circle shown on the map. You can move it around and strech it in different sizes and shows coffee shops within the circle only. (This function will be activated automatically every time when you click the map, but the radias circle will be invisible at that point. you can click the "selection" buttom to make it visible)

## Outcome and Evaluation: how did the visualization helps your users to achieve the objectives.
The visualization provides the user with a quick and easy to use tool that lets them view cities and neighbourhoods within cities by coffee shop type, cost and rating. This will make it easy to assess choices between different areas to live and work or meet someone. 

Shortcoming
* The visualization has no tooltip that would make it easier for the user to identify coffee shops. 
* the chart does not updated based on selection circle or zoom of map, which means the user cannot understand the specific characteristics of a specific neighbourhood. 

These two features should be improved. 


## Visualization Tools Used
React, Javascript, Carto, Python, PythonAnywhere, 



