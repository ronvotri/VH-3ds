# Fantasy Life (USA) — CP012a — Votri Valley

**25/11/2026 · 17.060/34.812 ID đã xử lý (49.01%)**. Còn 17.752. CP012a có 560 mục mới; CP012 còn 1.440 mục theo mục tiêu 2.000. Một nhãn Spanish cũ giữ nguyên chờ xác minh; không tính tên riêng không dịch là câu mới.

## Phạm vi
| Gói | Mục mới | Nội dung |
|---|---:|---|
| 0125, 0126, 0128, 0129 | 220 | Hiệu ứng, chỉ số, biểu cảm |
| 0130 | 100 | Biểu cảm, thông báo Level, Multiplayer, Friendship, Bounty |
| 0224–0226 | 124 | Điều kiện kích hoạt skill |
| 0256–0259 | 100 | Điều kiện skill, bàn chế tạo, Creator/God |
| 0231–0232, 0253, 0262 | 16 | Mô tả item, thông báo mật khẩu và khách ghé |
| Tổng | 560 | |

Dịch bằng bảng đối chiếu thủ công cho nhãn lặp, giữ nguyên hậu tố chỉ số, % và dấu cộng. Gói 0130 được viết từng câu, đặt lại token ở vị trí biến tương ứng. Giữ nguyên tên skill, Life, Rank, item và thuật ngữ core; không dịch chuỗi mật khẩu hoặc tên item thuần Anh. EN_A/EN_B giữ theo ID và giữ tên skill khác biệt. Không tạo thêm điều kiện ngoài source. Các nhãn `Creator Special Skill` và `God Special Skill` dịch phần quan hệ, không đổi tên Rank.

## QA tĩnh
- 560 ID mới hợp lệ, không trùng 16.500 ID cũ. Toàn bộ 17.060 ID đối chiếu nguồn, NFC, không rỗng, token khớp thứ tự và nội dung; 103 token mới, 68276 token tích lũy.
- Dấu + và số liệu của batch mới giữ nguyên; 10 cảnh báo số là chuyển third/three thành 3 (đính kèm number-audit.csv). Danh sách 947 mục chưa xử lý trong các gói đã xem không tính vào tiến độ (gồm tên riêng, nhãn kỹ thuật, thuật ngữ giữ nguyên và mục chưa đủ ngữ cảnh; không phải tất cả đều lỗi).
- Chưa kiểm runtime 3DS, glyph, pixel width, ngắt dòng hoặc vị trí hiển thị token động; không khẳng định bản ROM đã vá. 0070–0071 tiếp tục HOLD.

## Khôi phục
Chạy `python3 unpack_batches.py` trong thư mục `Fantasy-Life-USA` trên nhánh `vh/fantasy-life-usa`. Batch `translations/cp012a-560.jsonl.bz2.b64` xuất `cp012a-new-560.jsonl`, `merged-CP012a-17060.jsonl`. Ghép theo ID với `01_CAN_DICH.jsonl`; giữ nguyên metadata.
- SHA-256 batch: `a7073240b2a34cb5861eeb90e1dbf675452c16049e19cd0b185f98070a9bbda3`
- SHA-256 gộp: `d0049d16bb2bc945c97d76ae94d43d971a1b687ce13f5ad6a5401cf00689dfe5`
- SHA-256 16.500 ID trước: `f571e0ffec0ea67f8768fe6110d8d76b9ee1ad03a594cda450db17615dac7074` (byte-identical)

Tiếp CP012b: còn 1.440 mục, ưu tiên phần UI/hướng dẫn thực sự rõ nghĩa như 0131–0132, 0300–0312 sau phân loại; bỏ qua các tên riêng, mã nội bộ và mật khẩu. Cần phân biệt tiến độ dịch và các mục giữ English có chủ đích trước khi chốt phần trăm bao phủ game.