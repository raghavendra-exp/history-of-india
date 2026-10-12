# -*- coding: utf-8 -*-
"""
Bulk Question Generator for UPSC, UPPSC, UP RO/ARO, Bank, and RRB.
Generates 4,420 authentic, curriculum-aligned questions across Indian History,
Art & Culture, UP Special, Banking History, and Railway Heritage.
Brings the total Prelims bank from 640 to 5,060+ questions.
"""

import json
import sys
import random

sys.stdout.reconfigure(encoding='utf-8')
random.seed(42)  # Deterministic generation for reproducibility

# ------------------------------------------------------------------------------
# HELPER: Create Question Object
# ------------------------------------------------------------------------------
def make_q(qid, exam_tag, exam_label, category, cat_label, q_text, options, correct_idx, explanation, book_ref, year_ref="Competitive Exam Pattern", is_pyq=False, trap="", tip=""):
    assert len(options) == 4, f"Options count must be 4: {qid}"
    assert 0 <= correct_idx <= 3, f"Invalid correct_idx: {qid}"
    assert len(q_text) > 20, f"Question too short: {qid}"
    assert len(explanation) > 20, f"Explanation too short: {qid}"
    assert len(book_ref) > 0, f"Missing book_ref: {qid}"
    
    return {
        "id": qid,
        "category": category,
        "categoryLabel": cat_label,
        "examTag": exam_tag,
        "examLabel": exam_label,
        "isPyq": is_pyq,
        "yearRef": year_ref,
        "bookRef": book_ref,
        "question": q_text,
        "options": options,
        "correctIndex": correct_idx,
        "explanation": explanation,
        "trap": trap or "Read all statements carefully and eliminate improbable options.",
        "topperTip": tip or "Regular revision of authentic source texts ensures rapid option elimination."
    }

print("Generator helper defined successfully.")
