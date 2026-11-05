import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import polars as pl
    from vega_datasets import data
    return


@app.cell
def _():
    _cars_df = pl.DataFrame(data.cars())
    mo.ui.data_explorer(_cars_df)
    return


if __name__ == "__main__":
    app.run()
