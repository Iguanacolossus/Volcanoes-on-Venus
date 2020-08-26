# Detecting Volcanoes on Venus with a CNN

 ## The Data
 This dataset contains images collected by the Magellan expedition to Venus. Venus is the most similar planet to the Earth in size, and therefore researchers want to learn about its geology. Venus' surface is scattered with volcanos, and the aim of this dataset was to develop a program that can automatically identify volcanoes (from training data that have been labeled by human experts between 1-with 98% probability a volcano- and 4-with 50% probability)
link to data: https://www.kaggle.com/fmena14/volcanoesvenus?</br>
- Images from this data source come in a csv of 7000 flattened images with 12100 pixels each:</br>
<!-- ![eda1](images/volcanoe-eda-screenshot.png)</br> -->
![images](images/volcano_images.png)
<!--![eda2](images/vov_sreen2.png) --></br>

**Class Imbalance check**</br>
![classes](images/class-imbalance.png) </br>
**If I can get to it**
- perform some clustering to identify subgroups. clusters may reveal possibly the size categories to be compared to the radius column in labels set. or clusters could help identify if there are multiple volcanoes in the image and can be compared to the 'number of volcanoes' column in labels set.
- compare the cnns performance with other types of models (non nn) with a roc curve.








