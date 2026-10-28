#!/usr/bin/env python3
"""Extend the open awesome-x402 PR with the measured scoreboard and the field-notes article,
and refresh the two stale product counts (15 endpoints -> 26 routes, 16 tools -> 19 tools).
"""
import re, sys

P = "README.md"
src = open(P, encoding="utf-8").read()

# 1. Analytics Dashboards — the measured seller scoreboard.
anchor_dash = "- [SmartFlow Observatory](https://smartflowproai.com) - Public observatory for the x402 endpoint network on Base."
dash_entry = (
    "- [Akari x402 Seller Scoreboard](https://akari-x402.puzzling-marten.workers.dev/scoreboard) - "
    "Measured, free scoreboard of the x402 *seller* market, not the payment volume: every paid URL published "
    "in the 402index directory requested once and graded on what a machine buyer needs (402 on every listed "
    "route, a decodeable `payment-required` challenge with price + CAIP-2 network + payTo, a human-readable "
    "402 body, an MCP surface, latency). Method is stated in the payload and a 200 is recorded as "
    "free-or-mislisted, never as a broken paywall. Machine copy at `/scoreboard.json`; per-origin audit "
    "(`/x402/endpoint-audit`, $10) and a market report with real crawler referrer data (`/x402/market-report`, $15). "
    "([raw data](https://akari-x402.puzzling-marten.workers.dev/scoreboard.json))\n"
)
assert anchor_dash in src, "dashboard anchor missing"
src = src.replace(anchor_dash, dash_entry + anchor_dash, 1)

# 2. Technical Deep Dives — the field notes from the measurement.
anchor_deep = "- [Counterfeit Verifiability in Autonomous Agent Payments]"
deep_entry = (
    "- [I probed 442 x402 endpoints across 85 sellers. The code is fine; the market isn't.]"
    "(https://dev.to/edvyno/i-probed-442-x402-endpoints-across-85-sellers-the-code-is-fine-the-market-isnt-4knb) - "
    "Field notes from auditing the seller side: of 442 endpoints, 58% answered 402, only 3% of those paywalls "
    "failed to produce a decodeable challenge, 24% of listed URLs were dead, 18% answered 200 (recorded as "
    "free-or-mislisted, not broken). Includes the traffic reality check: ~99% of requests to a live paid "
    "endpoint were crawlers and monitoring probes, so fixing the handshake is table stakes that does not "
    "create a buyer.\n"
)
assert anchor_deep in src, "deep-dive anchor missing"
src = src.replace(anchor_deep, deep_entry + anchor_deep, 1)

# 3. Keep the two existing entries truthful about the current catalogue (26 routes, 19 tools, price ladder).
src = src.replace("- 15 pay-per-call crypto market-intelligence endpoints on Base:",
                  "- 26 pay-per-call crypto market-intelligence and seller-tooling routes on Base:", 1)
src = src.replace("$0.02-$1.00 USDC via the Coinbase CDP facilitator, no API keys or signup; free edge board and machine catalog.",
                  "$0.02-$15.00 USDC via the Coinbase CDP facilitator, no API keys or signup: per-call routes, a "
                  "$5.00 / 30-day pass covering every paid route, a $10 endpoint audit and a $15 market report; "
                  "free edge board, scoreboard and machine catalog.", 1)
src = src.replace("(JSON-RPC 2.0, 16 tools, price in `_meta.x402.price_usd`, `akari_board` free)",
                  "(JSON-RPC 2.0, 19 tools, price in `_meta.x402.price_usd`, `akari_board` free)", 1)

open(P, "w", encoding="utf-8").write(src)
print("inserted dashboard:", dash_entry.split("](")[0] + "]")
print("inserted deep dive:  I probed 442 x402 endpoints...")
print("counts refreshed:    26 routes / 19 tools / $5 pass")
