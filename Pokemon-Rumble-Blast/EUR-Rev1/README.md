# Super Pokémon Rumble — EUR Rev 1 (Việt hóa)

**Dự án chỉ dành cho EU English / EUR Rev1**, Title ID `0004000000066D00`, product `CTR-P-ACCP`. **Không dùng bản dịch này để vá game USA** `0004000000066C00`.

## Tiến độ đến Checkpoint 008

- Bộ gốc: **6.159 record / 16 bảng MSBT**; phân loại **1.932 mục cần dịch**, 2.590 mục giữ EN, 443 debug, 1.194 rỗng.
- **1.260/1.932 mục đã xử lý (65,22%)**, còn **672 mục**.
- Đã hoàn tất bản nháp của `kaiwa.msbt` (158/158), `main.msbt` (726/726), `NoticeDesc.msbt` (376/376).

| Đợt | Phạm vi | JSONL | Báo cáo |
|---|---|---|---|
| CP003 | 158 mục `kaiwa` | [Xem](ban_dich/kaiwa_CP003_158.jsonl) | [QA](CHECKPOINT-003.md) |
| CP004 | 200 mục `main` | [Xem](ban_dich/main_CP004_200.jsonl) | [QA](CHECKPOINT-004.md) |
| CP005 | 200 mục `main` | [Xem](ban_dich/main_CP005_200.jsonl) | [QA](CHECKPOINT-005.md) |
| CP006 | 200 mục `main` | [Xem](ban_dich/main_CP006_200.jsonl) | [QA](CHECKPOINT-006.md) |
| CP007 | 126 mục cuối `main` | [Xem](ban_dich/main_CP007_126.jsonl) | [QA](CHECKPOINT-007.md) |
| CP007 | 74 mục đầu `NoticeDesc` | [Xem](ban_dich/NoticeDesc_CP007_74.jsonl) | [QA](CHECKPOINT-007.md) |
| CP008 | 302 mục còn lại `NoticeDesc` | [Xem](ban_dich/NoticeDesc_CP008_302.jsonl) | [QA](CHECKPOINT-008.md) |

## 672 mục còn lại

| Bảng | Mục |
|---|---:|
| `WazaDesc.msbt` | 387 |
| `makuai.msbt` | 119 |
| `prefix.msbt` | 86 |
| `StageDesc.msbt` | 35 |
| `PasswordPiiDesc.msbt` | 25 |
| `PartsDesc.msbt` | 20 |

## Quy tắc

Giữ nguyên English: tên Pokémon, item, Move/Skill, các thuật ngữ, tên riêng và chế độ chính. Việt hóa lời thoại, hướng dẫn, thông báo và trạng thái thường bằng tiếng Việt NFC, tự nhiên, Gen Z vừa đủ, không tự suy đoán người nói. Mỗi record giữ nguyên ID và mọi mã `{CTRL:hex}`.

[Quy tắc xưng hô theo ngữ cảnh `kaiwa`](XUNG-HO-KAIWA.md).

## QA và tình trạng patch

- Importer của bộ nguồn gốc nhận đủ **1.260** bản nháp. CP008 giữ nguyên **77 token** ở 302 record, không lỗi thứ tự hoặc ID.
- Có **22 cảnh báo thuật ngữ** tích lũy cần rà cảnh (chủ yếu tên Move/Special Trait số nhiều và `Return` là lựa chọn menu đã Việt hóa); chi tiết trong [CP008](CHECKPOINT-008.md).
- Toàn bộ vẫn ở trạng thái `ban_nhap`. **Chưa repack MSBT/CX, chưa bổ sung glyph/font Việt, chưa test 3DS/giả lập, chưa có patch chơi được.**

Bản ZIP Checkpoint 008 bàn giao trong hội thoại gồm 302 mục mới, bản gộp 1.260 mục, corpus đầy đủ 6.159 record có trường `vi`, CSV đối chiếu và báo cáo QA.
