import marimo as mo

app = mo.App()

@app.cell
def _():
    mo.md("""
    # Hello world
    This is a _markdown_ **cell**.
    """)
    return
