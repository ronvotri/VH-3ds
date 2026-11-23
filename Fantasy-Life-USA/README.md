# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 007 hoàn thành — 23/11/2026**

- Bộ nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, **34.812 ID**.
- **Đã dịch/QA cấu trúc 8.500 / 34.812 ID (24,42%)**, còn **26.312**.
- CP001–CP006: 6.500 ID. **CP007: thêm 2.000 ID.**
- Đây là tiến độ dịch **bộ chuỗi bàn giao**, **không phải tỷ lệ ROM chơi được**.
- Nhánh riêng `vh/fantasy-life-usa`; không sửa `main`.

## CP007 — Phạm vi đã hoàn thành

| Nguồn | Số ID được duyệt | Nội dung |
|---|---:|---|
| 0066–0069 | 348 | Tóm tắt nhiệm vụ, NPC, item và điều kiện |
| 0070–0071 | **0 (HOLD 200)** | Chuỗi debug/bản đồ phiên âm Nhật, bản Anh bị dịch thô, **không được coi đã dịch** |
| 0072–0076 | 446 | UI, thông báo, mô tả, lời thoại và nhãn kỹ thuật |
| 0077–0083 | 700 | Quest/Event nội bộ, giữ ID/mã event |
| 0084–0088 | 500 | Challenge nghề: Angler, Hunter, Blacksmith, Woodcutter, Tailor, Paladin |
| 0089 | 6/100 | Paladin/Alchemist Challenge đầu gói |
| **Tổng CP007** | **2.000** | Chỉ các ID đã đối chiếu cấu trúc nguồn |

**Cảnh báo dữ liệu:** Gói `0070–0071` có các chuỗi nguồn vô nghĩa (ví dụ “rice impossible Dragon”) và địa danh không rõ. Không được đoán hoặc đưa bản nháp của chúng vào bản game. Tệp `HOLD-0070-0071-NOT-APPROVED.csv` để bảo lưu và kiểm sau, **không nằm trong bảng dịch chính**. Một số string debug/UI ở `0072–0074` cũng cần xác minh ngữ nghĩa theo cảnh game.

## Khôi phục toàn bộ 8.500 bản dịch

Trong thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Công cụ dùng Python stdlib để giải nén các file bzip2/gzip + base64 ở `translations/`, kiểm SHA-256, bản dịch rỗng và ID trùng rồi tạo:

- `translations/cp007-new-2000.jsonl` — 2.000 ID mới.
- `translations/merged-CP007-8500.jsonl` — 8.500 ID được duyệt, **không liên tiếp** vì chưa làm 0070–0071.
- Các file checkpoint cũ như `cp005-complete-2000.jsonl`, `cp006-complete-2000.jsonl`.

**SHA-256 CP007 mới:** `52b047c193a310f7942c78b4409dab9d217c1982ea0110798c95677b0ad40cb8`.

Mỗi dòng chứa `{"id":"FL-USA::...","vi":"..."}`. Ghép theo ID vào `01_CAN_DICH.jsonl` của nguồn gốc; không sửa `source`, `raw_hex`, `controls_hex`, `references`, `length_bindings`, `alias_ids`.

## Phong cách và giới hạn

Giữ tên riêng, item, skill, Life, Rank, Bounty và địa danh bằng tiếng Anh. Diễn đạt lời Việt có dấu, gọn, gần gũi, hài đúng nhân vật; thông báo và Quest/Event debug dịch theo chức năng. Giữ nguyên biến thể `EN_A/EN_B`, mọi `{CTRL:hex}` đúng giá trị/thứ tự và marker màu/nhánh giới tính.

**QA cấu trúc:** 2.000/2.000 ID đúng nguồn, không trùng 6.500 ID cũ, 5.814 token mới nguyên vẹn, Unicode NFC và literal markup/newline đúng nguồn.

**CHƯA KIỂM:** font Việt trên 3DS; chiều rộng/tràn khung và phân trang; speaker→target/ngôi xưng thực tế, nhánh runtime nam/nữ; tên kỹ thuật Nhật bị dịch thô. Chưa có patch RomFS/CIA.

**Tiếp theo:** `0089` mục thứ 7–100, rồi `0090` và các gói tiếp. Gói 0070–0071 phải xử lý lại riêng khi có nguồn Nhật hoặc màn hình thật. Xem `CHECKPOINT-007.md`, `QA-007.md`, `ISSUES-007.md`, `NGOI_XUNG_CP007.md`.
