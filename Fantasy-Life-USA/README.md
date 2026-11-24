# Fantasy Life (USA) — Việt hóa Votri Valley · CP010b 🇻🇳

**Ngày 24/11/2026 · CP010 chưa hoàn thành**

- **Mốc cũ:** 13.022/34.812 ID (CP010a).
- **Đã dịch thật CP010b:** **+643 ID** thuộc 7 gói `0182–0188`; loại **57 ID HOLD** không được tính.
- **Tổng đã xử lý:** **13.665/34.812 ID (39.25%)**, còn **21,147** ID chưa duyệt hoặc HOLD.
- **Mục tiêu riêng CP010:** CP010a +522 và CP010b +643 = **1.165/2.000**, còn **835** mục để khép.
- **Nhánh GitHub:** `ronvotri/VH-3ds` → `vh/fantasy-life-usa` (không sửa `main`).

## Nội dung đã dịch

| Gói | ID mới đã duyệt | Chủ đề |
|---|---:|---|
| 0182 | 99 | Tạo avatar, chỉnh tóc/mặt, túi đồ, nhuộm màu và lựa chọn Có/Không |
| 0183 | 68 | Thông báo Bag, Dosh, Lunares Coins, Life/License, Skill và chỉ số |
| 0184 | 99 | Nhà cửa, đồ nội thất, Storage, truy cập thế giới và Multiplayer |
| 0185 | 91 | Di chuyển nhanh, địa danh, nhà Holiday Home, quản lý save và SD |
| 0186 | 97 | Game mới, lưu/xóa dữ liệu, học skill, nhận đồ, Bliss, StreetPass |
| 0187 | 93 | Danh bạ StreetPass, giao quà, Quest, Ally Mode và nhật ký thông báo |
| 0188 | 96 | Link Mode, nội dung bổ sung, gửi tin, biểu cảm, save/SD và StreetPass |
| **Tổng** | **643** | **510 EN_A / 133 EN_B** |

57 chuỗi chỉ chứa tên core English, slot hoặc URL được giữ nguyên trong `HOLD-NOT-COUNTED.csv`, không lấy việc chép lại tiếng Anh để nâng %.

## Quy tắc Việt hóa

- Giữ **Life, Skill, License, Bliss, Dosh, Lunares Coins, StreetPass, Multiplayer, Link Mode, Ally Mode, Bag, Storage, Pouch, Guild Office**, và tên riêng, item, skill chính theo chuẩn đã thống nhất.
- Câu hỏi, mô tả và chỉ dẫn chuyển sang tiếng Việt tự nhiên; riêng thông báo lỗi/lưu dữ liệu dùng giọng rõ, không chọc cười quá tay.
- Bảo toàn `{CTRL:...}` theo thứ tự source, kể cả mã xuống dòng, lựa chọn menu, vùng biến động và các chuỗi định dạng `%d`, `%02d`, `%2d`.
- Bảo toàn khoảng trắng đệm ở các nhãn có chủ đích để tránh dính chữ trong UI. Hai bản `EN_A` và `EN_B` giữ từng ID riêng, không ép dùng một thuật ngữ nếu nguồn khác nhau.
- Chưa sửa data ROM, `source`, `raw_hex`, `alias_ids`, `references`, `length_bindings`, `controls_hex`.

## File bàn giao và khôi phục

- `cp010b-new.jsonl`: 643 cặp ID/vi mới.
- `merged-CP010b.jsonl`: **13.665** cặp ID/vi, giữ nguyên bản gộp CP010a làm tiền tố.
- `review-CP010b.csv`: đối chiếu source–VI cho các mục mới, theo gói và số dòng.
- `HOLD-NOT-COUNTED.csv`: 57 mục chưa tính.
- `package-0182.jsonl` đến `package-0188.jsonl`: dịch tách theo gói.
- `cp010b-new.jsonl.bz2.b64`: gói nén commit GitHub, có SHA-256 xác minh.
- `QA-010b.json`, `QA-010b.md`, `ISSUES-010b.md`, `THUAT_NGU-010b.md`.

Nếu đã clone nhánh GitHub ở thư mục `Fantasy-Life-USA`, chạy `python3 unpack_batches.py` sau khi script được cập nhật để tạo `translations/cp010b-new-643.jsonl` và `translations/merged-CP010b-13665.jsonl`.

**SHA-256 mới:** `c8b3da74ec21fad3f48057f0e7ad652cbc8c37ad3673b1b0ce0e04b46f4ec400`  
**SHA-256 gộp:** `ec5b7ce6d0376ca0c91d94de4480e9a6605039a3734eaa23646fb04eb7b4c68b`

## Hạn chế cần chú ý

**QA hiện chỉ là QA tĩnh**: kiểm ID, placeholder, mã điều khiển, Unicode, tính nhất quán tên core. Chưa xác minh giới hạn pixel, lệnh format động trong gameplay, font tiếng Việt trên 3DS hoặc bản vá RomFS/CIA. Một số nhãn điều khiển có ngắt dòng theo bố cục nguồn, phải xem trên máy trước khi phát hành. 200 chuỗi `0070–0071` và các nhãn debug các gói trước tiếp tục HOLD.

**Tiếp theo:** một phần giao diện còn rõ nghĩa ở `0189#1–12` rồi tra cứu các gói thông báo khác, tránh chuỗi `0189#15+` dạng debug và các gói `0190+` chỉ tên item.