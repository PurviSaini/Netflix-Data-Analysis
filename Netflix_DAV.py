#!/usr/bin/env python
# coding: utf-8

# # <center style="background-color:black;padding:50px;border-radius:23px;"><span style="margin:5px;color:white; font-family:monospace;font-size:20px;letter-spacing:12px;word-spacing:20px"><span style="border-radius:23px;border:2px dashed #E50914; padding:0 15px;color: #E50914;background-color:black;font-size:60px;">NETFLIX</span><br> <BR> Data Analysis and Visualization</span> </center>

# ## <p style="color: #ff6666; font-family:cursive;">Team Members: </p>
# 
# - **Seemran Sethi (13526)**
# - **Shikha Dhiman (13538)**
# - **Purvi Saini   (13546)**
# - **Deepali       (13559)**

# ## <p style="color: #ff6666; font-family:cursive;">Attributes information:</p>
# 
# 
# -	**Show_id - Unique ID for every Movie / TV Show (data type: object)**
# -	**Type – Categorizes the content as - A Movie or TV Show (data type: object)**
# -	**Title - Title of the Movie / TV Show (data type: object)**
# -	**Director – Name of the person(s) who directed the movie (data type: object)**
# -	**Cast – Actors/Actresses involved in the movie/show (data type: object)**
# -	**Country - Country where the movie/show was produced (data type: object)**
# -	**Date_added - Date it was added on Netflix (data type: object)**
# -	**Release_year - Actual Release year of the movie/show (data type: int64)**
# -	**Rating: Rating of the movie/show (data type: object)**
# - **Duration - Total Duration in minutes or number of seasons (data type: object)**
# - **Listed_in – Genre of the movie/show (data type: object)**
# - **Description - The summary description of the movie/show (data type: object)**
# 

# ## **<p style="color:#ff6666; font-family:cursive;">Objective:</p>**
# 
# - **Analyze the data and generate insights that could help Netflix in deciding which type of shows/movies to produce and how they can grow the business in different countries.**

# ## **<p style="color:#ff6666; font-family:cursive;">Importing the required libraries :</p>**

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## **<p style="color:#ff6666; font-family:cursive;">Storing the dataset as a dataframe :</p>**

# In[2]:


netflix = pd.read_csv("netflix_titles.csv")


# <hr noshade style="height:2px;">

# # <center><span style="color:crimson; font-family:monospace;font-size:35px;border-bottom:3px solid">Data Description</span></center>

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>First 10 rows in the dataset are :</i><span>

# In[3]:


netflix.head(10)


# In[4]:


print('\033[1m'+'Shape of Dataset is : ',netflix.shape)
(rows, cols) = netflix.shape
print("Thus, the dataset has : \n",rows,' Rows\n',cols,' Columns')


# ### &#9672;   <span style=" color: #ff6666; font-family:monospace;"><i>Information about the netflix dataset :</i></span>

# In[5]:


netflix.info()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:</span>
# >---
# >* ***Dataset is having 11 Object Data type columns and 1 Integer dataType Column. Some columns contain missing values.***
# >* ***We can see date_added column is of object type which should be of datetime.***
# >* ***We can see type and rating columns are also of object type which should be of category.***

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>The description of numerical data in the dataset is :</i></span>

# In[6]:


netflix.describe()


# ### &#9672;  **_<span style=" color: #ff6666; font-family:monospace;">Columns in the dataset are :</span>_**

# In[7]:


netflix.columns


# <hr noshade style="height:2px;">

# # <center><span style="color:crimson; font-family:monospace;font-size:35px;border-bottom:3px solid;">Handling Missing Values</span></center>

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Total number of null values in each column is/are :-></i></span>

# In[8]:


netflix.isnull().sum()


# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Checking the percentange of null values in each column is :-></i></span>

# In[9]:


for col in netflix.columns:
    null = netflix[col].isnull().sum()
    percentage = (null/len(netflix))*100
    print(col,":", percentage,"%")


# **Since columns: cast, country, date_added, duration, rating are having less than 10% null values, droping these NaN values wouldn't affect the dataset much.<br>Thus,**

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>Dropping null values from columns: cast, country, date_added, duration and rating :-></i></span>

# In[10]:


netflix.dropna(subset=['cast','country','date_added','duration','rating'],how='any', inplace=True)


# In[11]:


print('\033[1m Shape of dataset after dropping NaN values is : ', netflix.shape)


# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>Filling the null values of director by 'Not Known':-></i></span>

# In[12]:


netflix['director'].fillna(value='Not Known', inplace=True)


# In[13]:


netflix.isnull().sum()


# ***There is no null value in the dataset now***

# In[14]:


netflix.shape


# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Converting the data type of some columns:-></i></span>

# In[15]:


# - Converting 'date_added' column to datetime
netflix['date_added'] = pd.to_datetime(netflix.date_added)

# - Converting appropriate columns to category type.
netflix = netflix.astype({'type': 'category',
                           'rating':'category'})


# In[16]:


netflix.info()


# In[17]:


netflix.duplicated().sum()


# 
# ***Thus, there is no duplicate values in the dataset.***

# **There is no use of Description column in the analysis so we can drop that column:->**

# In[18]:


netflix.drop('description', axis=1, inplace=True)


# <hr noshade style="height:2px;">

# 
# # <center><span style="color:crimson; font-family:monospace;font-size:35px;border-bottom:3px solid;">Handling Outliers</span></center>

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>Viewing the box plot of columns having quantitaive data in the dataset:-></i></span>

# In[19]:


netflix.boxplot(column='release_year')


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
#     >* **We can clearly see here that there are many outlier values in <i>'release_year'</i> column but we can't manipulate or remove these outlier values because there is no limit on the releasing years. Hence we will not operate on these outlier values.**

# <hr noshade style="height:2px;">

# # <center><span style="color:crimson; font-family:monospace;font-size:35px;border-bottom:3px solid;">Queries</span></center>

# ### &#9672;   <span style=" color: #ff6666; font-family:monospace;"><i>Query 1:-></i></span> 
# >### <span style=" color: #ff6666; font-family:monospace;">Checking total number of Movies and TV shows added on Netflix</span>

# In[20]:


count = netflix['type'].value_counts()
print('\033[1m Total number of Movies : ',count['Movie'])
print('\033[1m Total number of TV shows : ',count['TV Show'])


# In[21]:


# Plotting Pie chart for comparison between total number of movies and total number of tv shows
plt.figure(figsize = (10,5))
plt.pie(count, 
        labels=['Movies', 'TV Shows'],
        shadow=True, 
        radius= 1.5, 
        colors = ["#DC143C","#FF8A8A"], 
        explode=[0,0.1], 
        startangle=90, 
        autopct= "%0.2f%%")
plt.legend(['Movies', 'TV Shows'], fontsize=13,
          title ="Content Type",
          loc ="center left",
          bbox_to_anchor =(1.3, 0.5, 2.5, 1.1))
plt.title('Movies V/S TV Shows',fontsize = 20, fontweight = 'bold',loc='center', pad=45)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***Large number of Movies are added on Netflix as compared to TV Shows.***

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>Query 2:-></i></span>
# >### <span style=" color: #ff6666; font-family:monospace;">Checking the type of content added on Netflix over the years

# In[22]:


#Adding required columns in the dataset

netflix['year_added']=netflix['date_added'].dt.year
netflix['month_added']=netflix['date_added'].dt.month_name()
netflix['day_added']=netflix['date_added'].dt.day_name()


#Dropping date_added column

netflix.drop('date_added', axis=1, inplace=True)
netflix.head()


# **Splitting the dataset into separate groups of year:**

# In[23]:


#grouping the data by column 'year_added'

grouped = netflix.groupby('year_added')['type'].value_counts().unstack()
grouped


# In[24]:


#Plotting
plt.figure(figsize = (15,5))
plt.plot(grouped['Movie'], marker='o', color='#DC143C')
plt.plot(grouped['TV Show'], marker='o', color='#FF8A8A')
plt.xlabel('Year',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.xticks(size = 10, ha="right")
plt.yticks(size = 10)
plt.title('Content added over the years on Netflix', fontsize=20, fontweight="bold")
plt.legend(['Movies', 'TV Shows'], loc='upper left')
plt.grid()
plt.show()


# >### <span style=" color: red; font-family:monospace;"> CONCLUSION:
# >---
# >* ***After year 2015 a lot of content is added on Netflix.***
# >* ***The number of movies added became significantly larger than TV shows since 2017.***
# >* ***There is a significant drop in content addition in both type after 2019, that is because of Covid.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 3:-></i></span> 
# >### <span style=" color: #ff6666; font-family:monospace;">Overall content added by netflix each month

# **Splitting the dataset into separate groups of Month:**

# In[25]:


grouped = netflix['month_added'].groupby(netflix['type']).value_counts().unstack('type')
grouped


# **Plotting Bar plot to check the count of content added each month:**

# In[26]:


plt.figure(figsize = (15,5))
fig = plt.subplots(figsize =(12, 10))
p1 = plt.bar(grouped.index, grouped['TV Show'], 0.5, color='#DC143C')
p2 = plt.bar(grouped.index, grouped['Movie'], 0.5,
             bottom = grouped['TV Show'], color='#FF8A8A')
plt.ylabel('Content',fontsize = 15)
plt.xlabel('Months',fontsize = 15)
plt.title('Month with most Content',fontsize = 20, fontweight = 'bold')
plt.legend((p1[0], p2[0]), ('TV Shows', 'Movies'))
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >* ***Most content was added on Netflix in the month of December, January and October in total.***
# > * ***Also the number of Movie content added is much higher than TV Show for every month.***

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>Query 4:-></i>
# >### <span style=" color: #ff6666; font-family:monospace;">Checking the number of movies and TV Shows added on Netflix every month

# **Plotting Bar plot to compare the number of Movies with the number of TV Shows added on Netflix every Month:**

# In[27]:


X_axis = np.arange(len(grouped.index))
plt.figure(figsize = (15,5))
plt.bar(X_axis-0.1, grouped['Movie'], 0.2, label = 'Movies', color='#DC143C')
plt.bar(X_axis+0.1, grouped['TV Show'], 0.2, label = 'TV Shows', color='#FF8A8A')
plt.title("Number of Movies & TV Shows uploaded each Month", fontsize = 20, fontweight = 'bold')
plt.xlabel("Month", fontsize = 15)
plt.ylabel("Number of Movies & TV Shows",fontsize=15)
plt.xticks(X_axis, grouped.index, size = 10)
plt.yticks(size = 10)
plt.legend()
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***On an average more movies were added on Netflix in the month of December, January and October.***
# >* ***On an average more TV Shows were added on Netflix in the month of December and July.***
# > * ***Also the number of Movie content added is much higher than TV Show for every month.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 5:-></i>
# >### <span style=" color: #ff6666; font-family:monospace;">Checking overall content added on Netflix monthly per year

# In[28]:


year_month_count = (netflix.loc[:,['year_added','month_added']]
                    .value_counts()
                    .reset_index()
                    .rename(columns={0:'count'})
                    .pivot("month_added", "year_added", "count")
                    .fillna(0)
                    .apply(lambda x: x.astype('int')))
year_month_count


# **Plotting Heatmap to check the content added on Netflix monthly over the years:**

# In[29]:


#plotting heatmap
plt.figure(figsize=(18,8))
ax = sns.heatmap(year_month_count, annot=True, fmt="d", cmap='Reds')
plt.ylabel('Month',fontsize = 15)
plt.xlabel('Year',fontsize = 15)
plt.title('Content added on Netflix monthly over the years',fontsize = 20, fontweight = 'bold')
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***The month of July has the highest content in 2021 but before 2021 content added in July was not very high.***
# >* ***If we do not consider the content added in 2021 as we don't have data for all months, then more content is added in October, November and December.***
# >* ***For year 2021 we do not have the data after september.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 6:-></i> 
# >### <span style=" color: #ff6666; font-family:monospace;">Overall content added by netflix each week day

# **Splitting the dataset into separate groups of weekdays:**

# In[30]:


grouped = netflix['day_added'].groupby(netflix['type']).value_counts().unstack('type')
grouped


# **Plotting bar graph to analyze the week day having most content:**

# In[31]:


plt.figure(figsize = (15,5))
fig = plt.subplots(figsize =(12, 10))
p1 = plt.bar(grouped.index, grouped['TV Show'], 0.4, color='#DC143C')
p2 = plt.bar(grouped.index, grouped['Movie'], 0.4,
             bottom = grouped['TV Show'], color='#FF8A8A')
plt.ylabel('Content',fontsize = 15)
plt.xlabel('Week Day',fontsize = 15)
plt.title('Week Day with most Content',fontsize = 20, fontweight = 'bold')
plt.legend((p1[0], p2[0]), ('TV Shows', 'Movies'))
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >* ***Large number of content is added on Friday and Thursday.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 7:-></i>
# >### <span style=" color: #ff6666; font-family:monospace;">Checking the Week day on which most Movies and TV Shows are added on Netflix

# **Plotting Bar plot to analyze the content added per week day on Netflix:**

# In[32]:


X_axis = np.arange(len(grouped.index))
plt.figure(figsize = (15,5))
plt.bar(X_axis-0.1, grouped['Movie'], 0.2, label = 'Movies', color='#DC143C')
plt.bar(X_axis+0.1, grouped['TV Show'], 0.2, label = 'TV Shows', color='#FF8A8A')
plt.title("Number of Movies & TV Shows uploaded per week day", fontsize = 20, fontweight = 'bold')
plt.xlabel("Weekday", fontsize = 15)
plt.ylabel("Number of Movies & TV Shows",fontsize=15)
plt.xticks(X_axis, grouped.index, size = 10)
plt.yticks(size = 10)
plt.legend()
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***On average Netflix added more movies on Friday and Thursday.***
# >* ***On an average significant number of TV Show are added on Friday than other days.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 8:-></i> 
# >### <span style=" color: #ff6666; font-family:monospace;">The most common durations of Movies.

# **Getting the durations of all the movies:**

# In[33]:


movie_durations = netflix[netflix['duration'].str.contains('min')]['duration'].apply(lambda x: x.split()[0]).astype('int')
movie_durations


# **Plotting Histogram and Boxplot to analyse the duration of Movies:**

# In[34]:


#plotting histogram
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(25,9))
g = sns.histplot(movie_durations, kde=True, color="#B00710", bins=50, ax = ax1)
ax1.set_title('Hist plot for Movie Duration', fontsize=20)
ax1.set_xlabel('Duration', fontsize=15)
ax1.set_ylabel('Count', fontsize=15)
g.set(xticks=np.arange(0, 350, 25))

# Box plot
sns.boxplot(x=movie_durations, color="#B00710", ax = ax2)
ax2.set_xticks(np.arange(0,350, 25))
ax2.set_xlabel('Duration', fontsize=15)
ax2.set_title('Box plot for Movies Durations', fontsize=20)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***Generally Movies have duration range around 100 minutes.***
# >* ***Also around 25 minutes there is an increase in count, that is because of short films.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 9:-></i>
# >### <span style=" color: #ff6666; font-family:monospace;">The most common number of seasons released on Netflix.

# **Getting the number of seasons for each TV Show on netflix:**

# In[35]:


seasons = netflix[netflix['duration'].str.contains('Season')]['duration'].value_counts().sort_values()
seasons


# **Plotting a bar graph to show the amount of shows that have the corresponding number of seasons:**

# In[36]:


plt.figure(figsize=(15,5))
ax = seasons.plot(y='duration', kind='barh',color=["#DC143C", '#FF8A8A'])
ax.set_title('Count of TV Show-Seasons added on Netflix', fontsize=20)
ax.set_xlabel('Number of TV Shows', fontsize=15)
ax.set_ylabel('Number of Seasons', fontsize=15)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***There is a significant drop of count of seasons after season 1.***
# >* ***Tv shows are of 1 - 2 Seasons mostly.***
# >* ***We can also observe that there are very rare TV shows having more than 10 seasons.*** 

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 10:-></i>
# >### <span style=" color: #ff6666; font-family:monospace;">Content as per rating

# **Getting the number of Movies and TV Shows for a particular rating:**

# In[37]:


grouped = netflix['rating'].groupby(netflix['type']).value_counts().unstack('type')
grouped


# **Plotting a bar graph to show the amount of Movies and TV Shows for each Rating type:**

# In[38]:


X_axis = np.arange(len(grouped.index))
plt.figure(figsize = (15,5))
plt.bar(X_axis-0.15, grouped['Movie'], 0.3, label = 'Movies', color='#DC143C')
plt.bar(X_axis+0.15, grouped['TV Show'], 0.3, label = 'TV Shows', color='#FF8A8A')
plt.title("Content as per ratings", fontsize = 20, fontweight = 'bold')
plt.xlabel("Weekday", fontsize = 15)
plt.ylabel("Number of Movies & TV Shows",fontsize=15)
plt.xticks(X_axis, grouped.index, size = 10)
plt.yticks(size = 10)
plt.legend()
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***Movies with rating TV-MA are mostly added and movies with rating NC-17, TV-Y7-FV, UR are negligible on netflix.***
# >* ***TV Shows with rating TV-MA are mostly added and there are no TV Shows with rating NC-17, TV-Y7-FV, UR, NR, R, PG-13,PG, G on netflix***
# >* ***Along with that TV-14 is also a commonly occurring rating in both Movies and TV Shows.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 11:-></i> 
# >### <span style=" color: #ff6666; font-family:monospace;">The count of content added as per audience type.

# **Dividing the Netflix content into 'Adult', 'Kid' and 'Teen' categories according to the rating:**

# In[39]:


# We are dividing audience in three types as per rating column
Kids = ['TV-Y', 'TV-Y7', 'G', 'TV-G', 'PG', 'TV-PG', 'TV-Y7-FV']
Teens = ['PG-13', 'TV-14']
Adults = ['R', 'TV-MA', 'NC-17', 'UR', 'NR']

def rate(x):
    if x in Kids:
        return 'Kid'
    elif x in Teens:
        return 'Teen'
    elif x in Adults:
        return 'Adult'
    
df1 = netflix['rating'].apply(rate)
df2 = pd.concat([df1, netflix['type']], axis=1)
df2


# **Getting the total number of Movies and TV Shows for each category:**

# In[40]:


grouped = df2['rating'].groupby(df2['type']).value_counts().unstack('type')
grouped


# **Plotting a bar graph showing the amount of Movies and TV Shows for each of the category:**

# In[41]:


X_axis = np.arange(len(grouped.index))
plt.figure(figsize = (10,5))
plt.bar(X_axis-0.15, grouped['Movie'], 0.3, label = 'Movies', color='#DC143C')
plt.bar(X_axis+0.15, grouped['TV Show'], 0.3, label = 'TV Shows', color='#FF8A8A')
plt.title("Content as per audience type", fontsize = 20, fontweight = 'bold')
plt.xlabel("Audience Type", fontsize = 15)
plt.ylabel("Number of Movies & TV Shows",fontsize=15)
plt.xticks(X_axis, grouped.index, size = 10)
plt.yticks(size = 10)
plt.legend()
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***Netflix added a lot of adult movies as compared to adult TV shows.***
# >* ***Adult and Teen content is the most common content on netflix.***
# >* ***Kid content is the least on Netflix for both movies and TV Shows.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 12:-></i>
# >### <span style=" color: #ff6666; font-family:monospace;">The count of content added for Top 20 countries.

# In[42]:


def explode_data(df, col, name, along):
    return (df[col].replace(' ,', ',').replace(', ',',').str.split(',')
                   .to_frame()
                   .set_index(df[along])
                   .explode(col)
                   .replace('',np.nan)
                   .replace('NA',np.nan)
                   .dropna()
                   .reset_index())


# In[43]:


countries = explode_data(netflix, 'country', 'country', 'type')
countries['country']=countries['country'].str.strip()
countries


# **Getting the number of Movies, TV Shows individually and both of them together for each country:**

# In[44]:


grouped = countries['country'].groupby(countries['type']).value_counts().unstack('type').replace(np.nan,0)
grouped.columns = grouped.columns.astype(str)
grouped['sum'] = grouped.sum(axis=1)
grouped=grouped.sort_values(by='sum', ascending=False)
grouped


# **Total there are 115 countries which are producing some content on Netflix:**

# In[45]:


#Top 20 countries producing content on Netflix
group=grouped.head(20)
group


# **Plotting bar graph of netflix content country-wise:**

# In[46]:


plt.figure(figsize = (20,10))
fig = plt.subplots(figsize =(12, 10))
p1 = plt.bar(group.index, group['TV Show'], 0.4, color='#DC143C')
p2 = plt.bar(group.index, group['Movie'], 0.4,
             bottom = group['TV Show'], color='#FF8A8A')
plt.ylabel('Content',fontsize = 15)
plt.xlabel('Country',fontsize = 15)
plt.xticks(size=10, rotation=60, ha='right')
plt.title('Top 20 countries producing content on Netflix',fontsize = 20, fontweight = 'bold')
plt.legend((p1[0], p2[0]), ('TV Shows', 'Movies'))
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***United States is producing much more content on netflix than any other country.***
# >* ***After United States, India and United Kingdom are the most content producing countries on Netflix.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 13:-></i> 
# >### <span style=" color: #ff6666; font-family:monospace;">Top 20 countries producing Movies and TV Shows respectively

# **Plotting a bar graph for number of movies and TV Shows separately for the top 20 countries:**

# In[47]:


#Top 20 countries producing Movies
grouped.sort_values(by='Movie',inplace=True, ascending=False)
group=grouped.head(20)
#Plotting
fig, (ax1, ax2) = plt.subplots(2,1,figsize=(18,15))
fig.subplots_adjust(hspace=0.5)
ax1.barh(group.index, group['Movie'], color=['#DC143C', '#FF8A8A'])
ax1.set_xlabel('Number of Movies', fontsize=20)
ax1.set_ylabel('Country', fontsize=20)
ax1.set_title('Top 20 Countries Producing Movies on Netflix', fontsize=25)

#Top 20 countries producing TV Shows
grouped.sort_values(by='TV Show', ascending=False, inplace=True)
group=grouped.head(20)
#Plotting
ax2.barh(group.index, group['TV Show'], color=['#DC143C', '#FF8A8A'])
ax2.set_xlabel('Number of TV Show', fontsize=20)
ax2.set_ylabel('Country', fontsize=20)
ax2.set_title('Top 20 Countries Producing TV Shows on Netflix', fontsize=25)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***The order of top 20 Movies and TV Shows separately is different.***
# >* ***In countries like India, Spain and Germany, Movies are more popular than TV Shows.***
# >* ***In countries like Japan, South Korea and Taiwan, TV Shows are more popular than Movies.***

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>Query 14:-></i>
# >### <span style=" color: #ff6666; font-family:monospace;">The amount of content added for Top 20 countries per year.

# **Getting the amount of netflix content of top 20 countries per year:**

# In[48]:


country_data = explode_data(netflix, 'country', 'country', 'year_added')
country_data['country']=country_data['country'].str.strip()
#As netflix content is grown after 2015, so we are considering that data
country_data = country_data[country_data['year_added']>2015]
country_data = (
    country_data
    [country_data['country'].isin(country_data['country'].value_counts().head(20).index)]
    .value_counts()
    .reset_index()
    .rename(columns={0:'count'})
    .pivot('country', 'year_added', 'count')
    .fillna(0)
    )
country_data


# **Plotting a heatmap of amount of content for the top 20 countries for years 2017-2021:**

# In[49]:


#plotting heatmap
plt.figure(figsize=(18,8))
ax = sns.heatmap(country_data, annot=True, fmt="f", cmap='Reds')
plt.ylabel('Country',fontsize = 15)
plt.xlabel('Year',fontsize = 15)
plt.title('Amount of content added for Top 20 countries per year',fontsize = 18)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***Top 5 countries where netflix is adding more content per year except United States are India, United Kingdom, Canada, France and Japan.***

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 15:-></i> 
# >### <span style=" color: #ff6666; font-family:monospace;">The top 10 genres popular on Netflix
# 

# In[50]:


genre=explode_data(netflix, 'listed_in', 'genre', 'type')
genre['listed_in']=genre['listed_in'].str.strip()
genre


# **Displaying the number of movies and tv shows according to different genres:**

# In[51]:


grouped = genre['listed_in'].groupby(genre['type']).value_counts().unstack('type').replace(np.nan,0)
grouped


# **Plotting the top 10 genres on netflix:**

# In[52]:


#Top 10 genres in Movies
grouped.sort_values(by='Movie', ascending=False, inplace=True)
group=grouped.head(10)
#Plotting
fig, (ax1, ax2) = plt.subplots(2,1,figsize=(18,15))
fig.subplots_adjust(hspace=0.5)
ax1.barh(group.index, group['Movie'], color=['#DC143C', '#FF8A8A'])
ax1.set_xlabel('Number of Movies', fontsize=20)
ax1.set_ylabel('Genre', fontsize=20)
ax1.set_title('Top 10 Genres in Movies on Netflix', fontsize=25)

#Top 10 genres in TV Shows
grouped.sort_values(by='TV Show', ascending=False, inplace=True)
group=grouped.head(10)

#Plotting
ax2.barh(group.index, group['TV Show'], color=['#DC143C', '#FF8A8A'])
ax2.set_xlabel('Number of TV Show', fontsize=20)
ax2.set_ylabel('Genre', fontsize=20)
ax2.set_title('Top 10 Genres in TV Shows on Netflix', fontsize=25)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***TV Show genres-Crime TV Shows and Kids' TV are more popular than their similar genre in Movies.***
# >* ***Movie genres-Documentaries and Action & Adventure are more popular than their similar genre in TV Show.***
# 

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 16:-></i> 
# >### <span style=" color: #ff6666; font-family:monospace;">The most popular genres added mostly per year on Netflix
# 
# 

# **Displaying the count of overall content according to different genres from 2016 to 2021:**

# In[53]:


genre_data = explode_data(netflix, 'listed_in', 'listed_in', 'year_added')
genre_data['listed_in']=genre_data['listed_in'].str.strip()

#As netflix content is grown after 2015, so we are considering that data
genre_data = genre_data[genre_data['year_added']>2015]
genre_data = (
    genre_data
    [genre_data['listed_in'].isin(genre_data['listed_in'].value_counts().head(10).index)]
    .value_counts()
    .reset_index()
    .rename(columns={0:'count'})
    .pivot('listed_in', 'year_added', 'count')
    .fillna(0)
    )
genre_data


# **Plotting heatmap for the most popular genres added mostly per year:**

# In[54]:


plt.figure(figsize=(18,8))
ax = sns.heatmap(genre_data, annot=True, fmt="f", cmap='Reds')
plt.ylabel('Genre',fontsize = 15)
plt.xlabel('Year',fontsize = 15)
plt.title('most popular genres added mostly per year',fontsize = 18)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***Five most popular genres in recent years are International movies, Dramas, Comedies, International TV Shows and Action & Adventure.***
# 
# 

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 17:-></i> 
# >### <span style=" color: #ff6666; font-family:monospace;">Top 10 Movie genre per country
# 
# 
# 

# In[55]:


def make_data(df):
    return (
        df
        [df['country'].isin(df['country'].value_counts().head(10).index)]
        .value_counts()
        .reset_index()
        .rename(columns={0:'count'})
        .pivot("listed_in", "country", 'count')
        .fillna(0)
        )


# In[56]:


country_data = explode_data(netflix, 'country', 'country', 'title')
country_data['country'] = country_data['country'].str.strip()

genre_data = explode_data(netflix, 'listed_in', 'listed_in', 'title')
genre_data['listed_in']=genre_data['listed_in'].str.strip()

genre_data_type = explode_data(netflix, 'listed_in', 'listed_in', 'type')
genre_data_type['listed_in']=genre_data_type['listed_in'].str.strip()

genre_data_type = genre_data_type.value_counts().reset_index(level=1)
top_movie_genres = list(genre_data_type.loc['Movie'].head(10)['listed_in'].values)

df = country_data.merge(genre_data).drop('title', axis=1)
df1 = df[df['listed_in'].isin(top_movie_genres)]
df1 = make_data(df1)
df1


# **Plotting heatmap for the top 10 Movie genre per country:**

# In[57]:


plt.figure(figsize=(18,8))
ax = sns.heatmap(df1, annot=True, fmt="f", cmap='Reds')
plt.ylabel('Genre',fontsize = 15)
plt.xlabel('Country',fontsize = 15)
plt.title('Top 10 Movie genre per country',fontsize = 18)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***Top 3 genres in movies for top 3 countries are:-***
# > - **United States** :	Dramas, Comedies, Action & Adventure
# > - **India** :	International Movies, Dramas and Comedies
# > - **United Kingdom** :	Dramas, International Movies, Documentries
# 
# 
# 
# 
# 
# 
# 

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>Query 18:-></i> 
# > ### <span style=" color: #ff6666; font-family:monospace;">Top 10 TV Show genre per country

# In[58]:


top_tv_genres = list(genre_data_type.loc['TV Show'].head(10)['listed_in'].values)
df2 = df[df['listed_in'].isin(top_tv_genres)]
df2 = make_data(df2)
df2


# **Plotting the heatmap for top 3 genres in tv shows for top 3 countries:**

# In[59]:


#plotting heatmap
plt.figure(figsize=(18,8))
ax = sns.heatmap(df2, annot=True, fmt="f", cmap='Reds')
plt.ylabel('Genre',fontsize = 15)
plt.xlabel('Country',fontsize = 15)
plt.title('Top 10 Movie genre per country',fontsize = 18)
plt.show()


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***Top 3 genres in TV Shows for top 3 countries are:-***
# > - **United States** : TV Comedies, TV Dramas, Kids' TV
# > - **United Kingdom** : British TV Shows, International TV Shows, Docuseries
# > - **Japan** :	International TV Shows, Anime Series, Kids' TV
# 

# ### &#9672; <span style=" color: #ff6666; font-family:monospace;"><i>Query 19:-></i> 
# >### <span style=" color: #ff6666; font-family:monospace;">Top 10 Movie Cast

# **Displaying the number of movies top 10 actors had acted in:**

# In[60]:


cast_data = explode_data(netflix, 'cast', 'cast', 'type')
cast_data.value_counts().loc['Movie'].head(10)


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***We can see that in top 10 Movie cast, most people are from India.***
# 
# 
# 

# ### &#9672;  <span style=" color: #ff6666; font-family:monospace;"><i>Query 20:-></i></span>
# >### <span style=" color: #ff6666; font-family:monospace;">Top 10 TV Show cast
# 
# 
# 

# **Displaying the number of tv shows top 10 actors had acted in:**

# In[61]:


cast_data.value_counts().loc['TV Show'].head(10)


# >### <span style=" color: red; font-family:monospace;">CONCLUSION:
# >---
# >* ***We can see that in Top 10 TV Show cast, most people are from Japan.***
# 

# <hr noshade style="height:2px;">

# ## <p style="color:#ff6666; font-family:cursive;">Summary:</p>
# 
# - **Netflix added more Movie than TV Show.**
# - **After 2019 there is a drop in content added. Drop in Movie content is more than TV Show content.**
# - **If we not consider the content added in 2021 as we don't have data for all months then more content is added in October, November and December.**
# - **More content for adults is there on Netflix.**
# - **Most of the content is added on Friday and Thursday, respectively.**
# - **United states has added most content on Netflix.**
# - **Top 5 countries where netflix is adding more content per year except United States are India, United Kingdom, Canada, France and Japan.**
# - **Five most popular genres in recent years are International movies, Dramas, Comedies, International TV Shows and Action & Adventure.**

# ## <p style="color:#ff6666; font-family:cursive;">Movie:</p>
# 
# - **Almost same count of movies added on Netflix monthly.**
# - **In countries like India, Spain, Germany Movies are more popular than TV Shows.**
# - **Movies are of duration around 100 minutes.**
# - **Top 5 countries where movies added are United States, India, United Kingdom, Canada and France.**
# - **Top 3 genres in Movies are International Movies, Dramas and Comedies.**
# - **Top people casted in Movies are from India.**

# ## <p style="color:#ff6666; font-family:cursive;">TV Show:</p>
# 
# - **Large number of TV Show added on Friday than other weekday.**
# - **TV Shows have mostly season 1 and season 2 respectively.**
# - **In countries like United Kingdom, Japan, South Korea, Taiwan TV Shows are more popular than Movies.**
# - **Top 5 countries where movies added are United States, United Kingdom, Japan, South Korea and Canada.**
# - **Top 3 genres in Movies are International TV Shows, TV Dramas and TV Comedies.**
# - **Top people casted in TV Shows are from Japan.**

# ## <p style="color:#ff6666; font-family:cursive;">Recommendations:</p>
# 
# ### <i>Movie</i>
#  
#  - **Netflix should be focusing on adding more movies in emerging countries like India, United Kingdom, Canada and France for    Adult audience.**
#  -**Preferred Duration of movies will be from 80-120 minutes.**
#  - **International Movies, Dramas, Comedies should be the preferred genres for Movies.**
# 
# ### <i>TV Show</i>
#  
#  - **For TV Shows Netflix should focus on countries like Japan, South Korea, Canada and France.**
#  - **TV Show seasons can be up to 3 preferably.**
#  - **International TV Shows, TV Dramas, TV Comedies should be the preferred genres for TV Shows.**
