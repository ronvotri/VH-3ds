# Fantasy Life USA — RC1 text preflight (2026-11-28)

RC1 data remains unchanged: 25,553 replacements, 8,629 KEEP, 630 deferred, 34,812 IDs. All 34,812 IDs exactly match the independently retained source-ID index (decoded signed zigzag delta pairs).

## Results

- Recovered 27 older checkpoint archives CP001–CP012. Review-source coverage: 34,532/34,812 IDs, with no conflicting recovered copies in the reconstructed index.
- 25,273/25,553 replacements compared against recovered source text; zero recognized token-sequence differences; 280 missing source texts all belong to F00008682 (avatar labels).
- Zero malformed recognized CTRL hex markers or unexpected literal control characters in replacements.
- 2,500 trailing-CR differences in CP005a/b/c and CP006a review exports require original-source verification (not automatically corrected).
- 363 raw numeric review warnings, including 6 Dosh amounts split by CTRL; no automatic changes.
- 226 printable required glyphs after filtering recognized tokens, not actual font coverage.
- Local read-only preflight script rejects an incomplete original-source input, changed replacement mapping and duplicate IDs; recovered-source mode reports REVIEW_REQUIRED, not build-ready.

Canonical mapping SHA-256: 44f1730feeb5a9fa00ec3438b8807fa1c3ce8518aca4609d30d63f4438170dce

Local handoff: FantasyLife-USA-RC1-preflight.zip (SHA-256 d33b033a9cb3bc8b728a587229637dfbcb71a9a134d7674470c38c6bf2e2fa). Contains the read-only checker, recovered review text and detailed QA. Recovered source text is intentionally not published to this public repository.

## Blocker before playable patch

Need the user's original USA resource files / extracted RomFS, F-number to actual resource-path map, original font and reinsertion/repack tooling. The original 01_CAN_DICH.jsonl or handover ZIP is still unavailable. Recovered review data must not substitute for original resource bytes. Font patch, reinsertion, full GitHub unpacker run and emulator runtime are not tested. No release-ready ROM/patch has been produced.
