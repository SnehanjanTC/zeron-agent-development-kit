---
organization: Teamcognito Solutions Pvt Ltd
framework: ISO27001
policy: iso27001-a8-technological-controls-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# ISO 27001 Technological Controls Policy (Annex A.8)
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy establishes the technological security controls required to protect Teamcognito Solutions Pvt Ltd's information systems, networks, applications, and data. It covers the full spectrum of technical security controls across endpoint devices, access, cryptography, vulnerability management, development security, and operational monitoring — in alignment with ISO/IEC 27001:2022 Annex A.8 (34 controls).

## 2. Scope
This policy applies to all information technology assets owned, leased, or managed by Teamcognito Solutions Pvt Ltd, including: employee endpoints, servers, cloud infrastructure, network devices, applications, development environments, and any third-party systems that interface with Teamcognito data. It applies to all technical staff, developers, system administrators, and any personnel interacting with the technology estate.

## 3. Policy Statement

### 3.1 User Endpoint Devices (A.8.1)
1. All endpoint devices (laptops, desktops, mobile phones, tablets) used to access Teamcognito systems must be enrolled in the organisation's Mobile Device Management (MDM) solution and comply with the Endpoint Security Standard.
2. Endpoints shall have full-disk encryption, approved antivirus/EDR, automatic OS and application patching, and screen lock enforced via MDM policy.
3. Personal (BYOD) devices are not permitted to access Teamcognito corporate data unless enrolled in MDM and meeting all endpoint security baseline requirements.

### 3.2 Privileged Access Rights (A.8.2)
4. Privileged access (administrator, root, service accounts) shall be managed through a Privileged Access Management (PAM) solution; no direct privileged access to production systems without PAM intermediation.
5. Privileged access shall be granted on a just-in-time (JIT) basis where technically feasible; standing privileged accounts are prohibited except for approved break-glass scenarios.
6. All privileged sessions shall be recorded and logs retained for a minimum of 12 months.
7. Privileged accounts shall not be used for day-to-day activities; administrators shall maintain separate accounts for privileged and standard operations.

### 3.3 Information Access Restriction (A.8.3)
8. Access to information and application functions shall be restricted in accordance with the Access Control Policy, following the principle of least privilege and need-to-know.
9. Role-Based Access Control (RBAC) shall be implemented across all critical systems; access roles shall be documented and reviewed quarterly.

### 3.4 Access to Source Code (A.8.4)
10. Access to source code repositories shall be restricted to authorised developers; access shall be managed via RBAC in the version control system (e.g., GitHub, GitLab, Bitbucket).
11. Production source code branches shall be protected; direct commits to main/master without peer review are prohibited.
12. Source code access rights shall be reviewed at minimum every 90 days and revoked immediately upon role change or departure.

### 3.5 Secure Authentication (A.8.5)
13. Multi-factor authentication (MFA) is mandatory for all user accounts accessing corporate systems, with no exceptions for remote access, cloud services, and privileged accounts.
14. Passwords shall meet minimum complexity requirements: at least 14 characters, including upper/lowercase, numbers, and special characters; passwords shall not be reused within 12 cycles.
15. Single Sign-On (SSO) shall be implemented for all corporate applications where technically feasible; credentials shall not be stored in browsers or plain-text files.
16. Account lockout shall activate after 5 consecutive failed authentication attempts; lockout duration shall be a minimum of 30 minutes or require administrator unlock for privileged accounts.

### 3.6 Capacity Management (A.8.6)
17. Capacity and performance of all critical information processing systems shall be monitored continuously; thresholds shall trigger automated alerts at 75% utilisation for proactive planning.
18. Capacity planning reviews shall be conducted quarterly; projections shall account for at least 12 months of expected growth.
19. Capacity management activities shall be documented and feed into the Business Continuity Plan.

### 3.7 Protection Against Malware (A.8.7)
20. All endpoints, servers, and email gateways shall be protected by approved, up-to-date antivirus and Endpoint Detection and Response (EDR) software.
21. Malware protection tools shall perform real-time scanning and shall update threat intelligence signatures at minimum every 4 hours.
22. Any malware detection shall generate an automated alert and an ITSM incident ticket; the Security team shall triage all detections within 1 hour.
23. Use of removable media is restricted; USB autorun is disabled on all endpoints via Group Policy/MDM.

### 3.8 Management of Technical Vulnerabilities (A.8.8)
24. Automated vulnerability scanning shall be performed against all internal and external-facing systems at minimum weekly (internal) and monthly (external/authenticated).
25. Critical vulnerabilities (CVSS ≥ 9.0) shall be remediated within 24 hours; High (CVSS 7.0–8.9) within 7 days; Medium (CVSS 4.0–6.9) within 30 days; Low within 90 days.
26. A vulnerability management programme shall include: asset discovery, scanning, prioritisation, remediation tracking, and exception management.
27. External penetration testing shall be conducted annually by a qualified third party; critical findings shall be remediated before the test report is closed.
28. Bug bounty or responsible disclosure programme shall be maintained for externally exposed services.

### 3.9 Configuration Management (A.8.9)
29. Security-hardened configuration baselines shall be established and enforced for all system types (servers, endpoints, network devices, cloud resources) based on CIS Benchmarks or equivalent.
30. Configuration drift shall be detected by automated tools (e.g., Chef, Ansible, AWS Config, Azure Policy); non-compliant configurations shall generate alerts and be remediated within defined SLAs.
31. Configuration changes shall be managed through the Change Management process (see A.8.32).

### 3.10 Information Deletion (A.8.10)
32. Information that is no longer required shall be securely deleted in accordance with retention schedules defined in the Data Retention Policy.
33. Deletion of Confidential or Restricted data shall be logged and, for data subject to regulatory requirements, certificates of deletion issued.

### 3.11 Data Masking (A.8.11)
34. Personal data and sensitive information used in non-production environments (development, testing, QA) shall be masked or anonymised before use.
35. Data masking techniques shall be appropriate to the sensitivity of the data; masking shall be verified before data is loaded into non-production environments.

### 3.12 Data Leakage Prevention (A.8.12)
36. Data Loss Prevention (DLP) controls shall be implemented at endpoint, email, and web gateway levels to detect and prevent the unauthorised transfer of sensitive information.
37. DLP policies shall be tuned based on data classification; alerts shall be reviewed by the Security team within 4 hours.
38. Transfer of Restricted data to personal cloud storage, personal email, or unapproved external services is prohibited and shall be technically blocked where possible.

### 3.13 Information Backup (A.8.13)
39. All critical business data, system configurations, and application data shall be backed up according to defined Recovery Point Objectives (RPO); default RPO is 24 hours.
40. Backup copies shall be stored in geographically separate locations (minimum one off-site or cloud-based copy).
41. Backup integrity shall be tested through restoration tests at minimum quarterly; results shall be documented and reported to the CISO.
42. Backups of Confidential and Restricted data shall be encrypted; encryption keys shall be managed separately from the backup data.

### 3.14 Redundancy of Information Processing Facilities (A.8.14)
43. Critical systems shall be architected with appropriate redundancy (e.g., active-active, active-passive, multi-AZ cloud deployments) to meet Recovery Time Objectives (RTO) as defined in the BCP/DRP.
44. Redundancy configurations shall be tested during annual DR exercises.

### 3.15 Logging (A.8.15)
45. Audit logs shall be generated, maintained, and protected for all critical systems, applications, and security tools.
46. Log retention shall be a minimum of 12 months online/searchable, with a further 12 months in cold storage (24 months total for regulated systems).
47. Logs shall capture at minimum: user login/logout events, privileged access events, system changes, failed authentication attempts, and data access events.
48. Log integrity shall be protected; logs must not be modifiable by non-security personnel; centralised SIEM ingestion is mandatory for all critical systems.

### 3.16 Monitoring Activities (A.8.16)
49. A Security Information and Event Management (SIEM) solution shall provide continuous monitoring of security events across the technology estate.
50. Security Operations Centre (SOC) monitoring shall operate on a 24/7 basis, either in-house or through a Managed SOC provider.
51. Use-case and detection rules shall be reviewed and updated quarterly; Mean Time to Detect (MTTD) target is <1 hour for critical events.

### 3.17 Clock Synchronisation (A.8.17)
52. All systems shall synchronise their clocks to a consistent, authoritative NTP source (e.g., NTP pool servers with Stratum 2 reliability); time deviation shall not exceed 1 second.
53. Clock synchronisation shall be monitored; failures shall be alerted and remediated within 1 hour (clock drift invalidates log forensics).

### 3.18 Use of Privileged Utility Programs (A.8.18)
54. The use of utility programs capable of bypassing system and application controls (e.g., debugging tools, network sniffers, raw disk editors) shall be restricted to authorised personnel and governed by the PAM process.
55. Use of privileged utility programs on production systems shall require change management approval.

### 3.19 Installation of Software on Operational Systems (A.8.19)
56. Software installation on operational (production) systems shall require formal change management approval.
57. Only software from the approved software catalogue shall be installed on Teamcognito endpoints; endpoint management tools shall block or alert on unapproved software installations.
58. A Software Bill of Materials (SBOM) shall be maintained for all internally developed applications.

### 3.20 Network Security (A.8.20 / A.8.21 / A.8.22)
59. Networks shall be segmented into security zones (e.g., DMZ, internal, production, development) using firewalls and network access controls; inter-zone traffic shall be explicitly permitted and all other traffic denied by default.
60. Network security shall include: stateful firewalls, IDS/IPS, web application firewalls (WAF) for externally exposed services, and network-based DLP.
61. Network security services (firewalls, load balancers, DNS) shall be documented in a network diagram reviewed and updated at minimum annually.
62. Third-party and guest network access shall be isolated from the internal network; guests shall access only the internet via a separate VLAN.

### 3.21 Web Filtering (A.8.23)
63. Web filtering shall be implemented to block access to malicious, inappropriate, or prohibited web categories from corporate endpoints.
64. Web filtering policies shall be reviewed quarterly; overrides shall require manager approval and shall be logged.

### 3.22 Use of Cryptography (A.8.24)
65. All data classified as Confidential or Restricted shall be encrypted at rest (AES-256 or equivalent) and in transit (TLS 1.2 minimum; TLS 1.3 preferred).
66. Encryption key management shall follow a documented key management procedure: key generation, storage (HSM or approved KMS), rotation (at minimum annually for symmetric keys), and secure destruction.
67. Use of deprecated or weak cryptographic algorithms (MD5, SHA-1, DES, RC4, TLS 1.0/1.1) is prohibited.
68. SSL/TLS certificates shall be managed through a centralised certificate management system; certificates shall be renewed at minimum 30 days before expiry.

### 3.23 Secure Development (A.8.25 – A.8.30)
69. A Secure Software Development Lifecycle (SSDLC) shall be followed for all internally developed software; security requirements shall be defined, security design reviews conducted, and security testing mandatory before release.
70. Developers shall receive training in secure coding practices annually; an OWASP Top 10 and SANS Top 25 awareness programme is mandatory for all developers.
71. Static Application Security Testing (SAST) and Software Composition Analysis (SCA) tools shall be integrated into CI/CD pipelines; builds with critical security findings shall not be promoted to production.
72. Dynamic Application Security Testing (DAST) and penetration testing shall be conducted for all externally exposed applications before major releases.
73. Outsourced development shall be subject to security requirements equivalent to internal development; code escrow and source code review rights shall be included in outsourcing contracts.

### 3.24 Test Information (A.8.33)
74. Production data shall not be used in test or development environments; masked or synthetically generated data shall be used instead.
75. Where production data must be used in testing for business-critical reasons, a formal exception shall be approved by the CISO with appropriate data handling controls in place.

### 3.25 Separation of Environments (A.8.31)
76. Development, testing/staging, and production environments shall be strictly separated; personnel with access to one environment shall not have uncontrolled access to another.
77. Automated pipelines shall enforce the promotion process; manual production deployments without change management approval are prohibited.

### 3.26 Change Management (A.8.32)
78. All changes to production systems shall be managed through a formal Change Management Process: Request → Review → Approval → Test → Deploy → Review.
79. Emergency changes shall follow an expedited but documented process; post-change review is mandatory within 24 hours.
80. A Change Advisory Board (CAB) shall review and approve significant/high-risk changes.

### 3.27 Protection of Systems During Audit Testing (A.8.34)
81. Security audit tools and techniques shall not be deployed against production systems without formal authorisation from the CISO and system owner.
82. Audit testing shall be conducted in dedicated audit accounts/environments where possible; testing scope, methodology, and schedule shall be agreed in advance.

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO | Own this policy; approve exceptions; oversee vulnerability management programme; chair CAB |
| IT/Security Team | Implement and maintain all technical controls; manage SIEM, EDR, DLP, PAM; conduct vulnerability scans |
| Development Team Lead | Enforce SSDLC; ensure secure coding standards; manage source code access |
| Cloud/Infrastructure Team | Maintain hardening baselines; manage cloud security posture; network segmentation |
| DevOps/Platform Team | Integrate SAST/DAST in CI/CD; manage configuration-as-code; enforce deployment controls |
| Change Manager | Administer change management process; chair CAB; maintain change log |
| All Technical Staff | Follow secure coding and configuration standards; report vulnerabilities; complete mandatory training |

## 5. Controls and Procedures

### 5.1 Vulnerability Management
- Automated scanners (e.g., Tenable, Qualys) scan all in-scope assets weekly.
- Vulnerability register maintained in GRC tool with ownership, SLA tracking, and risk acceptance.
- Monthly vulnerability management report provided to CISO.

### 5.2 SIEM & Monitoring
- SIEM platform (e.g., Splunk, Microsoft Sentinel) ingests logs from all Tier-1 assets.
- SOC alert triage workflow documented with escalation paths.
- MTTD and MTTR KPIs reported to CISO monthly.

### 5.3 Cryptography
- Key Management Policy documented and enforced via approved KMS (e.g., AWS KMS, Azure Key Vault, HashiCorp Vault).
- Certificate inventory maintained; automated renewal alerts configured.

### 5.4 Backup and Recovery
- Backup schedule, retention, and encryption documented per system in the CMDB.
- Quarterly restore tests conducted and results signed off by system owners.

## 6. Exceptions
Technical control exceptions (e.g., legacy system unable to support TLS 1.2+, temporary MFA bypass) must be approved by the CISO, documented with compensating controls, and reviewed every 30 days. No exception shall remain open for more than 90 days without escalation to the CTO and CEO.

## 7. Non-Compliance
Non-compliance with technological controls — including bypassing security tools, disabling endpoint protection, or exploiting access beyond authorised levels — shall result in immediate investigation and disciplinary action. Intentional circumvention of security controls may constitute gross misconduct or criminal behaviour.

## 8. References
- ISO/IEC 27001:2022 Annex A.8.1 through A.8.34 (all Technological Controls)
- ISO/IEC 27002:2022
- NIST Cybersecurity Framework (CSF) 2.0
- CIS Controls v8
- OWASP Top 10 (latest edition)
- NIST SP 800-53 (AC, CM, SI, AU control families)
- SOC 2 TSC: CC5, CC6, CC7, CC8, CC9, A1, PI1, C1

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
