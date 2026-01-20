from enum import Enum
from typing import List, TypedDict


class Audience(str, Enum):
    it = "it"
    executive = "executive"
    pm = "pm"


class TranslationResult(TypedDict):
    audience: Audience
    summary: str
    risks: List[str]
    recommended_actions: List[str]


def translate_text(text: str, audience: Audience) -> TranslationResult:
    cleaned = " ".join(text.strip().split())

    if audience == Audience.executive:
        summary = (
            "A technical issue was identified that could impact business operations. "
            "We are assessing scope and taking steps to reduce risk and prevent disruption."
        )
        risks = [
            "Potential service disruption or degraded performance",
            "Increased security exposure if not remediated",
            "Possible compliance/audit concerns depending on affected systems",
        ]
        actions = [
            "Confirm scope, impacted systems, and severity",
            "Apply recommended remediation and validate recovery",
            "Document decision, risk acceptance (if any), and next review date",
        ]
    elif audience == Audience.pm:
        summary = (
            "A technical dependency/risk was found that may affect timeline and delivery. "
            "We need a short remediation window and clear ownership to stay on track."
        )
        risks = [
            "Schedule risk if remediation requires downtime or rework",
            "Cross-team dependency risk (IT/Security/Engineering)",
            "Quality risk if changes are rushed without validation",
        ]
        actions = [
            "Create a tracked task with owner, due date, and acceptance criteria",
            "Coordinate a maintenance window (if needed) and stakeholder comms",
            "Add a validation step and rollback plan to the project plan",
        ]
    else:  # Audience.it
        summary = (
            "Technical finding received. Review indicators, confirm root cause, and "
            "implement remediation. Ensure monitoring and documentation are updated."

        )
        risks = [
            "Root cause may persist if remediation is incomplete",
            "False positives/alert fatigue if tuning is not addressed",
            "Configuration drift without change control",
        ]
        actions = [
            "Validate the finding, reproduce if possible, and identify root cause",
            "Implement remediation (patch/config change) and verify in logs/monitoring",
            "Update runbook/ticket notes and add follow-up monitoring",
        ]
    suffix = "..." if len(cleaned) > 240 else ""
    summary = f"{summary}\n\nSource (condensed): {cleaned[:240]}{suffix}"


    return {
        "audience": audience,
        "summary": summary,
        "risks": risks,
        "recommended_actions": actions,
    }
