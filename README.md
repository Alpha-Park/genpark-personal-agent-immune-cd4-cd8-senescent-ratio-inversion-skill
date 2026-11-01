# genpark-personal-agent-immune-cd4-cd8-senescent-ratio-inversion-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

CD4+/CD8+ lymphocyte ratio inversion (<1.0), CD28- CD57+ senescent memory T-cell expansion immune risk phenotype (IRP) calculator.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `evaluate_immune_risk_phenotype_ratio`
- **Category**: `personal_agent`

### Method Documentation
Evaluate immunosenescence and Immune Risk Phenotype (IRP) using flow cytometric CD4+ and CD8+ T-cell subsets.
An inverted CD4/CD8 ratio (< 1.0, and particularly < 0.8) along with accumulation of late-differentiated CD28- CD57+ effector memory T-cells (TEMRA)
predicts 2- to 4-year all-cause mortality in longitudinal elderly cohorts and poor vaccine responsiveness.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "evaluate_immune_risk_phenotype_ratio",
    "arguments": {
    "cd4_count_cells_ul": 620,
    "cd8_count_cells_ul": 780,
    "cd28_neg_cd57_pos_pct": 34.5,
    "cmv_seropositive": true
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
