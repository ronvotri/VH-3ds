# Fantasy Life (USA) — CP013k — Votri Valley

26/11/2026 — 19.625/34.812 ID có bản ghi dịch (56,37%). CP013k: 18 bản dịch mới, 85 KEEP, 1.634 HOLD.

## Phạm vi
- 18 nhãn mới: nhóm 0152, 0181, 0306, 0308, 0313, 0339. Dịch nhãn trang phục, danh xưng, phân loại; giữ tên riêng và thuật ngữ chính. Nhãn dịch thô cần kiểm tra hiển thị trong game.
- 85 KEEP_SOURCE_NAME: 67 ID trong bảng Rank/Life/địa danh gói 0154 (archive 5914/5918/5923/5927/5933); 18 ID tên nhân vật, Life và chỉ số chính trong các gói khác.
- 1.634 HOLD: 1.619 tên quái phiên âm/dịch thô và 15 placeholder ở các gói 0232–0250. Phân loại theo metadata cột 0, không xác nhận tên chính thức, không tự thay bằng tên Anh khác. Chưa duyệt từng tên về nghĩa.

## Tiến độ dự kiến
19.625 bản ghi dịch + 5.301 KEEP = 24.926/34.812 (71,60%); 7.723 HOLD và 2.163 ID chưa phân loại. Không coi HOLD là hoàn thành. Tổng cần chốt 9.886 ID.

## QA
Các ID mới khớp ZIP nguồn, không trùng nhau hoặc dữ liệu CP010c–CP013j đã phục hồi cục bộ. Đối chiếu phạm vi checkpoint cũ hơn qua báo cáo, chưa chạy kiểm toàn bộ. 18 bản dịch khác nguồn, không rỗng, NFC; giữ token, số, biến và xuống dòng. Ba file CP013k đọc lại từ GitHub khớp. Chưa thử ROM, font hay runtime.

Đã bổ sung cả CP013j và CP013k vào unpack_batches.py, giữ nguyên tiền tố CP013i. Script kiểm SHA256, số lượng và trùng ID khi khôi phục; chưa thực thi toàn bộ script. Dự kiến tạo merged-CP013k-19625.jsonl.

Mốc tiếp CP013l: rà 2.163 ID còn ngoài ledger, rồi xác minh nhóm HOLD theo nguồn/metadata và runtime. Không sửa main.
