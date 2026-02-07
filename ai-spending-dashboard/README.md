# AI Spending & Inference Tracker Dashboard

A single-page dashboard tracking global AI spending, inference costs, hyperscaler capex, and industry trends.

## View the Dashboard

Open `index.html` in any modern browser. No build step or server required.

## What It Tracks

- **Global AI spending** (Gartner, IDC, Goldman Sachs projections)
- **Inference vs. training** compute share and cost trends
- **Hyperscaler capex** (Amazon, Alphabet, Microsoft, Meta)
- **NVIDIA data center revenue** as a proxy for AI compute demand
- **Inference cost per token** decline over time
- **Cloud provider revenue** (AWS, Azure, GCP)
- **Consumer vs. enterprise** AI spending and adoption
- **Latest news** and industry developments

## Data Sources

- Gartner, Goldman Sachs, IDC, McKinsey
- NVIDIA quarterly earnings
- CNBC, Fortune, TechCrunch reporting
- a16z, Menlo Ventures, Epoch AI research
- Deloitte, Stanford AI Index

## Updating the Dashboard

To update with new data:

1. Edit the chart data arrays in the `<script>` section of `index.html`
2. Update KPI card values in the HTML
3. Add new entries to the news grid
4. Update the data sources section with new references

Key data arrays to update:
- `globalSpendingChart` — yearly total AI spending
- `inferenceTrainingChart` — inference vs training split
- `capexChart` — hyperscaler capex by company
- `inferenceCostChart` — cost per 1M tokens over time
- `nvidiaChart` — NVIDIA quarterly data center revenue
- `cloudRevenueChart` — cloud provider quarterly revenue
- `consumerShareChart` — chatbot market share

## Key Findings (as of Feb 2026)

- Global AI spending projected at **$2.52T** in 2026 (+44% YoY)
- Inference now ~67% of AI compute, overtaking training
- Hyperscaler capex approaching **$700B** combined in 2026
- Per-token inference costs dropped **~280x** in 2 years, but total spending up **320%**
- 63% of all VC funding now goes to AI startups
