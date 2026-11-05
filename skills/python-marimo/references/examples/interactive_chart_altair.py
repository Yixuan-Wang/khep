import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import altair as alt
    import polars as pl
    return


@app.cell
def _():
    # Load dataset
    _weather = pl.read_csv("https://raw.githubusercontent.com/vega/vega-datasets/refs/heads/main/data/weather.csv")
    _weather_dates = _weather.with_columns(
        pl.col("date").str.strptime(pl.Date, format="%Y-%m-%d")
    )
    _chart = (
        alt.Chart(_weather_dates)
        .mark_point()
        .encode(
            x="date:T",
            y="temp_max",
            color="location",
        )
    )
    chart = mo.ui.altair_chart(_chart)
    chart
    return


@app.cell
def _():
    # Display the selection
    chart.value
    return


if __name__ == "__main__":
    app.run()
