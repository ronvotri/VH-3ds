# Fantasy Life (USA) — CP014i — Votri Valley

Đợt rà soát theo bảng: 3.974 ID trong 5.695 HOLD trước đợt. Chỉ 160 ID thực sự chuyển khỏi HOLD: 138 bản dịch (112 chuỗi nguồn khác nhau) và 22 KEEP. 3.814 ID tách sang hàng đợi tên nguồn bảo toàn tạm thời, vẫn tính HOLD.

## Phạm vi
- 67 nhãn sự kiện (5423), 29 nhãn số/giao diện (8690), 7 nhãn nhà chứa máy bay, 6 nhãn nhà trọ, 29 mô tả khác (nhà ở, xưởng nghề, chuồng thú, giao diện, thống kê). Nguồn Anh dịch thô được dịch phần mô tả và giữ tên nguồn; chưa xác minh tên item/nhân vật tương ứng với tên Anh chính thức hoặc vị trí hiển thị.
- 22 KEEP: thuật ngữ NPC, nhãn Mini, tên/nhãn cấu trúc được giữ nguyên.
- 3.814 PRESERVE_PENDING_NAME_QA: 1.718 tên item trong 8690/5728, 1.482 tên quái trong bảng 6943–8050, 614 nhãn tên NPC lặp trong 5999. Không chép vào vi, không coi là đã xác minh tên Anh hoặc hoàn tất. Chỉ tách hàng đợi để tránh sửa nhầm dữ liệu. Không ánh xạ theo số hàng.
- 1.721 HOLD ngoài nhóm tên tạm giữ: 984 tên tiếng Tây Ban Nha, 228 nhãn ngoại hình mơ hồ, 206 nhãn sự kiện, 303 mục khác. Không tự chuyển tên tiếng Tây Ban Nha sang tiếng Anh khi chưa có ánh xạ đáng tin cậy.

## Tiến độ
20.736 bản ghi dịch; 8.541 KEEP; 5.535 HOLD (3.814 tên bảo toàn tạm + 1.721 HOLD khác). Tổng đã có quyết định 29.277/34.812 (84,10%). Số 3.814 không được cộng vào số hoàn thành. Đây là thống kê dữ liệu, không phải tỷ lệ ROM đã Việt hóa.

## QA
Tái lập ledger từ ZIP nguồn, CP013e–CP014h; 3.974 ID được rà và 1.721 ID khác tạo phân hoạch đúng 5.695 HOLD trước đợt, source khớp. Kiểm CTRL, số, NFC và xuống dòng cho 138 bản dịch. Tái lập 7.071 bản ghi dịch CP010c–CP014i cục bộ, không phát hiện trùng ID/CTRL/NFC. 13.665 bản ghi CP001–CP010b chưa phục hồi cục bộ đầy đủ; chưa chạy toàn bộ unpack_batches.py, chưa test ROM/font/runtime.

## Khôi phục
- reviews/cp014i-resolutions.jsonl.bz2.b64 — SHA256 giải nén 4ebbe67d5c592fcea677c5bdcb0e2d3679bd8a5b742824faa53f4ae62cee002b.
- reviews/cp014i-preserve-pending.jsonl.bz2.b64 — SHA256 giải nén 2991d987d00bd7836abc6c9ae971e0be0d0256d5e7055a9afc29e698df09dfb2.
Hai tệp GitHub đọc lại khớp; unpack_batches.py đã thêm bước kiểm tra và xuất merged-CP014i-20736.jsonl, remaining-HOLD-CP014i-5535.jsonl và remaining-active-HOLD-CP014i-1721.jsonl. Không sửa main.

Tiếp: rà theo bảng lớn, ưu tiên 737 nhãn ngoài nhóm tiếng Tây Ban Nha trong hàng đợi 1.721; cần tài liệu ánh xạ tên chính thức nếu muốn giải quyết 984 tên Tây Ban Nha và 3.814 tên bảo toàn tạm. 

Mốc trước: [CP014h](CHECKPOINT-014h.md). [Quy tắc ngôi xưng](NGOI_XUNG.md).
