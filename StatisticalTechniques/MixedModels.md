Mixed Models
================
Last Updated: 17, November, 2022 at 09:59

- <a href="#100-populations-of-penguins"
  id="toc-100-populations-of-penguins">100 populations of penguins</a>
  - <a href="#make-data" id="toc-make-data">Make data</a>
  - <a href="#fit-a-mixed-model" id="toc-fit-a-mixed-model">Fit a mixed
    model</a>
    - <a href="#fitting-the-model-using-the-lme-function"
      id="toc-fitting-the-model-using-the-lme-function">fitting the model
      using the lme function</a>
    - <a href="#intepreting-the-fitted-parameters"
      id="toc-intepreting-the-fitted-parameters">Intepreting the fitted
      parameters</a>
    - <a href="#fitting-the-model-using-the-lmer-function"
      id="toc-fitting-the-model-using-the-lmer-function">fitting the model
      using the lmer function</a>
- <a href="#pre-and-post-penguins" id="toc-pre-and-post-penguins">Pre and
  Post Penguins</a>
  - <a href="#make-data-1" id="toc-make-data-1">Make data</a>
  - <a href="#fit-model" id="toc-fit-model">Fit model</a>
  - <a href="#intepreting-the-model"
    id="toc-intepreting-the-model">Intepreting the model</a>
- <a href="#three-measures" id="toc-three-measures">Three measures</a>
- <a href="#interaction-effects" id="toc-interaction-effects">Interaction
  effects</a>
- <a href="#real-data-cars" id="toc-real-data-cars">Real data (cars)</a>
- <a href="#vik-2013-chapter-18-repeated-measures-anova"
  id="toc-vik-2013-chapter-18-repeated-measures-anova">Vik 2013, Chapter
  18 (Repeated measures ANOVA)</a>

``` r
library(tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.2 ──
    ## ✔ ggplot2 3.4.0      ✔ purrr   0.3.5 
    ## ✔ tibble  3.1.8      ✔ dplyr   1.0.10
    ## ✔ tidyr   1.2.1      ✔ stringr 1.4.1 
    ## ✔ readr   2.1.3      ✔ forcats 0.5.2 
    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()

## 100 populations of penguins

### Make data

``` r
sample_size <- 15
populations <- 100
variance_random_effect <- 0.25
fixed_effect <- 2.5

random_factor <- rnorm(populations, 0, sd=sqrt(variance_random_effect))


all_heights <-c()
all_weights <-c()
all_ids <-c()

for (i in 1:populations){
  heights <- rnorm(sample_size)
  errors <- rnorm(sample_size, sd=0.25)
  weights <- fixed_effect * heights + random_factor[i] + errors
  population_ids <- rep(i, times = sample_size)
  
  all_heights <- c(all_heights, heights)
  all_weights <- c(all_weights, weights)
  all_ids <- c(all_ids, population_ids)
}
 
penguin_data <- data.frame(all_ids, all_heights, all_weights)
colnames(penguin_data) <-c('id', 'height', 'weight')
head(penguin_data)
```

    ##   id      height      weight
    ## 1  1 -0.10012413 -0.19323234
    ## 2  1  1.11436759  3.18184570
    ## 3  1 -0.02026763 -0.04624253
    ## 4  1  0.93506020  2.77159108
    ## 5  1 -0.34994844 -0.42789869
    ## 6  1  1.42221733  3.59519078

### Fit a mixed model

``` r
v <- var(random_factor)
s <- sd(random_factor)
c(v, s)
```

    ## [1] 0.2656643 0.5154263

#### fitting the model using the lme function

The 1 indicates that an intercept is to be fitted for each level of the
random variable.

``` r
library(nlme)
```

    ## 
    ## Attaching package: 'nlme'

    ## The following object is masked from 'package:dplyr':
    ## 
    ##     collapse

``` r
model <- lme(weight ~ height, random=~1|id, data = penguin_data)
summary(model)
```

    ## Linear mixed-effects model fit by REML
    ##   Data: penguin_data 
    ##        AIC      BIC    logLik
    ##   481.6336 502.8811 -236.8168
    ## 
    ## Random effects:
    ##  Formula: ~1 | id
    ##         (Intercept) Residual
    ## StdDev:   0.5111989 0.245575
    ## 
    ## Fixed effects:  weight ~ height 
    ##                  Value  Std.Error   DF  t-value p-value
    ## (Intercept) -0.0897812 0.05151168 1399  -1.7429  0.0816
    ## height       2.5027627 0.00654667 1399 382.2953  0.0000
    ##  Correlation: 
    ##        (Intr)
    ## height 0.001 
    ## 
    ## Standardized Within-Group Residuals:
    ##         Min          Q1         Med          Q3         Max 
    ## -3.32653884 -0.67787379  0.02287255  0.68377169  3.18997266 
    ## 
    ## Number of Observations: 1500
    ## Number of Groups: 100

#### Intepreting the fitted parameters

A different intercept is fitted for each population.

``` r
coefs <-coefficients(model)
coefs$population <- seq(1, populations)
head(coefs, 15)
```

    ##      (Intercept)   height population
    ## 1   2.020947e-01 2.502763          1
    ## 2   5.748409e-05 2.502763          2
    ## 3  -8.927043e-01 2.502763          3
    ## 4   8.671594e-02 2.502763          4
    ## 5   2.828190e-01 2.502763          5
    ## 6  -4.016108e-01 2.502763          6
    ## 7   9.538646e-01 2.502763          7
    ## 8  -2.281433e-01 2.502763          8
    ## 9   5.754823e-01 2.502763          9
    ## 10  1.301575e-01 2.502763         10
    ## 11 -1.585606e-01 2.502763         11
    ## 12  3.699804e-01 2.502763         12
    ## 13 -4.642570e-01 2.502763         13
    ## 14  8.162645e-01 2.502763         14
    ## 15 -2.594248e-01 2.502763         15

``` r
head(penguin_data)
```

    ##   id      height      weight
    ## 1  1 -0.10012413 -0.19323234
    ## 2  1  1.11436759  3.18184570
    ## 3  1 -0.02026763 -0.04624253
    ## 4  1  0.93506020  2.77159108
    ## 5  1 -0.34994844 -0.42789869
    ## 6  1  1.42221733  3.59519078

``` r
population1<-filter(penguin_data, id==1)
population2<-filter(penguin_data, id==2)
population3<-filter(penguin_data, id==3)

prediction1 <- coefs$`(Intercept)`[1] + coefs$height[1] * population1$height
prediction2 <- coefs$`(Intercept)`[2] + coefs$height[2] * population2$height
prediction3 <- coefs$`(Intercept)`[3] + coefs$height[3] * population3$height

plot(population1$height, population1$weight, col='red')
points(population1$height, prediction1, type='l', col='red')

points(population2$height, population2$weight, col='green')
points(population2$height, prediction2, type='l', col='green')

points(population3$height, population3$weight, col='blue')
points(population3$height, prediction3, type='l', col='blue')
```

![](MixedModels_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

#### fitting the model using the lmer function

``` r
library(lme4)
```

    ## Loading required package: Matrix

    ## 
    ## Attaching package: 'Matrix'

    ## The following objects are masked from 'package:tidyr':
    ## 
    ##     expand, pack, unpack

    ## 
    ## Attaching package: 'lme4'

    ## The following object is masked from 'package:nlme':
    ## 
    ##     lmList

``` r
model <- lmer(weight ~ height + (1|id), data = penguin_data)
summary(model)
```

    ## Linear mixed model fit by REML ['lmerMod']
    ## Formula: weight ~ height + (1 | id)
    ##    Data: penguin_data
    ## 
    ## REML criterion at convergence: 473.6
    ## 
    ## Scaled residuals: 
    ##     Min      1Q  Median      3Q     Max 
    ## -3.3265 -0.6779  0.0229  0.6838  3.1900 
    ## 
    ## Random effects:
    ##  Groups   Name        Variance Std.Dev.
    ##  id       (Intercept) 0.26132  0.5112  
    ##  Residual             0.06031  0.2456  
    ## Number of obs: 1500, groups:  id, 100
    ## 
    ## Fixed effects:
    ##              Estimate Std. Error t value
    ## (Intercept) -0.089781   0.051512  -1.743
    ## height       2.502763   0.006547 382.295
    ## 
    ## Correlation of Fixed Effects:
    ##        (Intr)
    ## height 0.001

``` r
library(lmerTest)
```

    ## 
    ## Attaching package: 'lmerTest'

    ## The following object is masked from 'package:lme4':
    ## 
    ##     lmer

    ## The following object is masked from 'package:stats':
    ## 
    ##     step

``` r
#  To get (estimated) degrees of freedom and the p -values associated with the t -statistics and those degrees of freedom
model <- lmer(weight ~ height + (1|id), data = penguin_data)
summary(model)
```

    ## Linear mixed model fit by REML. t-tests use Satterthwaite's method [
    ## lmerModLmerTest]
    ## Formula: weight ~ height + (1 | id)
    ##    Data: penguin_data
    ## 
    ## REML criterion at convergence: 473.6
    ## 
    ## Scaled residuals: 
    ##     Min      1Q  Median      3Q     Max 
    ## -3.3265 -0.6779  0.0229  0.6838  3.1900 
    ## 
    ## Random effects:
    ##  Groups   Name        Variance Std.Dev.
    ##  id       (Intercept) 0.26132  0.5112  
    ##  Residual             0.06031  0.2456  
    ## Number of obs: 1500, groups:  id, 100
    ## 
    ## Fixed effects:
    ##               Estimate Std. Error         df t value Pr(>|t|)    
    ## (Intercept) -8.978e-02  5.151e-02  9.900e+01  -1.743   0.0845 .  
    ## height       2.503e+00  6.547e-03  1.402e+03 382.295   <2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Correlation of Fixed Effects:
    ##        (Intr)
    ## height 0.001

## Pre and Post Penguins

### Make data

``` r
sample_size <- 100
variance_random_effect <- 0.25
fixed_effect <- 0.5

random_factor <- rnorm(populations, 0, sd=sqrt(variance_random_effect))
noise <- rnorm(populations, 0, sd=0.1)


ids <- seq(sample_size)

pre_data <- rnorm(sample_size, mean = 10) + random_factor + noise
post_data <- rnorm(sample_size, mean = 10 + fixed_effect) + random_factor + noise


id <- c(ids, ids)
measurement<-c(rep(1, sample_size), rep(2, sample_size))
weight <-c(pre_data, post_data)

repeated_data <- data.frame(id, measurement, weight)
repeated_data$measurement <- as.factor(repeated_data$measurement)
head(repeated_data)
```

    ##   id measurement    weight
    ## 1  1           1 11.294076
    ## 2  2           1  8.758258
    ## 3  3           1 12.000155
    ## 4  4           1 11.676928
    ## 5  5           1  8.947033
    ## 6  6           1  9.899686

``` r
v <- var(random_factor)
s <- sd(random_factor)
c(v, s)
```

    ## [1] 0.2615894 0.5114581

### Fit model

``` r
library(lme4)
model <- lmer(weight ~ measurement + (1|id), data = repeated_data)
summary(model)
```

    ## Linear mixed model fit by REML. t-tests use Satterthwaite's method [
    ## lmerModLmerTest]
    ## Formula: weight ~ measurement + (1 | id)
    ##    Data: repeated_data
    ## 
    ## REML criterion at convergence: 593.5
    ## 
    ## Scaled residuals: 
    ##      Min       1Q   Median       3Q      Max 
    ## -2.62535 -0.49144 -0.02642  0.52810  2.23754 
    ## 
    ## Random effects:
    ##  Groups   Name        Variance Std.Dev.
    ##  id       (Intercept) 0.4212   0.6490  
    ##  Residual             0.7750   0.8804  
    ## Number of obs: 200, groups:  id, 100
    ## 
    ## Fixed effects:
    ##              Estimate Std. Error       df t value Pr(>|t|)    
    ## (Intercept)    9.9913     0.1094 176.1601  91.351  < 2e-16 ***
    ## measurement2   0.5102     0.1245  99.0000   4.098 8.53e-05 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Correlation of Fixed Effects:
    ##             (Intr)
    ## measuremnt2 -0.569

### Intepreting the model

``` r
predictions <-unname(predict(model))
before <- predictions[1: sample_size]
after <- predictions[101:length(predictions)]

c1 <- rgb(173,216,230,max = 255, alpha = 80, names = "lt.blue")
c2 <- rgb(255,192,203, max = 255, alpha = 80, names = "lt.pink")

hist(before, col=c1, xlim=range(predictions))
hist(after, add=TRUE, col=c2)
```

![](MixedModels_files/figure-gfm/unnamed-chunk-12-1.png)<!-- -->

``` r
plot(before, after)
```

![](MixedModels_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->

## Three measures

``` r
sample_size <- 100
variance_random_effect <- 0.25

time_effect1 <- 0.75
time_effect2 <- 1

random_factor <- rnorm(populations, 0, sd=sqrt(variance_random_effect))
ids <- seq(sample_size)

data1 <- rnorm(sample_size, mean = 10) + 0.0000000000 + random_factor
data2 <- rnorm(sample_size, mean = 10) + time_effect1 + random_factor
data3 <- rnorm(sample_size, mean = 10) + time_effect2 + random_factor

id <- c(ids, ids, ids)
measurement<-c(rep(1, sample_size), rep(2, sample_size), rep(3, sample_size))
weight <-c(data1, data2, data3)

three_repeats_data <- data.frame(id, measurement,  weight)
three_repeats_data$measurement <- as.factor(three_repeats_data$measurement)
head(three_repeats_data)
```

    ##   id measurement    weight
    ## 1  1           1  9.506154
    ## 2  2           1 10.016583
    ## 3  3           1  9.884038
    ## 4  4           1 11.050629
    ## 5  5           1  9.403579
    ## 6  6           1  8.682226

``` r
v <- var(random_factor)
s <- sd(random_factor)
c(v, s)
```

    ## [1] 0.2847779 0.5336458

``` r
library(lme4)
model <- lmer(weight ~ measurement + (1|id), data = three_repeats_data)
summary(model)
```

    ## Linear mixed model fit by REML. t-tests use Satterthwaite's method [
    ## lmerModLmerTest]
    ## Formula: weight ~ measurement + (1 | id)
    ##    Data: three_repeats_data
    ## 
    ## REML criterion at convergence: 888.1
    ## 
    ## Scaled residuals: 
    ##      Min       1Q   Median       3Q      Max 
    ## -2.77559 -0.57353 -0.03916  0.58887  2.79382 
    ## 
    ## Random effects:
    ##  Groups   Name        Variance Std.Dev.
    ##  id       (Intercept) 0.2668   0.5165  
    ##  Residual             0.8990   0.9481  
    ## Number of obs: 300, groups:  id, 100
    ## 
    ## Fixed effects:
    ##              Estimate Std. Error       df t value Pr(>|t|)    
    ## (Intercept)   10.1413     0.1080 268.8384  93.927  < 2e-16 ***
    ## measurement2   0.5267     0.1341 198.0000   3.928 0.000118 ***
    ## measurement3   0.8592     0.1341 198.0000   6.408 1.05e-09 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Correlation of Fixed Effects:
    ##             (Intr) msrmn2
    ## measuremnt2 -0.621       
    ## measuremnt3 -0.621  0.500

## Interaction effects

``` r
sample_size <- 100
variance_random_effect <- 0.25

random_factor <- rnorm(populations, 0, sd=sqrt(variance_random_effect))
sex <- c(rep(0, sample_size/2), rep(1, sample_size/2))
ids <- seq(sample_size)

data1 <- rnorm(sample_size, mean = 10) + 0 + sex * 0 + random_factor
data2 <- rnorm(sample_size, mean = 10) + 1 + sex * 2 + random_factor
data3 <- rnorm(sample_size, mean = 10) + 2 + sex * 4 + random_factor

id <- c(ids, ids, ids)
sex <-c(sex, sex, sex) # used when demoing interaction effects
measurement<-c(rep(0, sample_size), rep(1, sample_size), rep(2, sample_size))
weight <-c(data1, data2, data3)

interaction_data <- data.frame(id, measurement, sex,  weight)
interaction_data$measurement <- as.factor(interaction_data$measurement)
interaction_data$sex <- as.factor(interaction_data$sex)
head(interaction_data)
```

    ##   id measurement sex    weight
    ## 1  1           0   0  7.922162
    ## 2  2           0   0 10.455501
    ## 3  3           0   0 10.320741
    ## 4  4           0   0  8.564842
    ## 5  5           0   0  9.316711
    ## 6  6           0   0  9.056548

``` r
library(lme4)
model <- lmer(weight ~ measurement * sex + (1|id), data = interaction_data)
summary(model)
```

    ## Linear mixed model fit by REML. t-tests use Satterthwaite's method [
    ## lmerModLmerTest]
    ## Formula: weight ~ measurement * sex + (1 | id)
    ##    Data: interaction_data
    ## 
    ## REML criterion at convergence: 905.7
    ## 
    ## Scaled residuals: 
    ##      Min       1Q   Median       3Q      Max 
    ## -2.77501 -0.53857 -0.02449  0.60797  2.65723 
    ## 
    ## Random effects:
    ##  Groups   Name        Variance Std.Dev.
    ##  id       (Intercept) 0.1275   0.3571  
    ##  Residual             1.0624   1.0307  
    ## Number of obs: 300, groups:  id, 100
    ## 
    ## Fixed effects:
    ##                   Estimate Std. Error       df t value Pr(>|t|)    
    ## (Intercept)         9.8648     0.1543 287.3986  63.947  < 2e-16 ***
    ## measurement1        1.0960     0.2061 196.0000   5.317 2.87e-07 ***
    ## measurement2        2.2280     0.2061 196.0000  10.808  < 2e-16 ***
    ## sex1                0.3247     0.2182 287.3986   1.488    0.138    
    ## measurement1:sex1   1.7096     0.2915 196.0000   5.864 1.89e-08 ***
    ## measurement2:sex1   3.3767     0.2915 196.0000  11.583  < 2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Correlation of Fixed Effects:
    ##             (Intr) msrmn1 msrmn2 sex1   msr1:1
    ## measuremnt1 -0.668                            
    ## measuremnt2 -0.668  0.500                     
    ## sex1        -0.707  0.472  0.472              
    ## msrmnt1:sx1  0.472 -0.707 -0.354 -0.668       
    ## msrmnt2:sx1  0.472 -0.354 -0.707 -0.668  0.500

``` r
boxplot(interaction_data$weight ~ interaction_data$measurement * interaction_data$sex)
```

![](MixedModels_files/figure-gfm/unnamed-chunk-19-1.png)<!-- -->

## Real data (cars)

``` r
library(tidyverse)
library(readxl)
car_data <-read_xls('data/kuiper.xls')
colnames(car_data)
```

    ##  [1] "Price"    "Mileage"  "Make"     "Model"    "Trim"     "Type"    
    ##  [7] "Cylinder" "Liter"    "Doors"    "Cruise"   "Sound"    "Leather"

``` r
car_data$Price <-scale(car_data$Price)
car_data$Mileage <-scale(car_data$Mileage)
car_model <- lmer(Price ~ Mileage + (1|Make), data = car_data)
summary(car_model)
```

    ## Linear mixed model fit by REML. t-tests use Satterthwaite's method [
    ## lmerModLmerTest]
    ## Formula: Price ~ Mileage + (1 | Make)
    ##    Data: car_data
    ## 
    ## REML criterion at convergence: 1448.2
    ## 
    ## Scaled residuals: 
    ##     Min      1Q  Median      3Q     Max 
    ## -2.0336 -0.5711 -0.1192  0.2638  4.9021 
    ## 
    ## Random effects:
    ##  Groups   Name        Variance Std.Dev.
    ##  Make     (Intercept) 1.0387   1.0191  
    ##  Residual             0.3379   0.5813  
    ## Number of obs: 804, groups:  Make, 6
    ## 
    ## Fixed effects:
    ##              Estimate Std. Error        df t value Pr(>|t|)    
    ## (Intercept)   0.20404    0.41674   4.99449   0.490    0.645    
    ## Mileage      -0.14175    0.02057 797.02317  -6.891 1.13e-11 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Correlation of Fixed Effects:
    ##         (Intr)
    ## Mileage -0.001

## Vik 2013, Chapter 18 (Repeated measures ANOVA)

In this chapter, the author performs a repeated measures ANOVA using an
idiosyncratic calculation method. Here, I run the same analysis using
the rstatix and car packages to show that the numbers correspond to what
he calculates.

![](images/2022-11-16_22-23.png)

Vik, P. (2013). Regression, ANOVA, and the General Linear Model. SAGE
Publications, Inc. (US).
<https://bookshelf.vitalsource.com/books/9781483316017>

``` r
vik_data <- read_xls('data/vik_repeated.xls')
vik_data <- pivot_longer(vik_data, cols = c('time1', 'time2'))
head(vik_data)
```

    ## # A tibble: 6 × 3
    ##      id name  value
    ##   <dbl> <chr> <dbl>
    ## 1     1 time1     3
    ## 2     1 time2     5
    ## 3     2 time1     5
    ## 4     2 time2     4
    ## 5     3 time1     6
    ## 6     3 time2     4

``` r
library(rstatix)
```

    ## 
    ## Attaching package: 'rstatix'

    ## The following object is masked from 'package:stats':
    ## 
    ##     filter

``` r
res.aov <- anova_test(data = vik_data, dv = value, wid = id, within = name)
get_anova_table(res.aov)
```

    ## ANOVA Table (type III tests)
    ## 
    ##   Effect DFn DFd      F     p p<.05   ges
    ## 1   name   1  23 10.991 0.003     * 0.056

Here, the same thing using a different package that also spits out the
sums of squares.

``` r
library(car)
```

    ## Loading required package: carData

    ## 
    ## Attaching package: 'car'

    ## The following object is masked from 'package:dplyr':
    ## 
    ##     recode

    ## The following object is masked from 'package:purrr':
    ## 
    ##     some

``` r
design <- factorial_design(vik_data, dv = value, wid = id, within = name)
res.anova <- Anova(design$model, idata = design$idata, idesign = design$idesign, type = 3)
summary(res.anova)
```

    ## 
    ## Type III Repeated Measures MANOVA Tests:
    ## 
    ## ------------------------------------------
    ##  
    ## Term: (Intercept) 
    ## 
    ##  Response transformation matrix:
    ##       (Intercept)
    ## time1           1
    ## time2           1
    ## 
    ## Sum of squares and products for the hypothesis:
    ##             (Intercept)
    ## (Intercept)       12696
    ## 
    ## Multivariate Tests: (Intercept)
    ##                  Df test stat approx F num Df den Df     Pr(>F)    
    ## Pillai            1  0.798893 91.36671      1     23 1.7793e-09 ***
    ## Wilks             1  0.201107 91.36671      1     23 1.7793e-09 ***
    ## Hotelling-Lawley  1  3.972466 91.36671      1     23 1.7793e-09 ***
    ## Roy               1  3.972466 91.36671      1     23 1.7793e-09 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## ------------------------------------------
    ##  
    ## Term: name 
    ## 
    ##  Response transformation matrix:
    ##       name1
    ## time1     1
    ## time2    -1
    ## 
    ## Sum of squares and products for the hypothesis:
    ##       name1
    ## name1   216
    ## 
    ## Multivariate Tests: name
    ##                  Df test stat approx F num Df den Df   Pr(>F)   
    ## Pillai            1 0.3233533 10.99115      1     23 0.003017 **
    ## Wilks             1 0.6766467 10.99115      1     23 0.003017 **
    ## Hotelling-Lawley  1 0.4778761 10.99115      1     23 0.003017 **
    ## Roy               1 0.4778761 10.99115      1     23 0.003017 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Univariate Type III Repeated-Measures ANOVA Assuming Sphericity
    ## 
    ##             Sum Sq num Df Error SS den Df F value    Pr(>F)    
    ## (Intercept)   6348      1     1598     23  91.367 1.779e-09 ***
    ## name           108      1      226     23  10.991  0.003017 ** 
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
