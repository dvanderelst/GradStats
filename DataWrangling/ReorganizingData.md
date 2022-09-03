Reorganizing Data
================
Dieter

-   <a href="#loading-the-tidyverse-and-some-data"
    id="toc-loading-the-tidyverse-and-some-data">Loading the tidyverse and
    some data</a>
-   <a href="#grouping-and-summarizing-data"
    id="toc-grouping-and-summarizing-data">Grouping and summarizing data</a>
-   <a href="#converting-to-wide-format"
    id="toc-converting-to-wide-format">Converting to wide format</a>
-   <a href="#further-processing" id="toc-further-processing">Further
    processing</a>
-   <a href="#note-on-dropping-non-existing-levels"
    id="toc-note-on-dropping-non-existing-levels">Note on dropping
    non-existing levels</a>
-   <a href="#making-data-longer-melting-data"
    id="toc-making-data-longer-melting-data">Making data longer (melting
    data)</a>

## Loading the tidyverse and some data

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
car_data <- read_delim('data/cars.txt', delim = ' ')
```

    ## Rows: 93 Columns: 26
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr  (6): make, model, type, cylinders, rearseat, luggage
    ## dbl (20): min_price, mid_price, max_price, mpg_city, mpg_hgw, airbag, drive,...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

## Grouping and summarizing data

The `group_by()` function takes a tibble and returns the same tibble,
but with some extra information so that any subsequent function acts on
each unique combination defined in the `group_by()`.

``` r
grouped <- group_by(car_data, type, make)
```

If you inspect the `grouped` tibble it seems the same as the `car_data`
tibble. However, it has stored the grouping we asked for.

``` r
groups(grouped)
```

    ## [[1]]
    ## type
    ## 
    ## [[2]]
    ## make

Now, you can use the `summarize()` function to get summary data for each
subgroup

``` r
summaries <- summarise(grouped, mean.length = mean(length))
```

    ## `summarise()` has grouped output by 'type'. You can override using the
    ## `.groups` argument.

``` r
summaries
```

    ## # A tibble: 81 × 3
    ## # Groups:   type [6]
    ##    type    make          mean.length
    ##    <chr>   <chr>               <dbl>
    ##  1 Compact Audi                  180
    ##  2 Compact Chevrolet             183
    ##  3 Compact Chrysler              183
    ##  4 Compact Dodge                 181
    ##  5 Compact Ford                  177
    ##  6 Compact Honda                 185
    ##  7 Compact Mazda                 184
    ##  8 Compact Mercedes-Benz         175
    ##  9 Compact Nissan                181
    ## 10 Compact Oldsmobile            188
    ## # … with 71 more rows
    ## # ℹ Use `print(n = ...)` to see more rows

You can ask for more than one summary statistic.

``` r
summaries <- summarise(grouped, mean.length = mean(length), max.length = max(length), std_rpm = sd(rpm))
```

    ## `summarise()` has grouped output by 'type'. You can override using the
    ## `.groups` argument.

``` r
summaries
```

    ## # A tibble: 81 × 5
    ## # Groups:   type [6]
    ##    type    make          mean.length max.length std_rpm
    ##    <chr>   <chr>               <dbl>      <dbl>   <dbl>
    ##  1 Compact Audi                  180        180      NA
    ##  2 Compact Chevrolet             183        184       0
    ##  3 Compact Chrysler              183        183      NA
    ##  4 Compact Dodge                 181        181      NA
    ##  5 Compact Ford                  177        177      NA
    ##  6 Compact Honda                 185        185      NA
    ##  7 Compact Mazda                 184        184      NA
    ##  8 Compact Mercedes-Benz         175        175      NA
    ##  9 Compact Nissan                181        181      NA
    ## 10 Compact Oldsmobile            188        188      NA
    ## # … with 71 more rows
    ## # ℹ Use `print(n = ...)` to see more rows

## Converting to wide format

The result can be reshaped into a wide format. While this format is
often not suited for plotting or analysis, it might make it easier to
look at the data.

``` r
wide <- pivot_wider(summaries, id_cols = make, names_from  = type, values_from = mean.length)
head(wide)
```

    ## # A tibble: 6 × 7
    ##   make      Compact Large Midsize Small Sporty   Van
    ##   <chr>       <dbl> <dbl>   <dbl> <dbl>  <dbl> <dbl>
    ## 1 Audi          180    NA     193    NA    NA     NA
    ## 2 Chevrolet     183   214     198    NA   186    186
    ## 3 Chrysler      183   203      NA    NA    NA     NA
    ## 4 Dodge         181    NA     192   173   180    175
    ## 5 Ford          177   212     192   156   180.   176
    ## 6 Honda         185    NA      NA   173   175     NA

## Further processing

Keep in mind that, as the result of `summarize()` is a tibble, you can
use the data selection methods we saw earlier.

``` r
subset <- filter(summaries, make ==  'Ford')
head(subset)
```

    ## # A tibble: 6 × 5
    ## # Groups:   type [6]
    ##   type    make  mean.length max.length std_rpm
    ##   <chr>   <chr>       <dbl>      <dbl>   <dbl>
    ## 1 Compact Ford         177         177     NA 
    ## 2 Large   Ford         212         212     NA 
    ## 3 Midsize Ford         192         192     NA 
    ## 4 Small   Ford         156         171   1061.
    ## 5 Sporty  Ford         180.        180    636.
    ## 6 Van     Ford         176         176     NA

## Note on dropping non-existing levels

By default, the `group_by()` function drops non-existing combinations of
grouping variables.

``` r
grouped1 <- group_by(car_data, type, make)
c1<-count(grouped1)
summaries1 <- summarise(grouped, mean.length = mean(length))
```

    ## `summarise()` has grouped output by 'type'. You can override using the
    ## `.groups` argument.

``` r
dim(summaries1)
```

    ## [1] 81  3

However, this behavior can be changed using the `.drop = FALSE` argument
(and converting the variables to factors)

``` r
grouped2 <- group_by(car_data, as.factor(type), as.factor(make), .drop=FALSE)
c2<-count(grouped2)
summaries2 <- summarise(grouped2, mean.length = mean(length))
```

    ## `summarise()` has grouped output by 'as.factor(type)'. You can override using
    ## the `.groups` argument.

``` r
summaries2 <- complete(summaries2)
dim(summaries2)
```

    ## [1] 192   3

## Making data longer (melting data)

Here is a quick graphic:

![](images/pivot_longer_new.png)

Let’s look at some data:

``` r
head(relig_income, 5)
```

    ## # A tibble: 5 × 11
    ##   religion       `<$10k` $10-2…¹ $20-3…² $30-4…³ $40-5…⁴ $50-7…⁵ $75-1…⁶ $100-…⁷
    ##   <chr>            <dbl>   <dbl>   <dbl>   <dbl>   <dbl>   <dbl>   <dbl>   <dbl>
    ## 1 Agnostic            27      34      60      81      76     137     122     109
    ## 2 Atheist             12      27      37      52      35      70      73      59
    ## 3 Buddhist            27      21      30      34      33      58      62      39
    ## 4 Catholic           418     617     732     670     638    1116     949     792
    ## 5 Don’t know/re…      15      14      15      11      10      35      21      17
    ## # … with 2 more variables: `>150k` <dbl>, `Don't know/refused` <dbl>, and
    ## #   abbreviated variable names ¹​`$10-20k`, ²​`$20-30k`, ³​`$30-40k`, ⁴​`$40-50k`,
    ## #   ⁵​`$50-75k`, ⁶​`$75-100k`, ⁷​`$100-150k`
    ## # ℹ Use `colnames()` to see all variable names

This data is in a wider format. But we can easily melt it to a long
format.

``` r
new <- pivot_longer(relig_income, cols = !religion)
head(new, 5)
```

    ## # A tibble: 5 × 3
    ##   religion name    value
    ##   <chr>    <chr>   <dbl>
    ## 1 Agnostic <$10k      27
    ## 2 Agnostic $10-20k    34
    ## 3 Agnostic $20-30k    60
    ## 4 Agnostic $30-40k    81
    ## 5 Agnostic $40-50k    76

You can specify names for the new columns while melting.

``` r
new <- pivot_longer(relig_income, !religion, names_to = "income", values_to = "count")
head(new, 5)
```

    ## # A tibble: 5 × 3
    ##   religion income  count
    ##   <chr>    <chr>   <dbl>
    ## 1 Agnostic <$10k      27
    ## 2 Agnostic $10-20k    34
    ## 3 Agnostic $20-30k    60
    ## 4 Agnostic $30-40k    81
    ## 5 Agnostic $40-50k    76
