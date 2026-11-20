# Kid Icarus: Uprising — Checkpoint 060: Song song QA + sửa kiểm kê ID

**Nhánh:** `vh/kid-icarus-uprising`
**Nguồn đối chiếu:** ZIP bàn giao `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`, file `ban_dich/tieng_anh_can_dich.jsonl` (4.067 dòng; 4.023 không trống).

## A. Phát hiện và loại bản ghi trùng

| ID | Vấn đề | Cách sửa |
| --- | --- | --- |
| `resident/03.bin#01655` — `Large Arena` | Có từ `batch_015.jsonl` với `Đấu trường lớn`, nhưng CP059 thêm lại ở `batch_059.jsonl` | **Xóa toàn bộ `batch_059.jsonl`** vì chỉ chứa 1 ID trùng; bản dịch đúng vẫn ở batch 015. |
| `resident/03.bin#01656` — `Music` | Có từ `batch_015.jsonl` với `Nhạc`, nhưng CP046 thêm lại ở `batch_046.jsonl` | **Xóa dòng #01656 khỏi `batch_046.jsonl`**; giữ dòng #00085 `TOUCH!` → `CHẠM!`. |

Các báo cáo `COVERAGE_AUDIT_046.md` và `CHECKPOINT_059_TRANSLATION_AND_QA.md` được hiệu chỉnh. Điều này cho thấy kiểm kê số dòng trước đây đã nhầm số ID duy nhất. Không công bố kiểm toán toàn bộ repo đã PASS vì chưa chạy script trên checkout đầy đủ.

## B. QA thoại gốc song song

Đọc nguồn và bản Việt Chương 4 (`a0400`, 65 câu) và Chương 5 (`a0500`, 67 câu), gồm **132 câu đã rà**; sửa trực tiếp hai dòng:

| ID | Tiếng Anh gốc | Trước QA | Sau QA |
| --- | --- | --- | --- |
| `a0400.zrc#00005` | Ugh, I'm getting worked up just thinking about it! | Chỉ nghĩ thôi mà em đã nổi da gà rồi! | Mới nghĩ đến thôi mà em đã muốn phát hoảng rồi! |
| `a0500.zrc#00056` | We're losing our grip here! | Chúng ta mất phương hướng rồi! | Chúng ta rối tung cả lên rồi! |

Lý do: `worked up` biểu đạt tâm trạng lo lắng/kích động, không nhất thiết là phản ứng nổi da gà; `losing our grip` ở đây diễn đạt mất khả năng kiểm soát tình hình, không chỉ lạc đường.

## C. Phân loại dịch mới
- Đã rà nguồn `resident/03.bin#01550–01690`, `#02050–02146` và `resident/04.bin` để tìm nhãn thực sự cần Việt hóa.
- Nhóm UI `resident/03.bin#01655–01670` đã có các bản dịch phù hợp trong batch 015 và 044/046 hoặc là các tên/thuật ngữ phải giữ. Không thêm mục dịch mới chắc chắn trong Checkpoint 060.
- Các mục vũ khí, vật phẩm, định danh chính thức và nickname giữ tiếng Anh theo yêu cầu; không tạo bản nháp lặp lại để tăng %.

## D. Kiểm tra và độ phủ hiệu chỉnh
- Đã fetch lại bốn batch: `015`, `019`, `020`, `046`; hai câu sửa đúng ID, bản dịch `Large Arena` và `TOUCH!` vẫn còn.
- Mốc **3.268/4.023** từng báo ở CP059 bao gồm ít nhất **2 lần cộng thừa**: `Music` và `Large Arena`.
- Theo đối soát các mốc lịch sử đã xác định: **3.266/4.023 ≈ 81,18%** ID bản nháp (mốc *hiệu chỉnh tạm thời*, chưa thay thế kết quả chạy kiểm kê toàn repo).
- **+0 ID dịch mới hợp lệ; 132 câu rà; 2 câu sửa QA; 2 bản ghi trùng bị loại**.
- Chưa QA toàn bộ glyph/font, giới hạn byte, chạy patch hay thử trên máy Nintendo 3DS.
