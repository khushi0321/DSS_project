import subprocess
import sys
from pathlib import Path

NOTEBOOKS = [
    "01_data_loading_eda.ipynb",
    "02_data_cleaning.ipynb",
    "03_demand_forecasting.ipynb",
    "04_customer_segmentation.ipynb",
    "05_supplier_scorecard.ipynb",
    "06_inventory_alerts.ipynb",
    "07_model_comparison.ipynb",
    "08_supplier_score_with_returns.ipynb",
]

notebook_dir = Path("notebooks")

for nb in NOTEBOOKS:
    nb_path = notebook_dir / nb
    print(f"Running {nb} ...")
    result = subprocess.run([
        "jupyter", "nbconvert", "--to", "notebook", "--execute",
        "--inplace", str(nb_path)
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FAILED: {nb}")
        print(result.stderr)
        sys.exit(1)
    print(f"Done: {nb}")

print("\nAll notebooks executed successfully. CSV outputs refreshed.")