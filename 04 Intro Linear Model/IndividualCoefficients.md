Individual Coefficients
================
Last Updated: 24, October, 2023 at 09:18

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

``` r
data<-read_csv('data/vik_table_9_2.csv')
```

    ## Rows: 12 Columns: 4
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## dbl (4): Person, Y, X1, X2
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
data$X1X2<- data$X1 * data$X2
```

Fit three models

``` r
model1<-lm(Y~X1 * X2, data = data)
model2<-lm(Y~X1 + X2, data = data)
model3<-lm(Y~X2 + X1X2, data = data)
```

Summary of model 1

``` r
summary(model1)
```

    ## 
    ## Call:
    ## lm(formula = Y ~ X1 * X2, data = data)
    ## 
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max 
    ## -2.22367 -0.36698  0.00612  0.60481  1.59638 
    ## 
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)  
    ## (Intercept) 11.14965    4.77082   2.337   0.0476 *
    ## X1          -0.95535    0.59067  -1.617   0.1445  
    ## X2          -0.19880    0.75427  -0.264   0.7988  
    ## X1:X2        0.04679    0.10802   0.433   0.6763  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 1.333 on 8 degrees of freedom
    ## Multiple R-squared:  0.8223, Adjusted R-squared:  0.7557 
    ## F-statistic: 12.34 on 3 and 8 DF,  p-value: 0.002271

Compare model 2 and 3 with model 1

``` r
anova(model1,model2)
```

    ## Analysis of Variance Table
    ## 
    ## Model 1: Y ~ X1 * X2
    ## Model 2: Y ~ X1 + X2
    ##   Res.Df    RSS Df Sum of Sq      F Pr(>F)
    ## 1      8 14.214                           
    ## 2      9 14.547 -1  -0.33343 0.1877 0.6763

``` r
anova(model1,model3)
```

    ## Analysis of Variance Table
    ## 
    ## Model 1: Y ~ X1 * X2
    ## Model 2: Y ~ X2 + X1X2
    ##   Res.Df    RSS Df Sum of Sq     F Pr(>F)
    ## 1      8 14.214                          
    ## 2      9 18.862 -1    -4.648 2.616 0.1445
