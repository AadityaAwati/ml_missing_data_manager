# ml_missing_data_manager
A Python Program which takes a .csv dataset, displays the missing values and replaces them with the strategy of the user's choice.

## Example Program Output

```

Missing Data Manager - By Aaditya Awati

Please Enter Dataset(.csv) Path -> test_dataset.csv

Processing ...

Missing Values :-

Column: Location | Row: 8 - nan
Column: Location | Row: 9 - nan
Column: Unnamed: 1 | Row: 10 - nan
Column: Unnamed: 1 | Row: 12 - nan
Column: Experience(in years) | Row: 5 - nan
Column: Experience(in years) | Row: 6 - nan
Column: Experience(in years) | Row: 11 - nan
Column: Experience(in years) | Row: 13 - nan
Column: Time In Company(in years) | Row: 1 - nan
Column: Time In Company(in years) | Row: 7 - nan
Column: Time In Company(in years) | Row: 9 - nan
Column: Time In Company(in years) | Row: 11 - nan
Column: Salary(in dollars) | Row: 10 - nan
Column: Salary(in dollars) | Row: 12 - nan

Would you like to fill the numerical missing values? (Y/n) -> Y
Please Enter Strategy to be used for filling out Missing Values (mean/median/constant/most_frequent) -> median

Processing ...

All Numerical Values have been replaced with their column's median value(s).
         Location  Unnamed: 1  ...  Time In Company(in years)  Salary(in dollars)
0        New York        35.0  ...                        2.5             94000.0
1       Manhattan        27.0  ...                        5.0             53000.0
2   San Francisco        45.0  ...                        5.0            120000.0
3        New York        62.0  ...                       13.0            121000.0
4          Boston        24.0  ...                        0.5             49000.0
5          Boston        39.0  ...                        4.0             78000.0
6         Atlanta        30.0  ...                        7.0             96000.0
7          Denver        51.0  ...                        5.0            105000.0
8             NaN        42.0  ...                        9.0             94000.0
9             NaN        33.0  ...                        5.0            100000.0
10        Seattle        37.0  ...                        4.5             94000.0
11         Austin        46.0  ...                        5.0             83000.0
12        Chicago        37.0  ...                        7.0             94000.0
13       New York        29.0  ...                        5.0             60000.0

[14 rows x 5 columns]
Dataset 'test_dataset.csv' saved to Filled Datasets/test_dataset.csv

Process finished with exit code 0


```
