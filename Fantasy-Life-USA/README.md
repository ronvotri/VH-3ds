# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 006a — 23/11/2026 · CP006 đang thực hiện**

- Bộ nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, 34.812 ID.
- **Đã biên dịch 5.000 / 34.812 (14,36%)**, còn **29.812**.
- CP001–004: 2.500; CP005a–c: 2.000; **CP006a: 500** (gói 0046–0050).
- **CP006 đặt mục tiêu 2.000 câu mới, hiện chỉ có 500; còn 1.500 câu**, không ghi CP006 đã hoàn tất.
- Toàn bộ thay đổi nằm trên nhánh **`vh/fantasy-life-usa`**, không thay `main`.

## Phạm vi CP006a

0046: đóng tàu lặn, Pepita, Honey & Roy, Postman mê hoa.
0047: thầy bói, nội thất Barrel/Scarecrow, Cashew của Cocina Rica.
0048: zombie Tortuga, Bomba, Pepperonita, tiên tri Calumnus.
0049: Punching Palms/Jellings, hải tặc cầu hôn, Kevin và người trông trẻ.
0050: Fluffin, phỏng vấn đổi Life của Maajiknight, bà cụ sưu tập kính và thợ săn kho báu.

## Khôi phục bản dịch

Tại thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Bộ khôi phục giải nén 7 bản dịch CP001–CP006a, kiểm SHA-256, JSONL, tất cả ID độc nhất, rồi tạo:

- `translations/batch-001.jsonl`: 100
- `translations/cp002-new-200.jsonl`: 200
- `translations/cp003-new-200.jsonl`: 200
- `translations/cp004-new-2000.jsonl`: 2.000
- `translations/cp005a-new-700.jsonl`: 700
- `translations/cp005b-new-900.jsonl`: 900
- `translations/cp005c-new-400.jsonl`: 400
- `translations/cp005-complete-2000.jsonl`: 2.000 riêng CP005
- `translations/cp006a-new-500.jsonl`: 500 câu mới
- **`translations/merged-001-050.jsonl`: 5.000 câu tích lũy**

Mỗi dòng JSONL là `{"id":"FL-USA::...", "vi":"bản Việt hóa"}`. Ghép theo `id` với `01_CAN_DICH.jsonl` trong ZIP nguồn, giữ nguyên `source`, `raw_hex`, `alias_ids`, `references`, `length_bindings`.

## Quy tắc và QA

Giữ tiếng Anh tên riêng, địa danh, Life, item, skill và thuật ngữ chính; lời thoại Việt tự nhiên, vui đúng cá tính NPC; không tự chế cảnh và mối quan hệ khi `speaker=unknown`. Hai biến thể `EN_A`/`EN_B` giữ theo ID riêng. Tất cả token `{CTRL:hex}` phải bảo toàn.

**QA cấu trúc CP006a:** 500 ID mới được xác minh nguồn, không trùng, không rỗng, token đúng nội dung và thứ tự, Unicode NFC. Đã kiểm 250 tên/thuật ngữ bọc marker màu (chuẩn hóa khoảng trắng do xuống dòng), và không thiếu bất kỳ trị số dạng số nào trong nguyên tác. Các cảnh báo kiểm đếm số do token còn được giữ trong báo cáo; chưa phải đánh giá ngữ nghĩa toàn bộ.

**CHƯA THỂ CHƠI TRÊN 3DS:** chưa vá font Việt, chưa đo chiều rộng pixel/khung thoại, chưa QA scene/ngôi xưng, chưa xuất patch RomFS/CIA.

**Tiếp theo:** gói **0051**, câu thứ **5.001**. Xem `CHECKPOINT-006a.md`, `QA-006a.md`, `NGOI_XUNG_CP006a.md`.
