# Fantasy Life (USA) — CP012 hoàn tất — Votri Valley

**25/11/2026 · 18.500/34.812 ID đã xử lý (53.14%)**, còn 16.312. CP012a 560 + CP012b 497 + CP012c 527 + CP012d 416 = **2.000 ID**.

## Phạm vi CP012d

| Nhóm | ID mới |
|---|---:|
| Danh xưng NPC (0177–0178) | 56 |
| Tiêu đề chủ đề (0252) | 36 |
| Nhãn hướng dẫn nghề (0308) | 18 |
| Nhãn sự kiện (0114–0120; nội bộ, chưa xác minh hiển thị) | 306 |
| Tổng | 416 |

416 ID tương ứng 340 chuỗi nguồn khác nhau (411 EN_A, 5 EN_B). Nhãn sự kiện được dịch theo đúng phần nghĩa rõ trong nguồn EN, không phải lời thoại đã xác minh. Không suy ra speaker, quan hệ nhân vật hoặc địa danh chính thức từ nhãn nội bộ. Tên riêng, item, skill, Life, Rank và địa danh giữ EN. Các nhãn có thứ tự hội thoại “one/two/three” được dịch “lần 1/2/3” theo nhóm nguồn; cần đối chiếu cảnh nếu dùng trong runtime. Tiêu đề 0252 chưa xác minh chức năng UI. `Un-bear-able` giữ bản dịch nhất quán từ CP cũ.

Những nguồn mơ hồ, mã kỹ thuật, tên riêng và các nhãn lặp ưu tiên thấp còn để riêng: 608 ID trong các gói vừa xem chưa chọn, không đồng nghĩa tất cả cần Việt hóa. Không coi 306 nhãn nội bộ là 306 câu thoại. 200 ID 0070–0071 vẫn HOLD. Các nhãn 0114–0123 chưa chọn vẫn cần kiểm ngữ cảnh; không khẳng định đã dịch trọn các gói này.

## QA cấu trúc

- 416 ID mới có nguồn, không trùng, khác source, không rỗng, Unicode NFC. 18.500 ID tích lũy duy nhất, 68.277 token đúng thứ tự/nội dung; 0 token mới vì tất cả là nhãn ngắn.
- 13 trường hợp số viết chữ → chữ số chỉ là thứ tự đối thoại, đã đối chiếu; ký hiệu ② và mã E27 giữ nguyên. Không phát hiện bản dịch mới khác cách dịch cũ cho cùng chuỗi EN trong nhóm đã chọn. Bảo toàn byte 18.084 ID cũ.
- 18.500 là số ID xử lý ở cấp dữ liệu, **không phải % văn bản hiển thị trong ROM**. Các nhãn sự kiện nội bộ là bản dịch sơ bộ, chưa QA ngữ nghĩa độc lập. Chưa vá font, đo pixel, test phân trang hoặc build patch 3DS. Một nhãn item tiếng Tây Ban Nha từ CP cũ vẫn chưa dịch.

## Khôi phục

Trên nhánh `vh/fantasy-life-usa`, chạy `python3 unpack_batches.py` trong `Fantasy-Life-USA`. Gói `translations/cp012d-416.jsonl.bz2.b64` khôi phục `cp012d-new-416.jsonl`; bản gộp `merged-CP012-18500.jsonl`; riêng CP012 `cp012-complete-2000.jsonl`. Ghép theo ID với `01_CAN_DICH.jsonl`; không sửa metadata hoặc nguồn. Nhánh `main` không thay đổi.

- SHA-256 mới: `ee48ed9b0e6a066a5cde1a3bfa0fc1c12e3573fd2c0638931bde9b0c2196a617`
- SHA-256 CP012: `909e0100bf53eaef2ceb3af7880d418f0555440719048cd6ca98875b17418228`
- SHA-256 bản gộp: `037d707bc441ca32f7ca8b36404882f56ad8ce591b8304b2e17d4d5b0baba05f`
- SHA-256 CP012c: `b414d20de2ae935e01bd0340d45f4ea2367e9e29aec982404fa54b9c59e495bb`

## Tiếp theo

CP013: thống kê toàn bộ 16.312 ID chưa xử lý theo nhóm tên riêng cần giữ EN, nhãn kỹ thuật cần nguồn Nhật, và nội dung có nghĩa rõ; ưu tiên dịch nhóm người chơi đọc được, không chép tên EN vào VI để tăng tỷ lệ. Các nhãn sự kiện 0121–0123 và danh xưng NPC còn lại cần phân loại trước khi dịch tiếp.