# Fantasy Life USA — Checkpoint 005a 🇻🇳

**23/11/2026 · Phần 1/CP005**

- Đã dịch **700 câu mới** trong 7 gói **0026–0032**, 100 mục/gói.
- Tích lũy **3.200 / 34.812 ID (9,19%)**; còn 31.612 ID.
- Đợt CP005 đặt mục tiêu 2.000 câu mới nhưng **chưa hoàn thành**, đang thiếu 1.300; lần tới bắt đầu **gói 0033**.
- EN_A và EN_B được giữ riêng theo ID, không sao chép nhầm Creator/God, Wizard/Magician, Ally/Link, v.v.

## Phạm vi biên dịch

- 0026–0027: tutorial các Life, Special Skill/Mystic Skill/Creator Skill, Map, Quest, lưu dữ liệu, online, Bounty.
- 0028: God Mode và vật phẩm/hiệu ứng EN_B với 25%, EXP, Dosh, điều kiện nam/nữ.
- 0029–0030: thư NPC và Master; giọng riêng Noelia, Cap'n Ahab, Divinus, King Erik; mô tả kỹ năng và lời thoại.
- 0031–0032: đối thoại đời thường, khu vực Castele; xử lý chênh lệch EN_A/EN_B thủ công.

## Khôi phục

- `translations/cp005a-700.jsonl.bz2.b64`: bản dịch mới nén bzip2/base64.
- Dùng `python3 unpack_batches.py` để xác minh SHA-256 rồi tạo `translations/merged-001-032.jsonl` chứa 3.200 mục.

**SHA-256 CP005a mới sau giải nén:** `834af3e6f435f7f5efd95af3e4b7381d535638ecc807765f6e307f5a2b9a26d3`.

**Chưa phải patch:** chưa vá font, không dựng CIA/RomFS, chưa kiểm ngắt trang thực tế, chưa ánh xạ chắc chắn speaker=unknown.
