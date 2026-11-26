# Fantasy Life (USA) — CP013i — Votri Valley

**26/11/2026 · 19.486/34.812 ID có bản ghi dịch (55,97%)**. CP013a–i thêm 986 ID.

## Đợt này: 1.266 ID

- 49 dịch mới: 41 tiêu đề nhạc (0259), 4 mô tả vật phẩm (0216), 2 nhãn hướng dẫn (0311), 1 nhãn nhiệm vụ (0250), 1 nhãn công thức (0338). Giữ nguyên tên riêng/thuật ngữ chính. Không dịch lời nhạc. Tiêu đề bài nhạc mang tên địa danh thuần túy được giữ nguyên. Một số nhãn hướng dẫn dịch thô chưa đối chiếu UI thực tế.
- 412 KEEP_SOURCE_NAME: tên trang bị, item, quái, tên skill, chỉ số, thuật ngữ cốt lõi, nhãn phiên bản và tên địa danh. Tên quái từ bảng dịch thô chỉ KEEP khi trùng nguyên văn với một tên đã duyệt trong bảng tiếng Anh; không xác nhận cùng một thực thể.
- 805 HOLD: 592 nhãn metadata tài nguyên UI ở archive 8702 (cột 1), 213 placeholder/unused/preliminary. Chưa xác minh chúng có xuất hiện trong runtime; không áp dụng vào patch và không coi là hoàn thành.

## Tiến độ theo ledger

19.486 dịch + 5.216 KEEP = 24.702/34.812 (70,96% dự kiến). 5.625 HOLD; 4.485 ID chưa nằm trong ba nhóm này. 10.110 ID chưa chốt gồm HOLD và phần chưa phân loại. Không phải phần trăm ROM đã Việt hóa.

## Kiểm tra và khôi phục

49 bản dịch NFC, khác nguồn, không rỗng; bảo toàn 2 token CTRL, số, xuống dòng và biến printf theo nguồn ZIP. 1.266 ID mới không trùng nhau, tồn tại trong nguồn, không trùng 5.772 bản ghi CP010c–CP013h và 9.624 ID ledger trước được đối chiếu cục bộ. Đã giải nén và đối chiếu thêm các batch CP001–CP010b từ GitHub (13.665 ID, và 1 bản sửa CP009c), không trùng ID mới. Ba tệp CP013i tải lên rồi đọc lại khớp. Chưa chạy toàn bộ script khôi phục sau cập nhật, chưa kiểm thử ROM/font/hiển thị trên 3DS; số tổng vẫn là tiến độ theo ledger, không chứng nhận mọi bản dịch cũ đúng ngữ nghĩa.

- translations/cp013i-49.jsonl.bz2.b64 — SHA256 giải nén 83e1ba5446ce675722f2367300f9ee90f432571be05b34436ec2711eb6bd826c
- reviews/cp013i-keep.jsonl.bz2.b64 — e31bf2318835a94cbffc8a9e4156190a3531141d86311801c26fc7804a963a25
- reviews/cp013i-hold.jsonl.bz2.b64 — 71ef5e9a6020a7cbc111cd56e8ea7a57f448c647004c9ad48b020ec8de1123de

Chạy python3 unpack_batches.py dự kiến xuất merged-CP013i-19486.jsonl và ledger riêng; kiểm SHA, số lượng, trùng ID. Không thay đổi main.

Tiếp CP013j: tiếp tục 4.485 ID chưa phân loại, kiểm chứng bảng metadata/tên còn lại, không tự đổi nhãn kỹ thuật và tên ngoại ngữ chưa có căn cứ.
