# Marimo UI

Marimo provides interactive widgets (UI elements) and layouts to create interactive notebooks, dashboards, and apps.

## Fundamentals

- Widgets trigger cell updates when their values change. No need for explicit callbacks.
- Widget values are accessed through `.value` attribute, but cannot be accessed in the same cell where the widget is declared.
- Use `mo.hstack()`, `mo.vstack()`, and `mo.tabs()` to create layouts for better organization of widgets.

## References

### Widgets

- `mo.ui.button(value=None, kind='primary')`
- `mo.ui.run_button(label=None, tooltip=None, kind='primary')`
- `mo.ui.checkbox(label='', value=False)`
- `mo.ui.date(value=None, label=None, full_width=False)`
- `mo.ui.dropdown(options, value=None, label=None, full_width=False)`
- `mo.ui.file(label='', multiple=False, full_width=False)`
- `mo.ui.number(value=None, label=None, full_width=False)`
- `mo.ui.radio(options, value=None, label=None, full_width=False)`
- `mo.ui.refresh(options: List[str], default_interval: str)`
- `mo.ui.slider(start, stop, value=None, label=None, full_width=False, step=None)`
- `mo.ui.range_slider(start, stop, value=None, label=None, full_width=False, step=None)`
- `mo.ui.table(data, columns=None, selection="multi", sortable=True, filterable=True)`
- `mo.ui.text(value='', label=None, full_width=False)`
- `mo.ui.text_area(value='', label=None, full_width=False)`
- `mo.ui.data_explorer(df)`
- `mo.ui.dataframe(df)`
- `mo.ui.plotly(plotly_figure)`
- `mo.ui.tabs(elements: dict[str, mo.ui.Element])`
- `mo.ui.array(elements: list[mo.ui.Element])`
- `mo.ui.form(element: mo.ui.Element, label='', bordered=True)`

Check the [API reference](https://docs.marimo.io/api/inputs/) for further details.

### Layouts

- `mo.hstack(elements)` - stack elements horizontally
- `mo.vstack(elements)` - stack elements vertically
- `mo.tabs(elements)` - create a tabbed interface

Check the [API reference](https://docs.marimo.io/api/layouts/) for additional complex layouts and further details.
