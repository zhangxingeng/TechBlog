## Key parts of initializing a spark dataframe

### Create a session
```python
spark = SparkSession.builder.appName("app").master("local").getOrCreate()
```
### Define a Schema
```python
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("sex", StringType(), False),
    StructField("salary", IntegerType(), False)
])
```
### Read data with Schema
```python
df_csv = spark.read.schema(schema).csv("./input_data.csv", header=True)
df_json = spark.read.schema(schema).json("./input_data.json")
df_txt_delimited = spark.read.schema(schema).option("delimiter", "\t").csv("./input_data.txt")
df_parquet = spark.read.schema(schema).parquet("./input_data.parquet")
```

### Read as a stream
```python
# Read as Stream
df_stream_parquet = spark.readStream.schema(schema).format("parquet").load("./input_data")
# Perform some operations as usual
df_filtered = df_stream_parquet.filter(col("salary") > 50000)
df_aggregated = df_filtered.groupBy("sex").avg("salary")
# Write as Stream, need to wait for termination
query = df_aggregated.writeStream.format("parquet").option("path", "./outputs/").option("checkpointLocation", "./checkpoints/").outputMode("complete").start()
query.awaitTermination()
```

### Convert RDD to dataframe
```python
# Example RDD
rdd = spark.sparkContext.parallelize([
    Row(id=1, name='A', sex='m', salary=2500),
    Row(id=2, name='B', sex='f', salary=1500),
    Row(id=3, name='C', sex='m', salary=5500),
    Row(id=4, name='D', sex='f', salary=500)
])
# Convert RDD to DataFrame with schema
df_from_rdd = spark.createDataFrame(rdd, schema)
```

