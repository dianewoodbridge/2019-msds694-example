from pyspark import SparkConf, SparkContext

# Create SparkContext.
conf = SparkConf().setMaster("local[*]").setAppName("ex04")
sc = SparkContext(conf=conf)

# Load Data.
lines = sc.textFile("../Data/README.md")
count = lines.count()
first = lines.first()

print(str(count))
print(first)

sc.stop()
