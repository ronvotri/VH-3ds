# Kid Icarus: Uprising — Checkpoint 063: phân loại 760 ID còn thiếu, loại duplicate, dịch mới

## Dữ liệu và phạm vi
- ZIP gốc: `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`, `KidIcarusUprising-VietHoa/ban_dich/tieng_anh_can_dich.jsonl`.
- **4.067 ID gốc**; **4.023 có source không trống**; 44 blank.
- Đối chiếu bộ ID từ toàn bộ **49 batch hiện có trước lượt này** với source qua `resident/03.bin`, `resident/04.bin` và các tệp thoại. Phát hiện bốn ID `resident/03.bin#02143–#02146` xuất hiện cả ở batch 015 và 045; batch 045 không có ID mới.
- **Đã xóa `batch_045.jsonl`** do trùng toàn bộ 4/4 ID với `batch_015.jsonl`, không mất bản dịch hợp lệ.
- Số **ID duy nhất trước khi thêm mới: 3.263**, thay vì số bản ghi 3.267 đã công bố CP062.
- Phần chưa có overlay tại thời điểm bắt đầu: **760 ID** = 593 thuộc resident/03 và 167 thuộc resident/04; thoại không thiếu ID có văn bản.

## Dịch mới thực chất
Thêm `translations/batch_062.jsonl`:
- `resident/03.bin#02059`, EN `Petrified Palutena` → VI **`Palutena hóa đá`**.
- Đây là mô tả biến thể nhân vật, không phải tên vũ khí/vật phẩm.
- Đã fetch lại file từ GitHub, xác nhận đúng 1 ID/source/vi.

## Kết quả phân loại sơ bộ 760 ID
| Nhóm | Số ID | Hướng xử lý |
|---|---:|---|
| Tên Weapon/Power/Item/quái | 492 | Giữ tiếng Anh theo quy ước |
| Nickname/tên mẫu | 100 | Giữ nguyên |
| Ký hiệu, điều khiển, dấu câu, số, placeholder | 56 | Giữ nguyên |
| Tên item/thức ăn (resident/04) | 56 | Giữ nguyên theo quy ước giữ Item |
| Tên nhân vật/địa điểm/khái niệm riêng | 39 | Giữ nguyên |
| Thuật ngữ chính | 10 | Giữ nguyên |
| Tên CPU 1–6 | 6 | Giữ nguyên |
| Nhãn mô tả cần dịch: Petrified Palutena | 1 | **Đã dịch, batch_062** |
| **Tổng** | **760** | |

Phân nhóm trên được gắn theo **vị trí ID và nội dung nguồn**, mang tính **phân loại sơ bộ**. Chưa thể đồng nhất với nghiệm thu bản dịch từng tên trong ngữ cảnh gameplay. Danh mục đầy đủ được xuất thành JSONL với các trường `id`, `source`, `classification`, `action`, `reason` để rà từng mục nếu cần.

## Mốc mới, không còn dùng 81% làm tiến độ duy nhất
- **3.264 / 4.023 ID nguồn có overlay dịch**, sau khi loại 4 ID trùng và thêm 1 ID thật: **81,13%**.
- **759/4.023 ID không có overlay** đã nhận nhãn sơ bộ **giữ nguyên theo quy ước** (gồm các tên gốc, thuật ngữ, ký hiệu).
- **4.023 / 4.023 ID nguồn có nội dung đã có phương án xử lý sơ bộ**: có overlay hoặc chủ đích không dịch. Đây **không có nghĩa đã QA ngữ nghĩa 100%, cũng không có nghĩa game Việt hóa hoàn chỉnh**.
- **1.696/1.696 ID thoại có nội dung** có overlay bản nháp.

## Vấn đề tiếp theo
1. Rà thủ công các ID mang nhãn `giữ nguyên` nhưng có dạng mô tả ghép, nhất là UI và biến thể nhân vật, thay vì chỉ dựa vào ID range.
2. QA cú pháp control token và các dòng dài, chuẩn hóa ngôi xưng, thống nhất thuật ngữ.
3. Kiểm thử công cụ chèn ngược file MSBT/DARC/LZ11, glyph tiếng Việt và patch LayeredFS. ZIP bàn giao hiện có dữ liệu khảo sát nhưng **không xác nhận quy trình tạo patch hoạt động trên 3DS**.
4. Bổ sung phần text chưa trích xuất được từ CIA gốc nếu có.

**Chưa test bản vá trong game.** Không gắn trạng thái PASS cho từng câu ngoài các chỗ đã xác minh.
