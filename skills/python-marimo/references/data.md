# Marimo Data Science

Marimo is compatible with multiple data science libraries, including polars and duckdb.

## Best Practices

- Always prefer polars over pandas for data manipulation.
- If a dataframe should be interactively filtered, wrap it in `mo.ui.table(<df>)`, and the filtered dataframe can be accessed via `.value`.
- DuckDB SQL queries should be written as `mo.sql(f"""<sql>""")`.
