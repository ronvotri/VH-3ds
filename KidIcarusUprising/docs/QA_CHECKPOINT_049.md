# Kid Icarus: Uprising — QA Checkpoint 049

## Scope
Focused semantic and tone review of previously committed dialogues in Chapters 22–25 against the original handover ZIP `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`, focusing on three confirmed translation improvements. **Not** a full-game semantic QA pass.

## Corrections committed in-place

| Source ID | Original English | Old Vietnamese | Revised Vietnamese | Reason |
| --- | --- | --- | --- | --- |
| `a2300.zrc#00006` | Hades has overstepped his boundaries by exploiting and desecrating souls. | Hades đã vượt quá giới hạn, lợi dụng và xúc phạm các linh hồn. | Hades đã vượt quá giới hạn, lợi dụng và báng bổ các linh hồn. | `desecrating` means desecrating/profaning, not simply insulting. |
| `a2400.zrc#00025` | Of course! You want to slay Hades to protect the celestial balance. | Tất nhiên! Các ngươi muốn hạ Hades để bảo vệ thế cân bằng thiên giới. | Tất nhiên! Các ngươi muốn hạ Hades để giữ gìn thế cân bằng giữa các cõi. | Avoid wrongly narrowing `celestial balance` to only the heavenly realm; preserve context of all realms. |
| `a2500.zrc#00020` | On to death! / On to victory! | Đến chỗ chết nào! / Tiến tới chiến thắng! | Đến tận cửa tử! / Tiến tới chiến thắng! | Make two simultaneous exclamations natural in Vietnamese; keep spacing between two utterances. |

## Validation
- Each changed record's stored English `source` was checked against the original ZIP using its exact `a2300`, `a2400` or `a2500` ID.
- These source rows have no special control bytes (`controls_hex: []`).
- Re-fetched the three modified batch files from GitHub after the commits; **3/3 target translations are present**.
- Kept original IDs, English `source`, batch status, and overall JSONL row counts unchanged.
- **No new source IDs covered**: audited-coverage count stays **3,235 / 4,023** as documented in checkpoint 046.

## Pending
- Audit speaker identity and pronoun assignment over all the scene dialogue, not just selected samples.
- Validate font coverage, byte budgets, control codes and text wrapping on a built 3DS ROM.
- Run `KidIcarusUprising/audit_translations.py` on the full checkout and ZIP, and review all warnings and errors before declaring a structural QA PASS.

All changes remain `draft`; no on-device testing is claimed.
