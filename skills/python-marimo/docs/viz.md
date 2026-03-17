# Marimo Visualization

Marimo is compatible with multiple visualization libraries, including matplotlib, seaborn, and altair.

## Best Practices

- For matplotlib and seaborn, use `plt.gca()`, or the figure/axes object directly as the output expression.
- For altair, use the chart object or `.interactive()` directly as the output expression.
- Use underscore prefix for intermediate variables. Always use `_fig`, `_ax`, `_grid`, `_chart` for visualization objects to avoid cross-cell name conflicts.
