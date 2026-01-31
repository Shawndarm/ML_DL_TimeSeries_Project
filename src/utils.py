


import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import seasonal_decompose, DecomposeResult 


def plot_seasonal_decompose(result: DecomposeResult, title="Décomposition Saisonnière"):
    return (
        make_subplots(
            rows=4,
            cols=1,
            subplot_titles=["Observé (Observed)", "Tendance (Trend)", "Saisonnalité (Seasonal)", "Résidus (Residuals)"],
        )
        .add_trace(
            go.Scatter(x=result.observed.index, y=result.observed, mode="lines", name="Observé"),
            row=1, col=1,
        )
        .add_trace(
            go.Scatter(x=result.trend.index, y=result.trend, mode="lines", name="Tendance", line=dict(color='orange')),
            row=2, col=1,
        )
        .add_trace(
            go.Scatter(x=result.seasonal.index, y=result.seasonal, mode="lines", name="Saisonnalité", line=dict(color='green')),
            row=3, col=1,
        )
        .add_trace(
            go.Scatter(x=result.resid.index, y=result.resid, mode="markers", name="Résidus", marker=dict(color='gray', size=2)),
            row=4, col=1,
        )
        .update_layout(
            height=900, 
            title=title, 
            margin=dict(t=100), 
            title_x=0.5, 
            showlegend=False
        )
    )



