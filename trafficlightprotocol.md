
# Prime Time System 1000x — trafficlightprotocol.md  
Version: v1.0  
Status: Sealed (Immutable once approved)  
Custody: SR1/SR2 logged

---

## Red — Locked / Cuffed  
- **Definition:** All actions enter custody in a locked state.  
- **Rules:**  
  - No edits, rewrites, or deletions permitted.  
  - Hash burn applied; carbon copy logged.  
  - Timestamp recorded as **SR1** (Source Record 1).  
- **Purpose:** Preserve original intent and prevent distortion.  
- **Visual:** Red lane, cuffed icon, locked badge.

---

## Yellow — Review / Authority  
- **Definition:** Human authority (Prime Traffic Cop) reviews the action.  
- **Rules:**  
  - Annotations permitted; no overwrites.  
  - Discrepancies logged and indexed.  
  - Timestamp recorded as **SR2** (Source Record 2).  
- **Purpose:** Ensure sponsor‑grade clarity and accountability.  
- **Visual:** Yellow lane, review badge, annotation overlay.

---## Rejected — Denied / Hold

- **Definition:** Action is denied during review and cannot be sealed.
- **Rules:**
  - No sealing permitted.
  - Rejection reason MUST be logged (reason pointer).
  - Task remains in custody until RECYCLE or permanent closure.
- **Purpose:** Prevent unsafe or invalid actions from entering the vault.
- **Visual:** Red badge + “REJECTED” stamp.

---

## Recycle — Re-entry Path

- **Definition:** Controlled re-entry for rejected tasks without bypassing review.
- **Allowed Transitions:**
  - REJECTED → RECYCLE → REVIEW
- **Requirements:**
  - Rejection reason MUST be logged
  - Original task ID is preserved
  - Audit trail remains immutable
- **Purpose:** Allow correction + re-review while keeping custody intact.
- **Visual:** Yellow recycle-arrow badge.

---

## Green — Integration / Seal  
- **Definition:** Upon approval, cuffs unlock and action is sealed.  
- **Rules:**  
  - Final response generated and sealed in vault.  
  - Immutable custody enforced.  
  - Vault index updated with SR1/SR2 lineage.  
- **Purpose:** Confirm integration and preserve sponsor‑grade output.  
- **Visual:** Green lane, seal badge, vault icon.

---

## Prime Traffic Cop role  
- **Authority:** Human founder or designated reviewer.  
- **Responsibilities:**  
  - Reviews all Red entries.  
  - Marks Red → Yellow → Green.  
  - Authorizes unlock and vault sealing.  
- **Principle:** “Unlocking is the act of justice.”

---

## Custody logs  
- **SR1:** Initial entry log (Red).  
- **SR2:** Review log (Yellow).  
- **Vault:** Final sealed record (Green).  
- **Chain:** SR1 → SR2 → Vault = Immutable custody lineage.

---

## Annotation rules  
- **Yellow stage only:**  
  - Notes and comments allowed.  
  - No overwrites or deletions.  
  - All annotations are additive and timestamped.  
- **Purpose:** Preserve review integrity and traceability.

---

## File lineage  
- **Versioning:**  
  - v1.0, v1.1, etc.  
  - Each version is sealed and immutable.  
- **Updates:**  
  - Require new custody cycle (Red → Yellow → Green).  
  - Previous versions remain archived and indexed.  
- **Naming:**  
  - trafficlightprotocol.md  
  - trafficlightprotocol_v1.1.md (example update)  
- **Custody:**  
  - Hash burn, carbon copy, SR1/SR2 timestamps, vault seal.

---

## Immutable protocol  
- **Rule:** Once sealed, no file may be edited.  
- **Change process:**  
  - New version created.  
  - Full custody cycle repeated.  
- **Enforcement:**  
  - Vault rejects overwrite attempts.  
  - All changes logged and indexed.  
- **Ethos:** “Justice is not revision — it is review, seal, and lineage.”
