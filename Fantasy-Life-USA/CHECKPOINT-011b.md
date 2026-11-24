# Fantasy Life (USA) — CP011b — Votri Valley

**24/11/2026 · 15.577/34.812 ID đã xử lý (44,75%)**. Thêm 604 mục; còn 19.235 ID. CP011 đạt 1.077/2.000 mục, còn 923. Nhánh `vh/fantasy-life-usa`, không sửa `main`.

## Phạm vi mới
| Gói | ID mới | Nội dung |
|---|---:|---|
| 0333 | 99 | Tên nhiệm vụ |
| 0334 | 99 | Tên nhiệm vụ |
| 0335 | 100 | Tên nhiệm vụ |
| 0336 | 57 | Tên nhiệm vụ biến thể EN_B |
| 0346 | 100 | Hướng dẫn Life, điều khiển, chiến đấu |
| 0347 | 62 | Hướng dẫn, hiệu ứng và mô tả trang bị |
| 0348 | 14 | Nhãn trạng thái, điều kiện sau skill |
| 0350 | 73 | Hội thoại #28–100 |
| Tổng | **604** | 355 tiêu đề và 249 mục khác |

67 nhãn item/skill/chỉ số thuần English hoặc kỹ thuật thiếu ngữ cảnh được giữ riêng, không tính là câu dịch. Các gói 0349 và 0350#1–27 chứa nhiều nhãn debug dịch thô, vẫn chưa duyệt. 200 mục 0070–0071 tiếp tục HOLD; một nhãn Spanish cũ vẫn chưa xác minh.

## QA
- 604 ID đúng nguồn, không trùng 14.973 ID trước, không rỗng, NFC. 2.359 token mới, tổng 67.876 token khớp nguyên chuỗi/thứ tự. 77 vùng màu mã f7 03 giữ nguyên tên sau khi bỏ token bố cục và chuẩn hóa khoảng trắng.
- 44 cảnh báo số/chỉ số thô: tiêu đề Attack không phải chỉ số Attack; nhắc lại SP cho rõ nghĩa; Defense viết hoa; dấu phân cách hàng nghìn. So chữ số sau chuẩn hóa: 0 sai khác. Giữ EN_A/EN_B riêng. Hai tiêu đề trùng nguồn với CP cũ đã thống nhất.
- Ngôi xưng: Hansel tôi–cậu; Napollon tôi–bạn, Daphne cô ấy; Swabbie ta–cậu; người tiên tri ta–con; Gladstone ta–ngươi; bà lão bà–cháu; khi chưa biết người nói ưu tiên trung tính. Nhánh giới tính #0350/65 giữ nguyên token, chưa xác nhận hiển thị hai nhánh trên máy.
- QA tĩnh không thay QA ngữ nghĩa theo scene, font, pixel width, ngắt trang, nút bấm hoặc runtime. Chưa có patch RomFS/CIA chơi được.

## Khôi phục
Chạy `python3 unpack_batches.py` tại `Fantasy-Life-USA` trên GitHub. Batch `translations/cp011b-604.jsonl.bz2.b64`; tạo `cp011b-new-604.jsonl` và `merged-CP011b-15577.jsonl`. ZIP bàn giao chứa `cp011b-new.jsonl`, `merged-CP011b.jsonl`. Ghép theo ID vào 01_CAN_DICH.jsonl, không sửa metadata nguồn. 14.973 mục cũ giữ byte-identical.

SHA-256 batch: `e92384a54b1e0f6b7a24c93786745a2642913fab11e4c22697542ba89df5c6f2`

SHA-256 gộp: `b627c103a485f87dce708831c26cdfa9bc904d1c146689fda9f2b8bc79bcdf30`

## Tiếp theo
Ưu tiên hội thoại chưa dịch ở 0330–0332, sau đó các nhóm mô tả/ngữ cảnh rõ ràng còn thiếu. Rà theo danh sách ID chưa dịch thay vì đi theo thứ tự gói đơn thuần. Không đếm tên item giữ English, nhãn debug chưa rõ hoặc chuỗi đã dịch. CP011 còn 923 mục.