Exercises
================
Last Updated: 04, October, 2022 at 08:28

-   <a href="#part-1" id="toc-part-1">Part 1</a>

## Part 1

Use the following data for this part:

``` r
library(gapminder)
gap_data <- gapminder
```

-   Filter the data for the Americas in 2007. Retain only the `lifeExp`
    variable and deselect all other variables.
-   Create the variable `gdp`, defined as the product of `pop` and
    `gdpPercap`.
-   Identify the observation (combination of county, continent, and
    year) with lowest gdp per person.
-   Identify all observations with above average life expectancy,
    stratified for each continent.
-   Compute the mean life expectancy for each year per continent.
