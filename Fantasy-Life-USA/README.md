# Fantasy Life (USA) — CP014e — Votri Valley

1.129 ID chuyển khỏi HOLD: 49 bản dịch và 1.080 quyết định giữ nguyên.

- 30 bản ghi tiêu đề sự kiện/mô tả (5423), 11 nhãn giao diện và mô tả (8690), 8 nhãn phân loại sinh vật (6952). Giữ tên riêng và item. Các nhãn sự kiện và mô tả có thể là dữ liệu nội bộ; chưa xác minh màn hình hiển thị.
- 219 tên khớp với tên đã duyệt trong bảng EN gốc (6796/6800/5990/5994/6008/6012) sau khi chuẩn hóa chữ hoa/thường và khoảng trắng. Giữ nguyên chuỗi nguồn, không coi trùng chữ là bằng chứng cùng thực thể. CSV đối chứng đi kèm ZIP.
- 854 nhãn bắt đầu bằng dấu # trong bảng 8690 (757) và 5728 (97) được giữ nguyên để bảo toàn dữ liệu. Không khẳng định nhãn # luôn là unused.
- 7 tên phân loại sinh vật giữ tiếng Anh (Golem, Mandrake, Slime, Goblin, Wisp, Gargoyle, Minotaur).
- 9 bản ghi dự thảo khó xác định nghĩa hoặc thao tác thực tế được loại khỏi bản dịch mới và tiếp tục HOLD.

## Tiến độ
20.393 bản ghi dịch, 8.260 KEEP, 6.159 HOLD; 28.653/34.812 đã có quyết định theo ledger. Không phải tỷ lệ ROM Việt hóa.

## QA
Mở lại ZIP nguồn, tái lập ledger CP013e–CP014d; 1.129 ID duy nhất thuộc 7.288 HOLD còn lại, source khớp. 49 bản dịch khác nguồn, NFC, bảo toàn token CTRL, số, dấu +, ký hiệu số và xuống dòng theo phép kiểm cục bộ. Tệp GitHub đọc lại khớp. Chưa chạy toàn bộ unpack_batches.py, chưa kiểm font/runtime. Không tự ghép hàng giữa các bảng tên phiên âm hoặc đổi tên tiếng Tây Ban Nha dựa vào suy đoán.

## Khôi phục
reviews/cp014e-resolutions.jsonl.bz2.b64 — SHA256 giải nén b3925a80d6bb0e7e9966ba6fc08dc10f4594cdc8118a5a6e596eed64583c266c.
unpack_batches.py đã bổ sung kiểm tra chuyển trạng thái và dự kiến xuất merged-CP014e-20393.jsonl, remaining-HOLD-CP014e-6159.jsonl. Không sửa main.

Tiếp CP014f: đối chiếu các nhóm tên còn lại và nhãn giao diện khó hiểu, giữ nguyên dữ liệu khi không có bằng chứng đủ chắc chắn; ưu tiên kiểm khôi phục toàn bộ trước khi bàn giao.

Mốc trước: [CP014d](CHECKPOINT-014d.md). [Quy tắc ngôi xưng](NGOI_XUNG.md).
