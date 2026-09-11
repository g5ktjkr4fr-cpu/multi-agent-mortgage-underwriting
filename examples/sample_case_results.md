# Sample Synthetic Case Results

These examples are intentionally synthetic and are provided only to demonstrate the portfolio workflow.

## Case A — Strong Profile

- Credit score: 760
- DTI: 28.0%
- LTV: 85.0%
- Liquid assets: $120,000
- Illustrative result: **APPROVED**
- Human review: No additional escalation required by the demo rules

### Workflow
Supervisor → Credit Analyst → Income Analyst → Asset Analyst → Collateral Analyst → Critic Agent → Decision Agent

### Example interpretation
The specialist analyses do not identify material threshold breaches in the demonstration rules. The Critic Agent records a low aggregate risk score and the Decision Agent returns an approval recommendation.

---

## Case B — Borderline Profile

- Credit score: 660
- DTI: 45.88%
- LTV: 92.31%
- Liquid assets: $28,000
- Recent late payments: 1
- Illustrative result: **CONDITIONAL**
- Human review: Yes

### Example interpretation
The profile contains several moderate-risk indicators, including elevated DTI, elevated LTV, and a recent late payment. The Critic Agent flags the case for escalation and the Decision Agent returns a conditional recommendation.

---

## Case C — High-Risk Profile

- Credit score: 595
- DTI: 58.57%
- LTV: 92.65%
- Liquid assets: $14,000
- Recent late payments: 3
- Collections: 2
- Illustrative result: **DENIED**
- Human review: Yes

### Example interpretation
The demonstration rules identify multiple significant risks, including a sub-600 credit score and high DTI. The Critic Agent assigns a high risk score and the Decision Agent returns a denial recommendation with human review required.

## Important

These outputs are educational examples, not lending decisions or financial advice. A real underwriting system would require validated lending policy, fair-lending governance, model-risk controls, explainability, security, auditability, regulatory review, and qualified human oversight.
