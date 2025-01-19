import os
os.environ["SPARK_HOME"] = "/opt/homebrew/opt/apache-spark/libexec"
os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, round, desc

# Initialize SparkSession
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("hw3") \
    .config("spark.hadoop.fs.defaultFS", "file:///") \
    .config("spark.yarn.submit.file.replication", "1") \
    .getOrCreate()


# Function to load and display data
def load_csv(file_path, schema=None):
    try:
        df = spark.read.csv(file_path, header=True, schema=schema)
        print(f"Loaded dataset: {file_path}")
        df.show(5)
        return df
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

# Load datasets
users_df = load_csv('./hw3/datasets/users.csv')
purchases_df = load_csv('./hw3/datasets/purchases.csv')
products_df = load_csv('./hw3/datasets/products.csv')

# Drop nulls
users_df = users_df.dropna()
purchases_df = purchases_df.dropna()
products_df = products_df.dropna()

# Task 3: Sum of purchases for each category
print("\nTask 3: Total sum of purchases by category")
category_purchases = (
    purchases_df.join(products_df, "product_id", "inner")
    .select("category", col("quantity").cast("int"), col("price").cast("float"))
    .withColumn("sum_of_purchases", col("quantity") * col("price"))
    .groupBy("category")
    .agg(round(sum("sum_of_purchases"), 1).alias("total_sum_of_purchases"))
)
category_purchases.show()

# Task 4: Sum of purchases for each category for age 18-25
print("\nTask 4: Total sum of purchases by category for age 18-25")
age_filtered_purchases = (
    purchases_df.join(products_df, "product_id", "inner")
    .join(users_df, "user_id", "inner")
    .select("category", col("quantity").cast("int"), col("price").cast("float"), col("age").cast("int"))
    .withColumn("sum_of_purchases", col("quantity") * col("price"))
    .filter((col("age") >= 18) & (col("age") <= 25))
    .groupBy("category")
    .agg(round(sum("sum_of_purchases"), 1).alias("total_sum_of_purchases"))
)
age_filtered_purchases.show()

# Task 5: Percentage of purchases for each category for age 18-25
print("\nTask 5: Percentage of purchases by category for age 18-25")
grand_total = (
    purchases_df.join(products_df, "product_id", "inner")
    .join(users_df, "user_id", "inner")
    .select(col("quantity").cast("int"), col("price").cast("float"), col("age").cast("int"))
    .withColumn("sum_of_purchase", col("quantity") * col("price"))
    .filter((col("age") >= 18) & (col("age") <= 25))
    .agg(sum("sum_of_purchase").alias("grand_total"))
    .collect()[0]["grand_total"]
)

percentage_purchases = (
    age_filtered_purchases.withColumn(
        "percentage_of_purchases", round(col("total_sum_of_purchases") / grand_total * 100, 2)
    )
)
percentage_purchases.show()

# Task 6: Top-3 categories by percentage of purchases
print("\nTask 6: Top-3 categories by percentage of purchases")
top_3_categories = (
    percentage_purchases.orderBy(desc("percentage_of_purchases"))
    .limit(3)
)
top_3_categories.show()

# Extract top categories as a list
top_categories_list = [row["category"] for row in top_3_categories.collect()]
print("Top-3 product categories for 18-25 age group:", top_categories_list)

# Stop the SparkSession
spark.stop()
