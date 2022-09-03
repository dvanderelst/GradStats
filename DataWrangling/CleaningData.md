Cleaning Data
================
Dieter

-   <a href="#loading-the-tidyverse" id="toc-loading-the-tidyverse">Loading
    the tidyverse</a>
-   <a href="#some-simple-operations" id="toc-some-simple-operations">Some
    simple operations</a>
    -   <a href="#opening-large-text-files"
        id="toc-opening-large-text-files">Opening large text files</a>
    -   <a href="#detecting-outliers" id="toc-detecting-outliers">Detecting
        outliers</a>
    -   <a href="#missing-data" id="toc-missing-data">Missing data</a>
    -   <a href="#seperating-a-column" id="toc-seperating-a-column">Seperating a
        column</a>
    -   <a href="#combining-columns" id="toc-combining-columns">Combining
        columns</a>
    -   <a href="#strings-using-stringr" id="toc-strings-using-stringr">Strings
        using <code>stringr</code></a>
-   <a href="#example-social-security-applications"
    id="toc-example-social-security-applications">Example: Social Security
    Applications</a>
    -   <a href="#a-reminder-on-pivot_longer"
        id="toc-a-reminder-on-pivot_longer">A reminder on
        <code>pivot_longer()</code></a>
    -   <a href="#using-pivot_longer" id="toc-using-pivot_longer">Using
        <code>pivot_longer()</code></a>
    -   <a href="#using-separate" id="toc-using-separate">Using
        <code>separate()</code></a>
    -   <a href="#creating-an-other-column"
        id="toc-creating-an-other-column">Creating an <code>Other</code>
        column</a>
    -   <a href="#convert-fiscal_year-to-year"
        id="toc-convert-fiscal_year-to-year">Convert <code>Fiscal_Year</code> to
        year</a>
    -   <a href="#create-a-date-variable" id="toc-create-a-date-variable">Create
        a date variable</a>
    -   <a href="#plots" id="toc-plots">Plots</a>
-   <a href="#example-coal-data" id="toc-example-coal-data">Example: Coal
    data</a>
    -   <a href="#change-the-first-variable-name"
        id="toc-change-the-first-variable-name">Change the first variable
        name</a>
    -   <a href="#convert-to-a-long-data-format"
        id="toc-convert-to-a-long-data-format">Convert to a long data format</a>
    -   <a href="#separate-regions-and-countries"
        id="toc-separate-regions-and-countries">Separate regions and
        countries</a>

## Loading the tidyverse

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

## Some simple operations

### Opening large text files

One of the most simple things you can do is inspect your data using a
text editor. When text files are large, it’s a good idea to get an
editor that can handle large files. I suggest [Sublime Text
Editor](https://www.sublimetext.com/). This editor can handle much
larger files than you can open (as text) in Rstudio. Keep the file open
while you’re cleaning it!

### Detecting outliers

Outliers (as errors) can be most easily identified using graphs.
However, some textual output might be useful as well.

Let’s read in some data (see codebook.txt for info about the variables).

``` r
depression_data <- read_tsv('data/raw_depression.csv')
```

    ## Rows: 39775 Columns: 172
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: "\t"
    ## chr   (2): country, major
    ## dbl (170): Q1A, Q1I, Q1E, Q2A, Q2I, Q2E, Q3A, Q3I, Q3E, Q4A, Q4I, Q4E, Q5A, ...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

People have clearly made errors when entering their ages:

``` r
summary(depression_data$age)
```

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##   13.00   18.00   21.00   23.61   25.00 1998.00

The histogram looks weird because of the very few, very high ages. We
*could* try to fix these by assuming, for example, that `1998` is the
birthyear and not the age. We will do this later.

``` r
hist(depression_data$age)
```

![](CleaningData_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

``` r
dim(depression_data)
```

    ## [1] 39775   172

``` r
filtered_depression_data <- filter(depression_data, age < 120)
dim(filtered_depression_data)
```

    ## [1] 39770   172

``` r
hist(filtered_depression_data$age, breaks=100)
```

![](CleaningData_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

Here is another visualization.

``` r
par(mfcol=c(1,2))
boxplot(depression_data$age)
boxplot(filtered_depression_data$age)
```

![](CleaningData_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

Here is another problem with the data…

``` r
hist(filtered_depression_data$familysize, breaks=100)
```

![](CleaningData_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

``` r
summary(filtered_depression_data$familysize)
```

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##    0.00    2.00    3.00    3.51    4.00  133.00

Categorical data can also be messy. People entered their majors as free
text. And this is the result:

``` r
library(janitor)
```

    ## 
    ## Attaching package: 'janitor'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     chisq.test, fisher.test

``` r
result <- tabyl(depression_data$major)
head(result, 50)
```

    ##                          depression_data$major  n      percent valid_percent
    ##                                              _  1 2.514142e-05  3.513827e-05
    ##                                              - 34 8.548083e-04  1.194701e-03
    ##                                             --  1 2.514142e-05  3.513827e-05
    ##                                            ---  1 2.514142e-05  3.513827e-05
    ##                                          -nil-  1 2.514142e-05  3.513827e-05
    ##                                            ???  1 2.514142e-05  3.513827e-05
    ##                                              .  1 2.514142e-05  3.513827e-05
    ##                                              /  2 5.028284e-05  7.027654e-05
    ##  &#1055;&#1089;&#1080;&#1093;&#1086;&#1083;&#1  1 2.514142e-05  3.513827e-05
    ##    &#1593;&#1604;&#1605; &#1606;&#1601;&#1587;  1 2.514142e-05  3.513827e-05
    ##       &#22810;&#23186;&#39636;&#35373;&#35336;  1 2.514142e-05  3.513827e-05
    ##                               &#28888;&#22521;  1 2.514142e-05  3.513827e-05
    ##                                  &#304;lahiyat  1 2.514142e-05  3.513827e-05
    ##                                              0  2 5.028284e-05  7.027654e-05
    ##                         1. Social work, 2. Law  1 2.514142e-05  3.513827e-05
    ##                                      12th arts  1 2.514142e-05  3.513827e-05
    ##                                             18  1 2.514142e-05  3.513827e-05
    ##                                             19  1 2.514142e-05  3.513827e-05
    ##  2 majors: Computer science and industrial eng  1 2.514142e-05  3.513827e-05
    ##                                   2D animation  1 2.514142e-05  3.513827e-05
    ##                                         2D Art  1 2.514142e-05  3.513827e-05
    ##                                   3D Animation  1 2.514142e-05  3.513827e-05
    ##                     3d animation, architecture  1 2.514142e-05  3.513827e-05
    ##                                             75  1 2.514142e-05  3.513827e-05
    ##                                        a level  1 2.514142e-05  3.513827e-05
    ##                                      A Teacher  1 2.514142e-05  3.513827e-05
    ##                                             AA  1 2.514142e-05  3.513827e-05
    ##                                           AADT  1 2.514142e-05  3.513827e-05
    ##                                       academic  1 2.514142e-05  3.513827e-05
    ##                                            Acc  1 2.514142e-05  3.513827e-05
    ##                                      Acc maybe  1 2.514142e-05  3.513827e-05
    ##                                           acca  1 2.514142e-05  3.513827e-05
    ##                                           Acca  2 5.028284e-05  7.027654e-05
    ##                                           ACCA  2 5.028284e-05  7.027654e-05
    ##     ACCA Professional Accounting Qualification  1 2.514142e-05  3.513827e-05
    ##                                    Accaountant  1 2.514142e-05  3.513827e-05
    ##                                     accauntant  1 2.514142e-05  3.513827e-05
    ##                                     Accontancy  1 2.514142e-05  3.513827e-05
    ##                                      accontant  1 2.514142e-05  3.513827e-05
    ##                               Acconting degree  1 2.514142e-05  3.513827e-05
    ##                                        Accoung  1 2.514142e-05  3.513827e-05
    ##                                     Accounring  1 2.514142e-05  3.513827e-05
    ##                                        account 22 5.531113e-04  7.730419e-04
    ##                                        Account 78 1.961031e-03  2.740785e-03
    ##                                        ACCOUNT  1 2.514142e-05  3.513827e-05
    ##                            account and finance  1 2.514142e-05  3.513827e-05
    ##                            Account and finance  2 5.028284e-05  7.027654e-05
    ##                                    Account ing  1 2.514142e-05  3.513827e-05
    ##                                     Accountacy  1 2.514142e-05  3.513827e-05
    ##                                      accountan  2 5.028284e-05  7.027654e-05

### Missing data

R encodes missing values as `NA`. Missing values are contagious:
performing calculations on data that contains missing values often leads
to an `NA` result. Some functions are robust against missing values
(they simply ignore them). However, when a result comes back as `NA`
it’s often because the data contained missing values in the first place.

``` r
some_data <- c(1,2,3,4, NA)
mean(some_data)
```

    ## [1] NA

``` r
max(some_data)
```

    ## [1] NA

Tips from the field:

-   When reading in a file, it’s a good idea to know how missing values
    are encoded so you can tell R which values to interpret as missing.
-   Sometime people will use absurd values to indicate missing data. For
    example, they might enter -1 or 99999 when an age value is missing.
    These are then read by R as numbers and your calculations end up
    being nonsense. One way to catch this it by looking for outliers!

### Seperating a column

``` r
patient_data <-read_tsv('data/inpatient.tsv')
```

    ## Rows: 163065 Columns: 12
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: "\t"
    ## chr (10): DRG Definition, Provider Name, Provider Street Address, Provider C...
    ## dbl  (2): Provider Id, Total Discharges
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
colnames(patient_data) <- make.names(colnames(patient_data))
head(patient_data, 5)
```

    ## # A tibble: 5 × 12
    ##   DRG.Definition Provi…¹ Provi…² Provi…³ Provi…⁴ Provi…⁵ Provi…⁶ Hospi…⁷ Total…⁸
    ##   <chr>            <dbl> <chr>   <chr>   <chr>   <chr>   <chr>   <chr>     <dbl>
    ## 1 039 - EXTRACR…   10001 SOUTHE… 1108 R… DOTHAN  AL      36301   AL - D…      91
    ## 2 039 - EXTRACR…   10005 MARSHA… 2505 U… BOAZ    AL      35957   AL - B…      14
    ## 3 039 - EXTRACR…   10006 ELIZA … 205 MA… FLOREN… AL      35631   AL - B…      24
    ## 4 039 - EXTRACR…   10011 ST VIN… 50 MED… BIRMIN… AL      35235   AL - B…      25
    ## 5 039 - EXTRACR…   10016 SHELBY… 1000 F… ALABAS… AL      35007   AL - B…      18
    ## # … with 3 more variables: Average.Covered.Charges <chr>,
    ## #   Average.Total.Payments <chr>, Average.Medicare.Payments <chr>, and
    ## #   abbreviated variable names ¹​Provider.Id, ²​Provider.Name,
    ## #   ³​Provider.Street.Address, ⁴​Provider.City, ⁵​Provider.State,
    ## #   ⁶​Provider.Zip.Code, ⁷​Hospital.Referral.Region.Description,
    ## #   ⁸​Total.Discharges
    ## # ℹ Use `colnames()` to see all variable names

``` r
result <- tabyl(patient_data$Hospital.Referral.Region.Description)
head(result, 5)
```

    ##  patient_data$Hospital.Referral.Region.Description    n     percent
    ##                                     AK - Anchorage  231 0.001416613
    ##                                    AL - Birmingham 1881 0.011535277
    ##                                        AL - Dothan  340 0.002085058
    ##                                    AL - Huntsville  407 0.002495937
    ##                                        AL - Mobile  552 0.003385153

Let’s separate this column into two columns.

``` r
test <- separate(patient_data, Hospital.Referral.Region.Description, into=c('state', 'city'), sep='-')
```

    ## Warning: Expected 2 pieces. Additional pieces discarded in 791 rows [710, 711,
    ## 718, 830, 853, 1918, 1921, 1927, 1930, 1940, 2055, 2086, 3398, 3401, 3411, 3415,
    ## 3594, 3630, 5424, 5425, ...].

This resulted in some warnings in certain rows. Let’s look at some of
those rows.

``` r
patient_data$Hospital.Referral.Region.Description[710]
```

    ## [1] "NC - Winston-Salem"

``` r
patient_data$Hospital.Referral.Region.Description[711]
```

    ## [1] "NC - Winston-Salem"

``` r
patient_data$Hospital.Referral.Region.Description[1930]
```

    ## [1] "NC - Winston-Salem"

``` r
test <- separate(patient_data, Hospital.Referral.Region.Description, into=c('state', 'city'), sep=' - ', remove = FALSE)
```

No warnings anymore! Note, you can use regular expression for the `sep`
argument: [see
here.](https://cran.r-project.org/web/packages/stringr/vignettes/regular-expressions.html)

### Combining columns

The opposite operation!

``` r
test <- unite(test, 'combined', c(Provider.Id, Provider.Name), sep='_+_', remove = FALSE)
head(test$combined, 3)
```

    ## [1] "10001_+_SOUTHEAST ALABAMA MEDICAL CENTER"
    ## [2] "10005_+_MARSHALL MEDICAL CENTER SOUTH"   
    ## [3] "10006_+_ELIZA COFFEE MEMORIAL HOSPITAL"

### Strings using `stringr`

It does happen that you need to clean textual data. The `stringr`
package has a bunch of functions to make your life easier (but not
easy). I will run through some examples but do have a look at the
[cheatsheet](https://evoldyn.gitlab.io/evomics-2018/ref-sheets/R_strings.pdf)
as well.

Remember, this data?

``` r
depression_data <- read_tsv('data/raw_depression.csv')
```

    ## Rows: 39775 Columns: 172
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: "\t"
    ## chr   (2): country, major
    ## dbl (170): Q1A, Q1I, Q1E, Q2A, Q2I, Q2E, Q3A, Q3I, Q3E, Q4A, Q4I, Q4E, Q5A, ...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

We have to load `stringr` separately.

``` r
library(stringr)
```

Let’s convert the majors to lower case. Notice that strings that are not
coner

``` r
head(depression_data$major, 10)
```

    ##  [1] NA                          NA                         
    ##  [3] NA                          "biology"                  
    ##  [5] "Psychology"                NA                         
    ##  [7] "Mechatronics engeenerieng" "Music"                    
    ##  [9] "Psychology"                "computer programming"

``` r
depression_data$major <- str_to_lower(depression_data$major)
head(depression_data$major, 10)
```

    ##  [1] NA                          NA                         
    ##  [3] NA                          "biology"                  
    ##  [5] "psychology"                NA                         
    ##  [7] "mechatronics engeenerieng" "music"                    
    ##  [9] "psychology"                "computer programming"

Let’s try to find biology majors

``` r
depression_data$bio <- str_detect(depression_data$major, 'bio')
bio_students <- filter(depression_data, bio)
```

That matched also biomedical and biochemistry students. Let’s detect
those using a regex (See <https://regex101.com/> for a regex
construction tool).

``` r
depression_data$other <- !str_detect(depression_data$major, 'chem|med|phys|tech')
```

Let’s combine our columns

``` r
depression_data <- mutate(depression_data, selection = other * bio)
bio_students <- filter(depression_data, selection==1)
```

## Example: Social Security Applications

I got this example from
[here](https://www.linkedin.com/learning-login/share?account=2133849&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fdata-wrangling-in-r-14135737%3Ftrk%3Dshare_ent_url%26shareId%3D%252BDp0PBL0TaS6XMBZDGEN2w%253D%253D).
This data set tracks how many people apply for SS through the website
(internet) and the total applications (including applications through
mail).

**Take some time to think how you would convert this data to a tidy data
set.**

``` r
ss <- read_csv('data/ssadisability.csv')
```

    ## Rows: 10 Columns: 25
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (1): Fiscal_Year
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
glimpse(ss)
```

    ## Rows: 10
    ## Columns: 25
    ## $ Fiscal_Year     <chr> "FY08", "FY09", "FY10", "FY11", "FY12", "FY13", "FY14"…
    ## $ Oct_Total       <dbl> 176407, 244781, 286598, 299033, 227456, 224624, 206471…
    ## $ Oct_Internet    <dbl> 15082, 32578, 65533, 92856, 86811, 92542, 98400, 13374…
    ## $ Nov_Total       <dbl> 204287, 181161, 213297, 209553, 200140, 249910, 237621…
    ## $ Nov_Internet    <dbl> 17301, 25620, 50098, 63424, 71175, 107053, 117934, 967…
    ## $ Dec_Total       <dbl> 151687, 176107, 198733, 215239, 254766, 188183, 175607…
    ## $ Dec_Internet    <dbl> 14321, 27174, 44512, 62877, 91424, 79719, 83377, 89619…
    ## $ Jan_Total       <dbl> 162966, 249062, 265665, 264286, 221146, 199588, 240969…
    ## $ Jan_Internet    <dbl> 18391, 57908, 68843, 84944, 85848, 93703, 125320, 1294…
    ## $ Feb_Total       <dbl> 228623, 221368, 225319, 223625, 228519, 219604, 205737…
    ## $ Feb_Internet    <dbl> 26034, 50408, 58465, 71314, 83576, 101878, 108384, 101…
    ## $ Mar_Total       <dbl> 190716, 235360, 243266, 246630, 299267, 285923, 219696…
    ## $ Mar_Internet    <dbl> 21064, 53592, 62198, 77916, 112104, 129415, 114993, 10…
    ## $ Apr_Total       <dbl> 194403, 234304, 298065, 300359, 233685, 224804, 218172…
    ## $ Apr_Internet    <dbl> 22372, 53675, 76573, 94722, 88330, 101619, 112417, 101…
    ## $ May_Total       <dbl> 226549, 281343, 239409, 241673, 239503, 269955, 258726…
    ## $ May_Internet    <dbl> 26337, 65822, 65780, 77603, 93826, 123440, 134714, 122…
    ## $ June_Total      <dbl> 193094, 237329, 231964, 233351, 284136, 223238, 213389…
    ## $ June_Internet   <dbl> 22551, 54285, 67163, 79925, 113613, 104146, 110227, 99…
    ## $ July_Total      <dbl> 181552, 285172, 300442, 292949, 221745, 204072, 198484…
    ## $ July_Internet   <dbl> 22728, 66565, 92957, 105276, 91323, 98326, 106013, 124…
    ## $ August_Total    <dbl> 245429, 240611, 248284, 237555, 298458, 281828, 265979…
    ## $ August_Internet <dbl> 30580, 54915, 75535, 86514, 119795, 135423, 139000, 10…
    ## $ Sept_Internet   <dbl> 24141, 52687, 73403, 103564, 93375, 104270, 107284, 98…
    ## $ Sept_Total      <dbl> 186750, 228692, 238965, 280913, 230648, 214004, 203384…

``` r
colnames(ss)
```

    ##  [1] "Fiscal_Year"     "Oct_Total"       "Oct_Internet"    "Nov_Total"      
    ##  [5] "Nov_Internet"    "Dec_Total"       "Dec_Internet"    "Jan_Total"      
    ##  [9] "Jan_Internet"    "Feb_Total"       "Feb_Internet"    "Mar_Total"      
    ## [13] "Mar_Internet"    "Apr_Total"       "Apr_Internet"    "May_Total"      
    ## [17] "May_Internet"    "June_Total"      "June_Internet"   "July_Total"     
    ## [21] "July_Internet"   "August_Total"    "August_Internet" "Sept_Internet"  
    ## [25] "Sept_Total"

### A reminder on `pivot_longer()`

![](images/pivot_longer_new.png)

### Using `pivot_longer()`

``` r
longer_format <- pivot_longer(ss, cols=Oct_Total:Sept_Total, names_to = 'period_source', values_to = 'Count')
```

This is better. But not perfect yet.

``` r
count
```

    ## function (x, ..., wt = NULL, sort = FALSE, name = NULL) 
    ## {
    ##     UseMethod("count")
    ## }
    ## <bytecode: 0x55b802aaef38>
    ## <environment: namespace:dplyr>

### Using `separate()`

Let’s split the `period_source` column.

``` r
splitted <- separate(longer_format, period_source, into=c('Month', 'Source'), sep='_')
```

### Creating an `Other` column

I’d like to create a column listing the difference between `Internet`
and `Total`. I’ll do this by first creating a wider format.

![](images/pivot_wider_new.png)

``` r
wider <- pivot_wider(splitted, names_from = 'Source', values_from = 'Count')
head(wider)
```

    ## # A tibble: 6 × 4
    ##   Fiscal_Year Month  Total Internet
    ##   <chr>       <chr>  <dbl>    <dbl>
    ## 1 FY08        Oct   176407    15082
    ## 2 FY08        Nov   204287    17301
    ## 3 FY08        Dec   151687    14321
    ## 4 FY08        Jan   162966    18391
    ## 5 FY08        Feb   228623    26034
    ## 6 FY08        Mar   190716    21064

``` r
wider<-mutate(wider, Other = Total - Internet)
head(wider)
```

    ## # A tibble: 6 × 5
    ##   Fiscal_Year Month  Total Internet  Other
    ##   <chr>       <chr>  <dbl>    <dbl>  <dbl>
    ## 1 FY08        Oct   176407    15082 161325
    ## 2 FY08        Nov   204287    17301 186986
    ## 3 FY08        Dec   151687    14321 137366
    ## 4 FY08        Jan   162966    18391 144575
    ## 5 FY08        Feb   228623    26034 202589
    ## 6 FY08        Mar   190716    21064 169652

Now we can go back to the long format.

``` r
long_again <- select(wider, -Total)
long_again <- pivot_longer(long_again, cols = c(Internet, Other), names_to = 'Source', values_to = 'Count') 
```

### Convert `Fiscal_Year` to year

``` r
numbers <- str_extract(long_again$Fiscal_Year, '[0-9]{2}')
numbers <- 2000 + as.integer(numbers)
long_again <- add_column(long_again, Year = numbers)
long_again <- select(long_again, -Fiscal_Year)
```

### Create a date variable

``` r
library(lubridate)
```

    ## 
    ## Attaching package: 'lubridate'

    ## The following objects are masked from 'package:base':
    ## 
    ##     date, intersect, setdiff, union

``` r
long_again$date <- paste('01', long_again$Month, long_again$Year)
long_again$date<-dmy(long_again$date)
```

### Plots

Let’s create some plots.

``` r
data_2012 <- filter(long_again, Year == 2012)
ggplot(data_2012) + aes(x=date, y = Count, group=Source, color=Source) + geom_line()
```

![](CleaningData_files/figure-gfm/unnamed-chunk-30-1.png)<!-- -->

``` r
ggplot(long_again) + aes(x=Month, y = Count, group=Source, color=Source) + geom_line() + facet_grid(~Year)
```

    ## Warning: Removed 2 row(s) containing missing values (geom_path).

![](CleaningData_files/figure-gfm/unnamed-chunk-31-1.png)<!-- -->

## Example: Coal data

Have a look at the data in an editor: the first 2 lines can be skipped.
Missing values are given by `--`.

``` r
coal_data <- read_csv('data/coal.csv', skip=2, na = "--")
```

    ## New names:
    ## Rows: 232 Columns: 31
    ## ── Column specification
    ## ──────────────────────────────────────────────────────── Delimiter: "," chr
    ## (1): ...1 dbl (30): 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
    ## 1990, ...
    ## ℹ Use `spec()` to retrieve the full column specification for this data. ℹ
    ## Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## • `` -> `...1`

``` r
head(coal_data)
```

    ## # A tibble: 6 × 31
    ##   ...1        `1980`  `1981`  `1982`  `1983`  `1984` `1985` `1986` `1987` `1988`
    ##   <chr>        <dbl>   <dbl>   <dbl>   <dbl>   <dbl>  <dbl>  <dbl>  <dbl>  <dbl>
    ## 1 North Ame… 1.65e+1 1.70e+1 1.65e+1 1.71e+1 1.84e+1 18.8   18.5   19.4   20.4  
    ## 2 Bermuda    0       0       0       0       0        0      0      0      0    
    ## 3 Canada     9.62e-1 9.90e-1 1.06e+0 1.12e+0 1.24e+0  1.21   1.13   1.25   1.36 
    ## 4 Greenland  5   e-5 5   e-5 3   e-5 3   e-5 3   e-5  0      0      0      0    
    ## 5 Mexico     1.02e-1 1.06e-1 1.20e-1 1.29e-1 1.31e-1  0.146  0.156  0.170  0.160
    ## 6 Saint Pie… 0       0       0       0       0        0      0      0      0    
    ## # … with 21 more variables: `1989` <dbl>, `1990` <dbl>, `1991` <dbl>,
    ## #   `1992` <dbl>, `1993` <dbl>, `1994` <dbl>, `1995` <dbl>, `1996` <dbl>,
    ## #   `1997` <dbl>, `1998` <dbl>, `1999` <dbl>, `2000` <dbl>, `2001` <dbl>,
    ## #   `2002` <dbl>, `2003` <dbl>, `2004` <dbl>, `2005` <dbl>, `2006` <dbl>,
    ## #   `2007` <dbl>, `2008` <dbl>, `2009` <dbl>
    ## # ℹ Use `colnames()` to see all variable names

**Take some time to think how you would convert this data to a tidy data
set.**

### Change the first variable name

``` r
existing_names <- colnames(coal_data)
existing_names[1] <- 'country'
colnames(coal_data) <- existing_names
```

### Convert to a long data format

![](images/pivot_longer_new.png)

``` r
long_format <- pivot_longer(coal_data, names_to = 'year', values_to = 'coal_use', cols = '1980':'2009')
```

### Separate regions and countries

``` r
regions <- c("North America", "Central & South America", "Antarctica", "Europe", "Eurasia", "Middle East", "Africa", "Asia & Oceania", "World")
long_format <- mutate(long_format, is_region =long_format$country %in% regions)
region_data <- filter(long_format, is_region)
country_data <- filter(long_format, !is_region)
region_data <- select(region_data, -is_region)
country_data <- select(country_data, -is_region)
```
