# /// script
# [tool.marimo]
# ///

import marimo
__generated_with = "0.20.3"
app = marimo.App(width="medium")

with app.setup():
    import os

    import marimo as mo

    os.chdir(os.environ["PWD"])


@app.cell
def _():
   return


if __name__ == "__main__":
    app.run()
