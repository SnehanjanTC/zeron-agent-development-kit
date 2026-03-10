---
organization: Teamcognito Solutions Pvt Ltd
framework: SOC2
policy: soc2-vendor-management-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# SOC 2 Vendor Management Policy
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy establishes Teamcognito Solutions Pvt Ltd's framework for managing information security and privacy risks associated with third-party vendors, suppliers, and business partners. Third-party relationships introduce significant risk — including supply chain attacks, data exposure, and service availability impacts — and must be governed through a consistent, risk-based vendor management programme. This policy supports SOC 2 CC9.2, ISO 27001 Annex A.5.19–A.5.23, and applicable regulatory obligations.

## 2. Scope
This policy applies to all third-party vendors, suppliers, sub-processors, and business partners that:
- Access, process, store, or transmit Teamcognito or client information
- Provide systems, services, or infrastructure that are part of the SOC 2 service system
- Are integrated with Teamcognito's production, development, or corporate IT environments
- Have the potential to impact Teamcognito's information security posture or service availability

It applies to all business units responsible for engaging, managing, or terminating vendor relationships.

## 3. Policy Statement

### 3.1 Vendor Onboarding and Risk Assessment
1. No vendor shall be granted access to Teamcognito systems or data without completing the formal vendor onboarding process, including a security risk assessment.
2. Vendor risk assessments shall be tiered based on the vendor's access level and criticality:
   - **Tier 1 (Critical):** Direct access to client data, core production systems, or financial systems. Full security assessment required, including: SIG Lite questionnaire, review of current ISO 27001/SOC 2 certification, and IT security interview. Assessment must be completed and approved by CISO before engagement.
   - **Tier 2 (High):** Access to internal systems or Confidential data. Simplified security questionnaire + review of available certifications.
   - **Tier 3 (Standard):** No access to sensitive data or systems (e.g., office supplies, catering). Basic due diligence only.
3. All Tier-1 and Tier-2 vendors must provide evidence of current information security certifications (e.g., ISO 27001, SOC 2 Type II) or accept a right-to-audit clause in their contract.
4. Vendor risk assessment results shall be documented in the Supplier Risk Register with assigned risk ratings.

### 3.2 Contractual Security Requirements
5. All vendor contracts shall include mandatory security provisions, covering at minimum:
   - Confidentiality and data handling obligations
   - Data processing agreement (DPA) where vendor processes personal data
   - Security incident notification obligation (within 24 hours of discovery)
   - Right-to-audit clause (for Tier-1 vendors)
   - Compliance with applicable laws (DPDP Act, GDPR as applicable)
   - Business continuity and disaster recovery requirements (for Tier-1 vendors)
   - Data return or secure deletion upon contract termination
   - Sub-contractor restrictions (must notify Teamcognito before engaging sub-contractors who access Teamcognito data)
6. Security provisions in vendor contracts shall be reviewed by Legal before execution; the CISO shall approve security terms for Tier-1 vendor contracts.
7. Any vendor contract that does not include required security provisions shall not be executed until terms are agreed; exceptions require CISO approval.

### 3.3 Ongoing Vendor Monitoring
8. Tier-1 vendors shall be reviewed annually; review shall include: updated security questionnaire, review of current certifications, review of any incidents or breaches involving the vendor, and assessment of any material changes to the vendor's services.
9. Tier-2 vendors shall be reviewed every two years, or more frequently if the risk profile changes.
10. Vendors shall be monitored for publicly reported security incidents, data breaches, or certification lapses; the Security team shall subscribe to threat intelligence sources covering key vendors.
11. The Supplier Risk Register shall be maintained in the GRC tool; risk ratings shall be updated following each review.
12. Vendor performance against contractual security requirements shall be assessed during annual reviews; non-compliance shall be raised as a contractual issue and tracked to resolution.

### 3.4 Sub-Processor Management (Privacy)
13. All sub-processors (vendors processing personal data on Teamcognito's behalf) shall be listed in the organisation's Privacy Notice and sub-processor register.
14. New sub-processors shall be notified to clients with the contractually agreed notice period (default: 30 days) before access to client personal data is granted.
15. Sub-processors shall be subject to data processing agreements (DPAs) that impose obligations equivalent to those applicable to Teamcognito under applicable privacy laws.

### 3.5 Vendor Access Management
16. Vendor access to Teamcognito systems shall be provisioned on a least-privilege, time-limited basis; access shall be reviewed and revoked upon completion of the engagement task or contract termination.
17. Vendor access shall be facilitated through the standard IAM process; shared credentials for vendor access are prohibited.
18. Vendors with remote access shall use MFA and an approved connection method (VPN/ZTNA); unencrypted remote access is prohibited.
19. Vendor sessions on production systems shall be logged; PAM tools shall record sessions for Tier-1 vendors with access to critical systems.

### 3.6 Vendor Offboarding
20. Upon contract termination, vendor access (logical and physical) shall be revoked within 4 hours of notification.
21. Vendor data return or secure deletion shall be confirmed in writing within 30 days of contract termination; Certificates of Destruction shall be obtained for Restricted data.
22. Active vendor contracts and access permissions shall be audited quarterly; any vendor with active access but no active contract shall be treated as an exception and access revoked immediately pending investigation.

### 3.7 ICT Supply Chain Risk (A.5.21)
23. Critical dependencies in the ICT supply chain shall be identified and documented; single-point-of-failure vendor dependencies shall be flagged as high risk and mitigated through contractual SLAs, alternative sourcing plans, or technical redundancy.
24. The organisation shall maintain a Business Impact Assessment for all Tier-1 vendors, documenting the impact of the vendor becoming unavailable.

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO | Own vendor management policy; approve Tier-1 vendor assessments; review supplier risk register |
| Procurement / Vendor Manager | Manage vendor lifecycle; ensure security terms in contracts; conduct annual reviews |
| Legal Counsel | Review and negotiate vendor contracts; ensure DPAs are in place; advise on regulatory requirements |
| DPO | Manage sub-processor register; assess privacy implications of new vendors |
| IT/Security Team | Provision/revoke vendor access; monitor vendor sessions; assess technical security questionnaire responses |
| Business Unit Owners | Identify vendor requirements; participate in vendor reviews; escalate vendor performance concerns |

## 5. Controls and Procedures

### 5.1 Vendor Onboarding Workflow
- New vendor request submitted via procurement portal.
- Automatic tier classification based on data access type and system criticality.
- Security questionnaire sent automatically to vendor; response reviewed by Security team.
- Risk assessment report generated and reviewed by CISO (Tier-1) or IT Manager (Tier-2).
- Go/no-go decision documented in vendor record; approval required before contract execution.

### 5.2 Supplier Risk Register
- Maintained in GRC tool; includes: vendor name, tier, risk rating, last assessment date, certification status, open findings, contract expiry.
- Reviewed monthly by Procurement; quarterly by CISO.
- Automated alerts when vendor certifications expire or reviews are overdue.

### 5.3 Annual Vendor Review Process
- Procurement sends updated questionnaire to Tier-1 vendors each January.
- Security team reviews responses and updates risk ratings by end of February.
- Summary report provided to CISO and ISSC by end of March.

## 6. Exceptions
Engaging a vendor without completing the required tier assessment requires written CISO approval with documented compensating controls. This exception must be resolved within 60 days; if the full assessment cannot be completed within 60 days, the vendor engagement shall be suspended until assessment is complete.

## 7. Non-Compliance
Engaging vendors without completing the required onboarding process, or failing to maintain contractual security requirements, shall be treated as a significant compliance gap for SOC 2 purposes. Business units that engage vendors in breach of this policy shall be subject to internal audit investigation. Financial and reputational consequences of vendor security incidents attributed to inadequate oversight may be the responsibility of the engaging business unit.

## 8. References
- SOC 2 TSC: CC9.2 (Vendor and Business Partner Risk), CC6.6, CC6.7
- ISO/IEC 27001:2022 Annex A.5.19, A.5.20, A.5.21, A.5.22, A.5.23
- India DPDP Act 2023 (sub-processor obligations)
- GDPR Articles 28 and 29 (processor obligations)
- SIG (Standardised Information Gathering) Questionnaire
- NIST SP 800-161 (Supply Chain Risk Management)

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
