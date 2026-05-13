---
name: python-marimo
description: Guides on how to handle a marimo Python notebook.
disable-model-invocation: true
---

A marimo notebook is a Python script. Each cell in the notebook is a Python function decorated with `@app.cell`, where `app` is an instance of `marimo.App`. When making edits to a marimo notebook, only edit the contents within the function, and marimo will automatically handle adding the parameters and return statement of the function.

## Fundamentals

- Marimo cells form a directed acyclic graph. Modules, functions, classes, and variables that a cell depends on is represented as parameters. The return value of a cell is exposed to other cells that depend on it.
- A variable cannot be reassigned across cells, but can be reassigned within the cell it is declared in.
- Local variables not used in other cells should be prefixed with an underscore. Variables declared in `for`, `with`, `except`, and `match` should use the underscore prefix whenever possible.
- A bare expression on the second-to-last line of a cell is treated as the output of the cell, similar to a Jupyter notebook.
- Global imports, constants and variables should be defined in cells, or setup cells (`with app.setup()`) if applicable.
- Builtin-objects, arrays, tensors, dataframes, and plots work similarly to Jupyter notebooks, no extra API is required.
- Marimo is abbreviated as `mo` by convention.

## References

- When initializing a marimo notebook, check the template at [init_marimo.py](examples/init_marimo.py).
- For UI widgets and layouts, see [ui.md](docs/ui.md).
- For dataframes and SQL queries, see [data.md](docs/data.md).
- For visualization, see [viz.md](docs/viz.md).
- Some useful APIs:
  - `mo.md(text)` - display markdown
  - `mo.stop(predicate, output=None)` - stop execution conditionally if `predicate` is true.
  - `mo.output.append(value)` - append to the output when it is not the bare expression
  - `mo.output.replace(value)` - replace the output when it is not the bare expression
  - `mo.Html(html)` - display HTML
  - `mo.image(image)` - display an image

## Additional Resources

- [A few examples](examples/examples.md) for interactive usages.
- Refer to [marimo API docs](https://docs.marimo.io/).
