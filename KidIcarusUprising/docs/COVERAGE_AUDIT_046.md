# Kid Icarus: Uprising — Coverage Audit 046

**Branch:** `vh/kid-icarus-uprising`
**Source:** `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip` → `ban_dich/tieng_anh_can_dich.jsonl`
**Scope:** GitHub `translations/batch_001.jsonl`–`batch_046.jsonl`, excluding deleted duplicate `batch_043.jsonl`.
**Audit level:** ID uniqueness/coverage, source ZIP counts, targeted manual source comparisons. **Not** a comprehensive semantic source-to-translation audit or in-game test.

| Source section | Total IDs | Nonempty source | Unique processed IDs | Nonempty IDs not in batches |
| --- | ---: | ---: | ---: | ---: |
| `resident/03.bin` | 2,147 | 2,128 | 1,513 | 615 |
| `resident/04.bin` | 222 | 199 | 26 | 173 |
| All `stage/.../msg_00.bin` dialogue | 1,698 | 1,696 | 1,696 | 0 |
| **Total** | **4,067** | **4,023** | **3,234** | **789** |

## Observations

- The source has **44 blank entries**: 19 in `resident/03.bin`, 23 in `resident/04.bin` and 2 in dialogue (`a2100#00008` and `a2500#00038`). These are not treated as untranslated prose.
- All **1,696 nonempty stage-dialogue IDs** have a batch entry. This is *draft coverage*, not a guarantee of accuracy, text fit, speaker attribution or patch compatibility.
- GitHub `batch_043.jsonl` was previously removed because all its 15 entries duplicated `batch_016.jsonl`'s `resident/04.bin` IDs. Do not include batch 043 when counting coverage.
- The surviving groups checked contain no repeated IDs: batches 001–016 (1,479), 017–036 (1,382), 037–042 plus 044–045 (372), and batch 046 (2). **Correction in Checkpoint 060:** batch 046's `#01656 Music` had already been translated in batch 015; it was a duplicate, so the original unique-count assumption was wrong.
- **3,234 / 4,023 = 80.39% processed-source coverage**; NOT an 80.41% rate of translated Vietnamese text. Existing entries may deliberately preserve English names and key terms.
- The remaining 788 nonempty entries contain many names, Weapons, Powers, locations, symbols and other source strings that should remain unchanged under the project's localization conventions. Do not bulk-copy these into new batches merely to inflate progress.
- `batch_046.jsonl` originally repeated `resident/03.bin#01656` (Music → Nhạc) from batch 015. Checkpoint 060 removed that duplicate; only `#00085` (TOUCH! → CHẠM!) was a genuine new UI label. Historical figures above are corrected unique-ID counts, not the mistaken original claim.

## Next QA priorities

1. Review actual `resident/03.bin` and `resident/04.bin` not-yet-processed source entries one by one. Label them **translate / preserve official name / symbol or blank**, not simply missing.
2. Compare every batch's `source` (where present) and `vi` to the exact original source-ID text; especially batches with `vi` only. Flag mismatched source records or missing control tokens.
3. Run in-game 3DS line-length, font glyph, newline and control-code checks before changing statuses from `draft`.
4. Audit character address/pronoun consistency: Pit/Palutena, Dark Pit, Viridi, Pyrrhon, Hades, Dyntos and Arlon.

*This report is a bookkeeping audit, not a release-ready validation.*
