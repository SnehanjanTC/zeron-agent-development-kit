---
organization: Teamcognito Solutions Pvt Ltd
framework: SOC2
policy: soc2-change-management-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# SOC 2 Change Management Policy
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy establishes Teamcognito Solutions Pvt Ltd's controls for managing changes to production systems, applications, infrastructure, and configurations. Effective change management reduces the risk of service disruptions, security vulnerabilities, and processing integrity failures introduced by uncontrolled or poorly tested changes. This policy supports SOC 2 CC8.1 and ISO/IEC 27001:2022 Annex A.8.32, and is a critical General IT Control (GITC) evaluated during SOC 2 examinations.

## 2. Scope
This policy applies to all changes to:
- Production application code and software releases
- Production infrastructure (servers, cloud resources, containers, databases)
- Network configurations (firewalls, routers, load balancers, VPNs)
- Operating systems and middleware on production systems
- Security configurations (IAM policies, firewall rules, encryption settings)
- Third-party integrations and API configurations
- Database schemas and stored procedures in production

It applies to all personnel who initiate, review, approve, implement, or verify changes, including developers, system administrators, DevOps engineers, and third-party vendors with change access.

## 3. Policy Statement

### 3.1 Change Categories and Approval Levels
1. All changes to in-scope systems shall be classified into one of three categories:
   - **Standard Change:** Pre-approved, low-risk, repeatable changes following a documented and tested procedure (e.g., routine certificate renewal, approved patch deployment). No CAB review required; requires implementation team lead sign-off.
   - **Normal Change:** Planned changes with a known scope and risk profile. Require Change Advisory Board (CAB) review and approval before implementation. Test evidence required.
   - **Emergency Change:** Urgent changes required to prevent or resolve a Critical (P1) or High (P2) incident, or to address a Critical security vulnerability. Follow expedited approval process; post-implementation CAB review required within 24 hours.

2. Changes shall not be implemented in production without the required level of approval; implementing unapproved changes is a serious policy violation.

### 3.2 Change Request Process (CC8.1)
3. All Normal and Emergency changes shall be formally requested via the ITSM platform (e.g., Jira Service Management, ServiceNow) using the Change Request form, including:
   - Description of the change and business justification
   - Affected systems and components
   - Risk assessment (impact and likelihood of service disruption or security impact)
   - Rollback plan
   - Test plan and test results (for Normal changes)
   - Implementation schedule and maintenance window
   - Named implementer and approver

4. Change Requests shall be reviewed and approved by the Change Advisory Board (CAB), which shall meet at minimum weekly (or on-demand for urgent Normal changes).

5. CAB composition: CISO (or delegate), CTO (or delegate), Head of Engineering, relevant system owner, and Change Manager. Security-impacting changes require CISO attendance or sign-off.

6. Changes with potential security impact (IAM policy changes, firewall rule changes, cryptographic changes, code changes to security-critical functions) shall require explicit CISO approval regardless of change category.

### 3.3 Testing Requirements
7. All Normal changes shall include documented test results demonstrating the change functions as intended and does not introduce regressions.
8. Testing shall be conducted in a non-production environment (staging/UAT) that is representative of production; production data shall not be used in test environments (see Data Masking Policy).
9. Security testing requirements by change type:
   - **Application code changes:** SAST scan with no critical or high findings; peer code review by at least one security-aware developer.
   - **Infrastructure changes:** Security configuration review against hardening baseline.
   - **Major releases:** DAST scan and, where applicable, penetration test.
10. Test results shall be attached to the Change Request in the ITSM; changes without documented test evidence shall not be approved.

### 3.4 Separation of Duties
11. The person who develops or requests a change shall not be the same person who approves and deploys the change to production; separation of duties shall be enforced in the CI/CD pipeline and ITSM.
12. Production deployment access shall be restricted to the authorised deployment pipeline or designated release engineers; direct developer access to production is prohibited except via the PAM tool in approved emergency scenarios.

### 3.5 CI/CD Pipeline Controls
13. All production deployments shall be performed through the automated CI/CD pipeline; manual deployments outside the pipeline are prohibited (except emergency changes using PAM-controlled access with full audit trail).
14. The CI/CD pipeline shall enforce: automated SAST scanning, peer code review approval, successful test suite execution, and authorised approver sign-off before deployment to production.
15. Pipeline configurations shall be version-controlled and any changes to pipeline configurations shall themselves be subject to the change management process.

### 3.6 Post-Implementation Review
16. All Normal changes shall include a post-implementation review confirming: the change was implemented as planned, system functionality is confirmed, no unexpected impacts observed, and the change is marked as successfully closed in the ITSM.
17. Emergency changes shall be reviewed by the CAB at the next scheduled meeting (or within 24 hours for P1-related emergency changes); review shall confirm the change is appropriate and identify whether a permanent fix is required.
18. Failed changes (requiring rollback) shall trigger an incident ticket and root cause analysis.

### 3.7 Change Metrics and Reporting
19. Change management KPIs shall be tracked and reported monthly to the CISO:
    - Total changes by category (Standard / Normal / Emergency)
    - Change success rate (target: >95%)
    - Emergency change rate (target: <5% of all changes)
    - Failed changes requiring rollback (target: <2%)
    - Unauthorised changes detected (target: 0)
    - Average change lead time (Normal changes)
20. Trends in emergency changes or failures shall be investigated; systemic issues shall be addressed through process or tooling improvements.

### 3.8 Unauthorised Change Detection
21. Configuration monitoring tools (e.g., AWS Config, Azure Policy, Chef/Ansible drift detection) shall detect and alert on configuration changes that did not go through the approved change management process.
22. Alerts for unauthorised changes shall be treated as security incidents and investigated within 4 hours; unauthorised changes shall be rolled back unless confirmed safe by the CISO.
23. File integrity monitoring (FIM) shall be implemented on critical production servers to detect unauthorised file changes.

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO | Approve security-impacting changes; review unauthorised change incidents; oversee change management policy |
| Change Manager | Administer CAB; maintain change calendar; track change metrics; report to CISO |
| Change Advisory Board (CAB) | Review and approve Normal changes; conduct post-implementation reviews for Emergency changes |
| Developers / Engineers | Submit Change Requests; conduct testing; perform code reviews; implement changes via pipeline |
| DevOps / Platform Team | Maintain CI/CD pipeline; enforce pipeline controls; implement configuration monitoring |
| System Owners | Approve changes affecting their systems; participate in post-implementation review |
| Internal Audit | Audit sample of changes for compliance with this policy; report findings to CISO |

## 5. Controls and Procedures

### 5.1 Change Management Workflow
1. Developer creates Change Request in ITSM.
2. Automated risk scoring applied based on change type and affected systems.
3. Change routed to appropriate approval level (Standard → team lead; Normal → CAB; Emergency → expedited approval chain).
4. For Normal changes: test evidence reviewed; CAB approval obtained; implementation scheduled in change calendar.
5. Change implemented via CI/CD pipeline or authorised procedure.
6. Post-implementation verification completed; change ticket closed.
7. CAB reviews metrics weekly; Change Manager generates monthly report.

### 5.2 Emergency Change Process
1. P1/P2 incident or critical vulnerability triggers Emergency Change Request.
2. CISO or delegate provides emergency approval (documented in ITSM).
3. Implementation performed via PAM-controlled access with session recording if pipeline bypass required.
4. Full documentation completed within 2 hours of implementation.
5. CAB post-implementation review within 24 hours.

### 5.3 Evidence Retention
- All Change Request records (including approvals, test evidence, deployment logs) retained in ITSM for minimum 24 months (for SOC 2 examination evidence).
- CI/CD pipeline logs retained for minimum 12 months.
- CAB meeting minutes retained for minimum 24 months.

## 6. Exceptions
Exceptions to the change management process (e.g., production hotfix without full CAB review) require immediate CISO notification and must be documented within 2 hours of the change being applied. Repeated exceptions by the same team or individual shall be treated as a compliance issue and escalated to the ISSC.

## 7. Non-Compliance
Implementing unapproved changes to production systems is a serious violation of this policy and represents a potential SOC 2 control failure. Such incidents shall be investigated, documented, and escalated to the CISO. Disciplinary action, up to and including termination, may follow for intentional bypass of change controls.

## 8. References
- SOC 2 TSC: CC8.1 (Change Management), CC3.4, CC7.1
- ISO/IEC 27001:2022 Annex A.8.32 (Change Management), A.8.9 (Configuration Management), A.8.31 (Separation of Environments)
- ITIL v4 (Change Enablement practice)
- NIST SP 800-53 CM (Configuration Management) control family

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
