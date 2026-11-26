# Fantasy Life (USA) — CP014a — Votri Valley

26/11/2026 — Reviewed 326 previously held IDs: 73 new translations, 253 preserved resource labels.

## Scope
- 51 descriptive event/quest labels in archive 5423, including tutorial labels and short story headings. Preserve Event_XXX, digits, names and original markers. These labels may be internal; not confirmed in gameplay.
- 20 clear descriptive UI labels in archive 8690 (transport, Bag/Storage, shopping, scenario labels).
- 2 exact Spanish-source generic descriptions in archive 8710, reusing prior translations in the same table: Montón de libros and Caballo alquiler. No item name guessing.
- 253 KEEP_FORMAT_LITERAL decisions: explicit "unused frame" labels in resource tables, 222 in archive 8702 column 1 and 31 in archive 8690 UI-resource section. This preserves source bytes rather than asserting that these records never appear in game.

## Progress
19.709 translated entries, 5.699 KEEP, 9.404 HOLD. Resolved total 25.408/34.812 (72,99%); translated entries 56,62%. Technical labels are counted separately from new Vietnamese text. The 326 resolved IDs were already in the HOLD ledger; no new source IDs.

## QA
Reopened original source ZIP and reconstructed 9.730 historical HOLD records from local checkpoint archives; verified ID uniqueness, source equality and no overlap with available translated/KEEP records. Each new decision targets a historical HOLD ID and exact source; NFC, numeric tokens and Event_XXX markers checked. No changes to ambiguous avatar labels, proper names or internal codes. Still not tested in ROM or full restore of all prior batches.

## Recovery
reviews/cp014a-resolutions.jsonl.bz2.b64 — SHA256 uncompressed 917a9885679d89cf22a79b213075a24115d0f57f6edcd0e56f1a29f032218eaa.
Readback of resolution file from GitHub matched uploaded data. unpack_batches.py appends the 73 translations, preserves historical ledger files, checks the old HOLD IDs, exports remaining-HOLD-CP014a-9404.jsonl, and merged-CP014a-19709.jsonl. Full recovery remains untested.

Next CP014b: prioritize unambiguous visible UI/appearance descriptions and source-name cross-checks. Do not replace untranslated proper names without reliable mapping. No changes to main.

Mốc trước: [CP013l](CHECKPOINT-013l.md). [Quy tắc ngôi xưng](NGOI_XUNG.md).
