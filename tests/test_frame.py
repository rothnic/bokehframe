

from bokehframe import BokehFrame, auto_show, output_file
import numpy as np
import matplotlib.pyplot as plt


output_file('test.html')
auto_show(True)


def make_data():
    df = BokehFrame({'a': np.random.random_sample(size=(100,)),
                     'b': np.random.random_sample(size=(100,))})
    return df


def test_frame():
    df = make_data()
    df.plot()


def test_matplotlib():
    df = make_data()
    df2 = df.to_pandas()
    plt.show(df2.plot())


if __name__ == '__main__':
    test_frame()
    test_matplotlib()
