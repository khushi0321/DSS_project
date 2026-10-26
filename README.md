# AI-Powered Decision Support System for a Mobile Spare (Display) Parts Wholesale Business

**Purpose of this file.** This README is a complete, self-contained briefing on the project. It is written so that a report-writing tool (for example Antigravity) can read it together with the project ZIP and produce the **final Major Project Report, chapter by chapter, in the university format**, without inventing facts. Everything marked **[FACT]** has been verified from the project work. Everything marked **[VERIFY]** must be checked against the files in the ZIP before it is written into the report. Everything marked **[PLACEHOLDER]** needs information that only the student can supply.

---

## 0. Instructions to the report-writing tool (read first)

1. **Write the report from this README plus the ZIP.** Read the notebooks, output CSVs and dashboard file in the ZIP and use their real numbers. If a number in this README disagrees with the ZIP, the ZIP wins, but state the data window it refers to (see Section 17).
2. **Do not fabricate anything.** No invented results, citations, user studies, interviews, benchmarks, timings, accuracy figures, or screenshots. If something was not done, say so (Section 12 lists what was not done).
3. **Disclose that the dataset is synthetic** wherever results are reported. Results demonstrate that the pipeline works; they are not findings about a real business.
4. **Reach about 100 pages through depth, not padding.** Section 15 gives a page budget per chapter and lists legitimate ways to add depth (cell-by-cell notebook walkthroughs, fuller tables, more exploratory plots computed from the real data, deeper explanation of each technique, fuller test tables). Do not repeat paragraphs, add generic textbook filler, or invent content to hit a page count. If the honest content only supports fewer pages, say so rather than inflate.
5. **Use only real references.** Section 14 lists references already verified for this project. You may add more only if you are certain they exist and can give correct bibliographic details; otherwise omit them. Never invent DOIs.
6. **Follow the university format** summarised in Section 3 (fonts, spacing, margins, numbering, front matter, chapters, appendices, APA 7th referencing).
7. **Third-person, academic, past tense** for work done ("the system was implemented", "the author"). The student is "the author".
8. **Include the AI-assistance declaration** (Section 2) in the Acknowledgement and Appendix J.
9. Keep all numbers consistent across chapters, tables, figures and the abstract.
10. Leave clearly marked placeholders only for the items in Section 18; do not leave stray template text.

---

## 1. One-paragraph project summary [FACT]

Small wholesalers of mobile spare (display) parts keep their accounts in Tally, which records transactions but does not forecast demand, rank customers or suppliers, or warn about stock-outs. This project builds a decision support system (DSS) that takes the wholesaler's structured data (seven entities exported to a workbook) and produces four analytical outputs: a **30-day demand forecast** (six models compared, SARIMA selected), **customer segments** (RFM + K-Means, four segments), a **supplier composite score** (on-time delivery, cost, return rate), and **inventory reorder alerts** (stock, reorder level, recent demand velocity). Results are presented in a **six-page Power BI dashboard** with a landing page. The real business's Tally data was not available within the project period, so the system was developed on a **synthetic dataset** built around an authentic mobile-parts catalogue. The system is a **tested local prototype, not a deployed service**.

---

## 2. Student, guide and submission details

| Item | Value |
|---|---|
| Student | **Khushi Hemin Shah** |
| Enrollment number | **25IC03CS026** |
| Programme | M.Sc. Computer Science (Data Science & Machine Learning) — written on reports as "M.Sc. Computer Science (DS / ML)" |
| University / School | P P Savani University, Surat, Gujarat — School of Engineering |
| Project guide (mentor) | **Mr. Suman Pandit** — [PLACEHOLDER: designation] |
| Student email / phone | 25IC03CS026@PPSU.AC.IN / 7573086899 (appear on progress reports; not required in the final report) |
| Project period | 08-06-2026 to 03-10-2026 |
| Submission month/year | October 2026 |
| Project type | Individual project (no group contribution statement needed) |
| Report title | AI-Powered Decision Support System for a Mobile Spare (Display) Parts Wholesale Business |
| GitHub repository | https://github.com/khushi0321/DSS_project (raw and processed data folders are git-ignored, so the dataset is **not** in the repository) |

**AI-assistance declaration (must appear in Acknowledgement and Appendix J).** An AI assistant (Claude, developed by Anthropic) was used during the project for drafting and debugging code, generating diagrams, and planning and drafting the progress reports and the report. All code was executed and all results were produced on the author's own machine, and the report content was reviewed with the project guide. The student must confirm this wording matches the university's AI policy.

---

## 3. University report format (summary of the supplied format document)

The university supplied *PPSU MCA / M.Sc. Major Project Report Format*. Key rules:

- **Page**: A4. **Margins**: left 1.25 in, right 1 in, top 1 in, bottom 1 in.
- **Font**: Times New Roman. Body 12 pt. **Chapter headings 14 pt bold.** Section headings 12–13 pt bold; sub-sections bold/italic.
- **Spacing**: 1.5 line spacing, justified body text. Single spacing is allowed in tables, captions, code listings and references.
- **Page numbering**: front matter in lower-case Roman numerals; main body (from Chapter 1) in Arabic numerals starting at 1; no number on the cover.
- **Front-matter order**: Cover/title page → Certificate (guide) → Declaration (student) → Acknowledgement → Abstract (with keywords) → Table of Contents → List of Figures → List of Tables → List of Abbreviations.
- **Numbering**: chapters "Chapter N"; sections 1.1, 1.2…; figures "Figure 5.3" and tables "Table 5.3" numbered by chapter; **figure captions below figures, table captions above tables**.
- **References**: APA 7th edition; in-text author–date citations; every cited source in the list and vice versa.
- **Length guidance in the format**: about 100–125 pages, quality over quantity; no padding.
- **Evidence expectation**: results must be traceable to the project's actual artefacts; no fabricated results.
- **Chapters** (section numbers must match):

| Chapter | Sections |
|---|---|
| 1 Introduction | 1.1 Background and Context · 1.2 Problem Statement · 1.3 Need and Motivation · 1.4 Aim and Objectives · 1.5 Scope of the Project · 1.6 Proposed Solution and Contribution · 1.7 Methodology Overview · 1.8 Organisation of the Report |
| 2 Literature Review and Existing-System Study | 2.1 Review Method and Sources · 2.2 Review of Related Work · 2.3 Comparative Summary · 2.4 Gap Analysis · 2.5 How This Project Addresses the Gap · 2.6 Chapter Summary |
| 3 System Analysis and Requirements | 3.1 Preliminary Investigation · 3.2 Study of the Existing System · 3.3 Proposed System and Expected Benefits · 3.4 Functional Requirements · 3.5 Non-Functional Requirements · 3.6 Hardware and Software Requirements · 3.7 Feasibility Study · 3.8 Assumptions, Constraints, Dependencies and Risks · 3.9 Software Requirements Specification Summary |
| 4 Project Planning and Methodology | 4.1 Development Methodology · 4.2 Project Phases and Deliverables · 4.3 Work Breakdown Structure · 4.4 Schedule (Gantt Chart) · 4.5 Task Dependencies (PERT-style Network) · 4.6 Roles and Responsibilities · 4.7 Risk Register · 4.8 Data Collection, Dataset Preparation and Ethics |
| 5 System Design | 5.1 Overall System Architecture · 5.2 Module Decomposition and Responsibilities · 5.3 Data Flow Diagrams · 5.4 Use-Case Diagram · 5.5 Activity Diagram · 5.6 Entity-Relationship Diagram · 5.7 Database Schema · 5.8 Input and Output Design · 5.9 Algorithms and Process Logic · 5.10 Security, Privacy, Validation, Backup and Access Control · 5.11 Design Decisions and Trade-offs |
| 6 Implementation | 6.1 Development Environment and Tool Versions · 6.2 Project Folder Structure and Configuration · 6.3 Module-wise Implementation · 6.4 Important Algorithms and Code Excerpts · 6.5 Database Implementation and Sample Records · 6.6 API and External-Service Integration · 6.7 Authentication, Validation and Error Handling · 6.8 Screenshots of the Working System · 6.9 Build, Run and Deployment Instructions |
| 7 Testing and Validation | 7.1 Test Strategy, Scope and Environment · 7.2 Module-level Testing · 7.3 Integration Testing · 7.4 System and User-Acceptance Testing · 7.5 Model Validation, Usability, Performance and Security Checks · 7.6 Test Results Summary and Defects Found · 7.7 Requirement Traceability |
| 8 Results, Discussion and Limitations | 8.1 Implemented Features and Evidence · 8.2 Results Against Each Objective · 8.3 Quantitative Evaluation · 8.4 Comparison with Baseline or Existing Method · 8.5 Interpretation of Results · 8.6 Limitations · 8.7 Mentor and User Feedback Incorporated |
| 9 Conclusion and Future Scope | 9.1 Summary of the Work · 9.2 Achievement of Objectives · 9.3 Key Contributions · 9.4 Learning Outcomes · 9.5 Future Scope and Recommendations · 9.6 Closing Remarks |
| References | APA 7th |
| Appendices | A Approved Project Synopsis · B Detailed SRS / Use-Case Descriptions · C Additional Diagrams · D Detailed Test Cases and Evidence · E User Manual · F Source Code and Repository · G Progress Reports Summary · H Questionnaires/Interviews/Consent (Not applicable) · I Group Contribution (Not applicable, individual project) · J Plagiarism Report and AI-Assisted Contribution Declaration |

A 73-page draft that already follows this format (cover, certificate, declaration, acknowledgement, abstract, contents, lists, 9 chapters, references, appendices A–J) is provided as `Final_Project_Report_Khushi.docx`. **Use it as the baseline and expand it** rather than starting over; keep its numbering, captions and cross-references consistent as you add content. Figures used by the draft are in `report_assets.zip`.

---

## 4. Project aim and objectives [FACT]

**Aim.** To design, implement and validate an AI-powered DSS that converts a mobile spare-parts wholesaler's transaction data into demand forecasts, customer segments, supplier scores and reorder alerts, presented through an interactive multi-page dashboard.

| ID | Objective | Status at submission |
|---|---|---|
| O1 | Forecast demand; compare six models (Linear Regression, Random Forest, XGBoost, ARIMA, SARIMA, Prophet) and select the best | Achieved — SARIMA selected on lowest RMSE |
| O2 | Segment customers with RFM + K-Means | Achieved — four labelled segments |
| O3 | Supplier Intelligence: score reliability, cost, quality | Achieved — composite score incl. returns |
| O4 | Flag products needing reorder | Achieved — inventory alerts |
| O5 | Unified seven-entity data schema | **Partially achieved** — designed and populated, but stored as Excel/CSV flat files, not a relational database |
| O6 | Integrated multi-page dashboard | Achieved — six pages, local prototype, not hosted |

Scope included: data loading/cleaning, daily demand aggregation, six-model comparison and 30-day forecast, RFM segmentation, supplier scoring with returns, inventory alerts, six-page Power BI dashboard, automated output validation, pipeline automation script.
Scope **excluded**: live Tally connection, relational database server, hosting or scheduled refresh, per-product forecasting, formal user study.

---

## 5. ZIP / repository layout [FACT, VERIFY against the ZIP]

```
DSS_Project/
  data/
    raw/         Mobile_Parts_Wholesale_Dataset.xlsx   (seven sheets; may be absent from git, include in ZIP)
    processed/   daily_demand.csv
  notebooks/
    01_data_loading_eda.ipynb
    02_data_cleaning.ipynb
    03_demand_forecasting.ipynb            (Prophet baseline)
    04_customer_segmentation.ipynb
    05_supplier_scorecard.ipynb            (basic scorecard)
    06_inventory_alerts.ipynb
    07_model_comparison.ipynb              (six models; SARIMA final forecast)
    08_supplier_score_with_returns.ipynb   (returns attribution + composite score)
    09_testing_validation.ipynb            (ten automated checks)
  reports/       demand_forecast.csv, customer_segments.csv, supplier_scorecard.csv,
                 inventory_alerts.csv, model_comparison.csv, test_results.csv
  dashboard/     DSS_Prototype.pbix
  scripts/ models/  (reserved, mostly empty)
  run_pipeline.py     runs notebooks 01–08 in order via nbconvert
  watch_and_run.py    watches data/raw for .xlsx changes and re-runs run_pipeline.py
  .gitignore          excludes data/raw/*, data/processed/*, *.pkl, .env, .ipynb_checkpoints, __pycache__
```

Execution-order note: notebook 03 writes a **baseline** `demand_forecast.csv` (Prophet); notebook 07 later **overwrites** the same file with the SARIMA forecast (same columns: date, predicted_qty, lower_bound, upper_bound). Likewise notebook 08 overwrites notebook 05's `supplier_scorecard.csv`. Order therefore matters.

---

## 6. Dataset (synthetic) [FACT]

**Why synthetic.** The business keeps accounts in Tally and did not provide data within the project timeline. A search of public data (Kaggle auto-parts dataset, generic smartphone sales datasets, wholesale-orders datasets, mobile-parts supplier websites) found no public transactional dataset for mobile-display-parts wholesale. A synthetic dataset was therefore generated with Python (Faker for names, NumPy/random for sampling, fixed seeds) around an authentic catalogue and realistic patterns. It is disclosed as synthetic throughout.

**Catalogue.** 37 handset models across 6 brands (Apple 8, Samsung 8, Xiaomi 6, Oppo 5, Vivo 5, Realme 5) × 12 part types (LCD Display Combo, OLED Display Combo, Touch Screen Digitizer, Battery, Charging Port Flex, Back Glass Panel, Camera Module (Rear), Camera Module (Front), Speaker Module, Microphone Flex, Power Button Flex, SIM Tray); 4–6 part types per model → **179 products**. Prices in INR scaled by brand and part type.

**Generation patterns.** Poisson daily order counts (base 9, ×1.35 in Oct–Dec, ×1.2 in May–Jun, ×0.85 in Jan–Feb); 1–3 lines per order; quantity 1–10; discount from {0,0,0,5,10}%; customers only order after their first-order date; purchase orders ≈70% on time, ≈30% 1–6 days late, recent ones pending; returns ≈3% of sales lines with realistic reasons; customers ≈75% Gujarat cities (Surat, Ahmedabad, Vadodara, Rajkot, Bhavnagar, Navsari, Valsad, Anand) and others Mumbai, Pune, Indore, Nagpur.

**Workbook sheets and sizes (original dataset, data to 29 Jun 2026)**

| Sheet | Rows | Key columns |
|---|---|---|
| Customers | 180 | customer_id (PK), customer_name, shop_type, city, state, first_order_date |
| Suppliers | 14 | supplier_id (PK), supplier_name, city, country, lead_time_days, payment_terms |
| Products | 179 | product_id (PK), product_name, brand, compatible_model, part_type, unit_price_inr, cost_price_inr |
| Sales_Transactions | 6,016 | order_id (PK, **unique per sales line**), customer_id (FK), product_id (FK), order_date, quantity, unit_price_inr, discount_pct, total_amount_inr, payment_mode |
| Inventory | 179 | product_id (FK, one row per product), warehouse_location, current_stock_qty, reorder_level, last_restock_date |
| Purchase_Orders | 298 | po_id (PK), supplier_id (FK), product_id (FK), order_date, quantity_ordered, unit_cost_inr, promised_delivery_date, actual_delivery_date (null for 6 pending), status |
| Returns_Complaints | 180 | return_id (PK), order_id (FK), product_id (FK), return_date, reason, resolved (Yes/No) |

Sales dates run **22 Jan 2025 → 29 Jun 2026 = 524 calendar days**. Relationships: Customers 1:N Sales; Products 1:N Sales; Products 1:1 Inventory; Suppliers 1:N Purchase_Orders; Products 1:N Purchase_Orders; Sales 1:N Returns; Products 1:N Returns. The only nulls are `actual_delivery_date` on the 6 pending purchase orders.

**Data extension used to demonstrate automation.** 1,912 additional synthetic sales lines covering **30 Jun 2026 → 29 Sep 2026** were generated (order_id range O900001 upwards to avoid collisions; product_ids P0001–P0179; customer_ids C0001–C0180; same seasonality logic) and appended to the Sales_Transactions sheet, then the pipeline was re-run. [VERIFY whether the ZIP's workbook and CSVs contain this extension; see Section 17.]

---

## 7. Pipeline, notebook by notebook [FACT unless marked]

**01_data_loading_eda** — loads the seven sheets with pandas (`pd.read_excel(path, sheet_name=...)`), prints shapes (customers 180×6, suppliers 14×6, products 179×7, sales 6016×9, inventory 179×5, purchase_orders 298×9, returns 180×6), dtypes and null counts, converts `order_date` to datetime, plots daily revenue trend (seasonality visible; early weeks sparse).

**02_data_cleaning** — groups sales by `order_date` (sum of quantity → `total_qty`, sum of `total_amount_inr` → `total_revenue`), reindexes to every calendar day with zero fill → **524 rows**; saves `data/processed/daily_demand.csv`. First rows: 2025-01-22 qty 16; the next days 0.

**03_demand_forecasting** — Prophet baseline (yearly + weekly seasonality) on `ds`,`y`; 30-day forecast; first forecast total shown on dashboard ≈ 3.32 K units.

**04_customer_segmentation** — snapshot date = max order date + 1 day; per customer: recency (days since last order), frequency (`nunique(order_id)`, i.e. sales lines), monetary (sum of `total_amount_inr`); **179 customers** (those who ordered); `StandardScaler`; `KMeans(n_clusters=4, random_state=42, n_init=10)`. Centroid means and labels:

| Cluster | Label | Customers | Recency (days) | Frequency | Monetary (INR) |
|---|---|---|---|---|---|
| 0 | High Value | 29 | 13.38 | 60.93 | 261,585.55 |
| 1 | Steady/Regular | 57 | 8.37 | 39.91 | 160,288.67 |
| 2 | New/Occasional | 70 | 13.63 | 17.07 | 65,361.46 |
| 3 | At Risk | 23 | 46.30 | 33.87 | 122,304.98 |

Sample rows: C0001 (1, 9, 19,979.00, New/Occasional); C0002 (6, 32, 141,835.50, Steady/Regular); C0003 (19, 10, 36,461.00, New/Occasional); C0004 (43, 59, 257,908.50, High Value); C0007 (44, 46, 168,090.50, At Risk). Saved to `reports/customer_segments.csv`. Cluster count k=4 chosen for interpretability; **not** validated with elbow/silhouette.

**05_supplier_scorecard** — excludes Pending POs; `on_time` = actual_delivery_date ≤ promised_delivery_date; per supplier: total_orders, on_time_pct, avg_unit_cost; merged with supplier name/country; saved to `reports/supplier_scorecard.csv` (basic version).

**06_inventory_alerts** — last 60 days of sales per product → `avg_daily_demand = qty_60d / 60`; `projected_30d_demand = avg_daily_demand × 30` (0 if no recent sales); merged with Inventory and Products; rule implemented with `numpy.select` (earlier version used row-wise `.apply`):
```
IF current_stock_qty <= reorder_level            -> "REORDER NOW - Below threshold"
ELIF projected_30d_demand > current_stock_qty    -> "REORDER SOON - Demand exceeds stock"
ELSE                                             -> "Stock OK"
```
Saved to `reports/inventory_alerts.csv`.

**07_model_comparison** — chronological split: **train = first 494 days (to 30 May 2026), test = last 30 days (31 May–29 Jun 2026)**. Regression models use features `day_num`, `day_of_week`, `month`. Models and settings: LinearRegression; RandomForestRegressor(n_estimators=200, random_state=42); XGBRegressor(n_estimators=200, learning_rate=0.05, random_state=42); ARIMA(order=(5,1,2)); SARIMAX(order=(1,1,1), seasonal_order=(1,1,1,7)); Prophet(yearly_seasonality=True, weekly_seasonality=True) retrained on the training window. Metrics: RMSE and MAPE (sklearn). Results saved to `reports/model_comparison.csv`. Then the **final SARIMA** is refitted on the full series, `get_forecast(steps=30)`, writing `date, predicted_qty, lower_bound, upper_bound` to `reports/demand_forecast.csv`.

**08_supplier_score_with_returns** — returns link to `order_id` (a sales line), not to suppliers, so each product is mapped to its **most frequent supplier** via Purchase_Orders (mode of supplier_id); returns are counted per supplier; `return_rate_pct = return_count / total_units_purchased × 100` (guarded: 0.0 if units = 0); composite: `on_time_score = on_time_pct`; `cost_score = 100 − minmax(avg_unit_cost)×100`; `quality_score = 100 − minmax(return_rate_pct)×100`; **composite = 0.5·on_time + 0.3·cost + 0.2·quality** (weights are judgemental). Saved to `reports/supplier_scorecard.csv` with columns including on_time_pct, avg_unit_cost, total_orders, return_rate_pct, composite_score.

**09_testing_validation** — ten structural checks (Section 10); writes `reports/test_results.csv`.

Error-handling additions: a `safe_read_excel` function (raises clear error if file missing/sheet unreadable; warns if empty); division guard for return rate; `fillna(0)` for suppliers with no returns and products with no recent sales; Pending POs excluded.

---

## 8. Results bank [FACT — original data window to 29 Jun 2026]

### 8.1 Forecast model comparison (30-day hold-out)

| Model | RMSE (units/day) | MAPE (%) | Rank RMSE | Rank MAPE |
|---|---|---|---|---|
| SARIMA | 40.66 | 32.96 | 1 | 4 |
| Linear Regression | 41.00 | 32.89 | 2 | 3 |
| Prophet | 41.41 | 39.10 | 3 | 5 |
| ARIMA | 41.60 | 31.55 | 4 | 1 |
| Random Forest | 45.70 | 32.77 | 5 | 2 |
| XGBoost | 51.03 | 39.22 | 6 | 6 |

SARIMA chosen for lowest RMSE (RMSE penalises large misses, relevant to stock-outs) and explicit weekly seasonality. Relative RMSE improvement of SARIMA: 0.8% vs Linear Regression, 1.8% vs Prophet, 2.3% vs ARIMA, 11.0% vs Random Forest, 20.3% vs XGBoost. The top four are within ≈2.3%; **a single 30-day window cannot establish significance**. No naive/seasonal-naive baseline was computed. Plausible reasons (interpretation, label as such): synthetic Poisson daily noise sets an error floor; tree models received only three calendar features and no lags; Prophet has < 2 yearly cycles of history (≈17 months); MAPE unstable near zero. The SARIMA 30-day forecast shown on the dashboard totals **≈ 3.64 K units (≈121/day)** with upper bound ≈185–195 and lower bound ≈55–58 units/day (from the dashboard screenshot).

### 8.2 Customer segments
Sizes: New/Occasional 70 (39.1%), Steady/Regular 57 (31.8%), High Value 29 (16.2%), At Risk 23 (12.8%). At Risk is distinguished mainly by recency (≈46 days vs 8–14 for other segments) despite substantial past frequency (≈34) and spend.

### 8.3 Supplier scorecard (final, sorted by composite)

| Supplier | On-time % | Avg unit cost (INR) | Orders | Return rate % | Composite |
|---|---|---|---|---|---|
| Oommen Ltd Trading Co. | 68.4 | 475.94 | 19 | 0.14 | 77.0 |
| Goda-Anand Trading Co. | 71.4 | 354.42 | 21 | 0.29 | 76.5 |
| Peri, Grewal and Bhavsar Trading Co. | 60.0 | 317.60 | 25 | 0.26 | 73.8 |
| Gala, Agate and Ravi Trading Co. | 75.0 | 406.02 | 16 | 0.35 | 73.3 |
| Toor Inc Electronics | 63.6 | 524.70 | 22 | 0.13 | 73.1 |
| Das, Misra and Bava Electronics | 69.0 | 438.36 | 29 | 0.27 | 72.7 |
| Sekhon-Radhakrishnan Electronics | 73.9 | 412.95 | 23 | 0.35 | 72.4 |
| Sathe Ltd Trading Co. | 78.9 | 518.96 | 19 | 0.32 | 71.9 |
| Sarma LLC Electronics | 75.0 | 523.12 | 16 | 0.37 | 67.4 |
| Karpe and Sons Trading Co. | 63.6 | 584.84 | 22 | 0.22 | 66.2 |
| Dass, Magar and Dugar Trading Co. | 76.0 | 707.21 | 25 | 0.33 | 62.0 |
| Varughese-Kata Trading Co. | 75.0 | 460.86 | 16 | 0.55 | 61.5 |
| Issac, Bawa and Rau Trading Co. | 61.1 | 491.40 | 18 | 0.38 | 61.3 |
| Sachar-Sen Electronics | 66.7 | 1,028.00 | 21 | 0.27 | 46.7 |

Totals/means: 292 orders; mean on-time 69.83%; mean avg unit cost 517.46. Insight: Sathe has the highest on-time rate (78.9%) but ranks 8th on composite; Oommen ranks 1st with 68.4% on-time thanks to the lowest-tier return rate and mid-range cost; Sachar-Sen is last because its cost (≈2× the mean) dominates. Note the return rate divides returned sales **lines** by **units** purchased (mixed units — a stated limitation).

### 8.4 Inventory alerts
179 products: **144 Stock OK, 34 REORDER NOW, 1 REORDER SOON** → 35 flagged (19.6%). Two products at zero stock: P0044 Galaxy A32 Speaker Module (Samsung) and P0097 POCO X3 Speaker Module (Xiaomi). The single REORDER SOON item is iPad 9th Gen OLED Display Combo (stock 23, reorder level 21, projected 30-day demand 23.5). Other sample rows: A54 Battery (Oppo) stock 1, reorder level 39, projected 32.0; V23 Back Glass Panel (Vivo) stock 20, level 25, projected 32.0.

### 8.5 Overview KPIs
Total revenue 24.11 M INR; total orders (= sales lines) 6,016; customers 180; average order value 4.01 K INR. Highest city revenue: Nagpur (≈3.3 M), then Vadodara, Navsari, Bhavnagar, Ahmedabad, Rajkot, Pune, Valsad, Anand, Surat, Mumbai, Indore. Top product by revenue: iPhone 11 OLED display combo (see chart; verify from data).

---

## 9. Dashboard (Power BI, `dashboard/DSS_Prototype.pbix`) [FACT]

Six pages: **Home**, **Overview**, **Demand Forecast**, **Customer Segmentation**, **Supplier Performance**, **Inventory Alerts**. Navigation: Home has five colour-graduated cards with arrow icons (shape + icon grouped, one page-navigation action); every other page has a back arrow to Home. Data: the four module CSVs plus Sales_Transactions, Customers and Products sheets from the workbook.

| Page | Contents |
|---|---|
| Home | Title and one-line description; five navigation cards (each with a one-line description); date slicer (order date); two KPI cards (Total Revenue, Total Orders); donut of customer segments |
| Overview | Four KPI cards (Total Revenue 24.11M, Total Orders 6.016K, Total Customers 180, Avg Order Value 4.01K — DAX `DIVIDE(SUM(total_amount_inr), DISTINCTCOUNT(order_id))`); Historical Sales Trend line; Top 10 Products by Revenue bar (Top-N filter); Sales by City column; colours differentiated (purple KPIs, orange trend, green ranking) |
| Demand Forecast | Date slicer (default last 30 days), KPI "Next 30-Day Total Projected Demand" (3.64K, SARIMA), line chart with Predicted/Upper/Lower; explanatory text on bounds |
| Customer Segmentation | Column chart of four segments with data labels; RFM detail table (renamed headers, "Don't summarize"); explanation of each segment |
| Supplier Performance | Table (supplier, on-time, avg cost, orders, return rate, composite) sorted by composite with conditional formatting; "Supplier Composite Score" bar chart; text describing 50/30/20 weights. A scatter plot was considered and **deliberately dropped** for consistency |
| Inventory Alerts | Alert table filtered to exclude "Stock OK" (35 rows); KPI "Products Needing Reorder = 35"; alert-status donut; explanatory text on REORDER NOW / REORDER SOON |

Fixes/lessons (useful for the defect log): Power BI auto date hierarchy aggregated daily data to years (fixed with plain date field / disabling auto date-time); order_date imported as serial number (fixed data type); OLE DB/ODBC refresh errors from file locks/permissions; stale Power Query schema after new CSV columns (fixed by deleting/re-adding the source); arrow icons not clickable (grouped with shape); table totals summing percentages (changed aggregation); alert-table filter lost then re-applied. Mentor feedback drove: prototype early; navigation via landing page instead of tab scrolling; consistent two-visual-plus-text layout; clean colours and fonts.

**Screenshots available** (in `report_assets.zip`): ui_home, ui_overview, ui_demand, ui_customer, ui_supplier, ui_inventory. If you can open the .pbix or have newer screenshots, prefer those; otherwise use these.

---

## 10. Testing [FACT]

**Ten automated checks (notebook 09) — all PASS:** (TC-01) forecast has no negative predicted demand; (TC-02) lower_bound ≤ upper_bound for all rows; (TC-03) forecast covers exactly 30 days; (TC-04) segment counts sum to 179; (TC-05) no customer in more than one segment; (TC-06) on-time % between 0 and 100; (TC-07) composite score between 0 and 100; (TC-08) all 14 suppliers present; (TC-09) every REORDER NOW row has stock ≤ reorder level; (TC-10) no duplicate products in the alert list. Console output ended with `status PASS 10`. Caveat: TC-04 and TC-08 use hard-coded expected counts (179, 14) tied to the original dataset.

**Integration tests:** IT-01 run notebooks 01–08 via `run_pipeline.py` from the project root (first failed when run from `notebooks/` folder and when saved as .ipynb instead of .py); IT-02 Power BI loads the CSVs; IT-03 SARIMA forecast replaces baseline without dashboard redesign; IT-04 supplier scorecard new columns appear after Power Query reset; IT-05 pipeline re-run on extended workbook (1,912 rows).

**User-acceptance matrix** (criteria: page loads; navigation works; slicers filter; KPI spot-check vs raw data; no truncation/overlap; conditional formatting) — Home: P,P,P,P,P,N/A · Overview: P,P,N/A,P,P,N/A · Demand Forecast: P,P,P,P,P,N/A · Customer Segmentation: P,P,N/A,N/A,P,N/A · Supplier Performance: P,P,N/A,N/A,P,P · Inventory Alerts: P,P,N/A,P,P,P. Product names truncated in the top-products chart are readable on hover (accepted).

**Defect log (D-01…D-10)** is in Section 9 and in Chapter 7 of the draft. No formal usability study, performance benchmark or security test was done — say so.

---

## 11. Automation and deployment status [FACT]

- `run_pipeline.py` (run from project root, not from `notebooks/`) executes notebooks 01–08 in order with `jupyter nbconvert --to notebook --execute --inplace`, stops at the first failure. Notebook 09 (validation) is run separately. [VERIFY whether the student later added 09 to the list.]
- `watch_and_run.py` uses `watchdog` to watch `data/raw` and re-run the pipeline when an `.xlsx` is modified; works only while the terminal stays open.
- Power BI still needs a manual **Refresh**.
- **Deployment status:** local prototype only — static workbook, on-demand/file-triggered pipeline, Power BI Desktop file; **not hosted, not live-fed**. True deployment would need a live/scheduled data feed (Tally export/ODBC/XML or database), the pipeline on a server on a schedule, and publishing to Power BI Service with a data gateway for scheduled refresh. The student **does not** claim deployment.
- Tally integration options studied but not implemented: manual report export (chosen), ODBC driver, XML-over-HTTP interface.

---

## 12. Design decisions, limitations, and what was NOT done

**Decisions & trade-offs:** flat files vs MySQL/PostgreSQL (speed to validate analytics; matches Tally export); Power BI vs Streamlit (business-friendly visuals; originally planned Streamlit); SARIMA over Prophet (lowest RMSE); k=4 segments (interpretable); weights 0.5/0.3/0.2 (judgement: delivery > cost > quality); demand-velocity proxy instead of per-product forecasts (179 SKUs out of scope); two visuals + text per page (consistency).

**Limitations (must be reported honestly):** synthetic data; aggregate (all-products) forecast only; single 30-day hold-out, no rolling-origin validation, no hyper-parameter tuning, no significance test, no naive baseline; MAPE instability near zero; k not validated by an index; supplier weights not calibrated; return attribution to most-frequent supplier and mixed-unit return rate; `order_id` is unique per sales line so "orders" and RFM frequency count lines; inventory snapshot generated independently of sales; reorder level stored not computed; alerts use recent velocity not the forecast; flat-file storage; no hosting/live data; tests check structure not real-world correctness; no formal user study.

**Not done (do not claim):** relational database; live Tally connection; per-product forecasting; Croston/intermittent-demand methods (future work); formal user testing; performance benchmarking; Power BI Service publishing.

**Future scope:** real Tally data (ODBC/XML); relational DB with enforced keys; per-product/family forecasting with intermittent-demand methods (Croston 1972; Syntetos & Boylan 2005); rolling-origin validation, naive baseline, tuned SARIMA orders, lag features; cluster validation and AHP-calibrated weights; computed reorder point/safety stock (Silver et al., 2017); scheduled deployment on Power BI Service with gateway and access control; natural-language Q&A for non-technical users; structured usability study.

---

## 13. Project management facts [FACT]

- **Methodology:** iterative–incremental with weekly mentor review; ten progress reports (individual project).
- **Planned phase windows (from mentor schedule):** (1) 08 Jun–16 Jul title/problem/literature/scope; (2) 17–23 Jul requirements, feasibility, tech selection, methodology; (3) 24 Jul–06 Aug architecture, schema, module planning, environment; (4) 07–13 Aug UI/prototype, initial modules; (5) 14–27 Aug module implementation and code review; (6) 28 Aug–03 Sep integration, testing strategy, result analysis; (7) 04–10 Sep testing, error handling, optimisation; (8) 11–17 Sep final demonstration, documentation; (9) 18 Sep–03 Oct final evaluation, deployment status, final report.
- **Progress reports (scheduled dates):** 1 (16 Jul) title/objectives; 2 (23 Jul) requirements/feasibility/tech; 3 (06 Aug) architecture/DB design/modules/environment + prototype; 4 (13 Aug) inventory alerts + five-page dashboard; 5 (20 Aug) six-model comparison, SARIMA, diagrams; 6 (27 Aug) landing page/navigation, presentation pass; 7 (03 Sep) supplier returns integration, composite score; 8 (10 Sep) testing, error handling, optimisation; 9 (17 Sep) final demonstration prep, objective review; 10 (24 Sep) final evaluation, deployment status, innovation, final report. Actual reporting periods written on the reports may differ slightly.
- **Risk register:** real data unavailable (occurred, mitigated by synthetic data); short history for forecasting (occurred); Power BI refresh/cached-schema issues (occurred, resolved); notebook order dependencies (occurred, resolved); presentation judged unclear (addressed after feedback); scope creep (controlled).
- **Mentor feedback incorporated:** early prototype; development on a dataset resembling real data; reports to describe what was actually built rather than a fixed checklist; landing-page navigation; no video references (use documentation/academic sources).
- **Innovation points the student may claim (all true):** purpose-built authentic-catalogue synthetic dataset disclosed transparently; three-signal supplier composite with returns attributed through purchase history; landing-page dashboard redesigned from usability feedback; structural automated test suite for a statistical pipeline; honest achievement-of-objectives mapping with the partially met objective disclosed.

---

## 14. Verified reference bank (APA 7th) — use these; extend only with certain sources

- Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time series analysis: Forecasting and control* (5th ed.). Wiley.
- Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324
- Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785–794). ACM. https://doi.org/10.1145/2939672.2939785
- Croston, J. D. (1972). Forecasting and stock control for intermittent demands. *Operational Research Quarterly, 23*(3), 289–303.
- Dickson, G. W. (1966). An analysis of vendor selection systems and decisions. *Journal of Purchasing, 2*(1), 5–17.
- Fader, P. S., Hardie, B. G. S., & Lee, K. L. (2005). RFM and CLV: Using iso-value curves for customer base analysis. *Journal of Marketing Research, 42*(4), 415–430.
- Few, S. (2013). *Information dashboard design: Displaying data for at-a-glance monitoring* (2nd ed.). Analytics Press.
- Ho, W., Xu, X., & Dey, P. K. (2010). Multi-criteria decision making approaches for supplier evaluation and selection: A literature review. *European Journal of Operational Research, 202*(1), 16–24.
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and practice* (3rd ed.). OTexts. https://otexts.com/fpp3/
- Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. *International Journal of Forecasting, 22*(4), 679–688.
- Kraljic, P. (1983). Purchasing must become supply management. *Harvard Business Review, 61*(5), 109–117.
- MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. In L. M. Le Cam & J. Neyman (Eds.), *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability* (Vol. 1, pp. 281–297). University of California Press.
- Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2018). Statistical and machine learning forecasting methods: Concerns and ways forward. *PLOS ONE, 13*(3), Article e0194889. https://doi.org/10.1371/journal.pone.0194889
- McKinney, W. (2010). Data structures for statistical computing in Python. In *Proceedings of the 9th Python in Science Conference* (pp. 56–61).
- Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830. (In the reference list write out the authors per APA 7.)
- Power, D. J. (2002). *Decision support systems: Concepts and resources for managers*. Quorum Books.
- Seabold, S., & Perktold, J. (2010). Statsmodels: Econometric and statistical modeling with Python. In *Proceedings of the 9th Python in Science Conference* (pp. 92–96).
- Silver, E. A., Pyke, D. F., & Thomas, D. J. (2017). *Inventory and production management in supply chains* (4th ed.). CRC Press.
- Syntetos, A. A., & Boylan, J. E. (2005). The accuracy of intermittent demand estimates. *International Journal of Forecasting, 21*(2), 303–314.
- Taylor, S. J., & Letham, B. (2018). Forecasting at scale. *The American Statistician, 72*(1), 37–45. https://doi.org/10.1080/00031305.2017.1380080
- Microsoft. (n.d.). *Power BI documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/power-bi/
- NumPy Developers. (n.d.). *NumPy documentation*. https://numpy.org/doc/
- Open projects reviewed (cite only for what their own descriptions say): ycc710. (n.d.). *AI-Procurement-Operating-System* [Source code]. GitHub. https://github.com/ycc710/AI-Procurement-Operating-System · ajitsingh98. (n.d.). *Inventory-Management-Demand-Using-Time-Series-Analysis-and-Forecasting* [Source code]. GitHub. https://github.com/ajitsingh98/Inventory-Management-Demand-Using-Time-Series-Analysis-and-Forecasting · International Journal of Engineering Research & Technology. (2026). *AI-driven inventory and demand forecasting system with automated supplier communication and trend analysis*. https://www.ijert.org/ai-driven-inventory-and-demand-forecasting-system-with-automated-supplier-communication-and-trend-analysis-ijertv15is042201
- Dataset: Shah, K. H. (2026). *Synthetic mobile spare (display) parts wholesale dataset* [Data set]. Generated by the author for this project; available from the author on request.

What the sources support (for the literature review): Box et al./Hyndman — ARIMA/SARIMA and hold-out evaluation; Taylor & Letham — Prophet for business series with seasonality; Breiman, Chen & Guestrin — tree-based regressors; Makridakis et al. — statistical methods often more accurate and cheaper than ML on the series studied; Hyndman & Koehler — percentage errors unstable near zero; Croston, Syntetos & Boylan — intermittent demand; MacQueen/Pedregosa — K-Means; Fader et al. — RFM variables; Dickson — quality, delivery, performance history rank top vendor criteria; Ho et al. — quality, delivery, price are the most-used supplier criteria; Kraljic — portfolio view of purchasing; Silver et al. — reorder-point policies; Power — DSS definition; Few — glanceable dashboards.

---

## 15. Chapter-by-chapter writing plan and page budget (target ≈ 100–115 pages total)

| Part | Target pages | Legitimate ways to add depth (all from real project material) |
|---|---|---|
| Front matter (cover, certificate, declaration, acknowledgement, abstract, contents, lists, abbreviations) | ~11 (Roman) | Standard; keep abstract ≈250–300 words with real numbers |
| Ch 1 Introduction | 6–8 | Expand domain background (display assemblies, model compatibility, Tally's role), fuller problem decomposition (three decisions), objective table with verification evidence |
| Ch 2 Literature review | 10–14 | One subsection per technique with how each is used here; comparison table of 10–14 sources; deeper discussion of existing open systems and the Kaggle/GitHub search; gap analysis. Use only Section 14 sources unless certain |
| Ch 3 Analysis | 9–12 | Stakeholder needs, existing-system workflow, 12 FRs and 6+ NFRs with acceptance criteria, environment tables, four feasibility dimensions, assumptions/risks, SRS summary |
| Ch 4 Planning | 7–9 | Phases table, WBS tree, Gantt, PERT, risk register, **detailed dataset generation methodology** (catalogue, distributions, seasonality, supplier delay model, return model, seeds, validation of the dataset), ethics |
| Ch 5 Design | 13–17 | Layered architecture with explanation of each layer and interface; module specification; DFD, use cases with descriptions, activity diagram, ER, relationships and full data dictionary; page-by-page UI design; **each algorithm explained with formulas and worked examples** (e.g., worked RFM for C0004, worked composite score for one supplier, worked alert decision for two products); security/privacy/backup; decisions table |
| Ch 6 Implementation | 15–20 | **Cell-by-cell walkthrough of each notebook** with purpose, code excerpt, and the real printed output; folder structure; sample records from each output file; Power BI build details (relationships, measures, filters, formatting); error handling; full screenshot set with explanations; run instructions |
| Ch 7 Testing | 9–12 | Strategy; full TC table with expected vs actual; integration tests; UAT matrix with criterion definitions; model validation configuration; defect log with cause/fix; traceability matrix |
| Ch 8 Results | 9–12 | Feature/evidence table; objective-wise results; model comparison table and chart; extra analysis computed from real outputs (e.g., error by weekday, residual plot, forecast vs actual on the test window if reproducible); segment centroids and profile charts; full supplier table and ranking comparison (on-time vs composite); alert distribution by brand/part type; honest interpretation and limitations |
| Ch 9 Conclusion | 3–4 | As in Section 12 |
| References | 3 | Section 14 |
| Appendices A–J | 10–14 | A: synopsis (placeholder); B: use-case descriptions; C: Chen ER; D: all test cases + console output; E: user manual; F: scripts and notebook index; G: progress report summary; H, I: not applicable; J: AI declaration (+ similarity report placeholder) |

**Additional real exploratory material the tool can generate from the ZIP's workbook** (compute it; do not invent): monthly revenue and quantity trend; revenue by brand and by part type; top 10 products and cities; customer shop-type distribution; supplier lead-time and delay distribution; return reasons distribution; stock vs reorder-level distribution. Each must be a chart or table computed from the actual data and clearly labelled as synthetic-data analysis.

---

## 16. Figure and table plan (numbered by chapter, captions: figures below, tables above)

Figures (existing in `report_assets.zip`): `gantt.png` (4.1), `pert.png` (4.2), `architecture.png` (5.1), `dfd.png` (5.2), `usecase.png` (5.3), `activity.png` (5.4), `er_schema.png` (5.5, key-level ER with cardinalities), `navmap.png` (5.6), `pipeline.png` (6.1), `ui_home/overview/demand/customer/supplier/inventory.png` (6.2–6.7), `model_compare.png` (8.1), `seg_alert.png` (8.2), `supplier_compare.png` (8.3), `er_chen.png` (Appendix C), `logo.png` (cover). Graphviz sources for architecture, ER, navigation map and pipeline are included as `.dot` files if edits are needed. The Gantt shows **planned** windows only (actual dates are in the progress reports).

Tables to include at minimum: objectives; stakeholders; FR; NFR; environment; phases; risk register; dataset composition; module specification; relationships; data dictionary; page design; design decisions; notebook summary; sample records (segments, alerts); test levels; TC list; integration tests; UAT matrix; validation configuration; defect log; traceability; feature/evidence; model comparison; segment centroids; supplier scorecard; objective-wise status; use-case descriptions; progress reports summary.

---

## 17. Known inconsistencies and items to VERIFY from the ZIP

1. **Data window.** All numbers in this README come from the original run (data to 29 Jun 2026; forecast covers the following 30 days). If the ZIP's workbook/CSVs include the 30 Jun–29 Sep 2026 extension and were re-run, then totals, segments, forecasts, alerts, model comparison and test results may differ. Use the ZIP's values and state the data window explicitly; keep the original-window numbers only if the notebooks in the ZIP still show them.
2. **Test thresholds.** TC-04 (179 customers) and TC-08 (14 suppliers) are hard-coded; after the extension the RFM table may contain 180 customers, which would change TC-04. Check `test_results.csv` and the notebook outputs.
3. **Notebook count.** `run_pipeline.py` runs notebooks **01–08**; some progress reports say "all 9 notebooks". The accurate statement: 9 notebooks exist; the script runs 8; notebook 09 is the validation notebook run separately (unless the student added it).
4. **Orders vs lines.** `order_id` is unique per sales line in the generated data, so "Total Orders = 6,016" means sales lines; RFM "frequency" counts lines.
5. **Dataset not in GitHub.** `.gitignore` excludes `data/raw` and `data/processed`; the dataset is provided only in the ZIP.
6. **Tool versions.** Only these are known: Python 3.10.20, conda 25.11.1, Jupyter Server 2.20.0, Git 2.54.0.windows.1, Windows 11. Library versions must be read from the environment (`conda list`) or notebooks; do not guess.
7. **Prophet vs SARIMA on the dashboard.** The final dashboard uses SARIMA (KPI 3.64K). Earlier screenshots showing 3.32K are the Prophet baseline.
8. **Supplier page screenshot.** `ui_supplier.png` is the final version with composite score; older screenshots without return rate/composite must not be used.
9. **Power BI Desktop version** was not recorded; omit or fill from the student's machine.
10. **Actual vs planned dates.** Gantt is planned windows; do not invent actual dates.

---

## 18. Placeholders the student must supply or confirm

- Guide's designation (cover page and certificate); head/dean name if required.
- Signatures, place and date on certificate and declaration.
- Approved project synopsis scan (Appendix A).
- Similarity (plagiarism) report (Appendix J) per university tool.
- Library version numbers (Section 6.1) and Power BI Desktop version.
- Confirmation of the AI-assistance wording against university policy.
- Whether the data-extension re-run results (Section 17) should replace the original-window numbers.
- Any additional screenshots (e.g., validation console output, notebook run, Git history) the student wants as evidence.

---

## 19. Final pre-submission checklist for the tool

- [ ] Front matter in the required order; Roman numerals for front matter, Arabic from Chapter 1; no number on cover.
- [ ] Chapter and section numbering identical to Section 3; figure/table numbering by chapter; captions placed correctly.
- [ ] Every figure and table is referred to in the text; every in-text citation is in References and vice versa (APA 7th).
- [ ] All numbers match the ZIP outputs and are consistent across abstract, chapters, tables and conclusion.
- [ ] Synthetic-data disclosure present in abstract, Chapter 1 scope, Chapter 4.8, Chapter 8 and Chapter 9.
- [ ] Limitations (Section 12) fully stated; nothing from "Not done" claimed.
- [ ] AI-assistance declaration in Acknowledgement and Appendix J.
- [ ] No placeholder or template text left except the items in Section 18.
- [ ] Tables, code listings and references single-spaced; body 1.5 spaced and justified; Times New Roman.
- [ ] Table of contents and lists of figures/tables updated so page numbers are correct in the final file.
