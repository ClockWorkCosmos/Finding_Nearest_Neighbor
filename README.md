# Finding_Nearest_Neighbor
Python; Nearest Neighbor Problem

How this program is useful:
* Computer vision
	1. Image Retrieval: Finding similar images in a database based on visual similarity.
	2. Object Recognition: Identifying objects by comparing them to known prototypes.
	3. Face Recognition: Matching a given face with the nearest neighbors in a database.

* Machine learning
	1. k-Nearest Neighbors (k-NN): A classification algorithm that assigns a class label based on the majority class of its k-nearest neighbors.
	2. Anomaly Detection: Identifying outliers or unusual patterns in datasets.

* Natural language processing
	1. Document Similarity: Determining the similarity between documents for tasks like clustering or recommendation systems.
	2. Spelling Correction: Identifying and suggesting corrections for misspelled words by considering their nearest neighbors in terms of character similarity.

* Geographic information systems
	1. Spatial Analysis: Locating nearby points of interest or features on a map.
	2. Route Planning: Finding the closest facilities, such as gas stations or restaurants, for navigation.

* Data mining and analysis
	1. Clustering: Grouping similar data points together.
	2. Outlier Detection: Identifying unusual or abnormal data points.

* Robotics 
	1. Path Planning: Determining the next best move or location for a robot based on proximity to its surroundings.
	2. Object Grasping: Selecting the best grasp point for picking up objects.

Required modules / libraries:
* Math
* Random
* Pygame

Algorithm:
  1. Plot random points with randomly associated 'X' and 'Y' coordinates
  2. Origin point is always 'A'
  3. Compare distance between origin point and all other points
  4. Find median distance from 'X' and 'Y' coordinate distance ( ('X' position distance + 'Y' position distance) / 2 )
  5. Select point with the lowest median distance as the nearest neighbor
