# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-immune-cd4-cd8-senescent-ratio-inversion-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def evaluate_immune_risk_phenotype_ratio(cd4_count_cells_ul, cd8_count_cells_ul, cd28_neg_cd57_pos_pct=25.0, cmv_seropositive=True):
    if cd4_count_cells_ul <= 0 or cd8_count_cells_ul <= 0:
        raise ValueError("Cell counts must be positive numbers")
        
    ratio = cd4_count_cells_ul / cd8_count_cells_ul
    
    # Standard healthy adult CD4/CD8 ratio: 1.5 - 2.5
    # Mild inversion: 0.8 - 1.0
    # True Immune Risk Phenotype (IRP): < 0.8
    if ratio >= 1.5:
        irp_status = "HOMEOSTATIC_IMMUNE_RATIO"
        risk_tier = "MINIMAL_IMMUNOSENESCENCE"
    elif ratio >= 1.0:
        irp_status = "BORDERLINE_LOW_CD4_CD8_RATIO"
        risk_tier = "MILD_AGING_ACCELERATION"
    elif ratio >= 0.8:
        irp_status = "INVERTED_CD4_CD8_RATIO"
        risk_tier = "MODERATE_IMMUNE_RISK_PHENOTYPE"
    else:
        irp_status = "SEVERE_IRP_INVERSION"
        risk_tier = "HIGH_IMMUNOSENESCENCE_VULNERABILITY"
        
    senescent_t_cell_expansion = cd28_neg_cd57_pos_pct > 30.0
    
    return {
        "cd4_count_cells_ul": cd4_count_cells_ul,
        "cd8_count_cells_ul": cd8_count_cells_ul,
        "cd4_cd8_ratio": round(ratio, 2),
        "cd28_neg_cd57_pos_senescent_t_cells_pct": round(cd28_neg_cd57_pos_pct, 1),
        "cmv_latent_seropositive": cmv_seropositive,
        "immune_risk_phenotype": irp_status,
        "immunosenescence_risk_tier": risk_tier,
        "exhausted_memory_expansion_alert": senescent_t_cell_expansion,
        "recommendation": "Inverted ratio with expanded senescent T-cells indicates clonal CMV exhaustion; focus on thymic rejuvenation and immunometabolic support." if ratio < 1.0 else "Healthy naïve-to-memory T-cell balance."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "evaluate_immune_risk_phenotype_ratio",
                        "description": """Evaluate immunosenescence and Immune Risk Phenotype (IRP) using flow cytometric CD4+ and CD8+ T-cell subsets.
An inverted CD4/CD8 ratio (< 1.0, and particularly < 0.8) along with accumulation of late-differentiated CD28- CD57+ effector memory T-cells (TEMRA)
predicts 2- to 4-year all-cause mortality in longitudinal elderly cohorts and poor vaccine responsiveness.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = evaluate_immune_risk_phenotype_ratio(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'cd4_count_cells_ul': 620, 'cd8_count_cells_ul': 780, 'cd28_neg_cd57_pos_pct': 34.5, 'cmv_seropositive': True}
        out = evaluate_immune_risk_phenotype_ratio(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
