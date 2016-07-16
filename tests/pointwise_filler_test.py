# coding:utf-8
import catprep
import pandas as pd
import numpy as np


def test_fit_and_transform():
    df = pd.DataFrame([
        ['AA', 'a', 0],
        ['AA', 'b', 1],
        ['AA', 'b', 1],
    ], columns=['x1', 'x2', 'y'])
    filler = catprep.PointwiseFiller()
    filler.fit(df, columns=['x1', 'x2'], target='y')

    assert filler.means['x1']['x1'].tolist() == ['AA']
    assert np.abs(filler.means['x1']['x1_mean'].values - [2. / 3.]) < 1e-9
    assert filler.means['x2']['x2'].tolist() == ['a', 'b']
    assert np.all(np.abs(filler.means['x2']['x2_mean'].values - [0., 1.]) < [1e-9, 1e-9])

    transformed_df = filler.transform(df)
    assert np.sum(np.abs(transformed_df['x1_mean'].values - [2./3., 2./3., 2./3.])) < 1e-9
    assert np.sum(np.abs(transformed_df['x2_mean'].values - [0., 1., 1.])) < 1e-9
