# Fantasy Life (USA) — CP014j — Votri Valley

Rà hàng đợi 1.721 HOLD ngoài nhóm tên tạm giữ ở CP014i. 104 ID chuyển khỏi HOLD: 97 bản ghi dịch và 7 KEEP. 1.005 ID tên nguồn thêm vào hàng đợi xác minh, vẫn tính HOLD. 27 bản dịch thử riêng không nhập bản dịch chính.

## Phạm vi
- 54 nhãn ngoại hình đánh số: miệng, lông mày, tai; giữ nguyên từ Delivery chưa xác định nghĩa, chỉ dịch phần mô tả rõ. 18 nhãn Features và 18 nhãn name/lack vẫn chưa chốt.
- 26 nhãn sự kiện, 9 nhãn thống kê chế tạo, 8 nhãn mô tả giao diện/ngoại hình. Nhóm thống kê Alchemist đối chiếu cấu trúc hàng kề với các nghề chế tạo và nhãn khắc tên; chưa xác minh runtime.
- 6 nhãn tên nhân vật giữ nguyên và 1 nhãn dummy.
- 1.005 tên quái, item, skill và nhãn tên nguồn tạm giữ, không xác nhận tên Anh chính thức; 907 thuộc bảng 8710. Không cộng vào KEEP.
- 27 bản dịch thử: 18 nhãn Delivery Features, 9 nhãn ngoại hình tiếng Tây Ban Nha có tên riêng chưa xác minh. Không đưa vào vi chính thức.

## Tiến độ
20.833 bản ghi dịch; 8.548 KEEP; 5.431 HOLD (4.819 tên tạm giữ + 612 HOLD khác). Tổng đã có quyết định 29.381/34.812 (84,40%). Không phải tỷ lệ ROM Việt hóa.

## QA
Mở ZIP nguồn, tái lập ledger tới CP014i; các quyết định mới, tên tạm giữ và bản nháp không trùng nhau, đều khớp nguồn và thuộc HOLD trước đợt. Kiểm lại 7.168 bản ghi dịch cục bộ CP010c–CP014j, không phát hiện trùng ID, lỗi CTRL hoặc NFC. Kiểm tra ZIP đạt. Ba tệp GitHub đọc lại khớp. 13.665 bản ghi cũ chưa tái lập cục bộ; chưa thực thi toàn bộ unpack_batches.py, chưa test font, ROM hay runtime. Delivery và tên phiên âm chưa xác minh; các bản dịch nhãn thô cần kiểm tra ngữ cảnh thực tế.

## Khôi phục
- reviews/cp014j-resolutions.jsonl.bz2.b64 — SHA256 giải nén 3c07cc6503a5416475bd63305605086b97e6ceffde973be1c734990af6342eda.
- reviews/cp014j-preserve-pending.jsonl.bz2.b64 — 5903de8a5274596da2bf2dd989b2900a1ecd7e1563d272dd26a879788b547bc1.
- reviews/cp014j-drafts.jsonl.bz2.b64 — 919129f30b0db463c97adcc04d205214b1afa68da38c5ad7a30c0563a5465207.
unpack_batches.py bổ sung CP014j, dự kiến tạo merged-CP014j-20833.jsonl, remaining-HOLD-CP014j-5431.jsonl và remaining-active-HOLD-CP014j-612.jsonl. Không sửa main.

Tiếp CP014k: 612 HOLD ngoài nhóm tên; cần đối chiếu dữ liệu chính thức/metadata hoặc runtime để xác minh 4.819 tên còn lại. Ưu tiên khôi phục đầy đủ trước khi đóng gói.
