# Fantasy Life (USA) — CP014g — Votri Valley

138 ID chuyển khỏi HOLD: 49 bản ghi dịch và 89 quyết định giữ nguyên.

- 49 dịch mới: 19 nhãn sự kiện, 12 thống kê, 5 nhãn địa điểm, 4 phương tiện, 4 giao diện, 2 lựa chọn giọng nói, 1 thông báo tạo nhân vật, 1 tiêu đề Bliss và 1 phân loại. Giữ nguyên tên riêng theo nguồn; nhãn dịch thô cần xác minh ngữ cảnh thực tế.
- 81 tên được giữ nguyên sau đối chiếu bảng tên tương thích (tên NPC/quái với bảng NPC/quái, item với bảng item). Chỉ chấp nhận khác biệt chữ hoa/thường, dấu câu, khoảng trắng, hậu tố +. Không tự thay tên hoặc coi trùng chữ là chứng minh cùng một thực thể.
- 8 tên/tính năng giữ nguyên từ bảng tiếng Anh.

## Tiến độ
20.556 bản ghi dịch, 8.465 KEEP, 5.791 HOLD. Tổng đã có quyết định 29.021/34.812. Không phải tỷ lệ ROM đã Việt hóa.

## QA
Đọc lại ZIP nguồn và hướng dẫn bàn giao. Tái lập các ledger CP013e–CP014f, đối chiếu 138 quyết định mới với 5.929 HOLD và source gốc. Kiểm NFC, số, CTRL và xuống dòng trong batch mới. Tái lập 6.891 bản ghi dịch từ CP010c–CP014g cục bộ; không trùng ID với KEEP/HOLD, không phát hiện lỗi NFC hoặc CTRL. 13.665 bản ghi CP001–CP010b chưa được tái lập đầy đủ trong phiên này; chưa chạy toàn bộ unpack_batches.py, chưa test font/runtime. Không tự ghép các bảng tên khác ngôn ngữ.

## Khôi phục
reviews/cp014g-resolutions.jsonl.bz2.b64 — SHA256 giải nén e22d7463259713137bef34a747bdbbeff7118ad16c49c285b934aa3ab50b6552.
Đọc lại tệp GitHub khớp dữ liệu tải lên. unpack_batches.py đã bổ sung CP014g, dự kiến xuất merged-CP014g-20556.jsonl và remaining-HOLD-CP014g-5791.jsonl. Không sửa main.

Tiếp CP014h: ưu tiên kiểm toàn bộ bản gộp và rà 5.791 HOLD, đặc biệt các bảng tên và nhãn ngoại hình chưa có đối chiếu đáng tin cậy.

Mốc trước: [CP014f](CHECKPOINT-014f.md). [Quy tắc ngôi xưng](NGOI_XUNG.md).
