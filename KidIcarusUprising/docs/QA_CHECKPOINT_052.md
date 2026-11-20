# Kid Icarus: Uprising — QA Checkpoint 052

## Phạm vi
QA chọn mẫu Chương 19–20, đối chiếu đúng từng ID với `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`, giữ tên và thuật ngữ chính bằng tiếng Anh. Không thêm overlay ID mới.

## Ba câu đã sửa trực tiếp
| ID | English source | Việt trước QA | Việt sau QA | Lý do |
| --- | --- | --- | --- | --- |
| `a1900.zrc#00034` | My favorite act is the human cannonball. It's just such a...thrill ride! | Ta mê nhất tiết mục người đạn đại bác. Cảm giác mạnh cực kỳ! | Ta mê nhất màn bắn người khỏi đại bác. Cảm giác mạnh khỏi bàn! | Cụm `human cannonball` chỉ tiết mục bắn người ra khỏi đại bác; giữ giọng Viridi hào hứng. |
| `a2000.zrc#00006` | Gaaaaaaah! My skin feels like it's going to peel right off! | Áááá! Da tôi sắp bị lột sạch ra rồi! | Áááá! Da tôi có cảm giác sắp bong ra hết rồi! | Câu mô tả cảm giác do tốc độ, không có tác nhân lột da. |
| `a2000.zrc#00029` | You dummy! That place was a PRISON! And you freed the prisoner, the Chaos Kin! | Đồ ngốc! Chỗ đó là NHÀ TÙ! Cậu đã thả tù nhân Chaos Kin ra đấy! | Đồ ngốc! Nơi đó là NHÀ TÙ! Cậu đã thả Chaos Kin bị giam trong đó! | Nêu rõ Chaos Kin là sinh vật bị giam và được thả; câu Việt tự nhiên hơn. |

## Hậu kiểm
- Sửa trực tiếp `translations/batch_034.jsonl` và `batch_035.jsonl`, không phát sinh bản ghi mới.
- Đã fetch lại cả hai file trên GitHub: **3/3 câu đúng phiên bản sửa**.
- File vẫn có **84** và **35** ID duy nhất; không thay số ID và không đổi `status: draft`.
- Độ phủ kiểm kê giữ nguyên **3.235 / 4.023 (80,4%)**.

## Giới hạn
Chưa hoàn thành QA tất cả lượt thoại, xác định người nói từ metadata, rà kích thước font/byte hay kiểm thử trên 3DS. Không đánh dấu PASS toàn bộ chương hoặc bản vá.
