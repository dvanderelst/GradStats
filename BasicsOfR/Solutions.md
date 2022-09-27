Solutions
================
Last Updated: 27, September, 2022 at 08:28

-   <a href="#one" id="toc-one">One</a>
-   <a href="#two" id="toc-two">Two</a>
-   <a href="#three" id="toc-three">Three</a>
-   <a href="#four" id="toc-four">Four</a>

## One

Write a for loop that iterates over the numbers 1 to 7 and prints the
cube of each number using print().

``` r
for(i in 1:7){
  print(i^2)
  }
```

    ## [1] 1
    ## [1] 4
    ## [1] 9
    ## [1] 16
    ## [1] 25
    ## [1] 36
    ## [1] 49

## Two

Write a while loop that prints out standard random normal numbers (use
rnorm()) but stops (breaks) if you get a number bigger than 1.

Option 1

``` r
value <- 0
counter <-0
while(value < 1)
{
  value <- rnorm(1)
  counter <- counter + 1
}
print(value)
```

    ## [1] 1.178227

``` r
print(counter)
```

    ## [1] 11

Option 2

``` r
counter <-0
while(TRUE)
{
  value <- rnorm(1)
  counter <- counter + 1
  if (value > 1){break}
}
print(value)
```

    ## [1] 2.285224

``` r
print(counter)
```

    ## [1] 7

## Three

Using a for loop simulate the flip a coin twenty times, keeping track of
the individual outcomes (1 = heads, 0 = tails) in a vector.

``` r
repeats <- 20
outcomes <- character(repeats)
for(i in 1:repeats)
{
  outcome <- sample(c('H','T'), 1)
  outcomes[i] <- outcome
}
outcomes
```

    ##  [1] "T" "H" "T" "H" "H" "T" "H" "H" "T" "T" "T" "T" "T" "H" "T" "H" "H" "H" "H"
    ## [20] "H"

You could do this in one line (but that was not the exercise).

``` r
repeats <- 20
outcomes <- sample(c('H','T'), repeats, replace = TRUE)
outcomes
```

    ##  [1] "T" "T" "H" "T" "H" "H" "T" "H" "T" "H" "H" "H" "T" "T" "T" "T" "T" "H" "H"
    ## [20] "T"

## Four

Use a while loop to investigate the number of terms required before the
series 1 ,reaches above 10 million.

``` r
product <- 1
term <- 0

while(product < 10000000)
{
  term <- term + 1
  product <- product * term
  
}
print(term)
```

    ## [1] 11

``` r
# Check
1:term
```

    ##  [1]  1  2  3  4  5  6  7  8  9 10 11

``` r
cumprod(1:term)>10000000
```

    ##  [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE
