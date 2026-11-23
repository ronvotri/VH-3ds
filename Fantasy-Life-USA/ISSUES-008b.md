# Fantasy Life CP008b — các tồn đọng

1. **Chưa có font tiếng Việt chạy trên 3DS** hoặc bản vá RomFS/CIA.
2. **Độ rộng và vị trí các Ctrl ngắt trang:** dữ liệu mã điều khiển được giữ đúng thứ tự, nhưng vị trí ngắt trong câu tiếng Việt được phân phối tương đối ở ranh giới từ. Có thể tràn khung hoặc ngắt không tự nhiên; cần kiểm thử theo font/glyph thật.
3. **Ngôi xưng theo cảnh:** nguồn có `speaker=unknown` ở nhiều câu; sổ xưng hô dựa vào cụm thoại, chưa QA runtime.
4. **Số lượng và item:** 37 cảnh báo kiểm số thô, chủ yếu do dấu phân nghìn và Ctrl xen giữa số; một thiếu đơn vị `1 nhúm` đã sửa trước commit.
5. **EN_A/EN_B:** giữ riêng `Super/Superior`, `Good Quality/Good-Quality`, `Carrottys/Carrotys`, v.v. Cần kiểm phiên bản nào đang hoạt động.
6. **200 chuỗi nguồn map/debug 0070–0071** vẫn ở HOLD; tuyệt đối không gộp vào patch chưa xác minh.
7. **Tiếp tục từ 0109 mục 7**, vì 0109#1–6 thuộc CP008b. Các gói sau có quest dài, cần dịch theo cụm nhân vật.
8. **QA ngữ nghĩa độc lập:** bản dịch đã được đọc, sửa và qua QA cấu trúc nhưng chưa được tester khác kiểm toàn bộ trong game.

**Trạng thái:** CP008 hoàn thành ở cấp dữ liệu nguồn; chưa có patch chạy được.
