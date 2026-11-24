# Fantasy Life USA — CP010b 🇻🇳

**Ngày 24/11/2026 · đã hoàn thành 643 mục UI mới từ 0182–0188; CP010 còn 835 mục.**

- Nguồn: 34.812 ID, trước CP010b đã có 13.022 ID.
- Tích lũy: **13.665/34.812 = 39,25%**, còn 21.147 ID.
- Nội dung: tạo avatar, nhuộm trang bị, Bag, Storage, Holiday Home, dịch chuyển, lưu game, SD, StreetPass, Link Mode, Ally Mode, quest và thông báo học skill.
- Giữ riêng 510 EN_A và 133 EN_B; 57 dòng giữ nguyên English (item/feature/URL...) vào HOLD, không đếm là đã dịch.
- QA cấu trúc: 643 ID mới hợp lệ, không trùng, 223 mã CTRL đúng nguyên văn/thứ tự, biến printf `%d`, `%02d`, `%2d` được giữ nguyên; bản gộp không mất mã điều khiển.

Khôi phục từ GitHub: `python3 unpack_batches.py` trong `Fantasy-Life-USA`, sinh `translations/cp010b-new-643.jsonl` và `translations/merged-CP010b-13665.jsonl`.

**SHA-256 CP010b**: `c8b3da74ec21fad3f48057f0e7ad652cbc8c37ad3673b1b0ce0e04b46f4ec400`

**SHA-256 gộp**: `ec5b7ce6d0376ca0c91d94de4480e9a6605039a3734eaa23646fb04eb7b4c68b`

**Chưa có patch RomFS/CIA, chưa thử font, độ rộng pixel, phần chia trang và các biến hiển thị trong game 3DS.** 200 ID map/debug 0070–0071 và nhãn Event thiếu nghĩa còn HOLD. Đề xuất tiếp 0189#1–12 và các nhóm thông báo rõ nghĩa khác; không tính tên item hoặc tên NPC chép nguyên tiếng Anh.