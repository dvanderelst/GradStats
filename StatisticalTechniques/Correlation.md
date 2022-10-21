Correlation
================
Last Updated: 21, October, 2022 at 08:58

-   <a href="#correlation" id="toc-correlation">Correlation</a>

## Correlation

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
data <- read_csv('data/body.csv')
```

    ## Rows: 507 Columns: 25
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## dbl (25): Biacromial, Biiliac, Bitrochanteric, ChestDepth, ChestDia, ElbowDi...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
cor.test(data$ChestDepth, data$ElbowDia)
```

    ## 
    ##  Pearson's product-moment correlation
    ## 
    ## data:  data$ChestDepth and data$ElbowDia
    ## t = 20.022, df = 505, p-value < 2.2e-16
    ## alternative hypothesis: true correlation is not equal to 0
    ## 95 percent confidence interval:
    ##  0.6137075 0.7111244
    ## sample estimates:
    ##       cor 
    ## 0.6652377

``` r
plot(data$ChestDepth, data$ElbowDia)
```

![](Correlation_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

``` r
data <- read_csv('data/vik_table_9_2.csv')
```

    ## Rows: 12 Columns: 4
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## dbl (4): Person, Y, X1, X2
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
result <- cor.test(data$X1, data$Y)
plot(data$X1, data$Y)
```

![](Correlation_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

``` r
result
```

    ## 
    ##  Pearson's product-moment correlation
    ## 
    ## data:  data$X1 and data$Y
    ## t = -6.4208, df = 10, p-value = 7.627e-05
    ## alternative hypothesis: true correlation is not equal to 0
    ## 95 percent confidence interval:
    ##  -0.9710564 -0.6661805
    ## sample estimates:
    ##        cor 
    ## -0.8971007

``` r
# Note that the confidence interval is not symmetric around the
# estimated correlation value

estimate <- result$estimate
lower <- result$conf.int[1]
upper <- result$conf.int[2]

values <- c(lower, estimate, upper)
delta1 <- estimate - lower
delta2 <- estimate - upper
deltas <- c(delta1, delta2)

values
```

    ##                   cor            
    ## -0.9710564 -0.8971007 -0.6661805

``` r
deltas
```

    ##         cor         cor 
    ##  0.07395562 -0.23092019

``` r
x <-runif(100)
y <-runif(100)
cor.test(x, y)
```

    ## 
    ##  Pearson's product-moment correlation
    ## 
    ## data:  x and y
    ## t = -0.092134, df = 98, p-value = 0.9268
    ## alternative hypothesis: true correlation is not equal to 0
    ## 95 percent confidence interval:
    ##  -0.2053493  0.1874542
    ## sample estimates:
    ##          cor 
    ## -0.009306574

``` r
plot(x, y)
```

![](Correlation_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

``` r
library(faux)
```

    ## 
    ## ************
    ## Welcome to faux. For support and examples visit:
    ## https://debruine.github.io/faux/
    ## - Get and set global package options with: faux_options()
    ## ************

    ## 
    ## Attaching package: 'faux'

    ## The following object is masked from 'package:purrr':
    ## 
    ##     %||%

``` r
data <- rnorm_multi(n= 10, vars = 2, r=0.80)
result <- cor.test(data$X1, data$X2)

result
```

    ## 
    ##  Pearson's product-moment correlation
    ## 
    ## data:  data$X1 and data$X2
    ## t = 4.544, df = 8, p-value = 0.001889
    ## alternative hypothesis: true correlation is not equal to 0
    ## 95 percent confidence interval:
    ##  0.4712267 0.9635468
    ## sample estimates:
    ##       cor 
    ## 0.8489672

``` r
# Note that the confidence interval is not symmetric around the
# estimated correlation value

estimate <- result$estimate
lower <- result$conf.int[1]
upper <- result$conf.int[2]

values <- c(lower, estimate, upper)
delta1 <- estimate - lower
delta2 <- estimate - upper
deltas <- c(delta1, delta2)

values
```

    ##                 cor           
    ## 0.4712267 0.8489672 0.9635468

``` r
deltas
```

    ##        cor        cor 
    ##  0.3777405 -0.1145796
