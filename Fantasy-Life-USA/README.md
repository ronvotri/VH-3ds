# Fantasy Life (USA) — CP013e — Votri Valley

**26/11/2026 · 19.240/34.812 ID đã xử lý bản dịch (55,27%)**; còn 15.572 ID chưa có bản dịch. CP013a–e = 285 + 208 + 118 + 96 + 33 = 740 mục mới.

## Dịch mới

| Nhóm | ID |
|---|---:|
| Tùy chỉnh ngoại hình | 22 |
| Nhãn hướng dẫn | 7 |
| Nhãn nhà/tiêu đề | 4 |
| Tổng | 33 |

Nguồn 01_CAN_DICH.jsonl, gói 0252, 0265, 0301–0304, 0311–0312. Giữ nguyên tên nhân vật Leo, Olivia, Laura, Celestia; thống nhất Tension gauge với thanh tích lực. Nhãn ngoại hình từ nguồn Anh dịch thô chưa đối chiếu ảnh/gameplay; cần kiểm tra trước patch.

## Rà tên riêng, không tính vào số dịch

Gói 0190–0216, archive entry 6796/6800, bảng cột 0, EN_A/EN_B: 2.696 ID được phân loại. 2.599 KEEP_SOURCE_NAME (2.147 EN_A, 452 EN_B), 97 HOLD_PLACEHOLDER (96 EN_A, 1 EN_B). Tên định danh item, quái, trang bị giữ nguyên source, kể cả tên phong cách ngôn ngữ khác vốn có trong bảng. Không xác nhận từng tên bằng gameplay. Placeholder (Unknown, Unobtainable, v.v.) chưa duyệt dùng. Không ghi các mục này vào JSONL vi. Bảng danh mục riêng không tự động tạo patch.

Nếu không trùng các batch trước, tổng dịch + KEEP = 21.839/34.812 (62,73%), 12.973 chưa chốt (gồm 97 HOLD). Đây là mốc phân loại dự kiến, không phải tỷ lệ Việt hóa.

## QA và khôi phục

33 ID duy nhất, có nguồn, khác source, NFC, không rỗng, 0 token mới; chữ số, dấu +, printf và xuống dòng đối chiếu. 2.696 quyết định khớp nguồn và metadata. Kiểm trùng với CP010c–CP013d cục bộ; các batch cũ hơn đối chiếu theo phạm vi checkpoint. Chưa chạy đầy đủ công cụ phục hồi toàn bộ batch trong môi trường hiện tại. Script dừng nếu phát hiện trùng giữa bản dịch và danh sách tên giữ nguyên/HOLD. Đọc lại hai tệp GitHub khớp.
- Batch: translations/cp013e-33.jsonl.bz2.b64, SHA-256 giải nén 990af65270dd9c6f42945663424f7c26a0d302903e2a57dedb0998e15b7bf3ed.
- Phân loại: reviews/cp013e-name-decisions.jsonl.bz2.b64, SHA-256 giải nén 9e05b82e5e2e36bef71292630d574d6b03528b29783488eec9506ddb7dabbeae.
- Chạy python3 unpack_batches.py; dự kiến xuất merged-CP013e-19240.jsonl và danh sách quyết định tách riêng.

Chưa test font, UI, ngữ nghĩa theo hình ảnh hoặc ROM 3DS. Tiếp CP013f, duyệt bảng tên skill/Rank/thuật ngữ và bảng tên NPC, tránh cộng tên giữ nguyên vào số dịch.

Mốc trước: [CP013d](CHECKPOINT-013d.md). Xem [quy tắc ngôi xưng](NGOI_XUNG.md).
