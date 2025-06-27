from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Scikit-learn + XGBoost
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

class PredictionPage(QtWidgets.QWidget):
    def __init__(self, df, selected_domain):
        super().__init__()
        self.df = df
        self.selected_domain = selected_domain
        self.setWindowTitle(f"Prédictions pour {selected_domain} - 2025-2026")
        self.resize(1000, 500)

        self.figure = plt.Figure(figsize=(10, 4))
        self.canvas = FigureCanvas(self.figure)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.canvas)

        self.plot_predictions()

    def plot_predictions(self):
        future_months = pd.date_range(
            "2025-06-01", "2026-01-01", freq="MS"
        )
        future_months_str = future_months.strftime("%Y-%m").tolist()

        axes = self.figure.subplots(1, 2)
        regions = ["National", "International"]
        colors = ["#2a9d8f", "#e76f51"]

        for ax, region, color in zip(axes, regions, colors):
            df_filtered = self.df[
                (self.df["NOM_DOMAINE"] == self.selected_domain)
                & (self.df["SITE_TYPE"] == region)
            ].copy()

            df_filtered["DATE"] = pd.to_datetime(df_filtered["MOIS"], format="%Y-%m")
            df_filtered.sort_values("DATE", inplace=True)

            top_specialties = (
                df_filtered[df_filtered["ANNEE"] == "2025"]
                .groupby("NOM_SPECIALITE")["NOMBRE_OFFRES"]
                .sum()
                .sort_values(ascending=False)
                .head(3)
                .index.tolist()
            )

            width = 0.2
            x = np.arange(len(future_months))

            for idx, speciality in enumerate(top_specialties):
                df_spec = df_filtered[df_filtered["NOM_SPECIALITE"] == speciality]

                if df_spec.empty:
                    continue

                df_spec.sort_values("DATE", inplace=True)
                X = np.arange(len(df_spec)).reshape(-1, 1)  # time indices
                y = df_spec["NOMBRE_OFFRES"].values

                # ✅ Scikit-learn pipeline with scaler + XGB
                model = Pipeline(
                    steps=[
                        ("scaler", StandardScaler()),  # scale features
                        ("xgb", XGBRegressor(
                            n_estimators=100,
                            learning_rate=0.1,
                            max_depth=3,
                            random_state=42,
                        )),
                    ]
                )
                model.fit(X, y)

                future_X = np.arange(len(df_spec), len(df_spec) + len(future_months)).reshape(
                    -1, 1
                )
                predicted_values = model.predict(future_X).astype(int)

                ax.bar(
                    x + idx * width,
                    predicted_values,
                    width=width,
                    label=speciality,
                )

            ax.set_xticks(x + width)
            ax.set_xticklabels(future_months_str, rotation=45, ha="right")
            ax.set_title(f"📈 Prédiction - {region}")
            ax.set_ylabel("Offres Prédites")
            ax.legend()

        self.figure.tight_layout()
        self.canvas.draw()
