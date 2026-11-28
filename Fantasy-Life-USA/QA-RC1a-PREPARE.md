# Fantasy Life USA — RC1a technical preparation (2026-11-28)

Text-only correction delta: reviews/rc1a-corrections.jsonl.bz2.b64. Six existing Dosh amounts are no longer split across a line/page token. Old and new text included for exact application. Uncompressed SHA-256: bfabaea511b820bd833f0869a19b9ee86edec03fb60ccd333b2f9982dc594165.

Base canonical mapping SHA-256: 44f1730feeb5a9fa00ec3438b8807fa1c3ce8518aca4609d30d63f4438170dce.
RC1a canonical mapping SHA-256: 0aa42752f27313f2125480137e203e016e1768ccb786240b6f55d2e158ae76ff.
25,553 replacements, 8,629 KEEP, 630 deferred remain unchanged. 25,273 compared against recovered text, no recognized token-sequence errors; 363 raw numeric warnings remain (including grouping differences), 0 split Dosh amounts, 2,500 trailing CR differences, 280 missing source texts.

## First-import restrictions
Japanese Korean localization technical documentation identifies avatar labels as possible model lookup keys. Keep original F00008682 entries during first smoke test (404 replacement IDs). Flag 1,565 event/UI metadata replacements, 1,258 F5 choice strings, 149 E9 strings, and 280 missing-source replacements; these flags overlap (3,306 unique). They are not new KEEP decisions. Only 12 plain-text candidates selected for a first test after byte/pointer and font verification; none has been inserted. All remaining strings still require validation.

References: https://github.com/RainThunder/fantasylife_tools ; https://github.com/mhvuze/3ds-xfsatool ; https://github.com/snake759494/fantasy-life-3ds-korean-patch/blob/HEAD/docs/TECHNICAL.md . Japanese format and model key behavior require USA verification; third-party code/assets not included.

Local package FantasyLife-USA-RC1a-prepare.zip SHA-256 3ca336ace0f8d002c26c3b23b3aca0eb758d786c12c00422cca021810188b75b contains independent read-only archive probe and synthetic regression tests. No actual archive available. Need original USA romfs/_file_archive.bin before font inspection, real encoder/repacker, first insertion and runtime QA. No ROM or original resource included here.
