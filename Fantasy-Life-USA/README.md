# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 005a — 23/11/2026 · phần 1 của CP005**

- Nguồn: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip` · Title ID `0004000000113200` · **34.812 mục nguồn**.
- Đã dịch thật **3.200 / 34.812 ID (9,19%)**: CP001 100 · CP002 200 · CP003 200 · CP004 2.000 · **CP005a 700** (gói 0026–0032).
- Còn **31.612 ID**. Mục tiêu CP005 là 2.000 mục mới; hiện mới đạt 700, cần **thêm 1.300** để kết thúc CP005. Không gọi CP005 là hoàn thành.
- Giữ toàn bộ dữ liệu trên nhánh riêng **`vh/fantasy-life-usa`**, không sửa `main`.

## Nội dung CP005a

Gói 0026–0027: hướng dẫn Life, Special Skill, Mystic Skill và các tính năng hệ thống. Gói 0028: biến thể EN_B God Mode/God Skill/Link Mode/Magician và mô tả item. Gói 0029: thư của NPC và các Master. Gói 0030: mô tả skill và hội thoại. Gói 0031–0032: thoại NPC ở Castele và các biến thể tương ứng.

## Khôi phục 3.200 mục

Tại thư mục `Fantasy-Life-USA` chạy:

```bash
python3 unpack_batches.py
```

Script đọc 5 bản dịch nén (CP001/CP002/CP003/CP004/CP005a) trong `translations/`, đối chiếu SHA-256 và bảo đảm 3.200 ID không trùng, rồi tạo:

- `translations/batch-001.jsonl`: 100 ID.
- `translations/cp002-new-200.jsonl`: 200 ID.
- `translations/cp003-new-200.jsonl`: 200 ID.
- `translations/cp004-new-2000.jsonl`: 2.000 ID.
- `translations/cp005a-new-700.jsonl`: 700 ID.
- `translations/merged-001-032.jsonl`: **3.200 ID tích lũy**.

Mỗi dòng có dạng `{"id":"FL-USA::...", "vi":"bản dịch tiếng Việt có dấu"}`. Ghép theo `id` với `01_CAN_DICH.jsonl` của nguồn, giữ nguyên source, references, alias, raw_hex và các trường nhị phân.

## Quy tắc cố định

- Giữ tên riêng, Life, item, skill, địa danh và thuật ngữ chính bằng tiếng Anh.
- Ngôn ngữ Việt tự nhiên, dí dỏm theo nhân vật; cảnh báo hệ thống dịch nghiêm túc.
- Các token `{CTRL:hex}` phải giữ đúng danh sách và thứ tự; nút bấm và các marker tô màu/tên chèn vào mệnh đề hợp nghĩa.
- Không tự gộp EN_A/EN_B: Creator/God, Wizard/Magician, Ally/Link Mode, Damien/Daemon, Furlin/Fluffkin theo nguồn gốc.
- `speaker=unknown` nhiều đoạn; giọng và ngôi xưng tạm theo thư ký tên, cần QA theo cảnh game.

**QA tĩnh CP005a:** 700/700 có bản dịch, đủ token, 0 ID trùng, Unicode NFC. **Chưa QA pixel/font/ngắt trang trên 3DS, chưa có patch/ROM chơi được.** Xem `CHECKPOINT-005a.md` và `QA-005a.md`.

**Tiếp theo:** gói `0033`, từ mục thứ **3.201**. Đây là hội thoại nhiều nhánh điều kiện/nút chọn, ưu tiên dịch đủ nội dung từng nhánh hơn là cố đủ chỉ tiêu 2.000 bằng cách chép lại câu nguồn.
