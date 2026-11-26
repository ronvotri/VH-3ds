# Fantasy Life (USA) — CP014k — Votri Valley

26/11/2026 — rà 612 HOLD ngoài nhóm tên tạm giữ. Chốt 123 ID: 13 bản dịch tiếng Việt, 104 tên trang bị chuẩn hóa sang EN_A, 4 tên địa danh chuẩn hóa theo nghĩa, 2 KEEP.

## Phát hiện quan trọng
Bảng tiếng Tây Ban Nha 8682 (cột 1) và bảng tên tiếng Anh 6796 (EN_A, cột 0) có đoạn trang bị tương ứng theo từng cụm, không cùng chỉ số hàng toàn bảng. Các độ lệch row ES - row EN là 648 (1336–1365), 647 (1366–1440), 646 (1441–1469), 645 (1471–1499). Kiểm tra ngữ nghĩa từng tên trong 104 mục HOLD, đối chiếu nhóm mũ/áo/găng/giày, các bộ Bandit, Danuta, Pumpkin, Dragon King, Sea Lord, Dark Sultan, Spirit King. Chọn EN_A theo biến thể nguồn và quy tắc giữ tên item tiếng Anh. Đây là ánh xạ có căn cứ mạnh từ chuỗi ngữ nghĩa và vị trí tương đối, chưa chứng minh bằng khóa nhị phân hoặc runtime. Tệp name-evidence-CP014k.csv trong ZIP bàn giao ghi ID nguồn, ID đích, số hàng và độ lệch từng mục.

4 nhãn địa danh Cave of bone/Underground lake trong 5854/8690 được chuẩn hóa theo nghĩa thành Cave of Bones/Subterranean Lake từ 5933; 2 nhãn Spirit tree giữ nguyên theo đối chiếu không phân biệt hoa thường. Không áp dụng ánh xạ hàng loạt lên các bảng tên NPC, quái hoặc item khác. 13 nhãn sự kiện/mô tả dịch tiếng Việt; các nhãn nguồn dịch thô cần kiểm cảnh.

## Tiến độ
20.954 bản ghi thay thế (gồm cả 108 tên chuẩn hóa EN_A trong CP014k), 8.550 KEEP, 5.308 HOLD = 4.819 tên tạm giữ + 489 HOLD khác. Tổng quyết định 29.504/34.812 (84,75%). Bản ghi thay thế 60,19%, không đồng nghĩa tỷ lệ câu tiếng Việt hay tỷ lệ ROM Việt hóa.

## QA
612 ID active HOLD từ CP014j đối chiếu khớp 01_CAN_DICH.jsonl. 123 ID duy nhất, 121 bản ghi thay thế khác nguồn, bảo toàn số, CTRL và xuống dòng, Unicode NFC; 489 ID active HOLD còn lại. ZIP kiểm tra toàn vẹn đạt. Chưa phục hồi toàn bộ 13.665 bản ghi CP001–CP010b, chưa chạy toàn bộ script, chưa kiểm font hoặc runtime. Không tuyên bố ánh xạ được xác nhận trong game.

## Khôi phục
reviews/cp014k-resolutions.jsonl.bz2.b64 — SHA256 giải nén 5ce73c6f33e0a8f9e3b75e26bc379ff943f44f0141fdae9ff66d3452a8f4bd8d. Đọc lại GitHub khớp. unpack_batches.py bổ sung CP014k, dự kiến tạo merged-CP014k-20954.jsonl, remaining-HOLD-CP014k-5308.jsonl và remaining-active-HOLD-CP014k-489.jsonl.

Tiếp CP014l: dùng mốc ngữ nghĩa theo cụm để rà các bảng nguyên liệu 8690/6796; không nội suy những đoạn lệch hoặc tên có biến thể chưa xác minh. Ưu tiên kiểm bản gộp đầy đủ. Không sửa main.
