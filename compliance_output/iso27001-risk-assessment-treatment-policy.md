---
organization: Teamcognito Solutions Pvt Ltd
framework: ISO27001
policy: iso27001-risk-assessment-treatment-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# Information Security Risk Assessment and Treatment Policy
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy defines Teamcognito Solutions Pvt Ltd's approach to identifying, analysing, evaluating, and treating information security risks. A systematic, documented risk management process is a foundational requirement of ISO/IEC 27001:2022 (Clauses 6.1, 8.2, 8.3) and is essential to ensuring that security investment is directed towards the threats and vulnerabilities that pose the greatest risk to the business. This policy ensures that risk management is consistent, repeatable, and embedded throughout the organisation.

## 2. Scope
This policy applies to all information security risk assessments conducted for Teamcognito Solutions Pvt Ltd, including:
- Annual enterprise-wide ISMS risk assessments
- Project-level risk assessments
- Supplier/third-party risk assessments
- Change-driven risk assessments (triggered by significant technology, process, or business changes)
- Incident-driven risk reassessments

It applies to all business units, information assets, technology systems, and processes within the ISMS scope.

## 3. Policy Statement

### 3.1 Risk Assessment Methodology
1. Teamcognito shall follow a documented, repeatable risk assessment methodology based on ISO/IEC 27005 principles.
2. The risk assessment methodology shall be reviewed and approved by the CISO annually and shall remain consistent to enable year-on-year risk trending.
3. Risk shall be assessed using a 5×5 risk matrix, combining **Likelihood** (1=Rare, 5=Almost Certain) and **Impact** (1=Negligible, 5=Catastrophic), producing a Risk Score (1–25).
4. Risk appetite thresholds shall be defined by the ISSC and Board:
   - **Low (1–5):** Accept — monitor annually
   - **Medium (6–12):** Mitigate — treatment plan required within 90 days
   - **High (13–19):** Treat urgently — treatment plan required within 30 days
   - **Critical (20–25):** Escalate to ISSC — treatment plan within 7 days; CISO to brief CEO

### 3.2 Risk Identification
5. Risks shall be identified by considering: threats (internal and external), vulnerabilities (technical and procedural), existing controls, and potential impact on confidentiality, integrity, and availability (CIA triad).
6. The following inputs shall be used in risk identification: threat intelligence feeds, vulnerability scan results, incident history, audit findings, technology landscape changes, regulatory changes, and staff/management input.
7. All identified risks shall be documented in the central Risk Register, maintained in the GRC tool.

### 3.3 Risk Analysis and Evaluation
8. Each risk shall be assessed for its inherent risk (before controls) and residual risk (after existing controls are considered).
9. Risk owners shall be assigned for each risk — typically the business unit head or system owner most directly impacted.
10. Risk analysis shall consider both quantitative factors (financial impact, downtime costs) and qualitative factors (reputational damage, regulatory penalties) where relevant.

### 3.4 Risk Treatment
11. For each risk assessed as Medium or above, a risk treatment decision shall be made using one of four options:
    - **Mitigate:** Implement controls to reduce the likelihood or impact
    - **Transfer:** Transfer risk through insurance, contracts, or outsourcing
    - **Avoid:** Cease the activity that creates the risk
    - **Accept:** Formally accept the residual risk (requires CISO sign-off for Medium; ISSC sign-off for High/Critical)
12. Risk treatment plans shall include: control measures to be implemented, responsible owner, implementation timeline, residual risk estimate after treatment, and review date.
13. Treatment plans for High/Critical risks must be approved by the CISO and presented to the ISSC.

### 3.5 Statement of Applicability (SoA)
14. A Statement of Applicability (SoA) shall be maintained, documenting all 93 ISO 27001:2022 Annex A controls, their applicability, implementation status, and justification for inclusion or exclusion.
15. The SoA shall be reviewed and updated at minimum annually and following any significant change to the risk assessment results.

### 3.6 Risk Monitoring and Review
16. The Risk Register shall be reviewed at minimum every 6 months; risk owners shall confirm the current status of their risks and treatment plans.
17. The full enterprise risk assessment shall be repeated annually and following significant change events (major incidents, mergers, significant new product launches, large-scale technology changes).
18. Risk treatment progress shall be tracked in the GRC tool; overdue treatment actions shall be escalated to the CISO.
19. Risk management metrics (number of open risks by rating, treatment plan completion %, SLA adherence) shall be reported monthly to the CISO and quarterly to the ISSC.

### 3.7 Residual Risk Acceptance
20. Residual risks that remain Medium after treatment may be accepted by the CISO with documented justification.
21. Residual risks rated High or Critical after treatment must be accepted by the ISSC and Board Risk Committee; acceptance shall be formally documented and time-limited (maximum 6 months before re-review).

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO | Own the risk management process; review and approve risk assessments; accept Medium residual risks; present high/critical risks to ISSC |
| Information Security Steering Committee (ISSC) | Review and approve risk appetite; approve High/Critical risk treatment plans and residual risk acceptance |
| Risk Owners (Business Unit Heads / System Owners) | Identify risks within their domain; own treatment plans; update GRC tool; escalate emerging risks |
| IT/Security Team | Provide technical risk inputs; conduct vulnerability assessments; implement technical treatment controls |
| Legal & Compliance | Identify regulatory and contractual risk inputs; advise on legal treatment options |
| Internal Audit | Validate risk assessment quality; review effectiveness of treatment controls |
| All Employees | Report perceived security risks to their Security Liaison or CISO |

## 5. Controls and Procedures

### 5.1 Risk Assessment Schedule
- Annual enterprise-wide risk assessment: scheduled each January, completed by end of February.
- Project risk assessments: conducted at project initiation; reviewed at each phase gate.
- Supplier risk assessments: conducted prior to onboarding; reviewed annually for critical suppliers.
- Ad-hoc risk assessments triggered by: significant incidents, major changes, new regulatory requirements, or threat intelligence indicating elevated risk.

### 5.2 Risk Register Management
- GRC tool (e.g., OneTrust, Vanta, ServiceNow GRC) used as system of record for all risks.
- Risk entries include: Risk ID, description, threat/vulnerability source, CIA impact, inherent risk score, existing controls, residual risk score, treatment option, treatment plan, risk owner, review date.
- Risk Register access restricted to CISO, Security team, Internal Audit, and risk owners.

### 5.3 Risk Assessment Methodology Documentation
- Risk assessment methodology document maintained separately in DMS.
- Threat library and vulnerability catalogue maintained and updated quarterly.
- Risk scoring guidance and worked examples provided to all risk owners.

## 6. Exceptions
The risk assessment and treatment process is mandatory; no exceptions to the requirement to conduct risk assessments shall be permitted. However, the frequency or depth of assessment for specific asset categories may be varied by the CISO based on risk profile, with documented justification.

## 7. Non-Compliance
Failure by risk owners to actively participate in the risk assessment process, maintain their sections of the Risk Register, or implement approved treatment plans within agreed timelines shall be escalated to the relevant Business Unit Head and ISSC. Persistent non-participation may result in disciplinary action.

## 8. References
- ISO/IEC 27001:2022 Clauses 6.1.2, 6.1.3, 8.2, 8.3 (Risk Assessment and Treatment)
- ISO/IEC 27005:2022 (Information Security Risk Management)
- ISO/IEC 27002:2022
- NIST SP 800-30 Rev 1 (Guide for Conducting Risk Assessments)
- SOC 2 TSC: CC3.1, CC3.2, CC3.3, CC3.4, CC9.1
- India DPDP Act 2023

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
