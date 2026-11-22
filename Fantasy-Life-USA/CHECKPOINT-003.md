# Checkpoint 003 — Fantasy Life USA 🇻🇳

**Ngày:** 23/11/2026  
**Kết quả:** 200 mục mới, từ gói 0004 và 0005; tổng 500 / 34.812 mục, còn 34.312.

## Đã xử lý

- 0004: 100 thông báo lưu/tải game, SD card, StreetPass, Ally Mode / Link Mode, Multiplayer, bảo mật, Nintendo eShop.
- 0005: 100 mục về Joyne Plaza, chuyển dữ liệu, DLC, và mô tả kiếm, dao găm, cung, đũa phép.
- Toàn bộ ID trùng khớp nguồn; không trùng các checkpoint trước; 100% chuỗi token `{CTRL:hex}` được giữ nguyên thứ tự và nội dung.
- Chuỗi Việt chuẩn NFC, có dấu, không rỗng; phân tách theo control gốc thay vì rải token tự động.

## Cách lấy dữ liệu

Chạy `python3 unpack_batches.py` từ thư mục `Fantasy-Life-USA`. Lệnh sẽ kiểm mã SHA-256 và giải nén đủ 500 mục trong `translations/merged-001-005.jsonl`.

**SHA-256 bản CP003 mới (200 mục sau giải nén):** `dcfd61bdd206f2ffc0beaecc9c8fa1ec6722a7baa121f3def6d333a3052dfd46`

## Ngữ cảnh cần kiểm

- `EN_A` dùng Ally Mode / `EN_B` dùng Link Mode; không tự gộp.
- `Donatella L.C.` và `Dee Elle C.` giữ theo biến thể nguồn.
- Save, Extra Data, StreetPass, Joyne Plaza là văn bản hệ thống; giữ giọng thẳng thắn. Trêu đùa nhẹ chỉ áp vào mô tả vũ khí có sẵn hài hước.
- Các token thay thế biến tên nhân vật, chỉ số block thẻ SD, nút bấm và prefix thông báo vẫn cần thử trên game.

**Chưa làm:** Không vá font, không đóng gói patch/ROM, không đo tràn chữ trên màn hình 3DS, chưa đối chiếu giọng nhân vật trong từng scene.
