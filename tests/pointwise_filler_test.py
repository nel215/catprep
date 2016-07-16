# coding:utf-8
import catprep
import pandas as pd
import numpy as np


def test_fit():
    df = pd.DataFrame([
        ['A', 'a', 0],
        ['A', 'b', 1],
        ['A', 'b', 1],
    ], columns=['x1', 'x2', 'y'])
    filler = catprep.PointwiseFiller()
    filler.fit(df, columns=['x1', 'x2'], target='y')

    assert filler.means['x1']['column'].tolist() == ['A']
    assert np.abs(filler.means['x1']['mean'].values - [2. / 3.]) < 1e-9
    assert filler.means['x2']['column'].tolist() == ['a', 'b']
    assert np.all(np.abs(filler.means['x2']['mean'].values - [0., 1.]) < [1e-9, 1e-9])
