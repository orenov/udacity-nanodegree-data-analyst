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


