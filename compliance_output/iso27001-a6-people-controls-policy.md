---
organization: Teamcognito Solutions Pvt Ltd
framework: ISO27001
policy: iso27001-a6-people-controls-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# ISO 27001 People Controls Policy (Annex A.6)
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy defines the people-related information security controls that Teamcognito Solutions Pvt Ltd must implement to manage human risks across the full employment lifecycle — from pre-employment screening through to post-termination obligations. It is designed to ensure that personnel understand their information security responsibilities and are equipped to fulfil them, in alignment with ISO/IEC 27001:2022 Annex A.6.

## 2. Scope
This policy applies to all individuals who work for or on behalf of Teamcognito Solutions Pvt Ltd, including:
- Full-time and part-time employees
- Fixed-term and temporary staff
- Contractors, consultants, and agency workers
- Interns and graduate recruits
- Third-party personnel with access to Teamcognito systems or data

The policy covers all stages of the employment relationship: pre-hire screening, onboarding, ongoing employment, role changes, and offboarding.

## 3. Policy Statement

### 3.1 Pre-Employment Screening (A.6.1)
1. All candidates for employment or contractor engagement shall undergo background screening prior to being granted access to Teamcognito information assets.
2. Screening shall, at minimum, include: identity verification, right-to-work check, employment history verification (last 5 years), professional reference checks (minimum 2), and a criminal background check where legally permissible.
3. Screening for roles with access to Restricted or Confidential data shall include additional checks such as credit history (for financially sensitive roles) and education qualification verification.
4. Screening shall be conducted by HR or an approved third-party screening provider; results shall be documented and retained securely for the duration of employment plus 7 years.
5. Employment or engagement shall not commence until screening is satisfactorily completed; provisional access may only be granted with CISO approval and documented compensating controls.

### 3.2 Terms and Conditions of Employment (A.6.2)
6. Every employee and contractor shall sign an employment contract or engagement agreement that explicitly references information security responsibilities, data protection obligations, and adherence to Teamcognito's information security policies.
7. Security-related obligations (including confidentiality and acceptable use) shall be clearly stated as contractual conditions, not merely advisory.
8. Contractors shall sign a Confidentiality/Non-Disclosure Agreement (NDA) before commencing work; this NDA shall survive termination of the engagement.

### 3.3 Information Security Awareness, Education and Training (A.6.3)
9. All new hires shall complete mandatory information security awareness training within their first 5 business days of employment.
10. All personnel shall complete an annual refresher security awareness training programme; completion shall be tracked and reported to senior management quarterly.
11. Role-specific security training shall be provided to: developers (secure coding), system administrators (privileged access management), finance staff (social engineering/fraud), legal/HR (data protection and privacy), and incident responders (incident handling procedures).
12. Phishing simulation exercises shall be conducted at least quarterly; personnel who repeatedly fail simulations shall receive targeted remedial training.
13. Training completion records shall be maintained in the Learning Management System (LMS) and available for audit at any time.
14. Training content shall be reviewed and updated annually to reflect the current threat landscape.

### 3.4 Disciplinary Process (A.6.4)
15. A formal, documented disciplinary process shall exist and be applicable to all personnel who violate information security policies.
16. The severity of disciplinary action shall be proportionate to the nature, frequency, and impact of the violation, ranging from a written warning to termination of employment or engagement.
17. Intentional or malicious violations (e.g., data exfiltration, sabotage, fraud) shall be treated as gross misconduct and may result in immediate dismissal and referral to law enforcement.
18. All disciplinary actions related to information security shall be documented by HR and retained confidentially.

### 3.5 Responsibilities After Termination or Change of Employment (A.6.5)
19. Information security obligations — including confidentiality, intellectual property protection, and non-disclosure — shall survive the termination or change of employment.
20. Upon any role change, access rights shall be reviewed and adjusted to reflect new responsibilities within 24 hours. Access no longer required shall be revoked immediately.
21. Departing employees shall attend an offboarding session covering their post-employment security obligations before their last day.

### 3.6 Confidentiality and Non-Disclosure Agreements (A.6.6)
22. All employees, contractors, and third parties with access to Teamcognito confidential information shall sign an NDA.
23. NDAs shall be reviewed by Legal to ensure enforceability under applicable jurisdiction, coverage of all relevant information categories, and appropriate duration (minimum 3 years post-engagement).
24. NDA registers shall be maintained by HR and Legal and reviewed annually.

### 3.7 Remote Working (A.6.7)
25. Remote working is permitted only for approved roles and subject to compliance with the Remote Working Security Standard.
26. Remote workers shall use only company-approved and managed devices; use of personal devices for processing Confidential or Restricted information is prohibited without MDM enrolment and formal approval.
27. All remote connections to Teamcognito systems must use an approved, encrypted VPN or Zero Trust Network Access (ZTNA) solution.
28. Remote workers are responsible for maintaining a physically secure workspace; sensitive screens must not be visible to unauthorised persons.
29. Unattended screens must be locked (auto-lock set to maximum 5 minutes); devices must be encrypted with full-disk encryption enabled.
30. Public/unsecured Wi-Fi networks must not be used to access Teamcognito systems without VPN protection.

### 3.8 Information Security Event Reporting (A.6.8)
31. All employees and contractors are obligated to report any suspected or confirmed information security event or weakness as soon as they become aware of it — without fear of reprisal for good-faith reporting.
32. Reporting channels shall include: a dedicated security email (security@teamcognito.com), a ticketing portal, and an emergency hotline for critical incidents.
33. The organisation shall maintain a published, easy-to-find guide on "How to Report a Security Incident" accessible to all personnel.
34. Anonymous reporting mechanisms shall be available via the whistleblowing/ethics hotline.
35. The Security team shall acknowledge all reported events within 2 hours and provide an initial triage outcome within 4 hours.

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO | Own this policy; set training requirements; approve exceptions; oversee disciplinary cases |
| HR Director | Conduct screening; manage employment contracts; lead offboarding; administer disciplinary process |
| Line Managers | Ensure team members complete training; report security concerns; manage access change requests on role change |
| IT/Security Team | Provision/revoke access; deploy and monitor endpoint controls; manage remote access tools; respond to reported events |
| Legal Counsel | Draft and review NDAs; advise on post-employment obligations; manage regulatory interactions |
| All Employees & Contractors | Complete mandatory training; sign NDAs/AUP; report security events; comply with remote working security requirements |
| Internal Audit | Verify training completion rates; test offboarding process effectiveness; review screening records |

## 5. Controls and Procedures

### 5.1 Onboarding Process
- HR triggers an onboarding workflow in the ITSM system upon offer acceptance.
- IT provisions accounts only after HR confirms satisfactory background checks.
- New starter training assigned automatically via LMS on day 1.
- All new starters sign: Employment Contract, AUP, NDA, and Remote Working Agreement (if applicable) before system access is granted.

### 5.2 Offboarding Process
- Manager submits leaver request in ITSM at minimum 5 business days before departure.
- IT revokes all access on the leaver's last working day (or immediately for involuntary terminations).
- IT retrieves all company devices, tokens, and access cards.
- HR conducts exit interview covering post-employment security obligations.
- CISO reviews access revocation completion within 2 business days of departure.

### 5.3 Security Awareness Programme
- Annual programme delivered via LMS; modules updated by Security team each January.
- Phishing simulations conducted by Security team using approved platform (e.g., KnowBe4, Proofpoint Security Awareness).
- Metrics reported quarterly to CISO: training completion rate (target: ≥95%), phishing click rate (target: <5%).

### 5.4 Remote Working Controls
- MDM solution (e.g., Microsoft Intune, Jamf) enforces full-disk encryption, screen lock, and remote wipe capability on all endpoints.
- VPN/ZTNA enforced via policy; non-compliant devices blocked from accessing corporate resources.
- Remote working risk assessments reviewed annually.

## 6. Exceptions
Exceptions to this policy (e.g., expedited access before full screening completion) must be submitted to the CISO and HR Director with documented business justification, risk assessment, and compensating controls. Approved exceptions shall be logged in the exception register and are valid for a maximum of 30 days unless formally extended.

## 7. Non-Compliance
Failure to comply with this policy may result in disciplinary action up to and including termination of employment. HR and Legal shall be involved in all disciplinary proceedings. Violations involving criminal conduct (e.g., data theft, fraud) shall be reported to law enforcement.

## 8. References
- ISO/IEC 27001:2022 Annex A.6.1 through A.6.8 (all People Controls)
- ISO/IEC 27002:2022 (implementation guidance)
- India DPDP Act 2023
- GDPR Articles 5, 25, 32 (where applicable)
- Teamcognito Acceptable Use Policy
- Teamcognito Remote Working Security Standard
- SOC 2 TSC: CC1.1, CC1.4, CC1.5, CC2.2, CC6.2, CC6.3, CC6.5

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
