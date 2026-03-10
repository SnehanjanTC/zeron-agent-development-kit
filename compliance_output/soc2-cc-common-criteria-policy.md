---
organization: Teamcognito Solutions Pvt Ltd
framework: SOC2
policy: soc2-cc-common-criteria-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# SOC 2 Common Criteria (Security) Policy
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy defines Teamcognito Solutions Pvt Ltd's controls and commitments addressing the SOC 2 Common Criteria (CC) Trust Service Criteria — the Security category that forms the foundation of all SOC 2 examinations. It covers the nine CC domains: Control Environment (CC1), Communication and Information (CC2), Risk Assessment (CC3), Monitoring Activities (CC4), Control Activities (CC5), Logical and Physical Access (CC6), System Operations (CC7), Change Management (CC8), and Risk Mitigation (CC9). Compliance with these criteria is essential for maintaining client trust and achieving SOC 2 Type II attestation.

## 2. Scope
This policy applies to all Teamcognito Solutions Pvt Ltd services, systems, and infrastructure that are within the SOC 2 examination scope, including:
- All production cloud infrastructure (AWS/Azure/GCP environments)
- All client-facing SaaS applications and APIs
- All supporting corporate systems (identity management, SIEM, ITSM, HR systems)
- All personnel with access to in-scope systems
- All third-party service providers supporting in-scope services

## 3. Policy Statement

### 3.1 Control Environment (CC1)
**CC1.1 — Commitment to Integrity and Ethical Values**
1. Teamcognito shall maintain and publish a Code of Conduct and Ethics Policy, communicated to all employees and contractors upon hire and annually thereafter.
2. Management shall visibly model ethical behaviour; any management override of controls shall be documented, justified, and reported to the Audit Committee.

**CC1.2 — Board Oversight**
3. The Board of Directors shall maintain oversight of the organisation's information security and compliance programme; the CISO shall present to the Board at minimum bi-annually.
4. An Audit Committee (or equivalent Board-level oversight function) shall review internal audit findings and compliance programme status.

**CC1.3 — Organisational Structure, Authority, and Responsibility**
5. An organisational chart defining reporting lines and authority shall be maintained and published on the company intranet; it shall be reviewed and updated at minimum annually.
6. Delegated authority levels for financial and security decisions shall be documented in a Delegation of Authority (DoA) matrix.

**CC1.4 — Commitment to Competence**
7. Job descriptions for all roles shall include information security competency requirements; hiring decisions shall confirm candidates meet these requirements.
8. Annual performance reviews shall include assessment of compliance with information security responsibilities.
9. Continuing professional development (CPD) shall be supported for information security roles; budget shall be allocated for certifications and training (e.g., CISSP, CISM, CEH, cloud security certs).

**CC1.5 — Enforcement of Accountability**
10. Performance objectives for all employees shall include compliance with security policies as a measurable component.
11. Disciplinary processes for security policy violations shall be documented, consistently applied, and communicated to all staff.

### 3.2 Communication and Information (CC2)
**CC2.1 — Quality Information**
12. Management information systems shall produce accurate, timely, and relevant information to support decision-making; data quality controls shall be in place for key reporting systems.
13. Security dashboards (SIEM, vulnerability management, compliance) shall be reviewed by the CISO weekly and presented to the ISSC quarterly.

**CC2.2 — Internal Communication**
14. Information security policies, standards, and procedures shall be communicated to all relevant personnel through the intranet, email notifications, and team briefings.
15. Security alerts and threat intelligence relevant to staff roles shall be communicated within 24 hours of identification.
16. Security awareness campaigns shall be run at minimum quarterly.

**CC2.3 — External Communication**
17. Teamcognito shall maintain a published security policy statement and privacy notice accessible to clients and prospects.
18. Security-related commitments (e.g., data handling, breach notification SLAs) shall be documented in client agreements.
19. Clients shall be notified of material security changes (e.g., sub-processor changes, significant control changes) with appropriate notice periods as contractually agreed.

### 3.3 Risk Assessment (CC3)
**CC3.1 — Suitable Objectives**
20. Teamcognito's service commitments and system requirements (SCSRs) shall be documented and reviewed annually; they shall form the basis for identifying risks to service delivery.

**CC3.2 — Risk Identification and Analysis**
21. An enterprise information security risk assessment shall be conducted annually; risks shall be assessed for likelihood and impact, with documented risk treatment plans.

**CC3.3 — Fraud Risk Assessment**
22. A specific fraud risk assessment shall be included within the annual enterprise risk assessment, covering: asset misappropriation, financial statement fraud, data fraud, and insider threat scenarios.
23. Anti-fraud controls shall include: segregation of duties, dual authorisation for significant financial transactions, access logging, and anomaly monitoring.

**CC3.4 — Change Risk Assessment**
24. Significant changes to systems, processes, or the business environment shall trigger an ad-hoc risk assessment before implementation; change risk assessments shall be part of the change management process.

### 3.4 Monitoring Activities (CC4)
**CC4.1 — Ongoing and Separate Evaluations**
25. Continuous monitoring of controls shall be implemented using automated tools (SIEM, compliance monitoring, vulnerability scanners, cloud security posture management).
26. An annual internal audit programme shall include reviews of all SOC 2 in-scope controls; results shall be documented and tracked to resolution.

**CC4.2 — Evaluation and Communication of Deficiencies**
27. Control deficiencies identified through monitoring, audit, or incident review shall be logged in the GRC tool, assigned to an owner, and remediated within SLAs defined by severity.
28. Deficiencies shall be communicated to the CISO and relevant management within 5 business days of identification; High/Critical deficiencies shall be reported within 24 hours.

### 3.5 Control Activities (CC5)
**CC5.1 — Control Selection and Development**
29. Controls shall be selected based on risk assessment results; control design shall consider both automated and manual controls, preventive and detective mechanisms.
30. Control design documentation (control descriptions, control objectives, test procedures) shall be maintained for all SOC 2 in-scope controls.

**CC5.2 — General Technology Controls**
31. General IT Controls (GITCs) shall be implemented and operating effectively across: logical access management, change management, IT operations, and system development.
32. GITCs shall be reviewed annually; any significant gaps shall be remediated before the SOC 2 examination period commences.

**CC5.3 — Deployment Through Policies and Procedures**
33. All controls shall be supported by documented policies and procedures; undocumented controls shall not be considered operating effectively for SOC 2 purposes.
34. Policies shall be version-controlled; employees shall acknowledge receipt of updated policies within 30 days of publication.

### 3.6 Logical and Physical Access Controls (CC6)
**CC6.1 — Logical Access Security Measures**
35. Logical access to all in-scope systems shall be controlled through a centralised Identity and Access Management (IAM) platform enforcing RBAC, MFA, and SSO.
36. Network access controls (firewalls, VPN/ZTNA, network segmentation) shall restrict access to authorised users and systems only.

**CC6.2 — Registration and Authorisation of New Users**
37. New user accounts shall be created only upon receipt of a formally approved access request; requests shall be logged and retained for audit.
38. New user credentials shall be issued via a secure, automated provisioning process; temporary passwords shall require change on first login.

**CC6.3 — Removal of Access When No Longer Required**
39. Access rights shall be reviewed quarterly using automated access certification; any access deemed no longer required shall be revoked within 5 business days of certification completion.
40. Role changes shall trigger immediate access review and adjustment by IT within 24 hours of HR notification.

**CC6.4 — Restriction of Physical Access**
41. Physical access to server rooms, data centres, and secure areas shall be restricted to authorised personnel only; access shall be managed by electronic badge systems with logged entries.

**CC6.5 — Termination of Access**
42. All logical and physical access shall be revoked on or before the employee/contractor's last day of employment; involuntary terminations shall result in immediate (same-hour) access revocation.
43. IT shall provide CISO with a signed-off access revocation confirmation within 2 business days of every departure.

**CC6.6 — Protection from External Threats**
44. Perimeter security controls shall include: next-generation firewalls, IDS/IPS, WAF for web applications, DDoS mitigation, and email security (SPF, DKIM, DMARC).
45. External penetration testing shall be conducted annually by a qualified third party.

**CC6.7 — Restriction of Information Transmission**
46. DLP controls shall restrict the unauthorised transmission of sensitive information via email, web upload, removable media, and messaging platforms.
47. Sensitive data transmission outside the organisation shall require encryption (TLS 1.2+) and, for Restricted data, additional approval.

**CC6.8 — Prevention of Unauthorised Software**
48. Application whitelisting or equivalent control (e.g., next-gen EDR with application control) shall prevent the execution of unapproved software on corporate endpoints.
49. Software installation on production servers shall require change management approval; automated configuration management tools shall detect and alert on unauthorised installations.

### 3.7 System Operations (CC7)
**CC7.1 — Vulnerability Detection**
50. Automated vulnerability scanning tools shall continuously scan the production environment; critical vulnerabilities shall trigger P1 incident response within 24 hours.

**CC7.2 — Anomaly Detection**
51. SIEM-based behavioural analytics shall detect anomalous activity (unusual login times/locations, large data transfers, privilege escalation); SOC shall triage all high-fidelity alerts within 1 hour.

**CC7.3 — Evaluation of Security Events**
52. All security events shall be evaluated by the SOC to determine if they constitute an incident requiring escalation; decision criteria and escalation thresholds shall be documented.

**CC7.4 — Response to Security Incidents**
53. Security incidents shall be responded to per the Incident Response Policy; P1/P2 incidents shall activate the Incident Response Team within 15 minutes.

**CC7.5 — Recovery from Security Incidents**
54. Recovery procedures shall restore systems to known-good states within defined RTOs; recovery actions shall be documented and reviewed in post-incident analysis.

### 3.8 Change Management (CC8)
**CC8.1 — Authorised Change Management**
55. All changes to production systems shall be authorised, tested, approved, and documented before implementation; unauthorised changes are prohibited.
56. Emergency changes shall follow an expedited approval process; post-change review shall be completed within 24 hours.
57. Change success/failure rates and rollback frequencies shall be tracked as operational KPIs.

### 3.9 Risk Mitigation (CC9)
**CC9.1 — Risk Mitigation Activities**
58. Risk mitigation activities shall be selected based on risk assessment results; treatment plans shall be documented in the GRC tool with owners and timelines.

**CC9.2 — Vendor and Business Partner Risk Management**
59. All vendors and business partners with access to Teamcognito systems or data shall undergo a security risk assessment prior to onboarding.
60. Vendor risk ratings shall be maintained in the supplier risk register; critical vendors shall be assessed annually.
61. Contracts with vendors shall include security requirements, data handling obligations, breach notification requirements, audit rights, and compliance certifications (e.g., ISO 27001, SOC 2).

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO | Own SOC 2 programme; ensure CC controls are designed and operating effectively; engage external auditors |
| Compliance Manager | Maintain SOC 2 control evidence; coordinate audit activities; track control deficiencies |
| IT/Security Team | Implement and operate technical CC controls; maintain SIEM, IAM, vulnerability management |
| Legal Counsel | Review client contracts for security commitments; manage regulatory interactions |
| HR | Manage onboarding/offboarding; enforce Code of Conduct; support disciplinary processes |
| Internal Audit | Conduct annual CC controls review; report findings to CISO and Audit Committee |
| All Employees | Comply with CC control requirements; report security events; complete training |

## 5. Controls and Procedures
- SOC 2 control matrix maintained in GRC tool; updated quarterly and before each audit.
- Evidence collection automated where possible (API integrations between GRC and security tools).
- Annual readiness assessment conducted before external SOC 2 audit window.
- User access certification process run quarterly via IAM platform; results exported to GRC tool as audit evidence.
- Change management evidence (tickets, approvals, test results) retained in ITSM for minimum 12 months.

## 6. Exceptions
Exceptions to any CC control shall be documented in the GRC tool with risk justification, compensating controls, and CISO approval. Exceptions that may affect the SOC 2 audit opinion shall be disclosed to the auditor; undisclosed exceptions may constitute a qualified opinion or management representation issue.

## 7. Non-Compliance
Non-compliance with CC controls is treated as a material control deficiency for SOC 2 purposes and shall be escalated to the CISO and ISSC. Persistent non-compliance may result in disciplinary action and impacts the organisation's SOC 2 attestation.

## 8. References
- SOC 2 Trust Service Criteria (AICPA 2017): CC1.1–CC9.2 (all Common Criteria)
- ISO/IEC 27001:2022 (all Annex A controls)
- COSO Internal Control — Integrated Framework (2013)
- ISO/IEC 27002:2022
- NIST Cybersecurity Framework 2.0

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
