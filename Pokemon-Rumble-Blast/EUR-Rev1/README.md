# Super Pokémon Rumble — EUR Rev 1 (Việt hóa)

**Chỉ dành cho EU English EUR Rev 1**, Title ID `0004000000066D00`, product `CTR-P-ACCP`. Không nhập bản dịch vào ROM USA `0004000000066C00`.

## Tiến độ đến Checkpoint 010 — hoàn tất bản nháp dịch

- Nguồn: **6.159 record từ 16 bảng MSBT**.
- 1.932 record được phân loại cần dịch, 2.590 khóa EN, 443 debug, 1.194 rỗng.
- **1.932/1.932 bản nháp (100% số ID cần dịch)** đã đối chiếu ID / nhập thử; **không còn ID thuộc nhóm `translate` bị bỏ trống**.
- 9 bảng đã hoàn tất bản nháp, gồm `WazaDesc` (387/387): `kaiwa` (158/158), `main` (726/726), `NoticeDesc` (376/376), `PartsDesc` (20/20), `PasswordPiiDesc` (25/25), `StageDesc` (35/35), `prefix` (86/86), `makuai` (119/119).

| Checkpoint | Nội dung | JSONL | Báo cáo |
|---|---|---|---|
| 003 | 158 `kaiwa` | [Xem](ban_dich/kaiwa_CP003_158.jsonl) | [CP003](CHECKPOINT-003.md) |
| 004 | 200 `main` | [Xem](ban_dich/main_CP004_200.jsonl) | [CP004](CHECKPOINT-004.md) |
| 005 | 200 `main` | [Xem](ban_dich/main_CP005_200.jsonl) | [CP005](CHECKPOINT-005.md) |
| 006 | 200 `main` | [Xem](ban_dich/main_CP006_200.jsonl) | [CP006](CHECKPOINT-006.md) |
| 007 | 126 `main` + 74 `NoticeDesc` | [main](ban_dich/main_CP007_126.jsonl), [NoticeDesc](ban_dich/NoticeDesc_CP007_74.jsonl) | [CP007](CHECKPOINT-007.md) |
| 008 | 302 `NoticeDesc` | [Xem](ban_dich/NoticeDesc_CP008_302.jsonl) | [CP008](CHECKPOINT-008.md) |
| **009** | **285 mục / 5 bảng** | [PartsDesc](ban_dich/CP009_PartsDesc_20.jsonl) · [PasswordPiiDesc](ban_dich/CP009_PasswordPiiDesc_25.jsonl) · [StageDesc](ban_dich/CP009_StageDesc_35.jsonl) · [prefix](ban_dich/CP009_prefix_86.jsonl) · [makuai](ban_dich/CP009_makuai_119.jsonl) | [CP009](CHECKPOINT-009.md) |
| **010** | **387 mục cuối, `WazaDesc`** | [JSONL](ban_dich/WazaDesc_CP010_387.jsonl) | [CP010](CHECKPOINT-010.md), [QA](qa/QA_CP010.json), [134 mẫu](qa/Waza_CP010_134_templates.tsv) |

## Quy tắc

Giữ nguyên English đối với tên Pokémon, item, Move/Skill, tên riêng và thuật ngữ chính; Việt hóa lời thoại, menu, hướng dẫn và thông báo theo tiếng Việt NFC, Gen Z vừa phải và **xưng hô đúng từng cảnh**. Mỗi record giữ nguyên ID, placeholder, `{CTRL:hex}`. [Sơ đồ ngôi xưng `kaiwa`](XUNG-HO-KAIWA.md).

## QA và giới hạn

- Công cụ nhập gốc nhận **1.932/1.932 bản nháp**, còn 0 ID cần dịch; 2.590 record khóa EN được bảo toàn. CP010 giữ **9/9 mã điều khiển** và không có cảnh báo thuật ngữ mới.
- 25 cảnh báo từ điển tích lũy từ CP003–009 cần kiểm tra trong cảnh; CP010 không phát sinh cảnh báo mới (0).
- **Đã hoàn tất bản nháp 1.932 ID, chưa phải patch. Chưa repack MSBT/CX, chưa sửa font, chưa test trên máy thật/giả lập, chưa có patch chơi được.** Đếm ký tự trên mỗi dòng chỉ là QA sơ bộ, không đo độ rộng pixel của font 3DS.

**Bước kế tiếp:** QA nội dung theo scene, xử lý glyph BCFNT tiếng Việt (16 font thiếu 100–108 glyph mỗi font), sửa/đóng gói MSBT/CX, dựng patch và thử trên 3DS/giả lập đúng bản EUR Rev1.
