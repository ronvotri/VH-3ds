# Kid Icarus: Uprising — QA Checkpoint 050

## Phạm vi

Rà các bản dịch thoại Chương 18–22 (batch 033–037), đối chiếu các câu đã sửa với tiếng Anh gốc từ ZIP bàn giao `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip` theo ID nguồn. Ưu tiên ngôi xưng Pit / Palutena / Viridi / Dark Pit và câu có sắc thái sai hoặc gượng. Đây là **QA chọn mẫu**, không phải xác nhận toàn bộ 5 chương đạt PASS.

## Ba chỗ đã sửa trực tiếp

| ID nguồn | Anh gốc | Trước | Sau | Lý do |
|---|---|---|---|---|
| `a1900.zrc#00001` | Then let's get to rescuing Palutena! | Vậy đi cứu Palutena thôi! | Vậy đi cứu **ngài Palutena** thôi! | Giữ cách Pit kính trọng Palutena khi đang nói chuyện với Viridi. |
| `a1900.zrc#00004` | If they get in your way, I'll pull them out. | Nếu họ cản đường, ta sẽ rút họ đi. | Nếu họ cản đường cậu, ta sẽ **rút quân về**. | Ý là rút lực lượng chi viện, không phải kéo từng người đi. |
| `a2200.zrc#00004` | We both owe Pit. You know that. | Cả hai chúng ta đều mang ơn Pit. **Cậu** biết rõ điều đó. | Cả hai chúng ta đều mang ơn Pit. **Cô** biết rõ mà. | Lời thoại giữa hai nữ thần Palutena và Viridi; tránh xưng hô như đang nói với Dark Pit. |

## Các cặp xưng hô đã rà chọn mẫu

- **Pit → Palutena**: xưng `em`, gọi `ngài` hoặc `Lady Palutena`.
- **Pit ↔ Viridi**: Pit xưng `tôi`, gọi Viridi là `cô`; Viridi xưng `ta`, gọi Pit là `cậu`.
- **Dark Pit ↔ Viridi**: Dark Pit xưng `tôi`, không dùng `em` như Pit khi nói với Palutena.
- **Palutena ↔ Viridi**: nói chuyện ngang hàng theo `ta` / `cô`, không dùng `cậu` khi trực tiếp gọi nhau.
- Những câu cố ý lặp trong ZIP có ID độc lập vẫn được giữ nguyên; không tự xóa.

## Xác nhận sau commit

Đã fetch lại `batch_034.jsonl` và `batch_037.jsonl` từ nhánh `vh/kid-icarus-uprising`:
- Cả **3/3 chỉnh sửa** đều xuất hiện đúng ID.
- Hai file giữ nguyên **84** và **41** bản ghi, ID không trùng trong từng file.
- Không thêm ID mới: mốc kiểm kê vẫn **3.235 / 4.023**, tương đương **80,4% độ phủ bản nháp**.

## Còn cần thực hiện

1. Chạy `audit_translations.py` trên checkout đầy đủ với ZIP nguồn, phát hiện lệch ID / câu Anh / mã điều khiển.
2. Rà người nói toàn bộ thoại (đặc biệt các câu không chứa dấu hiệu xưng hô), sau đó QA nghĩa theo ngữ cảnh.
3. Kiểm tra font, chỗ ngắt dòng, độ dài và patch hiển thị trên máy Nintendo 3DS.

**Không đánh dấu QA toàn bộ là PASS hoặc bản vá đã chơi được.**
