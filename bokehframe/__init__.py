from pandas import DataFrame, Series

bokeh_loaded = False
try:
    from bokeh.charts import Line, show, output_notebook, output_file

    bokeh_loaded = True
except ImportError:
    print('Bokeh not loading, fallback to matplotlib.')


_auto_show = False


def auto_show(val=None):
    global _auto_show

    if val is not None:
        _auto_show = val

    return _auto_show


from .core import BokehFrame, BokehSeries