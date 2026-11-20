# Kid Icarus: Uprising — Checkpoint 061 (dịch mới và QA)

## 1. Nguồn kiểm chứng
- Đã mở chính ZIP bàn giao `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`, đọc `ban_dich/tieng_anh_can_dich.jsonl`: **4.067** source ID, **4.023** có nội dung.
- Đã xem `README.md`, `khao_sat/validation_report.json`, `khao_sat/summary.json`, `khao_sat/compatibility_comparison.json` và `khao_sat/patch_3DS_INSTALLATION.md` trong ZIP.
- Bộ ZIP là **dữ liệu khảo sát trích từ nhánh mod USA v172**; `validation_report.json` ghi PASS chỉ cho dữ liệu xuất/đọc offline, **không phải xác nhận patch Việt hóa chơi được**.
- Tác giả bộ tài liệu lưu ý: **CIA gốc còn mã hóa, 4.023 chuỗi không đại diện đầy đủ toàn bộ chữ trong game**. Đây là giới hạn quan trọng để không tuyên bố đã hoàn tất Việt hóa cả trò chơi.

## 2. Dịch mới đã commit
`translations/batch_061.jsonl` thêm đúng **1 ID**:
- `romfs/us/0.arc::resident/03.bin#00200`
- EN: ` ： Gear`
- VI: ` ： Trang bị`

Lưu nguyên **ký tự biểu tượng riêng `` và dấu hai chấm toàn chiều rộng**. Các mục liên quan trong `batch_003` đã dùng `GEAR → TRANG BỊ`; dòng #00200 bị bỏ sót tại chỗ. Đã fetch lại batch 061; một ID duy nhất và bản Việt đúng nội dung.

## 3. QA sửa trực tiếp hai mục
| ID | Câu gốc EN | Bản Việt trước | Bản Việt sau | Lý do |
|---|---|---|---|---|
| `resident/04.bin#00010` | Melee Dash Attack | Melee khi lướt | Đòn Melee khi lướt | Nhãn gốc là một **đòn đánh**, cần giữ nghĩa `Attack`; vẫn giữ thuật ngữ Melee. |
| `a0300.zrc#00053` | Where'd Lefty and Righty go? | Đầu Trái với Đầu Phải đâu rồi? | Lefty và Righty đâu rồi? | Lefty/Righty là biệt danh của hai đầu Hewdraw; quy ước tên riêng phải giữ tiếng Anh. |

File đã sửa: `translations/batch_016.jsonl`, `translations/batch_018.jsonl`. Đã đọc lại trên GitHub: 2/2 đúng ID, các file vẫn có lần lượt 66 và 94 ID duy nhất.

## 4. Kiểm kê dải giao diện
- So sánh nguồn `resident/03.bin#00000–00766` với các batch đầu, phát hiện các khoảng bỏ trống chủ yếu là ký hiệu, số, các tên chương đã nằm ở `batch_042`; **riêng `#00200` là nhãn có chữ cần dịch**.
- So sánh `#00943–01649` với batch 008–014: phần còn trống chủ yếu là rỗng, ký hiệu, dấu `???`, `Feather`, `Hearts`. Chưa tự điền vào các chuỗi giữ tiếng Anh.
- Dải `#00767–00942` là danh sách tên Weapon/Power, với token và tên skill cốt lõi theo quy ước giữ tiếng Anh.
- Dải `#01787–02105` chủ yếu tên Weapon, địch, Item và Power; `resident/04.bin#00110–00209` là nickname/tên mẫu. Từng trường hợp cần phân loại, không cộng vào tỷ lệ dịch.
- Đây là **kiểm kê theo dải nguồn + các batch kiểm tra**, chưa phải chạy audit toàn repository để bảo đảm không còn duplicate.

## 5. Tiến độ
- Checkpoint 060: mốc đã hiệu chỉnh tạm thời **3.266 / 4.023** ID duy nhất.
- Checkpoint 061: **+1 ID** → **3.267 / 4.023 ≈ 81,21%** bản nháp (vẫn chờ kiểm kê tự động toàn bộ).
- **2 sửa QA** không cộng số ID. Bản dịch vẫn ở `draft`.

## 6. Điều kiện còn thiếu để xuất bản vá
- Bộ bàn giao mới là tài liệu/trình trích xuất; chưa có trình **nhập bản Việt và đóng gói ngược** các file DARC/LZ11/MSBT, font có glyph tiếng Việt hoặc build patch.
- Chưa thử hiển thị, giới hạn chiều rộng, mã điều khiển sau thay thế, hoặc chạy trên phần cứng 3DS.
- Cần đối chiếu bổ sung phần RomFS chưa trích xuất từ CIA gốc nếu muốn tuyên bố Việt hóa toàn bộ game.
