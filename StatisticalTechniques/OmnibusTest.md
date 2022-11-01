Omnibus Test
================
Last Updated: 31, October, 2022 at 12:46

-   <a href="#data" id="toc-data">Data</a>
-   <a href="#default-method" id="toc-default-method">Default method</a>
-   <a href="#run-the-simple-model-explicitly"
    id="toc-run-the-simple-model-explicitly">Run the simple model
    explicitly</a>

## Data

``` r
library(tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.2 ──
    ## ✔ ggplot2 3.3.6     ✔ purrr   0.3.4
    ## ✔ tibble  3.1.8     ✔ dplyr   1.0.9
    ## ✔ tidyr   1.2.0     ✔ stringr 1.4.0
    ## ✔ readr   2.1.2     ✔ forcats 0.5.2
    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()

``` r
body_data <- read_csv('data/body.csv')
```

    ## Rows: 507 Columns: 25
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## dbl (25): Biacromial, Biiliac, Bitrochanteric, ChestDepth, ChestDia, ElbowDi...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
colnames(body_data)
```

    ##  [1] "Biacromial"     "Biiliac"        "Bitrochanteric" "ChestDepth"    
    ##  [5] "ChestDia"       "ElbowDia"       "WristDia"       "KneeDia"       
    ##  [9] "AnkleDia"       "Shoulder"       "Chest"          "Waist"         
    ## [13] "Navel"          "Hip"            "Thigh"          "Bicep"         
    ## [17] "Forearm"        "Knee"           "Calf"           "Ankle"         
    ## [21] "Wrist"          "Age"            "Weight"         "Height"        
    ## [25] "Gender"

## Default method

``` r
result <- lm(Weight ~ Height + Age, data = body_data)
summary(result)
```

    ## 
    ## Call:
    ## lm(formula = Weight ~ Height + Age, data = body_data)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -19.996  -5.909  -1.321   5.055  41.285 
    ## 
    ## Coefficients:
    ##               Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept) -109.06383    7.38820  -14.76  < 2e-16 ***
    ## Height         1.00227    0.04297   23.33  < 2e-16 ***
    ## Age            0.22127    0.04207    5.26 2.14e-07 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 9.072 on 504 degrees of freedom
    ## Multiple R-squared:  0.5398, Adjusted R-squared:  0.538 
    ## F-statistic: 295.6 on 2 and 504 DF,  p-value: < 2.2e-16

## Run the simple model explicitly

``` r
mean_dependent <- mean(body_data$Weight)
body_data <- mutate(body_data, dummy = mean_dependent)
base_model <- lm(Weight ~ dummy, data = body_data)
full_model <- lm(Weight ~ Height + Age, data = body_data)
anova(base_model, full_model)
```

    ## Analysis of Variance Table
    ## 
    ## Model 1: Weight ~ dummy
    ## Model 2: Weight ~ Height + Age
    ##   Res.Df   RSS Df Sum of Sq      F    Pr(>F)    
    ## 1    506 90123                                  
    ## 2    504 41476  2     48647 295.57 < 2.2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
