# Compliance Guide

## GDPR (EU Users)

### Key Principles
1. **Lawfulness:** Have a legal basis for processing (consent, contract, legitimate interest)
2. **Purpose limitation:** Only collect data for stated purposes
3. **Data minimization:** Only collect what you need
4. **Accuracy:** Keep data correct and up-to-date
5. **Storage limitation:** Don't keep data longer than needed
6. **Integrity:** Keep data secure

### User Rights
- Right to access their data
- Right to rectify incorrect data
- Right to erasure ("right to be forgotten")
- Right to restrict processing
- Right to data portability
- Right to object to processing

### Implementation Checklist
- [ ] Privacy policy covering all GDPR requirements
- [ ] Cookie consent banner (opt-in for non-essential cookies)
- [ ] Data processing agreements with all vendors
- [ ] User data export functionality
- [ ] User data deletion functionality
- [ ] Data breach notification process (72-hour requirement)
- [ ] Records of processing activities
- [ ] Data Protection Impact Assessment (for high-risk processing)

## CCPA (California Users)

### Key Requirements
- [ ] Disclose what personal information you collect
- [ ] Allow users to request deletion
- [ ] Allow users to opt out of "sale" of data
- [ ] Don't discriminate against users who exercise rights
- [ ] "Do Not Sell My Personal Information" link (if applicable)

## SOC 2 (B2B SaaS)

### When to Get SOC 2
- Enterprise customers start asking for it
- Usually around Series A or first enterprise deal
- Takes 3-6 months to prepare, 6-12 months to complete

### SOC 2 Type I vs Type II
- **Type I:** Design of controls at a point in time (faster, cheaper)
- **Type II:** Operating effectiveness over time (6-12 months, more credible)

### Trust Service Criteria
1. Security (required)
2. Availability
3. Processing Integrity
4. Confidentiality
5. Privacy

### Preparation Steps
- [ ] Choose an auditor
- [ ] Gap assessment
- [ ] Implement controls (access management, encryption, monitoring)
- [ ] Document policies and procedures
- [ ] Run for observation period (Type II)
- [ ] Complete audit

## Security Basics (All Stages)

### Always
- [ ] HTTPS everywhere
- [ ] Password hashing (bcrypt/scrypt)
- [ ] Input validation and sanitization
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention
- [ ] Secrets in environment variables (not code)
- [ ] Regular dependency updates
- [ ] Backup strategy tested

### When You Have Users
- [ ] Rate limiting on auth endpoints
- [ ] Session management (timeout, invalidation)
- [ ] RBAC (role-based access control)
- [ ] Audit logging
- [ ] Incident response plan
