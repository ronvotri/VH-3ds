# Fantasy Life (USA) — Việt hóa Votri Valley

**CP009 HOÀN TẤT — 24/11/2026**

- Bộ bàn giao: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, **34.812 ID**.
- CP001–CP008: 10.500 ID; **CP009a: 445**, **CP009b: 525**, **CP009c: 1.030** → **CP009 trọn 2.000 ID mới**.
- **Tổng được xử lý/QA cấu trúc: 12.500/34.812 ID (35,91%)**, còn **22.312 ID**.
- **12.499 ID có bản dịch khác nguồn**, 1 nhãn Tây Ban Nha `<color name="green"/>Orbe de especialidad<color/>` từ CP007 vẫn giữ nguyên để xác minh tên item; không coi nhãn đó đã Việt hóa.
- 200 mục gói `0070–0071` là map/debug thiếu ngữ nghĩa tiếp tục **HOLD**, không cộng vào 12.500 ID.
- Mọi cập nhật chỉ trên nhánh **`vh/fantasy-life-usa`**, không sửa `main`.

## CP009c — tiêu đề Challenge mới

- Dịch **1.030** tiêu đề Challenge từ gói `0137–0146` và `0147#1–32`. Tổng có 1.032 ID nguồn trong phạm vi, **không tính hai tên riêng chỉ giữ nguyên English**: `Philosopher's Stone` (`0140#90`) và `Levitanian Sardine` (`0145#40`).
- Phân bổ EN_A **784** và EN_B **246**, thuộc Blacksmith, Woodcutter, Tailor, Alchemist, Cook, Mercenary/Paladin, Carpenter, Wizard, Miner, Angler, Hunter.
- Lời Việt ngắn gọn, tự nhiên, có lối chơi chữ tương đương khi phù hợp; giữ nguyên tên item/skill/quái/cá, Life, Rank và địa danh. Không thêm yêu cầu, số lượng hoặc phần thưởng ngoài nguyên tác.
- Đã đồng nhất các tiêu đề trùng gốc, giữ `Plains Iron` và `Al Maajik Gold` nguyên cụm; sửa `0142#14` trước khi xuất.
- **Chỉnh một ID cũ không tính thêm tiến độ:** `FL-USA::F00008554@000014f8` đổi từ `Blacksmith's Song: Behold, the Master Smith!` thành `Khúc ca Blacksmith: Bậc thầy rèn lộ diện!`.

## Khôi phục bản gộp

Trong thư mục `Fantasy-Life-USA`:

```bash
python3 unpack_batches.py
```

Chương trình giải nén/check SHA-256 dữ liệu checkpoint đã commit, kiểm ID/câu rỗng, áp một sửa lỗi cũ, tạo:

- `translations/cp009c-new-1030.jsonl` — 1.030 mục mới.
- `translations/cp009-complete-2000.jsonl` — CP009a+b+c, **2.000 mục**.
- `translations/merged-CP009-12500.jsonl` — **12.500 ID** tích lũy, đã áp sửa một ID cũ.

Các file nguồn GitHub: `translations/cp009c-1030.jsonl.bz2.b64` và `translations/cp009c-corrections-1.jsonl`.

SHA-256 CP009c: `c72f173c149a9e7ec8453829c81dc3081f08c0e3661e66dde675f0e6eec40fd8`.

SHA-256 CP009 hoàn tất: `e61bfaa20fbb9c9fb58066052b814e9681ba426eba2b5c111376d730c0581477`.

SHA-256 bản gộp 12.500: `bb8d3a23d01e5c1f2c4b89fbe2aec35529d62475a81acf638c9a18998ecad67b`.

Bản JSONL dịch chỉ gồm `id` và `vi`; khi áp vào `01_CAN_DICH.jsonl` của ZIP nguồn phải ghép theo `id`, không sửa `source`, `raw_hex`, `references`, `alias_ids`, `length_bindings` hoặc control tokens.

## QA & tồn đọng

- Kiểm **12.500 ID** với nguồn 34.812: **0** ID sai, thiếu, trùng hoặc bản dịch rỗng.
- **63.414 mã `{CTRL:hex}`** của bản gộp giữ nguyên nội dung và thứ tự; gói CP009c chỉ là title nên có **0 token mới**.
- Unicode NFC PASS, hai tên item-only không tính là dịch, và một tên Spanish-only cũ còn chờ xác minh.
- **Chưa QA trên 3DS** font tiếng Việt, chiều rộng pixel, ngắt trang, nút bấm và speaker/target. **Chưa có patch RomFS/CIA chơi được**; 35,91% là tỷ lệ xử lý ID trong bộ nguồn, không phải tỷ lệ ROM đã chơi được.
- Xem `CHECKPOINT-009-complete.md`, `QA-009c.md`, `ISSUES-009c.md`, `THUAT_NGU_CP009c.md`.

**Tiếp theo:** `0147` mục 33 trở đi, rồi `0148+`. Cần xử lý lại 200 ID HOLD khi có nguồn Nhật/screenshot.
