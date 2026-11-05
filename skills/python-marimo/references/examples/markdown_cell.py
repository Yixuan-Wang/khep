import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    mo.md("""
    # Hello world
    This is a _markdown_ **cell**.
    """)
    return


if __name__ == "__main__":
    app.run()
