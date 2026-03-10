---
organization: Teamcognito Solutions Pvt Ltd
framework: SOC2
policy: soc2-confidentiality-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# SOC 2 Confidentiality Policy
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy defines Teamcognito Solutions Pvt Ltd's controls to identify, protect, and responsibly dispose of confidential information — in alignment with the SOC 2 Confidentiality Trust Service Criteria (C1.1 and C1.2). Protecting the confidentiality of client data, intellectual property, and business-sensitive information is both a commercial and ethical obligation. This policy ensures confidential information is handled with appropriate safeguards throughout its lifecycle.

## 2. Scope
This policy applies to all confidential information processed, stored, or transmitted by Teamcognito Solutions Pvt Ltd, including:
- Client data and personal data
- Proprietary business information (financial data, strategic plans, pricing, contracts)
- Intellectual property (source code, product designs, algorithms, trade secrets)
- Employee records and HR data
- Third-party confidential information shared under NDA or contract
- Any information designated as Confidential or Restricted under the Information Classification Policy

It applies to all employees, contractors, and third parties handling such information across all platforms (digital, physical, verbal).

## 3. Policy Statement

### 3.1 Identification and Maintenance of Confidential Information (C1.1)
1. All information assets shall be classified in accordance with Teamcognito's Information Classification Policy using the four-tier scheme: Public, Internal, Confidential, and Restricted.
2. A data inventory (data map) shall be maintained identifying where confidential information is stored, processed, and transmitted; this inventory shall be reviewed and updated at minimum annually and following significant system changes.
3. Confidential and Restricted information shall be labelled appropriately (digital metadata, file naming conventions, document headers/footers, physical labels) to ensure all handlers are aware of its classification.
4. Access to Confidential and Restricted information shall be granted on a strict need-to-know, least-privilege basis; access shall be controlled via RBAC and reviewed quarterly.
5. Confidential information in transit shall be encrypted using TLS 1.2 or higher; Confidential information at rest shall be encrypted using AES-256 or equivalent.
6. Client data shall be logically isolated per client; cross-client data access shall be technically prevented and verified through annual penetration testing.
7. Confidential information shall not be stored in personal cloud services (e.g., personal Google Drive, Dropbox, iCloud); DLP controls shall technically prevent or alert on such activities.
8. Non-disclosure agreements (NDAs) shall be in place with all employees, contractors, and third parties who access Confidential or Restricted information.
9. Confidentiality obligations shall be communicated to all relevant personnel through training, onboarding, and annual policy acknowledgement.
10. Any suspected or confirmed disclosure of confidential information to unauthorised parties shall be treated as a security incident and reported immediately to the CISO.

### 3.2 Disposal of Confidential Information (C1.2)
11. Confidential information shall be retained only for as long as required by business need, contractual obligation, or applicable law; retention schedules shall be defined and documented in the Data Retention Policy.
12. Upon expiry of the retention period (or upon client request/contract termination), confidential information shall be securely disposed of using methods appropriate to its medium:
    - **Digital data on storage media:** Cryptographic erasure (encrypted at rest, then key destruction), NIST SP 800-88-compliant overwriting, or physical destruction of media.
    - **Cloud-hosted data:** Confirmed deletion via cloud provider API with deletion confirmation log; reliance on cloud provider certification for physical media disposal.
    - **Physical documents:** Cross-cut shredding using a minimum DIN 66399 security level P-4 (confetti cut recommended for Restricted materials); shredding conducted by contracted, certified destruction vendor.
    - **Portable media:** Physical destruction (degaussing + shredding) for Confidential/Restricted data; Certificate of Destruction obtained from vendor.
13. Certificates of Destruction shall be obtained and retained for all disposal activities involving Restricted information; records shall be retained for a minimum of 7 years.
14. Client data shall be returned or deleted upon contract termination within the timeframe stipulated in the client agreement (default: within 30 days of termination); confirmation of deletion shall be provided to the client in writing.
15. Data deletion processes shall be periodically tested to verify that deletion is complete and data is unrecoverable; test results shall be documented and retained as audit evidence.
16. Employees handling confidential documents shall use the confidential waste disposal bins provided; document bins shall be emptied and shredded by the contracted vendor at minimum weekly.

### 3.3 Confidentiality in Supplier and Partner Relationships
17. All suppliers and partners with access to Teamcognito's or its clients' confidential information shall be bound by confidentiality obligations equivalent to those in this policy, via NDA or contractual confidentiality clauses.
18. Supplier access to confidential information shall be the minimum necessary to deliver the contracted service; supplier access rights shall be reviewed annually.

### 3.4 Confidentiality Training and Awareness
19. All employees shall receive confidentiality training as part of the annual security awareness programme, covering: classification obligations, handling procedures, approved sharing methods, and reporting requirements.
20. Employees in roles with elevated access to client data (e.g., data engineers, client success, legal) shall receive role-specific confidentiality training annually.

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO | Own confidentiality policy; oversee data classification programme; manage DLP tools; approve data disposal activities for Restricted data |
| Data Protection Officer (DPO) | Maintain data inventory; advise on retention obligations; manage data subject requests |
| IT/Security Team | Implement encryption, DLP, access controls; conduct data deletion; maintain data inventory tooling |
| Legal Counsel | Manage NDAs; advise on retention and disposal obligations; handle client data return/deletion requests |
| Data/Asset Owners | Classify information under their ownership; approve access to Confidential/Restricted data; oversee disposal |
| All Employees | Handle confidential information per classification; report unauthorised disclosures; use approved disposal channels |
| Procurement | Ensure confidentiality clauses are included in all vendor/partner agreements |

## 5. Controls and Procedures

### 5.1 Data Classification
- Classification guidelines published in the Information Classification Policy and on the company intranet.
- DLP tool configured with detection rules for each classification level (e.g., regex for client account numbers, PII patterns).
- Annual data classification audit conducted by CISO; findings reported to ISSC.

### 5.2 Encryption Management
- Encryption at rest enforced via: cloud provider encryption (AWS S3 SSE-KMS, Azure Storage Service Encryption), full-disk encryption on endpoints (BitLocker/FileVault via MDM), database TDE.
- Encryption in transit enforced via: TLS 1.2/1.3 on all APIs and web services, VPN for site-to-site connections, secure file transfer (SFTP/FTPS/AS2) for bulk data exchanges.
- Certificate and key management tracked in dedicated key management system.

### 5.3 Data Disposal
- Disposal requests submitted via ITSM; IT team executes and logs disposal method and date.
- Quarterly media disposal exercise coordinated by IT; Certificates of Destruction filed in DMS.
- Annual review of retention schedules by Legal and CISO.

## 6. Exceptions
Exceptions to confidentiality controls (e.g., sharing client data with a third party not under NDA for an emergency situation) shall require immediate CISO approval, shall be limited to the minimum information necessary, and shall be logged in the exception register. Post-exception review shall be conducted to prevent recurrence.

## 7. Non-Compliance
Unauthorised disclosure of confidential information is a serious breach of this policy. Depending on severity and intent, consequences include disciplinary action (up to termination), civil liability, and criminal prosecution. All suspected breaches shall be reported to the CISO immediately and treated as security incidents.

## 8. References
- SOC 2 TSC: C1.1, C1.2 (Confidentiality Criteria)
- ISO/IEC 27001:2022 Annex A.5.12, A.5.13, A.5.14, A.5.33, A.8.10, A.8.11, A.8.12
- NIST SP 800-88 (Guidelines for Media Sanitisation)
- India DPDP Act 2023
- GDPR Articles 5, 25, 32

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
