# Fantasy Life (USA) — CP013b — Votri Valley

**26/11/2026 · 18.993/34.812 ID đã xử lý (54,56%)**, còn 15.819. CP013a 285 + CP013b 208 = 493 ID mới thuộc CP013.

| Nội dung | ID |
|---|---:|
| Thư và tiêu đề hướng dẫn | 50 |
| Hiệu ứng, chỉ số | 48 |
| Danh xưng NPC và nhãn cùng ngữ cảnh | 108 |
| Hai nhãn UI lấy từ HOLD | 2 |
| Tổng | 208 |

Đối chiếu 269 ứng viên với 01_CAN_DICH.jsonl của ZIP nguồn người dùng cung cấp. 61 nhãn kỹ thuật/tài nguyên hoặc bắt đầu bằng # được giữ riêng, chưa gộp vào patch. 349 tiêu đề nhiệm vụ đã có trong CP011b không tính lại và không ghi đè. 208 bản dịch không rỗng, khác nguồn, NFC; giữ đủ 5 token điều khiển, chữ số, dấu + và %. Đã đối chiếu ID với các batch cũ (kiểm tra ứng viên trước đó và các batch CP012–CP013a tại phiên này). Chưa chạy toàn bộ công cụ phục hồi sau thay đổi với mọi batch trong môi trường hiện tại; chưa kiểm tra font, ngắt dòng, runtime hoặc ROM.

## Khôi phục

Chạy `python3 unpack_batches.py` trong `Fantasy-Life-USA` trên nhánh `vh/fantasy-life-usa`. Batch mới `translations/cp013b-208.jsonl.bz2.b64` được kiểm SHA-256 sau giải nén: `4b8fbfea8ae9d2de3e00841aa16ddd872f21845b3caec55574dafa0be4e49e8c`. Script giữ kiểm tra toàn bộ CP013a cũ và bổ sung đầu ra `merged-CP013b-18993.jsonl`.

Tiếp theo: CP013c, ưu tiên phân loại từng ID từ nguồn thật; giữ tên riêng/item/skill/thuật ngữ chính tiếng Anh, không tính tên giữ nguyên hoặc nhãn debug.

Mốc trước: [CP013a](CHECKPOINT-013a.md). Xem [quy tắc ngôi xưng](NGOI_XUNG.md).
