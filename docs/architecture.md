# Architecture: Multi-Agent Mortgage Underwriting System

## Purpose

This portfolio project demonstrates how a supervisor can coordinate specialized AI agents across a structured underwriting workflow while combining deterministic calculations, policy retrieval concepts, critique, and human-review escalation.

The original project used the following sequence:

**Supervisor → Credit → Supervisor → Income → Supervisor → Asset → Supervisor → Collateral → Supervisor → Critic → Supervisor → Decision**

## Agent Responsibilities

### Supervisor
Coordinates workflow order, maintains shared state, and routes the case to the next specialist.

### Credit Analyst
Reviews credit score, payment history, bankruptcies, foreclosures, collections, and other derogatory indicators.

### Income Analyst
Reviews income and recurring debt. Debt-to-income ratio (DTI) is calculated deterministically rather than left to the language model.

### Asset Analyst
Reviews liquid assets and reserve capacity, helping assess whether the borrower has sufficient financial resources.

### Collateral Analyst
Reviews appraisal information and calculates loan-to-value ratio (LTV) deterministically.

### Critic Agent
Reviews specialist outputs for completeness, contradictions, material risks, and escalation needs before a final recommendation is produced.

### Decision Agent
Synthesizes specialist findings and Critic review into an illustrative approve / conditional / deny recommendation and determines whether human review is required.

## Data and Policy Layer

The original project incorporated ChromaDB-based retrieval for mortgage policy context. The portfolio version keeps that concept documented while avoiding proprietary or course-only policy materials in the public repository.

A production-ready version would use a controlled RAG pipeline to retrieve only approved policy text, attach citations to material conclusions, and version policy sources for auditability.

## Deterministic Tools

The portfolio code intentionally calculates important financial ratios outside the LLM:

- **DTI = monthly debt / monthly income**
- **LTV = loan amount / appraised value**

This pattern reduces arithmetic error and makes calculations reproducible and auditable.

## Privacy-Oriented Controls

The project demonstrates sanitization concepts before data is sent to an LLM, including masking of SSNs and replacement of identifying fields. These are examples of privacy-oriented controls and should not be interpreted as a formal legal compliance certification.

## Human Oversight

The workflow is designed to escalate higher-risk or ambiguous cases for human review. The public portfolio implementation does not present the system as a replacement for qualified underwriters or regulated lending controls.

## Technology Stack Demonstrated

- Python
- LangGraph — orchestration and state management
- LangChain — LLM and tool integration
- OpenAI models — reasoning in the original project
- ChromaDB — policy retrieval in the original project
- RAG — policy-context retrieval
- Deterministic calculation tools
- Multi-agent workflow design
- Critic / quality-review patterns
- Human-in-the-loop escalation

## Portfolio Demo

The browser demo uses synthetic cases and pre-modeled workflow outputs so it can be shared publicly without exposing API keys, personal financial data, or private policy documents.
