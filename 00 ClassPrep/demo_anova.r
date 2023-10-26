library(tidyverse)
data<-read_tsv('data/vik_table_12_2.csv')
model1<-lm(score~sex + condition,data=data)
model2<-lm(score~sex * condition,data=data)

