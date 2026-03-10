---
organization: Teamcognito Solutions Pvt Ltd
framework: ISO27001
policy: iso27001-incident-response-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# Information Security Incident Response Policy
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy defines Teamcognito Solutions Pvt Ltd's approach to preparing for, detecting, responding to, and recovering from information security incidents. A structured incident response capability is essential to minimise the impact of security incidents on the organisation, its clients, and its stakeholders — and to meet obligations under ISO/IEC 27001:2022 Annex A.5.24–A.5.28 and applicable regulatory requirements (including CERT-In's 6-hour reporting mandate and GDPR's 72-hour breach notification). This policy ensures that incidents are handled consistently, efficiently, and in a legally sound manner.

## 2. Scope
This policy applies to all information security incidents affecting Teamcognito Solutions Pvt Ltd, including those involving:
- Cyberattacks (malware, ransomware, phishing, DDoS, APT)
- Unauthorised access to systems or data
- Data breaches (personal data, client data, intellectual property)
- Insider threats (malicious or accidental)
- Physical security breaches affecting information assets
- Third-party/supplier security incidents impacting Teamcognito data
- System outages or disruptions with a security root cause

It applies to all employees, contractors, and third parties who may discover, respond to, or be affected by such incidents.

## 3. Policy Statement

### 3.1 Incident Classification
1. All security incidents shall be classified by severity upon initial triage:
   - **P1 — Critical:** Active compromise with significant data loss, system unavailability, or regulatory breach notification trigger. Response: Immediate (within 15 minutes). Example: Ransomware affecting production systems, large-scale data breach.
   - **P2 — High:** Confirmed security incident with contained or potential significant impact. Response: Within 1 hour. Example: Confirmed phishing compromise of a user account, suspected data exfiltration.
   - **P3 — Medium:** Suspected or low-impact security incident. Response: Within 4 hours. Example: Single malware detection on an isolated endpoint.
   - **P4 — Low:** Minor security event or policy violation. Response: Within 24 hours. Example: Clear desk violation, weak password found in a scan.

### 3.2 Incident Response Lifecycle
2. All security incidents shall follow the defined Incident Response Lifecycle:
   **Preparation → Identification → Containment → Eradication → Recovery → Post-Incident Review (PIR)**
3. Each phase shall have documented procedures, responsible roles, and completion criteria before progressing to the next phase.

### 3.3 Preparation (A.5.24)
4. An Incident Response Plan (IRP) shall be maintained, tested at minimum annually, and communicated to all members of the Incident Response Team (IRT).
5. The IRT shall be formally constituted and include representatives from: Security Operations, IT Infrastructure, Legal, HR, Communications/PR, and senior management (CISO as Incident Commander for P1/P2).
6. Incident response tooling shall be maintained in a ready state: forensic tools, communication channels (out-of-band if primary systems are compromised), contact lists, and pre-drafted notification templates.
7. Annual tabletop exercises and, for P1 scenarios, simulation drills shall be conducted; lessons learned shall be documented and fed into IRP updates.

### 3.4 Identification and Reporting (A.5.25 / A.6.8)
8. All employees and contractors are obligated to report suspected security events immediately via the designated reporting channel (security@teamcognito.com, ITSM portal, or emergency security hotline: [defined and published internally]).
9. The Security Operations team shall triage all reported events within defined SLAs: P1/P2 within 15 minutes; P3 within 4 hours; P4 within 24 hours.
10. Events shall be assessed to determine whether they constitute a security incident requiring escalation; the determination shall be documented.
11. Threat intelligence sources shall be monitored continuously to aid in proactive identification of incidents before they are reported.

### 3.5 Containment (A.5.26)
12. Immediate containment actions shall be taken to prevent the spread or escalation of an incident; containment strategies shall be pre-defined for common incident types (malware, account compromise, data breach, DDoS).
13. Containment actions shall be documented in real time in the incident log.
14. Short-term containment (e.g., isolating a compromised host) shall be prioritised over eradication to preserve forensic evidence; system shutdown shall be avoided unless strictly necessary.

### 3.6 Eradication and Recovery (A.5.26)
15. Root cause analysis shall be performed to understand how the incident occurred before eradication actions are taken.
16. Eradication shall remove all traces of the threat (malware, attacker persistence mechanisms, compromised credentials) before systems are returned to service.
17. Recovery shall include: system restoration from clean backups, re-imaging of compromised endpoints, password resets, patching of exploited vulnerabilities, and enhanced monitoring during the recovery period.
18. Return-to-service decisions for P1/P2 incidents shall require CISO sign-off.

### 3.7 Evidence Collection and Preservation (A.5.28)
19. Forensic evidence shall be collected in accordance with legally admissible standards: original evidence preserved (disk images, memory dumps, log exports) before any remediation actions where feasible.
20. Chain of custody records shall be maintained for all evidence collected.
21. Evidence shall be stored securely and access restricted to the investigation team and legal counsel.
22. Forensic activities on personal data shall comply with applicable privacy laws; legal counsel shall be consulted before conducting forensic analysis involving personal data.

### 3.8 Regulatory and Client Notification
23. For incidents involving personal data, the CISO and Legal team shall jointly assess whether notification obligations are triggered:
    - **CERT-In:** Mandatory reporting within **6 hours** of detecting a cybersecurity incident (per CERT-In Directions 2022).
    - **GDPR (EU):** Notification to supervisory authority within **72 hours**; notification to affected data subjects without undue delay if high risk.
    - **India DPDP Act 2023:** Notify the Data Protection Board and affected data principals of personal data breaches per prescribed timelines.
    - **Client contractual obligations:** Client contracts typically require breach notification within 24–72 hours; all active client contracts shall be reviewed to confirm specific obligations.
24. Client and regulatory notifications shall be approved by the CISO and Legal Counsel before dispatch.
25. A Breach Notification Register shall log all notifications made, including content, timestamp, and recipient.

### 3.9 Post-Incident Review (A.5.27)
26. A Post-Incident Review (PIR) shall be conducted for all P1 and P2 incidents within 10 business days of incident closure.
27. PIR outputs shall include: root cause analysis, incident timeline, effectiveness of response, identified gaps in controls or procedures, and a lessons-learned action plan with owners and due dates.
28. PIR findings shall be presented to the CISO and ISSC; significant findings shall trigger updates to the IRP, risk register, and relevant controls.
29. All incidents (P1–P4) shall be recorded in the Incident Register; aggregated incident statistics shall be reported to the ISSC quarterly.

### 3.10 Learning from Incidents (A.5.27)
30. Lessons learned shall be tracked in the GRC tool; completion of remediation actions shall be verified by the CISO.
31. Recurring incidents or patterns (e.g., repeated phishing successes in a particular team) shall trigger targeted awareness or technical control improvements.
32. Incident trends shall inform the annual risk assessment and security awareness training content.

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO (Incident Commander) | Lead P1/P2 response; approve notifications; chair PIR; present findings to ISSC |
| Security Operations (SOC) | Detect, triage, and technically respond to incidents; maintain incident log |
| IT Infrastructure Team | Implement containment, eradication, and recovery technical actions |
| Legal Counsel | Advise on notification obligations; manage regulatory interactions; preserve legal privilege over investigation |
| HR | Support investigations involving employees; administer disciplinary process |
| Communications/PR | Manage external communications and media enquiries; draft client notifications |
| Data Protection Officer (DPO) | Assess personal data breach notification requirements; liaise with regulators |
| All Employees & Contractors | Report suspected incidents immediately; cooperate with investigations; preserve evidence |
| Third-Party Suppliers | Notify Teamcognito within agreed SLAs (typically 24 hours) of incidents affecting Teamcognito data |

## 5. Controls and Procedures

### 5.1 Incident Response Plan (IRP)
- IRP document maintained in DMS (accessible offline via printed copy in CISO's office for use during system outage).
- IRP reviewed and updated at minimum annually, after each P1/P2 incident PIR, and after each tabletop exercise.
- IRP contains: contact lists, communication trees, incident classification guidance, containment playbooks for top-10 incident types, regulatory notification templates, and evidence collection procedures.

### 5.2 Incident Tracking
- All incidents logged in ITSM platform (e.g., Jira Service Management, ServiceNow) with: classification, timeline, actions taken, evidence references, notification log, and PIR outcome.
- Incident records retained for a minimum of 5 years.

### 5.3 Testing and Drills
- Annual tabletop exercise covering a P1 scenario; participants include IRT, CISO, Legal, and Communications.
- Phishing simulation (at least quarterly) tests the identification and reporting element of this policy.
- After each drill, a brief lessons-learned session documents improvements.

### 5.4 Regulatory Reporting Workflow
- CERT-In reporting portal details and template stored in IRP appendix.
- GDPR/DPA notification template pre-approved by Legal; CISO authorised to submit within 72 hours.
- Client notification template library maintained by Legal; customisable per incident and client.

## 6. Exceptions
There are no exceptions to the requirement to report and document security incidents. The incident response process may be adapted for low-severity incidents (P3/P4) with CISO approval, but documentation requirements apply to all incidents without exception.

## 7. Non-Compliance
Failure to report a known security incident or evidence of deliberate concealment of an incident is a serious violation of this policy and applicable law. Such conduct will result in immediate disciplinary action, up to and including termination, and potential referral to law enforcement. Regulatory penalties for late or non-reporting may also be attributed to responsible individuals.

## 8. References
- ISO/IEC 27001:2022 Annex A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 (Incident Management Controls)
- ISO/IEC 27002:2022
- CERT-In Directions on Cybersecurity 2022 (6-hour reporting requirement)
- India DPDP Act 2023 (breach notification obligations)
- GDPR Articles 33 and 34 (breach notification)
- NIST SP 800-61 Rev 2 (Computer Security Incident Handling Guide)
- SOC 2 TSC: CC7.3, CC7.4, CC7.5

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
