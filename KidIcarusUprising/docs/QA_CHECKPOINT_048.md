# Kid Icarus: Uprising — QA Checkpoint 048

## Kết quả

- **18/25 tên chương trong menu đã được chỉnh thống nhất** với nhãn danh sách chương ở `batch_042.jsonl`.
- Các mục chỉnh thuộc `resident/03.bin#01671–01695` trong `batch_015.jsonl`; **không phát sinh ID mới** và không tính thêm vào tiến độ.
- Đã đọc lại cả hai file trên GitHub sau commit và đối chiếu từng nhãn: **25/25 khớp**.
- Các thuật ngữ tên riêng `The Seafloor Palace`, `The Wish Seed`, `The Aurum Hive`, `The Aurum Brain`, `The Ring of Chaos`, `The Lightning Chariot`, `The Chaos Vortex` được thống nhất với danh mục chương.
- Kiểm tra lại các nhãn từ ZIP nguồn theo đúng ID `resident/03.bin#00720–00744` và `resident/03.bin#01671–01695` (những ID này là hai cách hiển thị tên chương).
- **Không thay đổi** các chuỗi ngoài 25 tên chương trong batch 015.

## Giới hạn

Đây là QA nhất quán tên chương, **không phải** QA nội dung tất cả đoạn hội thoại, kiểm tra font, ký tự hiển thị, patch/build hay chạy thử trên Nintendo 3DS. Số ID đã xử lý vẫn là **3.235 / 4.023 (80,4%)** theo kiểm toán 046.

## Đề xuất tiếp theo

1. Chạy `audit_translations.py` trên checkout đủ batch và ZIP nguồn, xử lý lỗi đối chiếu nguồn nếu có.
2. Rà `resident/03.bin` và `resident/04.bin` theo nhãn: **cần dịch / giữ nguyên thuật ngữ / ký hiệu / trống**.
3. QA ngôi xưng Pit/Palutena/Dark Pit/Viridi/Hades trong hội thoại, rồi kiểm tra giới hạn hiển thị và mã điều khiển trên 3DS.
