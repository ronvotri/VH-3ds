# Kid Icarus: Uprising — QA Checkpoint 055

## Phạm vi
Rà toàn bộ 117 mục Chương 11–12 trong source ZIP `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip` (`a1100.zrc` có 57, `a1200.zrc` có 60), đối chiếu với các bản dịch hiện có `batch_026.jsonl` và `batch_027.jsonl`. Đợt này sửa ba lỗi rõ ràng, không coi 117 mục đều đạt QA ngữ nghĩa hay hiển thị.

| ID | Anh gốc | Việt trước QA | Việt sau QA | Lý do |
| --- | --- | --- | --- | --- |
| `a1100#00003` | The Underworld Army is here to gather souls. Clearly, they expect many casualties. | Quân Underworld tới thu thập linh hồn. Rõ là chúng chờ một cuộc đại thương vong. | Quân Underworld tới thu gom linh hồn. Rõ là chúng đoán sẽ có rất nhiều người chết. | Dịch cụ thể `expect many casualties`, tránh `đại thương vong` không tự nhiên. |
| `a1200#00017` | That bomb won't be resetting anything when I'm done with it! | Để tôi xử xong thì quả bom này khỏi Reset được thứ gì nữa! | Em xử xong thì quả bom này đừng hòng Reset được gì nữa! | Pit đang hội thoại với Palutena; thống nhất `em` và giữ `Reset`. |
| `a1200#00030` | Huh! It's like a shooting game. I can almost feel the controller in my hands! | Ồ! Cứ như game bắn súng ấy. Em gần như cảm thấy tay cầm trong tay luôn! | Ồ! Cứ như game bắn súng ấy! Em cứ ngỡ đang cầm tay điều khiển! | Giữ trò đùa phá bức tường thứ tư; sửa lặp từ `tay cầm trong tay`. |

## Kiểm tra sau commit
- Đã cập nhật trực tiếp `batch_026.jsonl` và `batch_027.jsonl` trên nhánh `vh/kid-icarus-uprising`.
- Đã fetch lại cả hai bản GitHub, xác nhận **3/3 thay đổi** đúng ID.
- Số bản ghi giữ nguyên **57** và **60**; không phát sinh ID trùng trong từng file.
- Độ phủ bản nháp giữ nguyên mốc đã kiểm kê **3.235 / 4.023 (80,4%)**.

## Chưa hoàn tất
Chưa kiểm thử font, độ dài, mã lệnh, công cụ vá ROM và chơi thực tế trên Nintendo 3DS. Không gắn nhãn PASS toàn bộ hội thoại hay bản vá.
