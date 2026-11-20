# Kid Icarus: Uprising — Checkpoint 064 — Xác minh ID và những phần còn thiếu

## Nguồn đã đọc trực tiếp

Nguồn: `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`, gồm `ban_dich/tieng_anh_can_dich.jsonl` và `ban_dich/messages_usa_patch.jsonl`.

- **4.067** bản ghi gốc tiếng Anh; **4.023** có `source` không rỗng.
- Bản xuất đa ngôn ngữ có **7.463** bản ghi: EN **4.067**, FR **1.698**, ES **1.698**. Không tính cả FR/ES vào việc cần dịch tiếng Anh.
- File danh mục CP063 có **760 mục**, **760 ID duy nhất**, tất cả ID tồn tại trong nguồn; **760/760 `source` khớp nguyên văn**, không có nguồn rỗng.
- Việc này xác minh danh mục nguồn, không chứng minh phần tiếng Việt đã QA xong hoặc có bản vá chạy được.

## Hai điều chỉnh phân loại

1. Bốn ID `resident/03.bin#00938–00941` với chuỗi ` Lv. 1`, ` Lv. 2`, ` Lv. 3`, ` Lv. 4` bị xếp vào nhóm Weapon/Power ở CP063. Chuyển sang nhóm **ký hiệu/hậu tố cấp độ**; không phải chuỗi cần dịch.
2. Hai ID `resident/03.bin#02061` (**Heart**) và `resident/03.bin#02072` (**Food**) được chuyển sang **cần xem ngữ cảnh**. Cần biết đây là tên Idol/đối tượng hay nhãn UI trước khi chốt giữ nguyên hoặc Việt hóa.

## Phân loại hiệu chỉnh 760 ID

| Nhóm | Số ID | Xử lý |
|---|---:|---|
| Tên Weapon, Power, Item, quái | 486 | Giữ tên |
| Nickname mẫu | 100 | Giữ nguyên |
| Ký hiệu, điều khiển, số, hậu tố level | 60 | Giữ nguyên |
| Tên Item/thức ăn (`resident/04`) | 56 | Giữ tên |
| Tên nhân vật/địa điểm | 39 | Giữ nguyên |
| Thuật ngữ chính | 10 | Giữ nguyên |
| CPU 1–6 | 6 | Giữ nguyên |
| Cần đối chiếu ngữ cảnh (Heart/Food) | 2 | Chưa chốt |
| Đã dịch Petrified Palutena (CP063) | 1 | Đã có `batch_062` |
| **Tổng** | **760** | |

## Các phần còn thiếu để gọi dự án DONE

- **QA tiếng Việt thực chất:** kiểm tra toàn bộ các bản nháp về nghĩa, ngôi xưng, thuật ngữ, câu dài, mã điều khiển và glyph tiếng Việt. Chưa có kiểm thử tiếng Việt trong game.
- **Kiểm tra phạm vi trích xuất:** chưa khẳng định bộ ZIP hiện tại chứa toàn bộ các văn bản cần Việt hóa của game từ CIA gốc. Báo cáo khảo sát cho biết CIA gốc còn mã hóa.
- **Pipeline patch:** chưa xác thực đường đi từ overlay JSONL → cập nhật đúng nội dung message/MSBT/LZ11/ARC → hỗ trợ font tiếng Việt → đóng gói LayeredFS → thử trên 3DS.
- **Hai mục Heart/Food** phải xem UI/Idol trong trò chơi hoặc hình ảnh nguồn trước khi quyết định.
- **Full-checkout audit:** kiểm kê lịch sử **3.264 / 4.023** ID có overlay sau khi loại trùng, nhưng cần chạy lệnh audit trên checkout chứa tất cả batch để xác nhận toàn cục, source/control code và các trường hợp lệch ID.

Không thêm ID dịch mới ở CP064 vì chưa thấy mục cần dịch mới có đủ căn cứ; không tự chép tên riêng vào overlay để tăng tỷ lệ. Danh mục CP064 đã được xuất thành file riêng, xác minh tất cả 760 ID với ZIP gốc.
