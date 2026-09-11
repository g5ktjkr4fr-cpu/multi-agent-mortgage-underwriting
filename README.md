# Multi-Agent Mortgage Underwriting System

Agentic AI portfolio project demonstrating multi-agent orchestration for mortgage underwriting, including specialist analysis, policy retrieval, deterministic financial calculations, privacy-oriented data handling, critic review, risk scoring, and human-review controls.

## Overview

This project demonstrates how multiple AI agents can collaborate within a structured underwriting workflow rather than relying on a single general-purpose model. A Supervisor coordinates specialized agents for credit, income, assets, collateral, quality review, and final decision synthesis.

The project was developed as part of my Johns Hopkins University Certificate Program in Agentic AI and is presented here as a portfolio demonstration of multi-agent architecture, orchestration, responsible AI, and workflow governance.

## Business Problem

Mortgage underwriting requires information from multiple domains to be reviewed consistently, including credit history, income, available assets, property value, policy requirements, risk factors, and documentation quality. Traditional workflows can involve repetitive handoffs, fragmented analysis, and inconsistent escalation.

This project explores how an agentic workflow can coordinate specialized analysis while keeping decision logic, calculations, policy context, review steps, and human oversight visible.

## Multi-Agent Architecture

```text
Applicant Case
     |
     v
Supervisor Agent
     |
     +--> Credit Analyst
     |
     +--> Income Analyst
     |
     +--> Asset Analyst
     |
     +--> Collateral Analyst
     |
     +--> Critic Agent
     |
     +--> Decision Agent
     |
     v
Final Decision Summary + Risk Score + Human Review Flag
```

The Supervisor routes the case through each specialist, tracks workflow progress, and ensures the required analyses are completed before final synthesis.

## What Each Agent Does

### Supervisor Agent
- Initializes and manages the workflow
- Routes the case to the appropriate specialist
- Tracks completion of required analyses
- Coordinates progression toward final review

### Credit Analyst
- Reviews credit score and payment history
- Evaluates bankruptcies, foreclosures, late payments, collections, inquiries, and tradeline history
- Identifies credit-related risks and potential policy concerns

### Income Analyst
- Reviews employment and income information
- Evaluates stability and qualifying income
- Calculates debt-to-income metrics using deterministic logic where appropriate

### Asset Analyst
- Reviews available funds and reserves
- Evaluates deposits and asset sufficiency
- Identifies documentation or sourcing concerns

### Collateral Analyst
- Reviews appraisal and property information
- Calculates loan-to-value metrics
- Evaluates collateral-related risk and policy considerations

### Critic Agent
- Reviews the specialist analyses for completeness and consistency
- Identifies missing information, contradictions, risk factors, and areas requiring further scrutiny
- Provides an independent quality-control layer before final decision synthesis

### Decision Agent
- Synthesizes specialist analyses and critic findings
- Produces a risk score and decision recommendation
- Documents strengths, weaknesses, disqualifying factors, and conditions
- Flags cases that require human review

## Technology Stack

- **Python** — deterministic calculations, workflow logic, and data processing
- **LangGraph** — multi-agent orchestration and state management
- **LangChain** — LLM and tool integration
- **OpenAI models** — reasoning and narrative synthesis
- **ChromaDB** — vector storage for policy retrieval
- **Retrieval-Augmented Generation (RAG)** — grounding specialist analysis in underwriting policy context

## Key Design Concepts Demonstrated

### Multi-Agent Orchestration
The solution separates responsibilities across purpose-built agents, making each analytical step easier to understand, test, and review.

### Deterministic + LLM Hybrid Design
Financial ratios and other calculations can be handled by deterministic Python functions, while LLMs are used for interpretation, synthesis, and structured narrative analysis.

### Policy-Grounded Analysis
RAG is used to retrieve relevant policy context so agents can ground analysis in supplied underwriting guidance rather than relying only on model memory.

### Privacy-Oriented Data Handling
The project demonstrates masking and sanitization of personally identifiable information before data is provided to the language model. The portfolio version describes these as privacy and compliance-oriented controls rather than asserting formal legal compliance.

### Critic / Review Layer
A dedicated Critic Agent reviews the work of specialist agents before the Decision Agent generates a final recommendation, creating an additional quality-control checkpoint.

### Human-in-the-Loop Controls
Cases can be flagged for human review when risk, policy, data quality, or workflow conditions warrant escalation.

## Example Workflow

A representative execution follows this sequence:

**Supervisor → Credit → Supervisor → Income → Supervisor → Asset → Supervisor → Collateral → Supervisor → Critic → Supervisor → Decision**

This allows the workflow to preserve clear responsibility and review checkpoints throughout the underwriting process.

## Skills Demonstrated

- Multi-agent AI architecture
- LangGraph orchestration
- Agent routing and state management
- Retrieval-Augmented Generation (RAG)
- Vector databases and semantic retrieval
- Deterministic financial calculations
- Workflow governance and control points
- Privacy-aware AI design
- Critic / evaluator patterns
- Risk scoring and escalation logic
- Human-in-the-loop workflow design
- Responsible AI considerations
- Python implementation and debugging

## Responsible AI & Limitations

This project is an educational and portfolio demonstration. It is not intended to make real lending decisions or replace licensed underwriting professionals, lender policies, legal review, fair-lending controls, or required human oversight.

The demo uses synthetic/sample applicant information and should not be used with real personal financial data. Portfolio materials are intentionally sanitized to avoid exposing API credentials, private course assets, or sensitive information.

## Planned Portfolio Enhancements

- Add a cleaned portfolio version of the multi-agent workflow code
- Add an architecture diagram
- Add sanitized example cases for approval, conditional review, and denial scenarios
- Add evaluation criteria for each specialist agent
- Add a browser-based interactive workflow demonstration
- Add program-management artifacts such as acceptance criteria, risk log, and production-readiness checklist

## About Me

**Chantell Harris-Headley**  
Technical Project / Program Manager | Agentic AI | AI Workflows & Automation | Digital Transformation

I combine enterprise technology and project leadership experience with hands-on training in generative and agentic AI. My focus is helping bridge business objectives, technical delivery, workflow governance, responsible AI, and adoption.
