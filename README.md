# Jaws

## Introduction

We will be analyzing the shark attacks dataset from Kaggle, where we obtain plenty of information about shark attacks around the world.
The poblem is the Data, which is not very clean, so we need to do a good cleaning before use them.

To make it funnier I have created maps to show where are the sharks attacks around the world and to respond/desmostrate my hypothesis

![image](https://user-images.githubusercontent.com/82879300/130495531-2bddc7fe-486e-4e1a-bda1-254fd5149167.png)



## Hypothesis
### 1.- Which coasts are the ones with more number of attacks?
### 2.- How are the sharks species distributed around the world?
### 3.- How will be the distributions of death attacks around the world?

### Data Cleaning
 I did a general data general cleaning fo columns and rows. The more specific clean have been done on the analysis stage.
### 1.-Row Cleaning

#### droppiing all rows where all columns are Nans
```` python 
df_sharks.dropna(how="all", inplace=True)
````

##### There are plenty of rows with all NaNs columns and a 0 on "Case Number" so we drop all those rows.
![image](https://user-images.githubusercontent.com/82879300/130502557-374a01e1-675a-4329-af16-8bd4b9964e9b.png)


### 2.-Columns deleted
We delete all columns we don't see necessary on this first cleaning stage.
````
df_sharks.drop(columns=["Case Number.1","Case Number.2"], inplace=True)
df_sharks.drop(columns=['Unnamed: 22', 'Unnamed: 23'], inplace=True)
df_sharks.drop(columns=['href formula', 'href', "Name", 
                        "Investigator or Source", "pdf", "original order"], inplace=True)
````

### Analysis
  
#### Map Preprocesing
Before starting to demostrate our hypothesis, we need to create a Data Frame with the structure required for displaying them in a Map.

* Create the structure of data (list of dictionaries) to store the columns we need.
* Use GeoPandas library to get the latitude, longitude from a location and adding it to our structure. If we have any problem (exception) on the process we don't add the info but we continue the iteration.
* Get info from the columns: Location, Species, Fatal and Year but keeping only the ones where we get a correct latitude longitude
* Create a Data Frame from our structure and save it in a pickle file:
  ** The process of getting latitude, longitude from a location is very slow so we need to save that info in a file so that we can recover it at the momment we would like to.

![image](https://user-images.githubusercontent.com/82879300/130497334-4c53ec22-657a-4428-8da5-5496f81426f9.png)



### 1.- Which coasts are the ones with more number of attacks ?¶
We use geopandas library to have a global idea about the location of the attacks around the world.

There are lots of attacks very close to each other so we need to use the alpha parameter to show more intensity of color where there are more atacks

![image](https://user-images.githubusercontent.com/82879300/130497642-588bab0a-6143-4cb7-aaaf-30ed65e2afe5.png)


Just with a quick view on the maps we can see that the intensity of the attacks are more clear on :

* North America West and East Coast
* South Africa Coast
* Austrila West Coast and East Coast with more intensity
* Obviously there are more places with lots of attacks but not with that intensity

### 2.- How are the sharks species distributed around the world?

![image](https://user-images.githubusercontent.com/82879300/130499661-a765e5b0-3187-47b7-a97f-3acb5a94ff7d.png)

Doing doble click on the leyend we can isolate any of the species on the map and we can see clearly that every kind of shark has their own areas (but sometimes really far away ones from another)

![image](https://user-images.githubusercontent.com/82879300/130499959-2a27dcb6-7423-433c-b3c3-ef9b46f3ecc3.png)

We can do zoom on the maps and in this case we are just seeing Lemon shark attacs. 

I have added rivers/lakes to his new map, because some of the attacks are on river apparently, but after taking a look most of them are on land which makes no sense, but might be for different causes:

* Location Data is wrong in those cases
* GeoPandas library returns an incorrect longitude, latitude from a Location
* There are rivers or lakes which doesn't appear on the map.

### 3.- How will be the distributions or death attacks around the world?

We are going to investigate how deadly are our 5 top Species and their location around the world.
![image](https://user-images.githubusercontent.com/82879300/130501287-a868c29e-4527-4540-91f5-4e4bf278fc9b.png)
We check that there are 3 dangerous species (White Shark, Tiger Shark and Bull Shark).


![image](https://user-images.githubusercontent.com/82879300/130501451-8edfa2f9-af14-45ea-ba27-8d1d1b1224c9.png)
There is not a big difference between locations where there are deahtly attacks and where there are not. In this maps all kind of sharks has been added (included Others).

### Conclusion

This is a fun dataset where you can practice all your cleaning skills.

I have been able of getting a lot of location information about the attacks that give us a cool spatial vision about it.

Maybe I will work a bit more on this dataset on the future but "We're going to need a bigger boat"
