
import gradio as gr

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

CONDITIONS = [
    ("Objectivity", "Observable conditions are shown; opinions are separated from observations."),
    ("Completeness", "The full roof system context is documented, including missing or limited viewpoints."),
    ("Traceability", "Each conclusion maps to specific evidence so a reviewer can identify where, what, and why."),
    ("Continuity", "Photos, notes, and diagrams align as one coherent narrative without contradiction."),
]

LEVELS = [
    {"id":1,"title":"The Maintenance Manual","desc":"Distinguish normal wear from storm damage.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/Homeowners_Guide_FINAL_KDP_MASTER-1.pdf","quiz":"https://quizgecko.com/learn/proactive-roof-maintenance-qonxgk","q":"Maintenance vs. Storm Damage?","a":"Maintenance is gradual aging. Storm damage is sudden and event-driven. Dates matter."},
    {"id":2,"title":"Roof Ancestry","desc":"Know your roof material history and why matching can be hard.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/pdf.net_Claim-Lineage.pdf","quiz":"https://quizgecko.com/learn/insurance-claims-roof-repairs-kdp-ready-v2-nqt8cq","q":"Why does lineage matter?","a":"Old roofs can be hard to repair because material compatibility and matching affect the scope."},
    {"id":3,"title":"Storm Spotter","desc":"Identify hail and wind indicators by looking for patterns that matter.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/pdf.net_Tree-and-Hail-1.pdf","quiz":"https://quizgecko.com/learn/storm-damage-claims-a-homeowners-roadmap-sqy9sq","q":"What connects the dots?","a":"Collateral indicators. If gutters, vents, or soft metals show impact patterns, roof damage can be evaluated in context."},
    {"id":4,"title":"The Roadmap","desc":"Master the claim timeline: inspection, decision, estimate, supplement.","pdf":"https://inspector-roofing.com/wp-content/uploads/2025/12/Homeowners_Guide_Downloadable.pdf","quiz":"https://quizgecko.com/learn/protect-your-homes-roof-a-practical-guide-mmicqk","q":"The golden rule of claims?","a":"Keep a timeline. Save every email, photo, receipt, and conversation note in one place."},
    {"id":5,"title":"Camera Protocols","desc":"Take photos that tell a story: context first, zoom second.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/pdf.net_Inspector-Roofing-Protocols-Manuscript.pdf","quiz":"https://quizgecko.com/learn/insurance-claim-documentation-standards-ukzdxy","q":"Photo sequence?","a":"Overview of property, roof slope, damage area, then close-up detail."},
    {"id":6,"title":"Evidence Standard","desc":"Make a claim verifiable. Facts beat opinions every time.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/Claim-Verifiability-Manuscript.pdf","quiz":"https://quizgecko.com/learn/insurance-roof-claims-verifiable-documentation-0dqjuq","q":"Verifiable vs. convincing?","a":"Verifiable means another reviewer can see the same evidence and reach the same conclusion without guessing."},
    {"id":7,"title":"The Organizer","desc":"Build a claim ledger and never lose track of a conversation again.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/pdf.net_Claim-Ledger.pdf","quiz":"https://quizgecko.com/learn/defensible-roof-inspections-the-haag-protocol-ll6uhl","q":"What is a claim ledger?","a":"A log of who you talked to, when, what was said, and what evidence supports the next step."},
    {"id":8,"title":"Meeting the Adjuster","desc":"Keep it calm and factual. Handle site meetings as verification events.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/pdf.net_The-Art-of-Adjuster-Meetings.pdf","quiz":"https://quizgecko.com/learn/insurance-claims-inspection-first-documentation-v2ljmx","q":"Goal of the meeting?","a":"Agree on observable facts and documented findings. Do not turn the meeting into a coverage argument."},
    {"id":9,"title":"Stall Breaker","desc":"Identify which missing information causes the claim to freeze.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/pdf.net_Claim-Continuity-Integrity.pdf","quiz":"https://quizgecko.com/learn/claim-structure-enduring-audits-and-ai-3hcw4e","q":"How do you stop a stall?","a":"Ask what specific information is needed to move forward, then provide exactly that evidence."},
    {"id":10,"title":"Decoder Ring","desc":"Understand denial letters and what phrases like wear and tear imply.","pdf":"https://inspector-roofing.com/wp-content/uploads/2025/12/Homeowners_Guide_to_Maintaining_Your_Roof.pdf","quiz":"https://quizgecko.com/learn/claim-defensibility-architecture-khddqp","q":"How do you read a denial?","a":"Look for the stated reason. Is it a policy issue or an evidence gap? Fix the evidence gap first."},
    {"id":11,"title":"Engineer Speak","desc":"Learn functional vs. cosmetic language and professional damage classification.","pdf":"https://inspector-roofing.com/wp-content/uploads/2025/12/haag-inspection-protocols-ebook.pdf","quiz":"https://quizgecko.com/learn/haag-protocol-defensible-roof-inspections-or3chn","q":"Functional damage?","a":"Damage that affects water shedding, seal integrity, material behavior, or system performance."},
    {"id":12,"title":"Green Protocols","desc":"Understand ventilation, longevity, and roof system performance.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/pdf.net_Green-Roof-Integration-Protocols™.pdf","quiz":"https://quizgecko.com/learn/performance-driven-green-roofing-longevity-and-ventilation-bvqif9","q":"What is a roof system?","a":"Not just shingles. It includes ventilation, insulation, intake, exhaust, flashing, underlayment, and accessories working together."},
    {"id":13,"title":"The Capstone","desc":"Final exam: vet advice and make confident decisions using evidence.","pdf":"https://inspector-roofing.com/wp-content/uploads/2026/01/Manuscript.pdf","quiz":"https://quizgecko.com/learn/roofing-authority-from-invisible-to-dominant-xqvurs","q":"Final takeaway?","a":"Trust but verify. Every conclusion should be backed by photos, measurements, notes, and standards."},
]


def evaluate_claim(*checks):
    complete = sum(bool(v) for v in checks)
    total = len(MEP_ITEMS)
    score = round(complete / total * 100)
    missing = [item for item, value in zip(MEP_ITEMS, checks) if not value]
    if score == 100:
        status = "REVIEW-READY: the minimum evidence package is complete."
    elif score >= 75:
        status = "STRONG BUT INCOMPLETE: close documentation gaps before treating conclusions as verifiable."
    elif score >= 50:
        status = "NEEDS WORK: the file may not survive neutral review without more context."
    else:
        status = "NOT YET VERIFIABLE: build the evidence package before presenting conclusions."
    report = f"""## Claim Verifiability Score: {score}%\n\n**Status:** {status}\n\n**Completed items:** {complete} of {total}\n\n### Missing / Weak Items\n"""
    if missing:
        report += "\n".join(f"- {item}" for item in missing)
    else:
        report += "- None. Keep the file organized and tie every conclusion back to specific evidence."
    report += "\n\n### Four Verifiability Conditions\n"
    report += "\n".join(f"- **{name}:** {desc}" for name, desc in CONDITIONS)
    report += "\n\n> Educational use only. This tool does not determine coverage, interpret policy, or guarantee approval."
    return score, report


def build_ledger(property_address, claim_number, loss_date, observations, standards):
    return f"""# Claim Verifiability Ledger\n\n- **Property:** {property_address or 'TBD'}\n- **Claim number:** {claim_number or 'TBD'}\n- **Reported loss date:** {loss_date or 'TBD'}\n\n## Observed Conditions\n{observations or 'Add observations tied to specific photos, slopes, elevations, and components.'}\n\n## Standards / Requirements Referenced\n{standards or 'Add applicable code, manufacturer, safety, or inspection methodology references.'}\n\n## Traceability Rule\nEvery conclusion should map to a photo, note, measurement, or standard. If it cannot be traced backward, it should not be presented as a conclusion.\n"""


def show_level(selection):
    level = next((lvl for lvl in LEVELS if f"Level {lvl['id']}" in selection), LEVELS[0])
    return f"""## Level {level['id']}: {level['title']}\n\n{level['desc']}\n\n**Flashcard question:** {level['q']}\n\n**Answer:** {level['a']}\n\n**Read Intel:** {level['pdf']}\n\n**Quiz:** {level['quiz']}\n"""

with gr.Blocks(title="Claim Verifiability Academy") as demo:
    gr.Markdown("""
    # Claim Verifiability Academy
    Evidence-first tools for insurance roof claim documentation.

    This app is an educational checklist and training companion. It does not make legal, coverage, or claim approval determinations.
    """)

    with gr.Tab("Evidence Checklist"):
        gr.Markdown("Check each item in the Minimum Evidence Package. The result shows whether the file is ready for neutral review.")
        checkboxes = [gr.Checkbox(label=item) for item in MEP_ITEMS]
        btn = gr.Button("Evaluate Evidence Package", variant="primary")
        score = gr.Number(label="Score", precision=0)
        report = gr.Markdown()
        btn.click(evaluate_claim, inputs=checkboxes, outputs=[score, report])

    with gr.Tab("Claim Ledger Builder"):
        property_address = gr.Textbox(label="Property address")
        claim_number = gr.Textbox(label="Claim number")
        loss_date = gr.Textbox(label="Reported loss date")
        observations = gr.Textbox(label="Observed conditions", lines=7, placeholder="Example: South slope - fractured shingle at grid S-04, close-up photo IMG_1021, overview IMG_1018...")
        standards = gr.Textbox(label="Standards / requirements referenced", lines=5, placeholder="Example: manufacturer installation instruction, IRC adoption, OSHA access limitation, HAAG-style damage mechanics...")
        ledger_btn = gr.Button("Generate Ledger Entry", variant="primary")
        ledger = gr.Markdown()
        ledger_btn.click(build_ledger, inputs=[property_address, claim_number, loss_date, observations, standards], outputs=ledger)

    with gr.Tab("Roof Hero Academy"):
        choices = [f"Level {lvl['id']} - {lvl['title']}" for lvl in LEVELS]
        level_select = gr.Dropdown(choices=choices, value=choices[0], label="Training level")
        level_card = gr.Markdown(show_level(choices[0]))
        level_select.change(show_level, inputs=level_select, outputs=level_card)

    with gr.Tab("About"):
        gr.Markdown("""
        ## Core Principle
        Evidence must carry the authority, not the individual.

        ## Boundary
        Claim Verifiability is an evidence standard. It does not determine coverage, override policy language, or guarantee claim approval.
        """)

if __name__ == "__main__":
    demo.launch()
