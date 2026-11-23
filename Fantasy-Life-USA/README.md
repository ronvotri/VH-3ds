# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 006c-02 — 23/11/2026**

- Bộ nguồn bàn giao `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip` · Title ID `0004000000113200` · **34.812 ID**.
- **Đã dịch 5.900/34.812 (16,95%)**, còn **28.912**. Đây là mức bao phủ *bộ chuỗi bàn giao*, không khẳng định mọi chữ/ROM đã được Việt hóa.
- CP001–CP004: 2.500; CP005: 2.000; CP006a: 500; CP006b: 500; CP006c-01: 100; **CP006c-02: 300** (gói 0057–0059).
- Riêng CP006 đạt **1.400/2.000 câu**, còn 600 câu cho gói 0060–0065.
- Dữ liệu trên nhánh **`vh/fantasy-life-usa`**, không sửa `main`.

## Nội dung CP006c-02

**Gói 0057:** Galaxy Apples, Divine Powder, Golden Apples, Ancient Orbs, Hot-Spring/Hot Spring Water, Penguin Eggs, Cherrybells, Dogosaurus Rex và Goddess Frappé/Goddess's Frappé.

**Gói 0058:** Heavenly Asparagus, Life-Force/Lifeforce Clusters, Mythical Meat, Superior/Super Glorious Dinner, Ancient Flowers, Black-Crab/Black Crab Shells, Good-Quality/Good Quality Rainbow Lamp, Fossilfish và Kevin.

**Gói 0059:** Kevin, Goddess Carp/Goddess's Carp, Hermit's Drink, Calumnus, Golden Egg, Lord Damien/Lord Daemon, Yggdrasil Branch, Goldweeds, Remote Island Honey, Mushroom Medley, Timmy và nghệ sĩ Furlin/Fluffkin.

## Khôi phục toàn bộ 5.900 bản dịch

Trong `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Script giải nén tất cả các bản CP001–CP006c-02 bằng thư viện chuẩn Python, kiểm SHA-256 và ID trùng, tạo các file riêng từng checkpoint và **`translations/merged-001-059.jsonl`** gồm 5.900 cặp `{"id":"FL-USA::...","vi":"..."}`.

Dữ liệu mới trên repo: `translations/cp006c02-300.jsonl.bz2.b64`, sau giải nén là `translations/cp006c02-new-300.jsonl` (300 ID).

SHA-256 của 300 dòng mới: `8ba564ad0377ce51afd72deb42590abefd892d603b234c05a42de0899b905b04`.

Các bản dịch chỉ được ghép theo `id` vào `01_CAN_DICH.jsonl` của nguồn, không sửa các trường `source`, `raw_hex`, `controls_hex`, `alias_ids`, `references`, `length_bindings`.

## Chất lượng và giới hạn

- Dịch tự nhiên, vui đúng ngữ cảnh; giữ tiếng Anh tên riêng, địa danh, Life, item, skill, thuật ngữ chính.
- Phân biệt `EN_A` và `EN_B` đúng từng ID; không tự đổi tên vật phẩm hay biến thể.
- **QA cấu trúc:** 300/300 ID hợp lệ, không trùng 5.600 ID cũ, **2.334 token** `{CTRL:hex}` bảo toàn nguyên chuỗi và thứ tự, 0 rỗng, 0 sai Unicode NFC.
- Một cảnh báo về lượng `One` đổi thành `1` trong tên tô màu bị ngắt trang `Goddess Frappé` (gói 0057 câu 89) đã kiểm; không thay giá trị số lượng.
- Tên item/thuật ngữ trong marker giữ theo nguồn; không có bản dịch vượt ngưỡng chiều dài thô. **Kiểm giới hạn pixel/font là công việc riêng**, chưa được xác nhận.
- Nguồn nhiều `speaker=unknown`, sổ ngôi xưng chỉ là phác thảo theo cụm thoại, cần QA theo cảnh thật.
- **Chưa có bản patch RomFS/CIA hoặc font Việt chơi được trên 3DS**, chưa kiểm tràn chữ, phân trang/nhánh giới tính runtime.

Chi tiết: `CHECKPOINT-006c-02.md`, `QA-006c-02.md`, `NGOI_XUNG_CP006c-02.md` và `ISSUES-006c-02.md`.

**Tiếp theo:** gói `0060_hoi_thoai_va_huong_dan.txt`, bắt đầu **ID thứ 5.901**. Mục tiêu thêm 600 câu để khép CP006, tiếp tục chỉ đếm câu đã thật sự biên dịch và QA.
