import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    mo.stop(not data.value, mo.md("No data to display"))

    if mode.value == "scatter":
        mo.output.replace(render_scatter(data.value))
    else:
        mo.output.replace(render_bar_chart(data.value))
    return


if __name__ == "__main__":
    app.run()
