# Fantasy Life (USA) — CP014m — Votri Valley

26/11/2026 — 256 ID chuyển khỏi HOLD: 254 tên chuẩn hóa tiếng Anh và 2 nhãn dịch tiếng Việt.

- 178 tên vật phẩm/món ăn: 127 nội thất và đồ trang trí từ bảng 8710, 48 tên món ăn từ 5728, 3 nguyên liệu từ 8690. Đối chiếu từng nhóm với bảng 6796 EN_A, bao gồm thảm, đồ lễ hội, trophy, món ăn. Không nội suy biến thể dấu +.
- 49 bản ghi tên NPC: 36 nhãn lặp của 4 tên trong 5999 và 13 nhãn tiếng Tây Ban Nha trong 8710, đối chiếu 5990 EN_A. Ánh xạ theo ngữ nghĩa/chính tả và chuỗi tên, không xác nhận bằng khóa thực thể; cần QA trong game.
- 27 nhãn địa danh từ 5854/8690 đối chiếu tên và mô tả bản đồ 5933 EN_A.
- 2 nhãn tiếng Việt về thống kê và giao diện.
- Loại 17 ứng viên chưa chắc nghĩa khỏi batch dự thảo; vẫn HOLD.

## Tiến độ
21.661 bản ghi thay thế; 8.550 KEEP; 4.601 HOLD (4.145 tên chờ xác minh + 456 HOLD khác). Tổng 30.211/34.812 ID đã có quyết định. Tỷ lệ này không phải tỷ lệ ROM Việt hóa hoặc số câu tiếng Việt.

## QA
Mở trực tiếp ZIP gốc, kiểm 256 ID duy nhất thuộc 4.857 HOLD ở CP014l, source khớp; kiểm NFC, số, CTRL, dấu + và xuống dòng; ZIP đạt kiểm toàn vẹn. Bảng name-evidence-CP014m.csv có ID và hàng đối chứng của từng tên. Tệp batch GitHub đọc lại khớp. Chưa chạy toàn bộ unpack_batches.py, chưa khôi phục đủ 13.665 bản ghi cũ, chưa kiểm font/runtime. Ánh xạ ngữ nghĩa/chính tả chưa chứng minh cùng thực thể bằng khóa nhị phân.

## Khôi phục
reviews/cp014m-resolutions.jsonl.bz2.b64 — SHA256 giải nén bbebe4a6400578d32a6033106f05c73df76141fc1ef1f4bda8caacd813023db9.
unpack_batches.py cập nhật CP014m, dự kiến xuất merged-CP014m-21661.jsonl, remaining-HOLD-CP014m-4601.jsonl và hai hàng đợi con. Không sửa main.

Tiếp: ưu tiên đối chiếu bảng tên quái theo ngữ cảnh có bằng chứng, tiếp tục các nhóm tên còn lại và kiểm bản gộp đầy đủ.
