"""Deterministic Claim Verifiability evaluator.

This module intentionally avoids legal or coverage determinations. It checks whether
an evidence package appears complete enough for structured review.
"""
from __future__ import annotations

MEP_ITEMS = [
    "Property context photos: front, back, and sides",
    "Roof plane orientation and elevations",
    "Date/time and location confirmation",
    "Consistent photo framing and scale reference",
    "Shingles or roofing material",
    "Flashings and penetrations",
    "Vents and accessories",
    "Gutters and soft metals",
    "Collateral indicators where present",
    "Clear labeling of evidence",
    "Logical sequencing",
    "Written observations tied to images",
]

CONDITIONS = ["Objectivity", "Completeness", "Traceability", "Continuity"]

def evaluate_checks(checks: list[bool]) -> dict:
    """Return a score and missing item list for the minimum evidence package."""
    if len(checks) != len(MEP_ITEMS):
        raise ValueError(f"Expected {len(MEP_ITEMS)} checks, received {len(checks)}")
    complete = sum(1 for value in checks if value)
    score = round(100 * complete / len(MEP_ITEMS))
    missing = [item for item, value in zip(MEP_ITEMS, checks) if not value]
    if score == 100:
        status = "Review-ready evidence package"
    elif score >= 75:
        status = "Strong but incomplete"
    elif score >= 50:
        status = "Needs documentation work"
    else:
        status = "Not yet verifiable"
    return {"score": score, "complete": complete, "total": len(MEP_ITEMS), "missing": missing, "status": status}

def build_ledger(property_address: str, claim_number: str, loss_date: str, observations: str, standards: str) -> str:
    """Create a concise Claim Verifiability ledger entry."""
    return f"""# Claim Verifiability Ledger

- Property: {property_address or 'TBD'}
- Claim number: {claim_number or 'TBD'}
- Reported loss date: {loss_date or 'TBD'}

## Observed Conditions
{observations or 'Add observations tied to specific photos, slopes, elevations, and components.'}

## Standards / Requirements Referenced
{standards or 'Add applicable code, manufacturer, safety, or inspection methodology references.'}

## Traceability Rule
Every conclusion should map to a photo, note, measurement, or standard. If it cannot be traced backward, it should not be presented as a conclusion.
"""
