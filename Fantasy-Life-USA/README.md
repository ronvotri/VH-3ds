# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 002 — 22/11/2026**

- Nguồn bàn giao: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, 34.812 chuỗi chính.
- Đã biên dịch **300/34.812 ID** (CP001: 100; CP002: +200 trong gói 0002 và 0003). Còn 34.512.
- Phạm vi CP002: Life, vùng đất Reveria, cốt truyện, nhiệm vụ Master, tiệm nhuộm, trang bị, dịch chuyển và kết nối.
- Dữ liệu mới **đã được đẩy lên nhánh riêng**, không sửa `main` hay công trình Việt hóa game 3DS khác.

## Mở dữ liệu Việt hóa

Trong thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Script sẽ giải nén từ hai bản văn nén được commit ở `translations/`, xác minh SHA-256 và kiểm tra 300 ID duy nhất, sau đó tạo:
- `translations/batch-001.jsonl` — 100 câu CP001
- `translations/cp002-new-200.jsonl` — 200 câu CP002
- `translations/merged-001-003.jsonl` — bảng dịch hợp nhất 300 câu

Mỗi dòng JSONL chứa `{"id":"FL-USA::...", "vi":"bản dịch có dấu"}`; đối chiếu theo `id` với `01_CAN_DICH.jsonl` trong bộ gốc. Không ghi đè các trường `source`, `raw_hex`, `alias_ids`, `references` hoặc `length_bindings`.

## Quy tắc

Giữ tên riêng, Life, item, skill và thuật ngữ chính bằng tiếng Anh; phần diễn giải dùng tiếng Việt tự nhiên, vui nhẹ và không chế tình tiết. Tuyệt đối bảo toàn mọi `{CTRL:hex}` và thứ tự token. Hai biến thể EN_A/EN_B không tự gộp. Xem `NGOI_XUNG.md`.

**Giới hạn:** Mới dịch dữ liệu nguồn, chưa vá font tiếng Việt, chưa xuất patch/ROM, chưa kiểm tra tràn khung trên 3DS. `speaker` trong bộ nguồn là `unknown`, do đó xưng hô nhân vật chỉ là nguyên tắc tạm; cần QA theo cảnh.

**Để tiếp tục**: xử lý gói `0004_hoi_thoai_va_huong_dan.txt`, nối tiếp 300 ID đã có.
