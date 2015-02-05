library(ggplot2)

df <- read.csv('pseudo_facebook.tsv', sep="\t")
ggplot(aes(x = age, y = friendships_initiated), data = subset(df, !is.na(gender))) + 
  geom_jitter(alpha=1/20, position = position_jitter(h=0)) + 
  xlim(13,113) + coord_trans(y = "sqrt")

library('dplyr')

filter()
group_by()
mutate()
arrange()

pf.age <- df %>% group_by(age) %>%
  summarise(friend_count_mean = mean(friend_count),
            friend_count_median = median(friend_count),
            n = n()) %>%
  arrange(age)
head(pf.age, 20)

ggplot(data = subset(df, !is.na(age)), aes(y=friend_count, x =age)) + 
  coord_cartesian(xlim = c(13,113), ylim=c(0,1200)) +
  geom_point(alpha=.05, position=position_jitter(h=0), color='orange') +
  geom_line(stat='summary', fun.y = mean) + 
  geom_line(stat='summary', fun.y = quantile, probs = .1, linetype = 2, color = 'blue') + 
  geom_line(stat='summary', fun.y = quantile, probs = .9, linetype = 2, color = 'blue') +
  geom_line(stat='summary', fun.y = quantile, probs = .5, color = 'blue')

with(subset(df, age < 90), cor.test(age, friend_count, method = 'pearson'))

ggplot(data=df, aes(y=likes_received, x= www_likes_received)) + 
  geom_jitter(alpha = 1/10, position = position_jitter(h=0), color = 'orange') +
  coord_cartesian(xlim = c(0, quantile(df$www_likes_received, .95)), ylim = c(0, quantile(df$likes_received, .95))) +
  geom_smooth(method = 'lm', color='red')
  
library(alr3)
data(Mitchell)

ggplot(data=Mitchell, aes(x=Month, y = Temp)) + geom_point() +
  scale_x_discrete(breaks = seq(0, 203, 12))

df$age_with_months <- (2014-df$dob_year) - (df$dob_month/12)

library(dplyr)

pf.fc_by_age_months <- df %>% group_by(age_with_months) %>%
  summarise(friend_count_mean = mean(friend_count),
            friend_count_median = median(friend_count),
            n = n()) %>%
  arrange(age_with_months)

ggplot(data=subset(pf.fc_by_age_months, age_with_months < 71), aes(y=friend_count_mean, x = age_with_months)) +
  geom_line() + geom_smooth()


%%=========================
  
df <- read.csv("pseudo_facebook.tsv", sep="\t")
library('dplyr')
pf.fc_by_age_gender <- subset(df, !is.na(gender)) %>% group_by(age, gender) %>%
  summarise(mean_friend_count = mean(friend_count),
            median_friend_count = median(as.numeric(friend_count)),
            n = n()) %>%
  arrange(age, gender)

ggplot(data=subset(pf.fc_by_age_gender, !is.na(gender)), aes(y=mean_friend_count, x = age, color = gender)) + geom_line()
  
  
library(reshape2)
pf <- dcast(pf.fc_by_age_gender, age ~ gender, value.var = 'median_friend_count')
library(ggplot2)
ggplot(data=pf, aes(x=age, y = female/male)) + geom_hline(alpha=0.7,yintercept = 1, linetype=2) + geom_point()


year_joined <- 2014 - ceiling(df$tenure/365)
df$year_joined <- year_joined
  
df$year_joined.bucket <- cut(df$year_joined, breaks = c(2004, 2009, 2011,2012, 2014))

ggplot(aes(x = age, y = friend_count), 
       data = subset(df, !is.na(gender))) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) +
  geom_line(aes(x = age, y = friend_count), stat= 'summary', fun.y=mean, linetype=2)

friend_rate <- with(subset(df, tenure >= 1), friend_count/tenure)

ggplot(data = subset(df, tenure >= 1), aes(y = friendships_initiated/tenure, x = tenure)) +
  geom_line(aes(color = year_joined.bucket), stat='summary', fun.y = mean) + geom_smooth(method = 'loess')

ggplot(data = subset(df, tenure >= 1), aes(y = friendships_initiated/tenure, x = tenure)) +
  geom_line(aes(color = year_joined.bucket), stat='summary', fun.y = mean) + geom_smooth(method = 'loess')

##-------------
##--------------

library(bayesm)
yo <- read.csv('yogurt.csv')
yo$id <- factor(yo$id)

library(ggplot2)
ggplot(data=yo, aes(x=price)) + geom_histogram(binwidth=10)
yo$all.purchases <- with(yo, strawberry + blueberry + pina.colada + plain + mixed.berry)
#price vs time

ggplot(data = yo, aes(y=price, x= time)) + geom_jitter(alpha=1/4, shape = 21, fill = I('#F79420'))


##Scatterplot matrix
library(GGally)
theme_set(theme_minimal(20))

set.seed(1432)
df <- read.csv('pseudo_facebook.tsv', sep='\t')
#df_subset <- df[,c(2:15)]
#ggpairs(df_subset[sample.int(nrow(df_subset), 1000), ])


df$prop_initiated <- with(df, ifelse(friend_count == 0, NA, friendships_initiated / friend_count))
year_joined <- 2014 - ceiling(df$tenure/365)
df$year_joined <- year_joined

df$year_joined.bucket <- cut(df$year_joined, breaks = c(2004, 2009, 2011,2012, 2014))

ggplot(data = subset(df, !is.na(prop_initiated) & tenure > 0), aes(y = prop_initiated, x = tenure)) +
  geom_line(aes(color = year_joined.bucket), stat='summary', fun.y=mean)
by(df$prop_initiated, df$year_joined.bucket, summary)


library(RColorBrewer)

ggplot(aes(x = carat, y = price), data = diamonds) + 
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  scale_color_brewer(type = 'div',
                     guide = guide_legend(title = 'Clarity', reverse = T,
                                          override.aes = list(alpha = 1, size = 2))) +  
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat and Clarity')


cuberoot_trans <- function() trans_new(
  'cuberoot', transform=function(x) x^(1/3),
  inverse=function(x) x^3)

ggplot(aes(x = carat, y = price, color = clarity), data = diamonds) + 
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  scale_color_brewer(type = 'div',
                     guide = guide_legend(title = 'Clarity', reverse = T,
                                          override.aes = list(alpha = 1, size = 2))) +  
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat and Clarity')