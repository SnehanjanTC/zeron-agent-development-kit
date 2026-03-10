---
organization: Teamcognito Solutions Pvt Ltd
framework: SOC2
policy: soc2-availability-policy
generated_by: ZAK ISO27001+SOC2 Compliance Agent
generated_date: 2026-03-10
status: DRAFT — Requires review and approval by Teamcognito Solutions Pvt Ltd management
---

# SOC 2 Availability Policy
**Organisation:** Teamcognito Solutions Pvt Ltd
**Classification:** Confidential — Internal Use Only
**Version:** 1.0 (Draft)
**Effective Date:** 2026-03-10
**Review Cycle:** Annual
**Policy Owner:** Chief Information Security Officer (CISO)
**Approved By:** [Pending Management Approval]

---

## 1. Purpose
This policy establishes Teamcognito Solutions Pvt Ltd's controls and commitments to ensure the availability of its systems and services in alignment with SOC 2 Availability Trust Service Criteria (A1.1, A1.2, A1.3). Availability is a core trust service category that ensures systems are operational and accessible to meet client commitments and service level agreements (SLAs). This policy governs capacity management, environmental threat protection, and business continuity/disaster recovery planning and testing.

## 2. Scope
This policy applies to all production systems, infrastructure, applications, and data that support Teamcognito's client-facing and internal services, including:
- Cloud infrastructure (AWS, Azure, GCP — as applicable)
- On-premises servers and network infrastructure
- SaaS platforms supporting business operations
- Data centres and co-location facilities
- Network connectivity (primary and redundant links)

## 3. Policy Statement

### 3.1 Capacity Monitoring and Management (A1.1)
1. Teamcognito shall maintain a Capacity Management Programme that monitors, analyses, and plans for the capacity requirements of all systems within the availability scope.
2. The following metrics shall be monitored continuously with automated alerting:
   - CPU utilisation (alert threshold: 75%; critical: 90%)
   - Memory utilisation (alert threshold: 80%; critical: 95%)
   - Storage utilisation (alert threshold: 75%; critical: 90%)
   - Network bandwidth (alert threshold: 70% of provisioned capacity)
   - Database connections and query performance
3. Capacity planning reviews shall be conducted quarterly; projections shall cover a minimum 12-month horizon factoring in business growth, seasonal peaks, and new product launches.
4. Auto-scaling capabilities shall be implemented for cloud-hosted systems to handle demand spikes without service degradation; scaling policies shall be tested quarterly.
5. Resource provisioning requests based on capacity planning outputs shall be reviewed and approved by the CTO/Engineering Lead; lead times for provisioning shall be factored into capacity plans.
6. Capacity metrics and planning reports shall be reviewed by the ISSC quarterly and escalated to the Board if projected capacity constraints present a service availability risk.

### 3.2 Environmental Threat Monitoring and Response (A1.2)
7. All data centre and server room environments shall be monitored for the following environmental threats, with automated alerting:
   - **Temperature:** Alert if above 25°C or below 18°C; critical above 30°C
   - **Humidity:** Alert outside 45–55% RH range
   - **Smoke/Fire:** Immediate alert and suppression system activation
   - **Flood/Water Ingress:** Immediate alert; water sensors under raised floors
   - **Power:** UPS status monitoring; generator fuel level monitoring; utility power failure alerting
8. Environmental monitoring systems shall be maintained in an operational state 24/7; failures shall be treated as a P2 incident and remediated within 4 hours.
9. Redundant cooling, power (dual UPS feeds + diesel generator with minimum 48-hour fuel capacity), and telecommunications (at least two independent ISP connections) shall be maintained at all data centre locations.
10. Physical environmental risk assessments for all facilities shall be reviewed annually; mitigation actions shall be tracked to completion.
11. Business continuity plans shall explicitly address responses to environmental threats; environmental incident scenarios shall be included in annual BCP testing.

### 3.3 Recovery Plan Procedures and Testing (A1.3)
12. A Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP) shall be maintained covering all systems within the availability scope.
13. Recovery objectives shall be defined and agreed with business stakeholders for each critical system:
    - **Recovery Time Objective (RTO):** Maximum acceptable time to restore service after a disruption
    - **Recovery Point Objective (RPO):** Maximum acceptable data loss measured in time
    - Default targets: Tier-1 systems (client-facing): RTO ≤ 4 hours, RPO ≤ 1 hour; Tier-2 systems (internal): RTO ≤ 24 hours, RPO ≤ 24 hours.
14. All critical systems shall have documented recovery procedures that are detailed enough to be executed by any qualified member of the IT team, not just the primary system owner.
15. Recovery plans shall be tested at minimum annually through one of the following methods:
    - **Tabletop exercise:** Walkthrough of scenarios with key personnel
    - **Failover test:** Live activation of DR environment for a defined system
    - **Full DR drill:** Complete switchover to DR environment with client service maintained
16. Testing results (success criteria, deviations from expected outcomes, time taken) shall be documented; any failed tests shall trigger immediate remediation actions and a re-test within 60 days.
17. Recovery plan tests shall include at minimum one scenario involving a significant cloud region failure per year.
18. Backup recovery shall be tested quarterly for at least one critical system per test cycle; results documented and signed off by system owner and CISO.
19. The BCP/DRP shall be reviewed and updated annually and following any significant technology change, incident, or test failure.
20. Key BCP/DRP personnel shall have 24/7 contact information maintained in an offline (hardcopy and securely hosted) contact directory.

### 3.4 Service Availability Commitments
21. Service availability SLAs shall be documented for all client-facing services in client agreements; uptime commitments shall be realistic and achievable based on system architecture.
22. Uptime monitoring shall be implemented for all production services using an independent monitoring tool (e.g., Datadog, New Relic, Pingdom); availability metrics shall be available on a client-accessible status page.
23. Monthly availability reports shall be generated; any month in which a service fails to meet its SLA shall trigger a Root Cause Analysis (RCA) and corrective action plan.
24. Planned maintenance windows shall be communicated to clients at minimum 5 business days in advance; emergency maintenance shall be communicated with as much notice as practical.

## 4. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| CISO | Own availability policy; oversee BCP/DRP programme; report availability risks to ISSC |
| CTO / Head of Engineering | Ensure system architecture meets RTO/RPO requirements; approve capacity plans; lead DR exercises |
| IT/Infrastructure Team | Monitor capacity and environmental metrics; implement redundancy; execute recovery procedures |
| DevOps/Platform Team | Implement auto-scaling; maintain monitoring tooling; manage cloud resilience configurations |
| Facilities Manager | Maintain physical environmental controls; manage UPS and generator maintenance schedules |
| Business Unit Heads | Define RTO/RPO requirements for their critical processes; participate in BCP testing |
| Client Success Team | Communicate maintenance windows and outage updates to clients |

## 5. Controls and Procedures

### 5.1 Capacity Management
- Automated monitoring dashboards (e.g., Datadog, CloudWatch, Prometheus/Grafana) configured with defined thresholds.
- Monthly capacity review meeting chaired by CTO; output: capacity utilisation report and next-quarter projections.
- Annual capacity planning cycle aligned with business planning cycle.

### 5.2 Environmental Monitoring
- Environmental monitoring platform (e.g., NetBotz, Nlyte, or equivalent) with 24/7 alerting to on-call team via PagerDuty/OpsGenie.
- UPS and generator maintenance contracts with defined SLAs for response and repair.
- Annual fire suppression system inspection and certification.

### 5.3 BCP/DRP Management
- BCP/DRP documents stored in DMS and offline backup; reviewed annually in Q4.
- DR environment maintained in a separate cloud region/zone; configurations synchronised monthly.
- Annual DR test coordinated by CTO and CISO; client success team notified in advance.
- Post-test report presented to ISSC within 30 days.

## 6. Exceptions
Exceptions to defined RTO/RPO targets for specific systems shall be formally approved by the CTO and CISO with documented risk assessment. Systems with approved lower availability requirements shall be explicitly excluded from standard availability reporting and documented in the system register.

## 7. Non-Compliance
Failure to maintain capacity monitoring, environmental controls, or up-to-date/tested recovery plans shall be treated as a critical control gap, potentially impacting both client trust and SOC 2 attestation. Such gaps shall be escalated to the CISO and ISSC immediately.

## 8. References
- SOC 2 TSC: A1.1, A1.2, A1.3 (Availability Criteria)
- ISO/IEC 27001:2022 Annex A.5.29, A.5.30, A.8.6, A.8.13, A.8.14
- ISO 22301:2019 (Business Continuity Management)
- NIST SP 800-34 Rev 1 (Contingency Planning Guide for Federal Information Systems)
- Uptime Institute Tier Classification Standards

## 9. Review and Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | ZAK Compliance Agent | Initial draft |

---
*This document was auto-generated by the ZAK ISO27001+SOC2 Compliance Agent and must be reviewed and approved by Teamcognito Solutions Pvt Ltd management before use.*
