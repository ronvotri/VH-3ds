# Fantasy Life (USA) — CP013g — Votri Valley

**26/11/2026 · 19.409/34.812 ID đã xử lý bản dịch (55,75%)**, còn 15.403 ID không nằm trong bản dịch. CP013a–g thêm 909 ID.

## Đợt này: 1.749 ID xem xét

- 56 ID dịch mới (21 chuỗi nguồn độc nhất): danh xưng NPC, vật thể luyện tập, phương tiện, nhạc cụ, điểm tương tác. Archive 5990; gói 0156–0168. Secret Point xuất hiện nhiều ID và dịch nhất quán "Điểm bí mật"; chưa xác minh nơi hiển thị.
- 1.065 KEEP_SOURCE_NAME: 976 tên/thuật ngữ từ bảng EN 5990/5994/6008/6012, 89 tên ở bảng 5999 trùng chính xác tên trong bảng EN. Không thay đổi source hay ghi vào JSONL vi. Trùng tên không chứng minh tương đương nhân vật/row.
- 628 HOLD: 623 tên phiên âm hoặc nhãn dịch thô trong bảng 5999, 5 nhãn EN chưa rõ ngữ cảnh. Không tự ghép tên giữa bảng khác nhau, không coi bảng 5999 là tên Anh chính thức. Chưa xử lý bảng item tiếng Tây Ban Nha.

Cộng dồn KEEP CP013e–g = 4.683, HOLD trong ba ledger = 725. Tổng bản dịch + KEEP dự kiến = 24.092/34.812 (69,21%), còn 10.720 chưa chốt (bao gồm HOLD). Không phải % Việt hóa ROM.

## QA và khôi phục

56 ID hợp lệ trong nguồn ZIP, không trùng batch mới và ledger KEEP/HOLD mới, NFC, khác nguồn, không rỗng, 0 token mới; số, dấu +, printf, xuống dòng đối chiếu. Kiểm trùng với CP010c–CP013f khôi phục cục bộ và ledger CP013e–f; các batch cũ hơn chỉ đối chiếu phạm vi đã ghi trong báo cáo checkpoint. Chưa chạy toàn bộ bản gộp, chưa xác minh tên chính thức bằng gameplay, font hoặc vị trí hiển thị 3DS.

Ba tệp GitHub đọc lại khớp:
- translations/cp013g-56.jsonl.bz2.b64 — SHA256 giải nén fca32d6f4511c71fcb2cbd92812a0b084fbb67b15097867a9ffe598d4fd226b5.
- reviews/cp013g-keep.jsonl.bz2.b64 — SHA256 giải nén 2e97e4b0c57fd8120f9ffa622128924a83a5460a0a125876331afaec0ae08019.
- reviews/cp013g-hold.jsonl.bz2.b64 — SHA256 giải nén 285c841ae9ea1a28a389af5fcdadaf1885c3a065d0335639202465293bd870e1.

Chạy python3 unpack_batches.py dự kiến tạo merged-CP013g-19409.jsonl, kiểm SHA, trùng ID và xuất ledger riêng. Chưa chạy toàn bộ script sau sửa trong môi trường hiện tại. Không sửa main.

Tiếp CP013h: ưu tiên đối chiếu nhóm item khác ngôn ngữ theo metadata; phân biệt tên chính thức, nhãn nội bộ và text cần dịch. Không thay tên nếu không có đối chiếu đáng tin cậy.

Mốc trước: [CP013f](CHECKPOINT-013f.md). Xem [quy tắc ngôi xưng](NGOI_XUNG.md).
