# Fantasy Life (USA) — CP014l — Votri Valley

451 ID chuyển khỏi HOLD: 447 tên vật phẩm chuẩn hóa sang EN_A và 4 bản dịch nhãn sự kiện tiếng Việt. 311 tên từ archive 8690, 136 tên từ archive 8710 đối chiếu với bảng EN_A archive 6796. Bảng đối chứng trong ZIP ghi từng ID nguồn/đích, archive, row và tên tiếng Anh. Không đổi các tên có hậu tố + chưa xác minh.

## Phương pháp
Đối chiếu từng cụm có nhiều mốc tương ứng, gồm quặng, gỗ, cá, nguyên liệu, món ăn, nội thất, vũ khí và công cụ Life. Chỉ dùng bản ghi tên EN_A có thật trong bộ nguồn. Loại những cặp quá mơ hồ hoặc thiếu đối chứng, không dùng một độ lệch cho toàn bảng. Đây là ánh xạ thủ công theo ngữ nghĩa và cấu trúc nhóm, chưa xác minh bằng khóa nhị phân hoặc runtime. 4 nhãn sự kiện dịch theo nội dung rõ, gồm hai nhãn thất bại chế tạo Oak Beam. Tên được khôi phục sang tiếng Anh không phải câu dịch tiếng Việt mới.

## Tiến độ
21.405 bản ghi thay thế, 8.550 KEEP, 4.857 HOLD (4.372 tên chờ xác minh + 485 HOLD khác); tổng đã có quyết định 29.955/34.812. Không phải tỷ lệ ROM Việt hóa.

## QA
451 ID duy nhất thuộc HOLD trước đợt; source khớp ZIP nguồn, khác bản thay thế, NFC, kiểm số, CTRL và xuống dòng; ZIP kiểm toàn vẹn đạt. File GitHub đọc lại khớp dữ liệu tải lên. Chưa tái lập toàn bộ 13.665 bản ghi cũ, chưa thực thi toàn bộ unpack_batches.py và chưa thử font/runtime 3DS. Tên chính thức cần kiểm thêm trong game.

## Khôi phục
reviews/cp014l-resolutions.jsonl.bz2.b64 — SHA256 giải nén a9add11979e1bb54795a1210517e8aaa21ef2bb94fcc824b8efbaf9da8290b7b.
unpack_batches.py đã bổ sung CP014l, dự kiến xuất merged-CP014l-21405.jsonl, remaining-HOLD-CP014l-4857.jsonl và hai danh sách con. Không sửa main.

Tiếp CP014m: rà tiếp cụm tên trang bị/nội thất và nguyên liệu còn lại, kiểm chứng các biến thể chất lượng cao; ưu tiên kiểm thử khôi phục toàn bộ.

Mốc trước: [CP014k](CHECKPOINT-014k.md). [Quy tắc ngôi xưng](NGOI_XUNG.md).
