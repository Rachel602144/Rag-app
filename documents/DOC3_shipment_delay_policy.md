# GlobalFreight Shipment Delay & Exception Policy
## Document Reference: GF-DEL-POL-2025-v2.3
## Applicable to: All GlobalFreight Account Holders
## Last Updated: 15 March 2025

---

## 1. PURPOSE & SCOPE

This policy defines the procedures, thresholds, communication standards, and compensation rules that apply when a GlobalFreight shipment experiences a delay, exception, or disruption. It covers all service tiers (Platinum, Gold, Standard) and all shipment types (domestic and international).

---

## 2. DELAY CLASSIFICATION FRAMEWORK

All delays are classified into one of four categories to determine the appropriate response action:

### Category 1 — Minor Delay (0–4 hours past ETA)
- **Automatic action:** System updates ETA; customer receives automated notification
- **Agent action required:** None unless customer contacts support
- **SLA impact:** None for Gold/Standard; SLA breach warning triggered for Platinum

### Category 2 — Significant Delay (4–24 hours past ETA)
- **Automatic action:** ETA updated; automated notification sent with reason code
- **Agent action required:** Proactive outreach required for Platinum customers within 1 hour of breach
- **SLA impact:** SLA breach for Platinum; warning state for Gold
- **Compensation trigger:** Platinum only — 15% freight refund per 24-hour block

### Category 3 — Major Delay (24–72 hours past ETA)
- **Automatic action:** Escalation ticket created automatically
- **Agent action required:** Dedicated case manager assigned; customer contacted within 2 hours
- **SLA impact:** Breach for Platinum and Gold; warning for Standard
- **Options offered to customer:**
  a. Wait with updated ETA (no additional charge)
  b. Emergency re-routing via alternative carrier (surcharge applies: 20–40% of original freight cost)
  c. Cancel and full refund if shipment not yet departed

### Category 4 — Critical Delay (> 72 hours past ETA or unknown ETA)
- **Automatic action:** CEO escalation alert triggered; operations war room activated
- **Agent action required:** Senior account manager contacts customer within 30 minutes
- **SLA impact:** Full SLA breach across all tiers
- **Compensation:** Full freight refund + 10% goodwill credit on next shipment
- **Options:** All Category 3 options plus free re-booking on next available service

---

## 3. DELAY REASON CODES

Use these codes in all system entries, notifications, and reports:

| Code | Reason | SLA Clock Paused? | Compensation Owed? |
|---|---|---|---|
| DLY-01 | Traffic congestion / road delay | No | Yes |
| DLY-02 | Port congestion | No | Yes |
| DLY-03 | Carrier capacity shortage | No | Yes |
| DLY-04 | Weather — severe (declared) | YES | No |
| DLY-05 | Weather — minor | No | Yes |
| DLY-06 | Customs hold — documentation incomplete | No | No (shipper fault) |
| DLY-07 | Customs hold — inspection triggered | No | No (regulatory) |
| DLY-08 | Strike / labour action | YES | No |
| DLY-09 | Mechanical failure — carrier vehicle | No | Yes |
| DLY-10 | Airline cancellation — carrier fault | No | Yes |
| DLY-11 | Airline cancellation — weather / ATC | YES | No |
| DLY-12 | Public holiday at destination | No | Yes (if not disclosed) |
| DLY-13 | Address / delivery issue | No | No (shipper fault) |
| DLY-14 | Recipient unavailable | No | No |
| DLY-15 | Security screening — standard | No | No |
| DLY-16 | System / IT outage (carrier) | No | Yes |
| DLY-17 | Force majeure (declared) | YES | No |
| DLY-18 | Regulatory embargo | YES | No |

---

## 4. AUTONOMOUS AGENT DECISION RULES

The following actions **may be taken autonomously** by the logistics operations system without human approval:

| Action | Condition | Limit |
|---|---|---|
| Send delay notification to customer | Any delay > 30 minutes | No limit |
| Update ETA in system | Category 1 or 2 delay | No limit |
| Create escalation ticket | Category 3+ delay | No limit |
| Offer alternative route information | Category 2+ delay | No limit |
| Apply SLA credit to account | Category 2+ and compensation owed | Up to ₹50,000 per shipment |
| Notify escalation manager | Category 3+ | No limit |

The following actions **require human approval** before execution:

| Action | Approval Required From | Reason |
|---|---|---|
| Cancel a shipment | Operations Manager | Irreversible action |
| Re-route to alternate carrier | Dispatcher on duty | Cost impact |
| Issue refund > ₹1,00,000 | Finance Manager | Financial authority |
| Declare Force Majeure for customer | Senior VP Operations | Legal implication |
| Cancel more than 3 shipments in any 10-minute window | Operations Director | Bulk action risk |
| Communicate externally on behalf of carrier | PR/Communications Manager | Reputational risk |

---

## 5. COMMUNICATION STANDARDS

### 5.1 Customer Notification Templates

**Category 1 SMS/Email:**
> "Your shipment [TRACKING_ID] is experiencing a minor delay. New estimated delivery: [NEW_ETA]. No action required. Track at globalfreight.in/track"

**Category 2 Proactive Call Script (Platinum):**
> "Hello [CUSTOMER_NAME], this is [AGENT_NAME] from GlobalFreight. I'm calling about your Platinum shipment [TRACKING_ID] which is running [X] hours behind schedule due to [REASON]. The new ETA is [NEW_ETA]. You are eligible for a freight credit of [AMOUNT] per our SLA. Would you like me to apply that now?"

**Category 3 Re-routing Offer:**
> "We regret that shipment [TRACKING_ID] has been delayed by [X] hours due to [REASON]. We are offering the following options: (1) Revised delivery by [DATE1] at no additional cost; (2) Emergency re-routing via [CARRIER] arriving by [DATE2] at a surcharge of [SURCHARGE]; (3) Full cancellation and refund. Please select your preferred option by [DEADLINE]."

### 5.2 Internal Escalation Protocol
- All Category 3+ events must be logged in the Operations Dashboard within 15 minutes of classification
- Escalation email must include: Shipment ID, customer tier, delay hours, reason code, action taken, next steps
- Operations Manager must sign off on all actions within 30 minutes of escalation

---

## 6. PRIORITY SHIPMENTS — SPECIAL HANDLING

### 6.1 Perishable Goods
- Maximum acceptable delay: 4 hours (regardless of SLA tier)
- If delay > 4 hours: Immediate human escalation; offer temperature-controlled storage at nearest facility
- If goods spoiled: Full refund + replacement cost compensation up to freight value

### 6.2 Pharmaceutical / Medical Supplies
- Cold chain monitoring required; alert if temperature breach
- Any delay > 2 hours requires escalation to Medical Supplies Desk (+91-22-6789-0001)
- WHO-GMP documentation must accompany shipment

### 6.3 Time-Sensitive Legal / Government Documents
- Treat as Platinum regardless of stated tier
- Maximum 2-hour delay tolerance
- Dedicated courier hand-off required at destination

---

## 7. BULK CANCELLATION POLICY

No agent — human or automated — may cancel more than **3 shipments within any rolling 10-minute window** without explicit written authorisation from the Operations Director. This limit exists to prevent cascading failures in the network. Requests beyond this threshold must be queued and reviewed one by one.

---

## 8. REPORTING REQUIREMENTS

Every delay incident of Category 2 or above must generate:
1. Incident Report (auto-generated within 1 hour)
2. Root Cause Analysis (submitted within 24 hours for Category 3+)
3. Customer Communication Log (all touchpoints documented)
4. SLA Compliance Record (for monthly audit)

Monthly SLA performance reports are shared with Platinum account holders on the 5th of each month.

---

*Questions? Contact ops-policy@globalfreight.in*
*© 2025 GlobalFreight Logistics Pvt. Ltd. Internal Policy Document — Confidential*