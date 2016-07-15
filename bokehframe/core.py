from . import DataFrame, Series, bokeh_loaded, output_notebook, Line, show, auto_show


def safe_show(chart, **kwargs):
    do_show = kwargs.get('show', auto_show())

    if do_show:
        show(chart)

    return chart


class BokehStructure(object):

    def output_notebook(self):
        if bokeh_loaded:
            output_notebook()
        else:
            print('Bokeh is not loaded, no action taken.')


class BokehFrame(DataFrame):

    @property
    def _constructor(self):
        return BokehFrame

    @property
    def _constructor_sliced(self):
        return BokehSeries

    def plot(self, *args, **kwargs):
        if bokeh_loaded:
            l = Line(self.copy(), legend=True)
            return safe_show(l, **kwargs)
        else:
            return super(BokehFrame, self).plot(*args, **kwargs)

    def to_pandas(self):
        return DataFrame(self)


class BokehSeries(Series):

    @property
    def _constructor(self):
        return BokehSeries

    @property
    def _constructor_expanddim(self):
        return BokehFrame

    def to_pandas(self):
        return Series(self)

    def plot(self, *args, **kwargs):
        if bokeh_loaded:
            l = Line(self.copy(), legend=True)
            return safe_show(l, **kwargs)
        else:
            return super(BokehSeries, self).plot(*args, **kwargs)



