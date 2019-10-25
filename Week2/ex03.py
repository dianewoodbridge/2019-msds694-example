from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("ex03")
sc = SparkContext(conf=conf)


sc.stop()
