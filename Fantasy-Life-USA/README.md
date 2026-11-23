# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 005 hoàn thành — 23/11/2026**

- Nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, tổng **34.812 mục**.
- **Đã dịch 4.500/34.812 (12,93%)**, còn **30.312 mục**.
- CP001–CP004: 2.500 mục; **CP005 trọn 2.000 mục**: CP005a 700 (0026–0032), CP005b 900 (0033–0041), CP005c 400 (0042–0045).
- Nhánh làm việc riêng `vh/fantasy-life-usa`. Không ghi đè `main` hoặc dự án game khác.

## Khôi phục dữ liệu

Chạy trong thư mục `Fantasy-Life-USA`:

```bash
python3 unpack_batches.py
```

Công cụ giải nén 6 checkpoint, kiểm SHA-256 và 4.500 ID duy nhất, tạo:

- `translations/batch-001.jsonl` — 100
- `translations/cp002-new-200.jsonl` — 200
- `translations/cp003-new-200.jsonl` — 200
- `translations/cp004-new-2000.jsonl` — 2.000
- `translations/cp005a-new-700.jsonl` — 700
- `translations/cp005b-new-900.jsonl` — 900
- `translations/cp005c-new-400.jsonl` — 400
- **`translations/merged-001-045.jsonl` — 4.500 câu tích lũy**

Mỗi dòng là `{"id":"FL-USA::...", "vi":"bản dịch có dấu"}`. Ghép theo `id` với `01_CAN_DICH.jsonl` của bộ nguồn, giữ nguyên `source`, `raw_hex`, `references`, `alias_ids`, `length_bindings`.

## Nội dung CP005c

- 0042: Marine Silk, Snow Runners, Sun/Star/Moon Clusters, sưu tập kiếm và trang phục.
- 0043: các nhiệm vụ Tailor, người nuôi bọ chét, bưu điện Lettina và câu chuyện Roland.
- 0044: người sưu tầm Royal Furniture giả làm thầy tiên tri, Magical Pudding/Pie, hải tặc mê thời trang, chú chim thích hạt.
- 0045: đầu bếp nuôi đám hải tặc, Alejandro khó tính và dự án đóng thuyền sa mạc.

## Quy tắc và QA

- **Giữ tiếng Anh** cho tên nhân vật, địa danh, Life, item, skill và thuật ngữ chính; dịch còn lại sang tiếng Việt tự nhiên, hài đúng nhân vật.
- Giữ hai biến thể `EN_A/EN_B` theo **ID gốc** (Dueling/Duelling, Super/Superior, Aridian/Drysand).
- Bảo toàn `{CTRL:hex}` đúng nội dung và thứ tự. Hai lỗi tiền tố nam/nữ đã sửa trước khi đóng CP005c.
- **QA tĩnh 4.500/4.500 PASS:** ID đối chiếu nguồn, không trùng, không mất token, không câu rỗng, Unicode NFC chuẩn.
- Chưa kiểm font Việt, chiều rộng pixel, ngắt trang, ngôi xưng theo scene/runtime, và chưa có bản patch/CIA chạy được.

Chi tiết trong `CHECKPOINT-005c.md`, `QA-005c.md`, `NGOI_XUNG_CP005c.md`.

**Tiếp theo:** gói `0046`, từ mục thứ 4.501. Mục tiêu 2.000 câu mỗi đợt chỉ là mức phấn đấu; không tính câu chưa được biên dịch và QA.
