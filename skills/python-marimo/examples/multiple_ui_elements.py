import marimo as mo
import polars as pl
import altair as alt

app = mo.App()

@app.cell
def _():
    import marimo as mo
    import polars as pl
    import altair as alt
    return

@app.cell
def _():
    iris = pl.read_csv("hf://datasets/scikit-learn/iris/Iris.csv")
    return

@app.cell
def _():
    species_selector = mo.ui.dropdown(
        options=["All"] + iris["Species"].unique().to_list(),
        value="All",
        label="Species",
    )
    x_feature = mo.ui.dropdown(
        options=iris.select(pl.col(pl.Float64, pl.Int64)).columns,
        value="SepalLengthCm",
        label="X Feature",
    )
    y_feature = mo.ui.dropdown(
        options=iris.select(pl.col(pl.Float64, pl.Int64)).columns,
        value="SepalWidthCm",
        label="Y Feature",
    )
    mo.hstack([species_selector, x_feature, y_feature])
    return

@app.cell
def _():
    filtered_data = iris if species_selector.value == "All" else iris.filter(pl.col("Species") == species_selector.value)

    chart = alt.Chart(filtered_data).mark_circle().encode(
        x=alt.X(x_feature.value, title=x_feature.value),
        y=alt.Y(y_feature.value, title=y_feature.value),
        color='Species'
    ).properties(
        title=f"{y_feature.value} vs {x_feature.value}",
        width=500,
        height=400
    )

    chart
    return
