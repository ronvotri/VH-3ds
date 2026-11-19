# Kid Icarus: Uprising — QA Checkpoint 047

## Deliverable
Added `KidIcarusUprising/audit_translations.py` to audit source/overlay integrity without changing translation text.

Run from the repository root, with the original handover ZIP available locally:

```bash
python KidIcarusUprising/audit_translations.py \
  --zip KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip \
  --translations KidIcarusUprising/translations \
  --output KidIcarusUprising/docs/QA_047_RESULT.json
```

An exit code of 1 means the script found structural errors. JSON results include exact IDs for review. Warnings, such as missing `source` snapshots in older batches, do not automatically indicate translation errors.

## Source ZIP verification
The actual `ban_dich/tieng_anh_can_dich.jsonl` in the handover ZIP contains:
- `resident/03.bin`: 2,147 rows; 2,128 nonempty English entries.
- `resident/04.bin`: 222 rows; 199 nonempty English entries.
- Stage dialogue: 1,698 rows; 1,696 nonempty English entries.
- **Total: 4,067 rows; 4,023 nonempty English entries; 44 blank rows.**

Verified examples of source-ID identity and literal newlines:
- `resident/03.bin#00085`: `TOUCH!`
- `resident/03.bin#01656`: `Music`
- `resident/03.bin#02143`: `Motion Control`
- `resident/03.bin#02144`: `Motion\nControl:\nON`
- `resident/03.bin#02145`: `Motion\nControl:\nOFF`
- `resident/03.bin#02146`: `Toggle the motion control on or off.\nWhen enabled, move the system to aim the reticle.`

Earlier batch spot-checks found the source includes intentional repeated dialogue lines (e.g. `a1800#00035` and `#00036`, and `a2300#00001` and `#00002`). They have separate, valid IDs; **do not deduplicate by text**.

## Known bookkeeping state
- The previous coverage audit (046) counted **3,235 unique processed IDs**, **788 nonempty source IDs without overlays**, and no detected duplicate IDs in surviving batches. No newly translated ID was added in batch 047.
- `batch_043.jsonl` was deleted as a duplicate of existing `batch_016.jsonl` entries. Do not count it.
- Full repository source-text audit is **not yet claimed complete**: run the new script on a checkout containing all batch files and the supplied ZIP, then review any errors/warnings before status changes.
- Preserve English names, items, Weapon/Power terms and game locations per style guide.
- QA of semantics, speaker identity, line length, 3DS font/glyph support, and patch integration remains **pending**.

**Checkpoint 047 is QA tooling, not a new translation batch or an in-game-tested release.**
