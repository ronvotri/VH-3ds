# Kid Icarus: Uprising — QA Checkpoint 054

## Phạm vi
QA chọn mẫu hội thoại Chương 13–14 bằng cách mở trực tiếp ZIP gốc `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip` và đối chiếu theo các ID `a1300` và `a1400`. Giữ tên nhân vật, địa điểm và thuật ngữ chính bằng tiếng Anh.

## Ba chỉnh sửa

| ID nguồn | Tiếng Anh gốc | Trước QA | Sau QA | Lý do |
| --- | --- | --- | --- | --- |
| `a1300.zrc#00017` | I wish they wouldn't. I get stage fright. | Ước gì đừng nhìn. Em sợ bị chú ý lắm. | Ước gì đừng nhìn. Em ngại bị soi lắm! | Giữ sắc thái hài của `stage fright` khi Pit thấy hai mặt trăng như đang nhìn mình. |
| `a1300.zrc#00038` | Before you cause a most unnatural harm, let us sit down for a chat. | Trước khi gây tổn hại trái tự nhiên, hay ta ngồi đàm đạo? | Trước khi gây thêm chuyện trái lẽ tự nhiên, hay ta ngồi xuống nói chuyện? | Diễn đạt mạch lạc, lịch sự theo giọng Arlon. |
| `a1400.zrc#00014` | So Thanatos was resurrected as...a glowworm? | Thanatos hồi sinh thành... con đom đóm phát sáng á? | Thanatos hồi sinh thành... con sâu phát sáng á? | `glowworm` không phải `firefly`; tránh đổi hình ảnh so sánh trong câu gốc. |

## Sau commit
- Sửa trực tiếp `translations/batch_028.jsonl` (2 mục) và `batch_029.jsonl` (1 mục), không tạo overlay ID mới.
- Fetch lại từ nhánh `vh/kid-icarus-uprising`: **3/3 mục có bản sửa**, tổng **76** và **86** ID duy nhất trong hai file.
- Không cộng tiến độ. Kiểm kê trước vẫn là **3.235 / 4.023 (80,4%)** ID xử lý bản nháp.

## Giới hạn
QA chọn mẫu, chưa kiểm tra đầy đủ mọi câu thoại hoặc người nói, giới hạn chiều rộng 3DS, font, mã điều khiển khi patch hoặc kiểm thử thực tế trên phần cứng.
