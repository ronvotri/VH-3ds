# Fantasy Life (USA) — CP014h — Votri Valley

96 ID chuyển khỏi HOLD: 42 bản ghi dịch, 54 quyết định giữ nguyên.

- Việt hóa nhãn mô tả sự kiện, thống kê, bố trí nhân vật và nhà ở, giao diện công thức; giữ nguyên tên riêng và thuật ngữ chính.
- 38 tham chiếu nhóm quái có cấu trúc số lượng/tỷ lệ được giữ nguyên để bảo toàn định dạng dữ liệu. Các tên nguồn và nhãn kỹ thuật còn lại thuộc nhóm KEEP đã đối chiếu theo nội dung và ngữ cảnh bảng.
- Đối chiếu cho thấy bảng tên phiên âm và bảng tên chính thức không cùng thứ tự hàng; không tự động ghép tên theo số dòng.

## Tiến độ

20.598 bản ghi dịch, 8.519 KEEP, 5.695 HOLD; tổng đã có quyết định 29.117/34.812 (83,64%). Tỷ lệ bản ghi dịch 59,17%, không đồng nghĩa tỷ lệ hiển thị trong ROM.

## QA

96 ID chuyển trạng thái khớp nguồn, không trùng với các quyết định cũ. Kiểm tra cục bộ 6.933 bản ghi từ CP010c–CP014h: không phát hiện lỗi CTRL, NFC hoặc trùng ID. 13.665 bản ghi đầu chưa được tái lập cục bộ; chưa thực thi toàn bộ unpack_batches.py từ đầu và chưa thử runtime/font trên 3DS. Các nhãn sự kiện và bố trí có thể là metadata; không khẳng định chúng hiển thị trong gameplay.

## Khôi phục

reviews/cp014h-resolutions.jsonl.bz2.b64 — SHA256 dữ liệu giải nén 669f1fa8cbaee497001588fe0ca2c35dc2fbbf9401a339a082f61a6a33f4dfbc.
Đã đọc lại tệp GitHub khớp dữ liệu tải lên; công cụ khôi phục bổ sung CP014h, dự kiến tạo merged-CP014h-20598.jsonl và remaining-HOLD-CP014h-5695.jsonl.

Tiếp CP014i: ưu tiên đối chiếu các bảng tên chưa có ánh xạ đáng tin cậy và QA bản gộp. Không sửa main.
