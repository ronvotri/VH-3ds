# Super Pokémon Rumble — EUR Rev 1 (Việt hóa)

**Đây là nguồn EUR Rev 1**, không phải bản Pokémon Rumble Blast USA đã khảo sát ở Checkpoint 002. Không nhập nhầm bản dịch vào ROM USA.

- Title ID: `0004000000066D00`, product `CTR-P-ACCP`, nguồn tiếng Anh `EU_English`.
- Bộ giao nguồn ngày 20/11/2026: **6.159 record trong 16 MSBT**, gồm 1.932 mục cần dịch, 2.590 mục giữ tiếng Anh, 443 debug, 1.194 rỗng.
- Bản dịch hiện có: **158/1.932 mục**, hoàn tất toàn bộ phần cần dịch của `kaiwa.msbt`; còn **1.774** mục.
- [Bản dịch 158 câu, JSONL](ban_dich/kaiwa_CP003_158.jsonl) (ID `EUR-REV1::/msg/EU_English/kaiwa.msbt.cx#00000` đến `#00161`; các ID rỗng không được thêm).
- [Báo cáo và checklist](CHECKPOINT-003.md); [Sơ đồ giọng nói](XUNG-HO-KAIWA.md).

## Quy tắc

Giữ EN tên Pokémon, item, Move/Skill, Special Trait, Type, form và thuật ngữ/địa danh chính. Dịch lời thoại và văn bản còn lại sang tiếng Việt có dấu NFC. Ngữ điệu thân thiện, Gen Z vừa phải; không đoán danh tính người nói từ label. Giữ chính xác mã `{CTRL:hex}`.

## QA

Đã nhập thử 158 mục bằng `tools/nhan_ban_dich.py` từ ZIP bàn giao: **0 lỗi token, 0 trùng/khác ID, 0 Unicode lỗi**. Có 4 cảnh báo rà từ điển: `Awesome`, `Amazing`, `Wrap`, `Return` là từ thường trong câu, không phải tên Move cần giữ trong ngữ cảnh này.

**Chưa test game, chưa vá font hoặc repack MSBT/CX**, font gốc thiếu 100–108 glyph tiếng Việt tùy kiểu. 158 câu vẫn ở trạng thái `ban_nhap`; việc đo chữ 3DS, kiểm giọng đúng NPC và test màn hình cần làm sau.
