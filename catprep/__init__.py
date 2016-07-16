# coding:utf-8
import pandas as pd
import numpy as np


class PointwiseFiller(object):
    def __init__(self):
        self.means = {}

    def fit(self, df, columns, target):
        for column in columns:
            rows = []
            for key, value in df.groupby(column):
                row = [key[0], value[target].mean()]
                rows.append(row)
            self.means[column] = pd.DataFrame(rows, columns=['column', 'mean'])
