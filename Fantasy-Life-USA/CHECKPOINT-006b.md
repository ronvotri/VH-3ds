# Fantasy Life (USA) — Checkpoint 006b 🇻🇳

**23/11/2026 · CP006 đang thực hiện, phần b**

- 500 mục dịch mới từ gói **0051–0055**, 100 mục mỗi gói.
- Tổng tích lũy **5.500 / 34.812 (15,80%)**, còn 29.312.
- Riêng CP006 đã có **1.000 / 2.000** (CP006a 500 + CP006b 500). Mốc kế tiếp: **gói 0056, mục thứ 5.501**.
- Giữ thay đổi trên `vh/fantasy-life-usa`, không đụng `main`.

## Nội dung và phong cách

Chủ đề 0051: Mercenary mê thịt rồng, carp kỳ lạ, Snoot's Emporium và Woodcutter. 0052: Alchemist/Tailor/Blacksmith, Calumnus, người đưa thư. 0053: Zerk, Khubz mê cầu vồng, ông đầu bếp sợ hội bạn của vợ. 0054: nhà chính trị nhận vơ chiến công cho Dark Sultan, chú chó Chai, người yêu vượt sa mạc, Hội Calumnus. 0055: nhà phiêu lưu nhát gan, thương nhân đồ lạ, NPC cây nói ngọng, Paul mê pancake và Henrietta.

Quy tắc: giữ tên nhân vật, item, skill, địa danh, Life và các từ chính bằng tiếng Anh; Việt hóa câu thoại hài đúng nhân vật. Giữ riêng EN_A / EN_B, không tự gộp. Nguồn nhiều chỗ `speaker=unknown`, xưng hô mới là quy tắc tạm.

## Tài sản trong repository

- `translations/cp006b-500.jsonl.bz2.b64` — dữ liệu mới nén bzip2, biểu diễn base64.
- `python3 unpack_batches.py` — kiểm SHA-256 trước khi tạo `translations/cp006b-new-500.jsonl` và `translations/merged-001-055.jsonl`.
- SHA-256 của 500 câu CP006b sau giải nén: `f967eeba1206e1c65e64ae4e45830d3e948a00d16f27627ed418d62bdae467e3`.

**Chưa thể chơi trên 3DS:** chưa vá glyph/font, chưa đo khung chữ hoặc xuất patch. Không dùng QA tĩnh làm tuyên bố QA runtime.
