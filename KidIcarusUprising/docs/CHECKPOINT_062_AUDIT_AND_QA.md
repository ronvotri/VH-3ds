# Kid Icarus: Uprising — Checkpoint 062 (Kiểm kê GitHub + QA, phân loại phần còn thiếu)

## Nguồn và phạm vi

- Mở lại ZIP bàn giao `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`, đọc `ban_dich/tieng_anh_can_dich.jsonl`, **4.067 source ID**, **4.023 không trống**.
- Fetch trực tiếp nhánh `vh/kid-icarus-uprising` của `ronvotri/VH-3ds` để kiểm kê batch.
- Không tìm ra câu mới có thể chắc chắn dịch mà không phá quy tắc giữ tên Weapon, Power, Item, địa danh hoặc nhân vật; **Checkpoint 062 không tạo batch dịch mới**.

## Kiểm kê bản dịch

| Phạm vi tệp batch | Số tệp đọc | Số bản ghi | Trùng ID trong nhóm |
|---|---:|---:|---|
| `001–016` | 16 | 1.479 | 0 |
| `017–032` | 16 | 1.142 | 0 |
| `033–046`, không có `043` | 13 | 613 | 0 |
| `056, 057, 058, 061` | 4 | 33 | 0 |
| **Tổng** | **49** | **3.267** | **0 trong từng nhóm** |

Tổng **3.267 / 4.023 = 81,21%** overlay ID. Phạm vi nhóm 001–016 gồm resident/03, resident/04 và một ít thoại; các nhóm 017–041 là thoại; 042 và 044–046 là bổ sung ID menu/title; các nhóm 056–058,061 là vùng ID riêng đã được đối chiếu trước. **Chưa chạy máy kiểm toán Python trên full checkout**, nên chưa coi đây là PASS toàn bộ source/translation và mọi ngoại lệ ID xuyên nhóm.

Đã xóa các batch sai trước đây `043`, `059`; `batch_046` sau hiệu chỉnh chỉ còn một ID.

## Phân loại các ID không cần tạo bản dịch mới

Đối chiếu ZIP:
- `resident/03.bin#00037–00048`: sao đánh giá `☆`, `★`, ... → **giữ nguyên**.
- `#00064–00068`, `#00080`, `#00087–00103`, `#00149–00151`: ký hiệu nút, số, dấu câu, số La Mã → **giữ nguyên**.
- `#00720–00744`: tên 25 chương thực tế đã có overlay trong `batch_042`, không tạo trùng.
- `#01180–01182`: `Feather`, `Hearts`, `？？？` → giữ thuật ngữ/cấu trúc đặc biệt.
- `#01787–02105`: phần lớn tên Weapon, Power, Item, tên địch và đối tượng → **giữ chính danh tiếng Anh theo quy tắc**.
- `resident/04.bin#00026–00090`: tên món ăn, item, equipment → giữ tên item bằng tiếng Anh; `#00110–00209` nickname mẫu, không Việt hóa tên.
- Những chuỗi rỗng trong nguồn không tính vào 4.023.

Lưu ý: danh sách trên là các **nhóm đã xem**, không phải phân loại ID-by-ID hoàn chỉnh của toàn bộ 756 ID chưa có overlay.

## QA sửa trong batch_042

| ID | Original EN | Trước | Sau |
| --- | --- | --- | --- |
| `resident/03.bin#01703` | `At the Seafloor Palace (Ch. 7)` | `Tại The Seafloor Palace (Chương 7)` | `Tại Seafloor Palace (Chương 7)` |
| `resident/03.bin#01728` | `Credits` | `Danh sách thực hiện` | `Ê-kíp thực hiện` |

Giữ tên `Seafloor Palace` tiếng Anh, bỏ mạo từ `The` không phù hợp khi đứng sau `Tại`; dịch màn `Credits` gọn và tự nhiên. Đã fetch lại tệp: **2/2 câu đúng**, batch vẫn có 60 ID duy nhất.

## Chưa xác minh
- Chưa build ROM/LayeredFS hay thử patch 3DS; chưa kiểm tra glyph, độ dài byte, UI/tràn dòng, mã điều khiển ngoài các ca đã xem.
- Không có ID mới đủ cơ sở được tạo trong CP062; tiến độ giữ **3.267/4.023**.
- Bước kế tiếp nên phân loại **756 ID còn lại** thành `giữ nguyên tên` / `ký hiệu` / `cần dịch` / `cần xác minh` bằng manifest để đo đúng tiến độ hoàn thành nội dung, thay vì lấy 100% ID làm mục tiêu sai.
