#!/usr/bin/python
#-*- coding:utf-8 -*-
import pyspark
from pyspark import SparkContext as sc
from pyspark import SparkConf

conf=SparkConf().setAppName("miniProject").setMaster("local[*]")
sc=sc.getOrCreate(conf)
#（a）利用list创建一个RDD;
# 使用sc.parallelize可以把Python list，NumPy array或者Pandas Series,Pandas DataFrame转成Spark RDD。
rdd = sc.parallelize([1,2,3,4,5])
print(rdd)
#Output:ParallelCollectionRDD[0] at parallelize at PythonRDD.scala:480

#（b）getNumPartitions()方法查看list被分成了几部分
print(rdd.getNumPartitions())
#Output:4



