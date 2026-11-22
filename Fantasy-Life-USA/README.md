# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 003 — 23/11/2026**

- Bộ nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip` · Title ID `0004000000113200` · 34.812 mục.
- **Đã dịch 500/34.812 ID (1,44%)**: CP001 100 · CP002 200 · **CP003 200** (gói 0004–0005). Còn 34.312.
- CP003: cảnh báo save/SD/StreetPass, Ally/Link Mode, Parental Controls, Joyne Plaza, mô tả vũ khí và trang bị.
- Nhánh Việt hóa riêng `vh/fantasy-life-usa`; không sửa `main`.

## Khôi phục toàn bộ bảng dịch

Trong thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Công cụ giải nén 3 tệp của các checkpoint từ `translations/`, kiểm tra SHA-256 và 500 ID duy nhất rồi tạo:

- `translations/batch-001.jsonl` — CP001, 100 mục.
- `translations/cp002-new-200.jsonl` — CP002, 200 mục.
- `translations/cp003-new-200.jsonl` — CP003, 200 mục.
- `translations/merged-001-005.jsonl` — toàn bộ **500** mục.

Dạng dữ liệu mỗi dòng: `{"id":"FL-USA::...", "vi":"bản dịch có dấu"}`. Ghép qua `id` vào nguồn gốc `01_CAN_DICH.jsonl` và giữ nguyên các trường `source`, `raw_hex`, `alias_ids`, `references`, `length_bindings`.

## Quy tắc dịch & QA

- Giữ tên nhân vật, địa danh, Life, item, skill và thuật ngữ chính bằng tiếng Anh.
- Lời thoại Việt tự nhiên, dí dỏm vừa phải; cảnh báo hệ thống rõ ràng, không đùa sai chỗ.
- Giữ đủ mọi `{CTRL:hex}` đúng thứ tự, không xóa hay sửa token.
- Giữ riêng `EN_A` và `EN_B` theo ID; không gộp biến thể.
- `speaker=unknown` tại bộ nguồn: mọi ngôi xưng theo nhân vật phải được kiểm khi có cảnh thật.
- Xem `NGOI_XUNG.md`, `CHECKPOINT-003.md` và `QA-003.md`.

**Lưu ý:** Đây là **bản dịch văn bản**, chưa có font Việt, patch/ROM hay kiểm tra hiển thị trên Nintendo 3DS. Độ dài câu và chức năng online phải thử nghiệm độc lập.

**Tiếp theo:** gói `0006_hoi_thoai_va_huong_dan.txt` (ID 501–600).
