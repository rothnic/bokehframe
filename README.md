BokehFrame
---

[Pandas](http://pandas.pydata.org/pandas-docs/stable/) structures with integrated [Bokeh](http://bokeh.pydata.org/en/latest/) plotting.

***This project is currently a proof of concept and not fully functional.***

This project is built around the convenience of having plotting utilities built into a dataframe. Often the desire is to use a piping interface to send the output of some operation into some function. However, I personally feel that the user experience is poor because tools are not able to provide the same docstring integration and intents as if the function was built-in. You also are often forced into sending keyword arguments or using a partial evaluation of the function.

The intent is to be somewhat consistent with the pandas plotting api, but there will likely have to be some differences to match up with the capabilities of Bokeh. One main benefit is that the data manipulations can be performed with Pandas, which can also be used to infer the inputs into the chart, which isn't possible with Bokeh alone. So, when we see a GroupBy then a scatter plot called, we can by default color by the groups.


``` python

df = BokehFrame({'a': np.random.random_sample(size=(100,)),
                 'b': np.random.random_sample(size=(100,))})

df.plot()

```

Produces the following output:

![](http://i.imgur.com/ojFwNtB.png)
