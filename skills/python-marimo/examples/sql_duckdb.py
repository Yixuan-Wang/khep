import marimo as mo
import polars as pl

app = mo.App()

@app.cell
def _():
    import marimo as mo
    import polars as pl
    return

@app.cell
def _():
    weather = pl.read_csv('https://raw.githubusercontent.com/vega/vega-datasets/refs/heads/main/data/weather.csv')
    return

@app.cell
def _():
    seattle_weather_df = mo.sql(
        f"""
        SELECT * FROM weather WHERE location = 'Seattle';
        """
    )
    return
