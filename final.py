import csv
from ggplot import *
import pandas as pd
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns

########################Import data ########################

#create a dataframe of movies and fill data from csv file
df = pd.read_csv('movie_metadata.csv')

##########################Remove Unneeded data #############
#Remove unneeded values 
df = df.drop(
	columns=['color', 'actor_3_name', 
	'actor_3_facebook_likes', 'facenumber_in_poster', 
	'plot_keywords', 'movie_imdb_link','aspect_ratio']
)

#get rows num before duplicate deletion
beforeDel = len(df)
df = df.drop_duplicates()
print str(beforeDel - len(df)) + " Duplicate records removed"

#Print values about remaining data 
rows = len(df)
cols = len(df.columns)
print str(len(df)) + " rows \t" + str(len(df.columns)) + " columns\n"

##########################Cleaning #########################

#print extensive view of missing values 
# print df.isnull().sum().to_string() + "\n"

# #percentage of movies left after all removals
# print 3761.0 / 4998.0 

#clean whitespace of movie titles 
df['movie_title'] = df['movie_title'].str.strip()

#fill missing duration value with the mean
df['duration'] = df['duration'].fillna(df['duration'].mean().round())

#fill mising countries with a space
df['country'] = df['country'].fillna('unknown') 

#Drop records with null values 
df = df[np.isfinite(df['gross'])]
df = df[np.isfinite(df['budget'])]

#Create new 
df= df.assign(profit = df.gross - df.budget)
df= df.assign(investmentReturn = (df.profit/df.budget)*100)

#remove movies before 1980 
df = df.drop(df[df.title_year < 1980].index)
df = df[np.isfinite(df['title_year'])]

# print "After dropping movies before 1980 " +\
#  str(len(df.title_year.index)) + " records remain"

##########################Visualization#####################

#Plots

################Year Histogram to show how the data is spread by year 


# yearHist = ggplot(df, aes(x="title_year")) +\
# ggtitle("Movie data by year") + xlab("Year") + ylab("Amount") +\
# geom_histogram(binwidth=.05)

# t = theme_gray()
# t._rcParams['font.size'] = 30

# print yearHist + t



#############Separate each genres into a dataframe 

# actionDf = df[df['genres'].str.contains("Action")]
# adventureDf = df[df['genres'].str.contains("Adventure")]
# animationDf = df[df['genres'].str.contains("Animation")]
# biographyDf = df[df['genres'].str.contains("Biography")]
# comedyDf = df[df['genres'].str.contains("Comedy")]
# crimeDf = df[df['genres'].str.contains("Crime")]
# documentaryDf = df[df['genres'].str.contains("Documentary")]
# dramaDf = df[df['genres'].str.contains("Drama")]
# familyDf = df[df['genres'].str.contains("Family")]
# fantasyDf = df[df['genres'].str.contains("Fantasy")]
# filmNoirDf = df[df['genres'].str.contains("Film-Noir")]
# historyDf = df[df['genres'].str.contains("History")]
# horrorDf = df[df['genres'].str.contains("Horror")]
# musicalDf = df[df['genres'].str.contains("Musical")]
# mysteryDf = df[df['genres'].str.contains("Mystery")]
# newsDf = df[df['genres'].str.contains("News")]
# romanceDf = df[df['genres'].str.contains("Romance")]
# sciFiDf = df[df['genres'].str.contains("Sci-Fi")]
# shortDf = df[df['genres'].str.contains("Short")]
# sportDf = df[df['genres'].str.contains("Sport")]
# thrillerDf = df[df['genres'].str.contains("Thriller")]
# warDf = df[df['genres'].str.contains("War")]
# westernDf = df[df['genres'].str.contains("Western")]

# genres = [
# ["Action", actionDf.imdb_score.mean().round(2)],
# ["Adventure", adventureDf.imdb_score.mean().round(2)],
# ["Animation", animationDf.imdb_score.mean().round(2)],
# ["Biography", biographyDf.imdb_score.mean().round(2)],
# ["Comedy", comedyDf.imdb_score.mean().round(2)],
# ["Crime", crimeDf.imdb_score.mean().round(2)],
# ["Documentary", documentaryDf.imdb_score.mean().round(2)],
# ["Drama", dramaDf.imdb_score.mean().round(2)],
# ["Family", familyDf.imdb_score.mean().round(2)],
# ["Fantasy", fantasyDf.imdb_score.mean().round(2)], 
# ["History", historyDf.imdb_score.mean().round(2)],
# ["Horror", horrorDf.imdb_score.mean().round(2)],
# ["Musical", musicalDf.imdb_score.mean().round(2)],
# ["Mystery", mysteryDf.imdb_score.mean().round(2)],
# ["Romance", romanceDf.imdb_score.mean().round(2)],
# ["Sci-Fi", sciFiDf.imdb_score.mean().round(2)],
# ["Short", shortDf.imdb_score.mean().round(2)],
# ["Sport", sportDf.imdb_score.mean().round(2)],
# ["Thriller", thrillerDf.imdb_score.mean().round(2)],
# ["War", warDf.imdb_score.mean().round(2)],
# ["Western", westernDf.imdb_score.mean().round(2)]]

# genresDfs = pd.DataFrame.from_records(genres, columns=['genres', 'imdb_score'])
# genresDfs = genresDfs.sort_values('imdb_score')
# genreScore = ggplot(genresDfs, aes(x="genres", weight="imdb_score")) +\
# ggtitle("Genre Average Rating") + xlab("Genres") + ylab("Rating") +\
# geom_bar()

# #increse font 
# t = theme_gray()
# t._rcParams['font.size'] = 14
# print genreScore + t


###############Create a scatter plot of highest grossing movies and imdb scores 

plt.rcParams.update({'font.size': 24})
# grossScatter = ggplot(df, aes(x='gross', y='imdb_score')) +\
# geom_point() +\
# ylab("IMDB Rating") +\
# xlab("Money Earned") +\
# ggtitle("Rating vs. Gross") +\
# xlim(0,1000000000)
# #increse font 
# t = theme_gray()
# t._rcParams['font.size'] = 30
# print grossScatter + t
# plt.show()
# grossScatter.save('grossScatter.png')



##################Get the top 20 directors by average gross

# df.groupby('director_name').gross.mean().nlargest(20).plot(kind='bar')
# plt.show()

##################Get the average imdbscore by director

# print df.groupby('content_rating').imdb_score.mean().plot(kind='bar')
# plt.show()


#################Correlation plot

# 
# corr = df.corr()
# corrPlot = sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
# sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
# plt.show()

#Manually save the plot


# ################Country Mean Plot 

# df.groupby('country').imdb_score.mean().nlargest(20).plot(kind='bar')
# plt.show()


################## Actor likes vs gross 

# likeGrossPlot = ggplot(df, aes('movie_facebook_likes', 'imdb_score')) +\
# ggtitle("Movies Likes vs. Rating") + xlab("Total Facebook Likes") + ylab("imdb rating") +\
# geom_point(color='steelblue')
# print likeGrossPlot

################# Profit vs IMDB score 
# profitPlot = ggplot(df, aes('profit', 'imdb_score')) +\
# ggtitle("Profit vs. Rating") + xlab("Money Earned") +\
# ylab("IMDB Rating") + xlim(-100000000, 750000000) +\
# geom_point(color = 'steelblue')
# print profitPlot

# print df.profit.max()