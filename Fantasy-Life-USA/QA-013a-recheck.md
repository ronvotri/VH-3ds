# Fantasy Life (USA) — CP013a recheck / CP013b handoff

Date: 2026-11-25. Branch: `vh/fantasy-life-usa` (do not alter `main`).

- GitHub branch commit before this recheck: `8984fa9a2613e549066820116403bb3fddfd3b16`.
- CP013a is **already committed**: 285 new appearance labels, total **18,785 / 34,812 (53.96%)**; remaining **16,027**. Do not double count it.
- Decoded `cp013a-285.jsonl.bz2.b64` from the matching Library transfer. 285 lines, unique IDs within this batch, nonempty Vietnamese text, all NFC.
- There is **one repeated Vietnamese target**: `Mắt lấp lánh` at CP013a rows 50 and 159. This does not automatically mean a translation error; compare the English source and avatar visuals before modifying.
- The original `01_CAN_DICH.jsonl` **is not in the branch**; the handover ZIP is not accessible in this new chat's mounted files and was not found by a filename search in the connected Drive. Therefore CP013b has **0 verified new translations** in this session.
- The new `triage_cp013b.py` reads the original user-supplied ZIP and existing translation batches, ensures source-ID consistency, and writes a review queue. Its classification is heuristic, not a decision to translate.
- Keep names, items, skills, Life, Rank, all `{CTRL:hex}` tokens and EN_A / EN_B differences. Keep 0070–0071 HOLD until contextual approval; do not count copied English names.
- Structural QA does not equal in-game validation. Font, pixel width, page layout, and RomFS/CIA patch have **not** been verified.

**Next practical step:** supply the *original handover ZIP* containing `01_CAN_DICH.jsonl`; run `python3 triage_cp013b.py /path/to/ZIP` to select source-grounded, meaningful next strings rather than guessing.
