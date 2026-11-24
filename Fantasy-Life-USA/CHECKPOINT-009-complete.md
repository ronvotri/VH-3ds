# Fantasy Life USA — CP009 hoàn tất (24/11/2026)

**CP009a 445 + CP009b 525 + CP009c 1.030 = 2.000 ID mới.** Tích lũy **12.500/34.812 ID (35,91%)**, còn 22.312; có 1 nhãn tiếng Tây Ban Nha cũ giữ nguyên chờ xác minh (12.499 ID thực sự khác chuỗi nguồn). 200 ID map/debug trong 0070–0071 vẫn HOLD.

## CP009c

1.030 tên Challenge được biên dịch thủ công từ gói 0137–0146 và 0147#1–32. Bản EN_A 784, EN_B 246. Chủ đề Blacksmith, Woodcutter, Tailor, Alchemist, Cook, Paladin/Mercenary, Carpenter, Wizard, Miner, Angler, Hunter. Giữ tên item, skill, monster/fish, địa danh, Life và Rank bằng English. Dịch ngắn, dí dỏm khi có câu chơi chữ, không thêm điều kiện.

**Không đếm:** 0140#90 `Philosopher's Stone` và 0145#40 `Levitanian Sardine` chỉ là tên vật phẩm/cá thuần tiếng Anh.

**Sửa lỗi cũ không đếm ID:** `FL-USA::F00008554@000014f8` từ `Blacksmith's Song: Behold, the Master Smith!` → `Khúc ca Blacksmith: Bậc thầy rèn lộ diện!`.

## Khôi phục

Chạy `python3 unpack_batches.py` tại `Fantasy-Life-USA`. Script tạo `translations/cp009c-new-1030.jsonl`, `translations/cp009-complete-2000.jsonl`, `translations/merged-CP009-12500.jsonl`.

- SHA-256 CP009c (1030): `c72f173c149a9e7ec8453829c81dc3081f08c0e3661e66dde675f0e6eec40fd8`.
- SHA-256 CP009 trọn (2000): `e61bfaa20fbb9c9fb58066052b814e9681ba426eba2b5c111376d730c0581477`.
- SHA-256 bản gộp (12500, sau sửa ID cũ): `bb8d3a23d01e5c1f2c4b89fbe2aec35529d62475a81acf638c9a18998ecad67b`.

**Tiếp theo:** gói 0147 mục 33 trở đi; không làm lại 32 mục đầu và hai tên English-only đang giữ nguyên.

**Giới hạn:** chưa có font/patch RomFS/CIA và chưa test trực tiếp trên 3DS.
