# Fantasy Life (USA) — CP014f — Votri Valley

230 ID chuyển khỏi HOLD: 114 bản ghi dịch, 116 quyết định giữ nguyên.

- 78 nhãn sự kiện (5423); 14 nhãn thống kê (5786); 13 nhãn UI/ngoại hình (8690, 8702); 6 nhãn mô tả địa điểm; 3 nhãn bố trí nhà (8090).
- 68 mô tả AI/chọn mục tiêu (5445, 6677), 28 nhãn hiệu ứng dự phòng, 11 dummy, 9 nhãn map test/dự phòng: giữ nguyên nguồn để tránh sửa nhầm dữ liệu kỹ thuật. Chưa xác nhận các nhãn không xuất hiện trong game.
- Tên nhân vật phiên âm vẫn giữ theo từng nguồn, không tự đổi sang tên Anh suy đoán. Các nhãn Delivery chưa đủ căn cứ tiếp tục HOLD. Những nhãn sự kiện có thể là metadata, cần kiểm thử nơi hiển thị.

## Tiến độ
20.507 bản ghi dịch; 8.376 KEEP; 5.929 HOLD. Tổng đã có quyết định 28.883/34.812 ID (82,97%). Không phải tỷ lệ ROM Việt hóa.

## QA
Mở ZIP nguồn và khôi phục ledger CP013e–CP014e từ bản bàn giao, xác nhận 6.159 HOLD và 8.260 KEEP trước đợt. 230 ID duy nhất thuộc HOLD, source khớp; 114 bản dịch khác nguồn, NFC, bảo toàn CTRL, chữ số, dấu +, printf và xuống dòng theo kiểm tra cục bộ. File GitHub đọc lại khớp. Chưa chạy toàn bộ unpack_batches.py từ đầu, chưa test font, runtime hoặc ROM.

## Khôi phục
reviews/cp014f-resolutions.jsonl.bz2.b64 — SHA256 giải nén 203ffa86774b0acd96344caced97d2aee3c0efb98d4f76949b8febb18c80bf28.
unpack_batches.py đã bổ sung CP014f; dự kiến xuất merged-CP014f-20507.jsonl và remaining-HOLD-CP014f-5929.jsonl. Không sửa main.

Tiếp CP014g: kiểm chứng bản gộp và tập trung các bảng tên/nhãn còn HOLD dựa trên metadata và đối chiếu nguồn.

Mốc trước: [CP014e](CHECKPOINT-014e.md). [Quy tắc ngôi xưng](NGOI_XUNG.md).
