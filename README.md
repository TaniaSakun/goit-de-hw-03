# goit-de-hw-03
The repository for the 3rd GoItNeo Data Engineering homework

**Homework tasks:**
1. Load and read each CSV file as a separate DataFrame.
2. Clean the data by removing any rows with missing values.
3. Determine the total purchase amount for each product category.
4. Determine the total purchase amount for each product category for the 18–25 age group.
5. Calculate the share of purchases for each product category as a percentage of the total expenditure for the 18–25 age group.
6. Select the top 3 product categories with the highest percentage of spending by consumers aged 18–25.

**Homework results:**

|user_id|  name|age|            email| 
| ------- | ------- | ------- | ------- |
|      1|User_1| 45|user1@example.com|
|      2|User_2| 48|user2@example.com|
|      3|User_3| 36|user3@example.com|
|      4|User_4| 46|user4@example.com|
|      5|User_5| 29|user5@example.com|

Loaded dataset: ./hw3/datasets/purchases.csv

| purchase_id |user_id|product_id|      date|quantity|
|-------------|--- |--- |--- |--- |
| 1           |     52|         9|2022-01-01|       1|
| 2           |     93|        37|2022-01-02|       8|
| 3           |     15|        33|2022-01-03|       1|
| 4           |     72|        42|2022-01-04|       9|
| 5           |     61|        44|2022-01-05|       6|

Loaded dataset: ./hw3/datasets/products.csv

|product_id|product_name|   category|price|
|---|--- |--- |--- |
|         1|   Product_1|     Beauty|  8.3|
|         2|   Product_2|       Home|  8.3|
|         3|   Product_3|Electronics|  9.2|
|         4|   Product_4|Electronics|  2.6|
|         5|   Product_5|Electronics|  9.4|

Task 3: Total sum of purchases by category

|   category|total_sum_of_purchases|
|--- |--- |
|       Home|                1523.5|
|     Sports|                1802.5|
|Electronics|                1174.8|
|   Clothing|                 790.3|
|     Beauty|                 459.9|

Task 4: Total sum of purchases by category for age 18-25

|   category|total_sum_of_purchases|
|--- |--- |
|       Home|                 361.1|
|     Sports|                 310.5|
|Electronics|                 249.6|
|   Clothing|                 245.0|
|     Beauty|                  41.4|

Task 5: Percentage of purchases by category for age 18-25

|   category|total_sum_of_purchases|percentage_of_purchases|
|--- |--- |--- |
|       Home|                 361.1|                   29.9|
|     Sports|                 310.5|                  25.71|
|Electronics|                 249.6|                  20.67|
|   Clothing|                 245.0|                  20.29|
|     Beauty|                  41.4|                   3.43|

Task 6: Top-3 categories by percentage of purchases

|   category|total_sum_of_purchases|percentage_of_purchases|
|--- |--- |--- |
|       Home|                 361.1|                   29.9|
|     Sports|                 310.5|                  25.71|
|Electronics|                 249.6|                  20.67|

Top-3 product categories for 18-25 age group: ['Home', 'Sports', 'Electronics']