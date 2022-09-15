# Lab 02

## The dataset

### 1. How many splits does the dataset has ?

The dataset has 3 splits: train, test, unsupervised.

```py
from datasets import get_dataset_split_names

get_dataset_split_names("imdb")
```

### 2. How big are these splits

The train and the test have 25 000 rows.  
The unsupervised split has 50 000 rows.

### 3. What is the proportion of each class on the supervised splits ?


