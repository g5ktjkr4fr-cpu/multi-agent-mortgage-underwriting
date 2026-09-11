"""Multi-Agent Mortgage Underwriting System

Portfolio-ready implementation based on my Johns Hopkins University Agentic AI
project. The workflow demonstrates supervisor orchestration, specialist agents,
policy retrieval, deterministic financial calculations, critic review, risk scoring,
and human-review escalation.

Important:
- This is an educational portfolio project, not a production underwriting system.
- Use only synthetic or de-identified data.
- Do not rely on this code for real lending decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List, Literal, TypedDict


Decision = Literal["APPROVED", "CONDITIONAL", "DENIED"]


@dataclass
class MortgageCase:
    case_id: str
    credit_score: int
    monthly_income: float
    monthly_debt: float
    liquid_assets: float
    loan_amount: float
    appraised_value: float
    recent_late_payments: int = 0
    bankruptcies: int = 0
    foreclosures: int = 0
    collections: int = 0
    notes: str = ""


class UnderwritingState(TypedDict):
    case: Dict
    analyses: Dict[str, Dict]
    workflow_log: List[str]
    critic_review: Dict
    decision: Dict


def calculate_dti(monthly_debt: float, monthly_income: float) -> float:
    """Deterministic debt-to-income calculation."""
    if monthly_income <= 0:
        return 999.0
    return round((monthly_debt / monthly_income) * 100, 2)


def calculate_ltv(loan_amount: float, appraised_value: float) -> float:
    """Deterministic loan-to-value calculation."""
    if appraised_value <= 0:
        return 999.0
    return round((loan_amount / appraised_value) * 100, 2)


def mask_pii(payload: Dict) -> Dict:
    """Example privacy-oriented sanitization layer for portfolio use."""
    sanitized = dict(payload)
    for key in ("name", "address", "phone"):
        if key in sanitized:
            sanitized[key] = f"[{key.upper()}]"
    if "ssn" in sanitized and sanitized["ssn"]:
        last4 = str(sanitized["ssn"])[-4:]
        sanitized["ssn"] = f"***-**-{last4}"
    return sanitized


def supervisor(state: UnderwritingState, next_agent: str) -> UnderwritingState:
    state["workflow_log"].append(f"Supervisor routed case to {next_agent}")
    return state


def credit_agent(case: MortgageCase) -> Dict:
    risks = []
    if case.credit_score < 620:
        risks.append("Credit score below illustrative conventional threshold")
    if case.recent_late_payments > 0:
        risks.append("Recent late-payment history")
    if case.bankruptcies > 0:
        risks.append("Bankruptcy history")
    if case.foreclosures > 0:
        risks.append("Foreclosure history")
    if case.collections > 0:
        risks.append("Outstanding collections")

    return {
        "agent": "Credit Analyst",
        "credit_score": case.credit_score,
        "risk_level": "low" if not risks and case.credit_score >= 700 else "elevated" if case.credit_score >= 620 else "high",
        "risks": risks,
        "summary": "Credit profile reviewed for score, payment history, and derogatory indicators.",
    }


def income_agent(case: MortgageCase) -> Dict:
    dti = calculate_dti(case.monthly_debt, case.monthly_income)
    risks = []
    if dti > 43:
        risks.append("Debt-to-income ratio above illustrative guideline")
    return {
        "agent": "Income Analyst",
        "monthly_income": case.monthly_income,
        "monthly_debt": case.monthly_debt,
        "dti": dti,
        "risks": risks,
        "summary": "Income and recurring debt reviewed using a deterministic DTI calculation.",
    }


def asset_agent(case: MortgageCase) -> Dict:
    estimated_reserve_months = round(case.liquid_assets / max(case.monthly_debt, 1), 1)
    risks = []
    if case.liquid_assets < case.loan_amount * 0.03:
        risks.append("Limited liquid assets relative to loan size")
    return {
        "agent": "Asset Analyst",
        "liquid_assets": case.liquid_assets,
        "estimated_reserve_months": estimated_reserve_months,
        "risks": risks,
        "summary": "Liquid assets and indicative reserve capacity reviewed.",
    }


def collateral_agent(case: MortgageCase) -> Dict:
    ltv = calculate_ltv(case.loan_amount, case.appraised_value)
    risks = []
    if ltv > 95:
        risks.append("Very high loan-to-value ratio")
    elif ltv > 90:
        risks.append("Elevated loan-to-value ratio")
    return {
        "agent": "Collateral Analyst",
        "loan_amount": case.loan_amount,
        "appraised_value": case.appraised_value,
        "ltv": ltv,
        "risks": risks,
        "summary": "Collateral value reviewed using a deterministic LTV calculation.",
    }


def critic_agent(analyses: Dict[str, Dict]) -> Dict:
    all_risks = []
    for analysis in analyses.values():
        all_risks.extend(analysis.get("risks", []))

    score = min(100, len(all_risks) * 20)
    return {
        "agent": "Critic Agent",
        "risk_score": score,
        "identified_risks": all_risks,
        "quality_review": "Specialist analyses reviewed for completeness, contradictions, and escalation needs.",
        "human_review_required": score >= 40,
    }


def decision_agent(analyses: Dict[str, Dict], critic: Dict) -> Dict:
    credit = analyses["credit"]
    income = analyses["income"]
    collateral = analyses["collateral"]
    asset = analyses["asset"]

    hard_fail = credit["credit_score"] < 600 or income["dti"] > 55 or collateral["ltv"] > 100
    moderate_flags = len(critic["identified_risks"]) >= 2 or critic["risk_score"] >= 40

    if hard_fail:
        decision: Decision = "DENIED"
    elif moderate_flags:
        decision = "CONDITIONAL"
    else:
        decision = "APPROVED"

    return {
        "agent": "Decision Agent",
        "decision": decision,
        "risk_score": critic["risk_score"],
        "human_review_required": critic["human_review_required"] or decision != "APPROVED",
        "summary": (
            "Final recommendation synthesized from specialist analyses and critic review. "
            "This result is illustrative and requires human oversight in any real lending context."
        ),
        "key_metrics": {
            "credit_score": credit["credit_score"],
            "dti": income["dti"],
            "ltv": collateral["ltv"],
            "liquid_assets": asset["liquid_assets"],
        },
    }


def run_underwriting_workflow(case: MortgageCase) -> UnderwritingState:
    state: UnderwritingState = {
        "case": asdict(case),
        "analyses": {},
        "workflow_log": [f"Application {case.case_id} initialized"],
        "critic_review": {},
        "decision": {},
    }

    supervisor(state, "Credit Analyst")
    state["analyses"]["credit"] = credit_agent(case)

    supervisor(state, "Income Analyst")
    state["analyses"]["income"] = income_agent(case)

    supervisor(state, "Asset Analyst")
    state["analyses"]["asset"] = asset_agent(case)

    supervisor(state, "Collateral Analyst")
    state["analyses"]["collateral"] = collateral_agent(case)

    supervisor(state, "Critic Agent")
    state["critic_review"] = critic_agent(state["analyses"])

    supervisor(state, "Decision Agent")
    state["decision"] = decision_agent(state["analyses"], state["critic_review"])
    state["workflow_log"].append(
        f"Decision Agent returned {state['decision']['decision']} for {case.case_id}"
    )
    return state


SYNTHETIC_CASES = {
    "strong": MortgageCase(
        case_id="DEMO-001",
        credit_score=760,
        monthly_income=12500,
        monthly_debt=3500,
        liquid_assets=120000,
        loan_amount=425000,
        appraised_value=500000,
    ),
    "borderline": MortgageCase(
        case_id="DEMO-002",
        credit_score=660,
        monthly_income=8500,
        monthly_debt=3900,
        liquid_assets=28000,
        loan_amount=360000,
        appraised_value=390000,
        recent_late_payments=1,
    ),
    "high_risk": MortgageCase(
        case_id="DEMO-003",
        credit_score=595,
        monthly_income=7000,
        monthly_debt=4100,
        liquid_assets=14000,
        loan_amount=315000,
        appraised_value=340000,
        recent_late_payments=3,
        collections=2,
    ),
}


if __name__ == "__main__":
    for label, case in SYNTHETIC_CASES.items():
        result = run_underwriting_workflow(case)
        print(f"\n=== {label.upper()} ===")
        print(result["workflow_log"])
        print(result["decision"])
