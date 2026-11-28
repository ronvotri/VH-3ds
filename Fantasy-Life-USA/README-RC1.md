# Fantasy Life USA — RC1 dữ liệu (2026-11-28)

**Chưa phải bản vá chơi được.** Bản này chốt dữ liệu văn bản, hợp nhất CP014o–CP015f, thêm bốn tên rìu đối chiếu thứ tự và tách các mục thiếu căn cứ để kiểm thử sau.

| Trạng thái | ID |
|---|---:|
| REPLACE | 25.553 |
| KEEP | 8.629 |
| DEFER_SOURCE_FALLBACK | 630 |
| Tổng | 34.812 |

98,19% là tỷ lệ quyết định nội dung, không phải tỷ lệ ROM Việt hóa. 630 ID (367 tên, 263 mục khác) chưa xác minh; giữ nguyên nguồn khi chèn bản dịch, không đổi chúng thành KEEP đã duyệt.

## Khôi phục

Tại thư mục này, chạy `python restore_rc1.py` (Python 3, thư viện chuẩn). Script chạy bộ giải nén CP014n hiện có rồi phát lại các delta theo thứ tự trong [rc1-manifest.json](rc1-manifest.json). Kết quả trong `rc1-output/` gồm bảng thay thế, KEEP ID, ngoại lệ và sổ ID đầy đủ. Không tự động sửa ROM. Các bước kiểm tra SHA và ID sẽ dừng nếu dữ liệu không khớp.

## QA

- Phát lại 18 checkpoint bằng dữ liệu CP014n tái lập tại môi trường cục bộ: 3.703 quyết định, 26 hiệu đính cũ, 4 tên bổ sung. Khớp các checkpoint thực tế, không trùng/mất ID trong sổ tái lập.
- 25.553 bản ghi thay thế không rỗng và đạt NFC.
- 7.184 bản ghi có nguồn đối chiếu qua kiểm tra mã điều khiển nhận diện được, 18.369 bản ghi chưa kiểm nguồn đầy đủ.
- Script khôi phục đã chạy thành công với fixture CP014n cục bộ; dữ liệu delta hỏng bị từ chối. Chưa chạy toàn bộ unpacker GitHub trong môi trường cục bộ.
- Thiếu dump nguồn gốc đầy đủ, khóa thực thể, font và công cụ chèn lại tài nguyên; chưa kiểm thử runtime. Cần cung cấp chúng trước khi làm bản vá thử nghiệm thực tế.

Lịch sử CP014n được giữ nguyên trong các checkpoint cũ; không thay đổi nhánh main.
