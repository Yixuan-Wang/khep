import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import altair as alt
    import polars as pl
    import numpy as np
    return


@app.cell
def _():
    n_points = mo.ui.slider(10, 100, value=50, label="Number of points")
    n_points
    return


@app.cell
def _():
    _x = np.random.rand(n_points.value)
    _y = np.random.rand(n_points.value)

    _df = pl.DataFrame({"x": _x, "y": _y})

    _chart = alt.Chart(_df).mark_circle(opacity=0.7).encode(
        x=alt.X('x', title='X axis'),
        y=alt.Y('y', title='Y axis')
    ).properties(
        title=f"Scatter plot with {n_points.value} points",
        width=400,
        height=300
    )

    _chart
    return


if __name__ == "__main__":
    app.run()
