import marimo as mo
import altair as alt
import polars as pl

app = mo.App()

@app.cell
def _():
    import marimo as mo
    import altair as alt
    import polars as pl
    return

@app.cell
def _():
    # Load dataset
    weather = pl.read_csv("https://raw.githubusercontent.com/vega/vega-datasets/refs/heads/main/data/weather.csv")
    weather_dates = weather.with_columns(
        pl.col("date").str.strptime(pl.Date, format="%Y-%m-%d")
    )
    _chart = (
        alt.Chart(weather_dates)
        .mark_point()
        .encode(
            x="date:T",
            y="temp_max",
            color="location",
        )
    )
    return

@app.cell
def _():
    chart = mo.ui.altair_chart(_chart)
    chart
    return

@app.cell
def _():
    # Display the selection
    chart.value
    return
