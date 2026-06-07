"""Sample inbox used by the /api/demo endpoint so the app runs with no setup."""
from __future__ import annotations

from .models import RawEmail

SAMPLE_EMAILS: list[RawEmail] = [
    RawEmail(
        id="d1",
        sender="Dr. Sarah Lin <s.lin@university.edu>",
        subject="URGENT: Grant report due tomorrow 5pm",
        date="Mon, 1 Jun 2026 09:12:00 -0700",
        snippet="The NSF progress report is due tomorrow and I still need your section...",
        body=(
            "Hi, the NSF progress report is due tomorrow at 5pm. I still need your "
            "section on the experimental results and the updated budget table. "
            "Can you send it by noon so I have time to integrate? This is critical."
        ),
    ),
    RawEmail(
        id="d2",
        sender="GitHub <noreply@github.com>",
        subject="[daisubc/repo] CI run failed on main",
        date="Mon, 1 Jun 2026 08:40:00 -0700",
        snippet="Your workflow 'build' failed for commit a1b2c3...",
        body="The build workflow failed on main. 2 tests failed in test_summarize.py.",
    ),
    RawEmail(
        id="d3",
        sender="TechWeekly <digest@techweekly.com>",
        subject="Your Monday digest: 12 stories you missed",
        date="Mon, 1 Jun 2026 06:00:00 -0700",
        snippet="The biggest stories in tech this week. Unsubscribe anytime.",
        body="This week's top stories in AI, startups and gadgets. Click to read. Unsubscribe.",
    ),
    RawEmail(
        id="d4",
        sender="Alex Chen <alex.chen@gmail.com>",
        subject="Re: Coffee next week?",
        date="Sun, 31 May 2026 19:30:00 -0700",
        snippet="Tuesday or Wednesday works for me, let me know what's good...",
        body="Hey! Tuesday or Wednesday afternoon both work for me. Let me know which you prefer and I'll book a spot.",
    ),
    RawEmail(
        id="d5",
        sender="Amazon <auto-confirm@amazon.com>",
        subject="Your order has shipped",
        date="Sun, 31 May 2026 14:05:00 -0700",
        snippet="Arriving Wednesday. Track your package.",
        body="Your order of 'USB-C cable' has shipped and will arrive Wednesday. Track your package in your account.",
    ),
    RawEmail(
        id="d6",
        sender="Finance Dept <accounts@university.edu>",
        subject="Action needed: reimbursement form incomplete",
        date="Fri, 29 May 2026 11:20:00 -0700",
        snippet="We could not process your travel reimbursement because a receipt is missing...",
        body=(
            "Your travel reimbursement could not be processed because the hotel receipt "
            "is missing. Please upload it within 7 days or the claim will be closed."
        ),
    ),
]
