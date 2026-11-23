# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 006b — 23/11/2026 · CP006 chưa hoàn tất**

- Bộ gốc: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, gồm **34.812 ID đã chọn để giao dịch**, chưa khẳng định bao phủ mọi chữ trong game.
- **Đã dịch 5.500/34.812 ID (15,80%)**: CP001–004 2.500, CP005 2.000, CP006a 500, **CP006b 500**.
- **Còn 29.312 ID**. Mục tiêu CP006 là 2.000 câu mới, hiện đạt **1.000/2.000**, cần thêm 1.000 câu ở gói 0056–0065 để khép.
- Nhánh riêng **`vh/fantasy-life-usa`**; không ghi đè `main`.

## Nội dung CP006b (0051–0055)

- 0051: thợ săn kho báu mê thịt rồng, nhà nghiên cứu Ornamental/Pirate/Evil Carp, Snoot's Emporium, Woodcutter.
- 0052: ghép việc cho Alchemist, Tailor, Blacksmith; tiên tri Calumnus; người đưa thư và côn trùng/Jackals.
- 0053: các nhiệm vụ của Zerk, Khubz mê cầu vồng và đầu bếp bị cả hội bạn của vợ đặt món.
- 0054: dân chúng cần đánh quái nhưng để Dark Sultan nhận công, Chai và đồ nội thất Forest, Hội Calumnus, Mummies.
- 0055: thợ săn kho báu nhát gan, người buôn đồ kỳ lạ, NPC cây nói ngọng, Paul mê pancake, Henrietta chăm gà.

## Khôi phục **5.500 câu**

Tại `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Script giải nén các bản dịch nén theo từng checkpoint, kiểm SHA-256, đối chiếu ID trùng và bản dịch rỗng, rồi tạo `translations/merged-001-055.jsonl` gồm **5.500 ID**. Ngoài các tệp cũ còn có:
- `translations/cp006a-new-500.jsonl` — gói 0046–0050.
- `translations/cp006b-new-500.jsonl` — gói 0051–0055.
- `translations/cp006b-500.jsonl.bz2.b64` — bản nén CP006b trong GitHub.

Bảng JSONL giữ cặp `id` + `vi`; ghép qua `id` vào `01_CAN_DICH.jsonl` của bộ gốc. **Không thay `source`, `raw_hex`, `controls_hex`, `length_bindings`, `references` hoặc `alias_ids`.**

## Quy luật và giới hạn QA

Giữ tên riêng, Life, item, skill, thuật ngữ chính bằng tiếng Anh. Tiếng Việt có dấu, tự nhiên, hài đúng phong cách nhân vật. Giữ riêng biến thể `EN_A` và `EN_B` theo ID (CP006b: 257 EN_A, 243 EN_B). Token `{CTRL:hex}` giữ 100% giá trị và thứ tự.

**QA tĩnh CP006b:** 500/500 ID nguồn hợp lệ, 0 ID trùng, 0 dịch rỗng, 0 token sai (3.506 token đã đối chiếu), 0 sai tên item trong marker màu, Unicode NFC PASS; 6 cảnh báo số được đối chiếu riêng do chữ số/chữ viết và dấu phân cách. Độ dài kiểm sơ bộ không phát hiện dòng >1,7 lần nguồn đồng thời dài trên 140 ký tự hiển thị.

**Chưa QA:** ánh xạ chính xác người nói (`speaker=unknown`), ngôi xưng qua cảnh game, giới hạn khung theo font thật, ngắt trang, font tiếng Việt trên 3DS và patch RomFS/CIA. **Đây chưa phải bản chơi được.**

Xem `CHECKPOINT-006b.md`, `QA-006b.md`, `NGOI_XUNG_CP006b.md`.

**Tiếp theo:** `0056_hoi_thoai_va_huong_dan.txt`, mục thứ 5.501, tiếp mục tiêu 2.000 câu CP006 mà không tính câu chưa được dịch/QA.
