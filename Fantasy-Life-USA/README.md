# Fantasy Life (USA) — CP013c — Votri Valley

**26/11/2026 · 19.111/34.812 ID đã xử lý (54,90%)**, còn 15.701. CP013a 285 + CP013b 208 + CP013c 118 = 611 ID mới trong CP013.

| Gói | ID mới | Nội dung |
|---|---:|---|
| 0152 | 12 | Nhãn loại trang bị/dụng cụ |
| 0299 | 76 | Danh mục vật phẩm/nguyên liệu |
| 0300–0304 | 18 | Nhãn tùy biến ngoại hình |
| 0322 | 12 | Nhãn vật thể tương tác từ tiếng Tây Ban Nha |
| Tổng | 118 | |

Đối chiếu nguồn ZIP 01_CAN_DICH.jsonl. 88 nhãn phân loại (tận dụng bản CP010a khi cùng nghĩa), 18 nhãn ngoại hình, 12 nhãn tương tác. Tên riêng/item/skill/Life/Rank tiếp tục giữ theo quy tắc. 31 ứng viên thiếu chắc chắn được tách HOLD, không tính. Nhiều tên còn lại là tiếng Tây Ban Nha hoặc tiếng Anh dịch thô; không tự đặt tên tiếng Anh chính thức.

QA tĩnh batch: 118 ID duy nhất, đều tồn tại nguồn, khác source, NFC, không rỗng; bảo toàn token/số/dấu +/%. Không trùng với các batch CP010c–CP013b đã khôi phục cục bộ; phạm vi các checkpoint cũ hơn được kiểm qua báo cáo. Chưa chạy khôi phục tổng toàn bộ batch trong môi trường hiện tại; script có kiểm trùng với toàn bộ dữ liệu khi chạy. Chưa xác minh nhãn ngoại hình, vị trí hiển thị, font và runtime 3DS. Các nhãn danh mục có thể thuộc bảng nội bộ, cần kiểm trước khi đóng patch.

Khôi phục: chạy `python3 unpack_batches.py`. Batch `translations/cp013c-118.jsonl.bz2.b64` có SHA-256 sau giải nén `caa176ee3ee0e6f178f545572dd834e3d8314b02e433c8c5f360cd674d280594`. Kết quả dự kiến `merged-CP013c-19111.jsonl`, giữ nguyên tiền tố CP013b.

Mốc tiếp: CP013d, phân loại tên cần giữ EN và nhãn thiếu ngữ cảnh; chỉ tính dịch thực sự, không cộng tên chép nguyên.

Mốc trước: [CP013b](CHECKPOINT-013b.md). Xem [quy tắc ngôi xưng](NGOI_XUNG.md).
