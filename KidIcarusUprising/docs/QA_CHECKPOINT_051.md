# Kid Icarus: Uprising — QA Checkpoint 051

## Phạm vi
Đối chiếu trực tiếp câu tiếng Anh trong ZIP bàn giao `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip` với bản Việt đã commit, tập trung Chương 18, 21 và 22, trong quá trình rà ngôi xưng Pit / Dark Pit / Palutena / Viridi. Đây là **QA chọn mẫu**, không phải QA toàn bộ lời thoại hay kiểm thử in-game.

## Bốn câu đã sửa

| ID nguồn | Tiếng Anh | Bản Việt mới | Lý do |
|---|---|---|---|
| `a1800.zrc#00023` | She's still fighting the Underworld Army, but she's mankind's enemy now too. | Cô ấy vẫn đánh quân Underworld, nhưng giờ còn là kẻ thù của loài người. | Diễn đạt chính xác `mankind's enemy`, không làm nhẹ thành `chống lại`. |
| `a2100.zrc#00019` | Aw yeah, it's a hot spri— | Ồ, suối nước nóng— | Khôi phục thông tin `hot spring`, giữ câu nói bị ngắt ngang. |
| `a2100.zrc#00021` | Hey, you've got your color back. | Này, sắc mặt cậu bình thường lại rồi kìa. | Đổi cách dịch cứng `có lại màu sắc` sang câu Việt tự nhiên. |
| `a2100.zrc#00022` | I also got water up my nose. | Mũi tôi cũng sặc nước luôn. | Giữ nghĩa nước vào mũi và chất hài của Pit. |

## Kiểm tra
- Đã đọc nguyên văn các ID liên quan từ ZIP nguồn; xác nhận không có mã điều khiển đặc biệt.
- Đã cập nhật **trực tiếp** `translations/batch_033.jsonl` (1 câu) và `translations/batch_036.jsonl` (3 câu), không tạo ID mới.
- Đã fetch lại hai file GitHub: **4/4 câu đúng bản sửa**. Hai file vẫn có lần lượt **62** và **59** ID duy nhất.
- Mốc độ phủ giữ nguyên **3.235 / 4.023 = 80,4%** theo kiểm kê trước; tất cả vẫn là bản nháp.

## Chưa hoàn thành
- Chưa gắn danh tính người nói cho toàn bộ thoại; khi không có speaker metadata, không suy diễn chắc chắn người nói chỉ từ cách xưng hô.
- Chưa kiểm tra font, giới hạn độ dài, hiển thị, bản vá hay test trên Nintendo 3DS.
- Chưa chạy kiểm toán tự động trên đầy đủ checkout và nguồn ZIP để xác nhận QA cấu trúc toàn dự án.
