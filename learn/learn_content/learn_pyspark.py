"""
pyspark使用
"""
from pyspark import SparkConf, SparkContext

# 创建sparkConf对象，local为本地，集群时需要多选
conf = SparkConf().setMaster("local[*]").setAppName("test_python_database")

# 为sparkConf创建sparkContext对象
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("test")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"1": "1", "2": "2", "3": "3", "4": "4"})
print(sc.version)
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# 停止spark对象运行
sc.stop()
