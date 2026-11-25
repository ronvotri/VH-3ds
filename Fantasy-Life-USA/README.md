# Fantasy Life (USA) — CP012c — Votri Valley

**25/11/2026 · 18.084/34.812 ID đã xử lý (51,95%)**. Còn 16.728 ID. CP012a 560 + CP012b 497 + CP012c 527 = **1.584/2.000**, còn **416**.

## Phạm vi

| Nhóm | ID mới |
|---|---:|
| Danh xưng NPC/cốt truyện | 356 |
| Tiêu đề thử thách | 42 |
| Mô tả hiệu ứng | 31 |
| Nhãn thao tác và bản đồ | 45 |
| Nhãn điều khiển chiến đấu | 47 |
| Thông báo trùng nguồn | 6 |
| **Tổng** | **527** |

Dịch danh xưng NPC và các tiêu đề cốt truyện ở 0157–0163, 0167–0168, 0178; tiêu đề mô tả ở 0253; hiệu ứng 0337; nhãn bản đồ/thao tác 0306–0307; nhãn chiến đấu 0349–0350. Sáu thông báo khác dùng lại đúng bản dịch đã có theo nguồn trùng khớp. Các mục lặp cùng nguồn được dịch nhất quán theo danh xưng, mỗi ID có một bản ghi. Đây không phải 527 câu thoại độc nhất. Giữ tên riêng, tên item/skill/Life/Rank. Boy/Girl trong bảng danh xưng NPC dùng Cậu bé/Cô bé, khác với Nam/Nữ ở màn hình tạo nhân vật. Không giả định quan hệ người nói khi nguồn không xác định.

Một số nhãn 0306–0307 và 0349–0350 có thể là tài nguyên UI nội bộ hoặc nguồn Anh dịch thô; chưa xác nhận được chúng xuất hiện ở màn hình nào. Tên mô tả ở 0253 chưa xác minh loại tiêu đề chính xác bằng gameplay. Bỏ qua tên quái/item thuần tiếng Anh, mã debug và các nhãn không đủ ngữ cảnh; 1.083 ID chưa chọn trong các gói đã xem được thống kê riêng, không đồng nghĩa tất cả là lỗi.

## QA tĩnh

- 527 ID mới thuộc nguồn, không trùng, khác source, không rỗng, Unicode NFC. 18.084 ID tích lũy không trùng; 68.277 token đúng nội dung/thứ tự, 1 token mới. So chữ số, dấu + và biến printf trên batch mới đều đạt. 17.557 ID CP012b giữ nguyên byte.
- Chưa QA ngữ nghĩa độc lập, font, độ rộng pixel, ngắt trang hoặc chạy game 3DS. Không khẳng định tỷ lệ ROM đã Việt hóa thành công. Các nhóm 0070–0071 và nhãn Spanish cũ vẫn cần xác minh.

## Khôi phục

Chạy `python3 unpack_batches.py` trong thư mục `Fantasy-Life-USA` trên nhánh `vh/fantasy-life-usa`. File `translations/cp012c-527.jsonl.bz2.b64` khôi phục `cp012c-new-527.jsonl` và `merged-CP012c-18084.jsonl`. Ghép theo ID với `01_CAN_DICH.jsonl`, không sửa metadata.

- SHA-256 batch: `139ad3b4f736d894ff1f4e2a7eb45abb8568a9dc72395d6f9b106fcdc36d541c`
- SHA-256 gộp: `b414d20de2ae935e01bd0340d45f4ea2367e9e29aec982404fa54b9c59e495bb`
- SHA-256 CP012b: `a66a8703876165316420fa9dbdca987bd9fb386bd90692524498eb28a9a4d7f5`

Tiếp CP012d: còn 416 ID để đạt mục tiêu 2.000; ưu tiên nhãn có nghĩa rõ, tách tên riêng cần giữ nguyên khỏi chuỗi thật sự chưa dịch.