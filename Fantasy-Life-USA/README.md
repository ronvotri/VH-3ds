# Fantasy Life (USA) — CP013f — Votri Valley

**26/11/2026 · 19.353/34.812 ID đã xử lý bản dịch (55,59%)**, còn 15.459 ID không nằm trong JSONL vi. CP013a–f = 853 ID mới.

## Dịch mới

113 ID tiêu đề nhạc nền/khúc ca trong gói 0260–0261, bảng 8554/8558. Dịch tiêu đề, không dịch lời bài hát. Giữ nguyên tên riêng, Life và biến thể EN_A/EN_B. Các tiêu đề địa danh thuần tên giữ nguyên; chưa xác minh màn hình phát nhạc thực tế. Việc Việt hóa tên khúc nhạc (không phải tên item/skill/nhân vật) là lựa chọn biên tập của checkpoint.

## Giữ nguyên tên/thuật ngữ — không cộng vào số dịch

| Nhóm | ID |
|---|---:|
| Rank và chỉ số | 442 |
| Tên skill/thuật ngữ kỹ năng | 435 |
| Tên phần thưởng/item | 111 |
| Địa danh | 19 |
| Tiêu đề nhạc chỉ là địa danh/tên khu vực | 12 |
| Tổng | 1.019 |

Các bảng 6855/6861, 6866/6870, 8489/8493, 8545/8549 và các bảng phần thưởng 6877–6917; kiểm theo metadata và nội dung nguồn. Không tự đổi tên NPC hay tên Tây Ban Nha khi chưa có đối chiếu chính thức.

Cộng dồn KEEP từ CP013e–f: 3.618. Tổng bản dịch + KEEP dự kiến: 22.971/34.812 (65,99%), còn 11.841 chưa chốt (bao gồm 97 HOLD CP013e). Đây là tiến độ phân loại, không phải tỷ lệ Việt hóa, và chưa chạy kiểm gộp toàn bộ.

## QA

113 bản dịch không trùng nhau, khớp ID nguồn, khác nguồn, NFC, không rỗng; mã CTRL, số, dấu +, printf và xuống dòng bảo toàn. 1.019 quyết định giữ nguồn khớp ID và không trùng batch mới, CP013e KEEP/HOLD hoặc các batch CP010c–CP013e có cục bộ; phạm vi checkpoint cũ hơn đối chiếu qua báo cáo. Hai tệp đọc lại từ GitHub khớp dữ liệu. Chưa chạy toàn bộ script khôi phục trong môi trường hiện tại; chưa kiểm font, độ rộng, runtime, hay build ROM.

## Khôi phục
- `translations/cp013f-113.jsonl.bz2.b64`: SHA-256 giải nén `4eb1e0ccd1ac4cd3430b21d40b62fe2a7b798047aae1e8aa78609fbeeb8b352f`.
- `reviews/cp013f-keep.jsonl.bz2.b64`: SHA-256 giải nén `7978fad9809afa1dad66071d2d2b89628c68d4d6ae67b4b3ec45da1cf366a3f8`.
- `python3 unpack_batches.py` dự kiến xuất `merged-CP013f-19353.jsonl`, kiểm trùng giữa bản dịch và danh sách KEEP/HOLD, không tự vá các quyết định giữ tên.

Tiếp CP013g: rà bảng NPC/quái và những UI có ngữ cảnh rõ; đối chiếu tên ngoại ngữ với bảng EN trước khi chốt. Không sửa main.

Mốc trước: [CP013e](CHECKPOINT-013e.md). Xem [quy tắc ngôi xưng](NGOI_XUNG.md).
