# Fantasy Life (USA) — CP014c — Votri Valley

## Kết quả
1.031 ID được chuyển trạng thái từ 8.660 HOLD ở CP014b.
- 40 nhãn UI, Happy, thao tác tích lực và hướng dẫn chế tạo (archive 8690).
- 22 nhãn phân loại sinh vật phổ thông trong bảng 6952, không phải tên riêng từng quái.
- 9 nhãn nhà ở, hướng dẫn và phương tiện trong các bảng 8062, 8072, 6687.
- 960 KEEP_FORMAT_LITERAL: 369 mô tả tài nguyên UI/icon (8702, 5887), 245 mô tả tài nguyên âm thanh (8509, 8518, 8527, 8536), 278 tham chiếu sự kiện/ô dự phòng, 68 nhãn ô chưa dùng rõ ràng. Chọn bảo toàn nguồn theo ngữ cảnh bảng, không khẳng định các chuỗi này không bao giờ xuất hiện trong game.

Giữ nguyên tên riêng, Life, Bag, Storage. Không suy đoán nghĩa của Delivery trong nhãn ngoại hình; các nhãn ấy vẫn HOLD. Các bản dịch từ nguồn Anh dịch thô phải kiểm tra hiển thị.

## Tiến độ theo ledger
20.299 bản ghi dịch (58,31%), 6.884 KEEP, 7.629 HOLD. Dịch + KEEP = 27.183/34.812 (78,08%). Đây là tỷ lệ xử lý dữ liệu, không phải tỷ lệ ROM Việt hóa thực tế.

## QA
Mở ZIP nguồn 01_CAN_DICH.jsonl, tái lập 9.730 HOLD lịch sử và trừ CP014a/b. Kiểm 1.031 ID duy nhất, đều thuộc 8.660 HOLD còn lại, source khớp. 71 chuỗi dịch khác nguồn, không rỗng, NFC, kiểm số/CTRL/printf/xuống dòng. Bản dịch dùng ngữ cảnh hàng kề cho nhãn thao tác X và quả cầu tích lực, cần QA gameplay. Tệp GitHub đọc lại khớp. Chưa chạy toàn bộ script khôi phục, chưa test font hoặc runtime 3DS.

## Khôi phục
reviews/cp014c-resolutions.jsonl.bz2.b64 — SHA256 giải nén ff85192518442c95498cdfe6becfdd7eb5a87b68c35f4dff70e4651b1c83f927.
unpack_batches.py đã bổ sung kiểm tra chuyển trạng thái, dự kiến xuất merged-CP014c-20299.jsonl và remaining-HOLD-CP014c-7629.jsonl. Lịch sử giữ nguyên, không sửa main.

Tiếp CP014d: xác minh các nhóm tên item, quái, địa danh phiên âm; đối chiếu dữ liệu cùng thực thể thay vì ghép theo thứ tự; ưu tiên text có khả năng hiển thị.