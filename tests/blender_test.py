# coding:utf-8
import catprep
import pandas as pd
import numpy as np


def gen_data(dim, n, label):
    res = []
    for i in range(n):
        x = np.random.randint(4, size=dim)
        y = np.sum(x) % 2
        row = list(map(lambda x: chr(65+x), x))
        if label:
            row = row + [y]
        res.append(row)
    return res


def test_fit_and_blend():
    np.random.seed(215)
    dim = 2
    x_columns = ['x{}'.format(i) for i in range(dim)]
    columns = x_columns + ['y']

    df = pd.DataFrame(gen_data(dim, 100, label=True), columns=columns)
    blender = catprep.Blender()
    blender.fit(df, columns=x_columns, target='y')
    blended_df = blender.blend(df, columns=x_columns, target='y')
    assert blender.best_score < 1e-9
    assert blender.best_param == {'n_estimators': 100, 'max_depth': 8}
    assert blender.best_reg is not None


def test_fit_and_transform():
    np.random.seed(215)
    dim = 2
    x_columns = ['x{}'.format(i) for i in range(dim)]
    columns = x_columns + ['y']

    df = pd.DataFrame(gen_data(dim, 100, label=True), columns=columns)
    blender = catprep.Blender()
    blender.fit(df, columns=x_columns, target='y')

    test_df = pd.DataFrame(gen_data(dim, 10, label=False), columns=x_columns)
    blended_test_df = blender.transform(test_df, columns=x_columns, target='y')
    assert blended_test_df['blended_y'].shape == (10,)
