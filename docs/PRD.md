# Product Requirements Document (PRD)
## Governance Translator Tool

**Author:** Mya Zylberberg  
**Status:** In Development  
**Last Updated:** January 2026

---

## 1. Product Overview

### Problem Statement
Technical cybersecurity and IT findings are often communicated in language that is:
- overly technical for business stakeholders,
- too abstract for project and program managers,
- or not actionable across teams.

This misalignment creates delays, risk misinterpretation, and poor decision-making across IT, business leadership, and delivery teams.

### Solution
The **Governance Translator Tool** translates technical cybersecurity or IT language into **audience-specific, governance-aligned communication**, producing structured outputs that support clear decision-making and accountability.

---

## 2. Goals and Success Criteria

### Primary Goals
- Translate technical findings into stakeholder-appropriate language
- Standardize governance-style outputs (risks, impacts, actions)
- Provide traceability through saved translation history
- Demonstrate backend, data, and product-thinking skills for portfolio review

### Success Metrics (MVP)
- API successfully translates text for all supported audiences
- Swagger UI available and functional
- Translations stored and retrievable from database
- Clean, documented GitHub repository with reproducible setup

---

## 3. Target Users

### Primary Personas
1. **IT / Security Teams**
   - Need structured outputs for tickets, audits, and incident reporting

2. **Executives / Business Stakeholders**
   - Need concise summaries framed in risk and business impact

3. **Project / Program Managers**
   - Need clarity on timeline impact, dependencies, and ownership

---

## 4. In-Scope Features (MVP)

### Backend (FastAPI)
- `GET /health`
- `POST /translate`
  - Inputs:
    - Technical text
    - Target audience (`it`, `executive`, `pm`)
  - Outputs:
    - Summary
    - Risks
    - Recommended actions
- `GET /history`
  - Retrieve recent translations

### Data Layer
- SQLite database
- Each translation record stores:
  - Audience
  - Input text
  - Summary
  - Risks
  - Recommended actions
  - Timestamp

### Architecture
```text
governance-tool/
  backend/
  frontend/
  docs/
