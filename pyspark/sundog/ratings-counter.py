# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 20:47:59 2018

@author: bhansn
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Test').getOrCreate()

df = spark.read.csv('C:/Naveen/1_Udemy/sundog/SparkCourse/ml-100k/u.data', sep='\t')

df.groupBy(df._c2).count().orderBy('count').show()
