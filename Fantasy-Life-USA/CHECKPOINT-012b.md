# Fantasy Life (USA) — CP012b — Votri Valley

**25/11/2026 · 17.557/34.812 ID đã xử lý (50,43%)**. Còn **17.255 ID**. CP012a 560 + CP012b 497 = 1.057/2.000; còn 943 mục để khép CP012.

## Phạm vi

| Gói | Mục mới |
|---|---:|
| 0124 | 28 |
| 0300 | 72 |
| 0301 | 67 |
| 0302 | 49 |
| 0303 | 58 |
| 0304 | 21 |
| 0305 | 20 |
| 0308 | 6 |
| 0309 | 28 |
| 0310 | 10 |
| 0311 | 68 |
| 0312 | 38 |
| 0313 | 32 |
| **Tổng** | **497** |

- Nhãn ngoại hình, loại đồ, giọng nói, các thao tác A/X/Y/L/R, tiêu đề hướng dẫn Life, chế tạo và menu.
- 267 nhãn trong 0300–0304 và 20 trong 0305 (tùy biến/loại đồ); 28 mục 0124 về tính cách/dáng người; 28 mục 0309; 116 mục 0310–0312; 32 mục 0313; 6 mục 0308. Phân loại theo nội dung nguồn, không khẳng định mọi chuỗi xuất hiện trên màn hình.
- Chỉ dịch các nhãn có nghĩa đủ rõ trong ngữ cảnh. Nhiều nhãn EN_A trong nhóm 0300–0313 có dạng tiếng Anh dịch thô; chưa kiểm hình minh họa hay chức năng UI thực tế. Bỏ qua các tên riêng, tên Life/Rank/skill, mã nội bộ, nhãn `Unused`/`Preliminary`, và các chuỗi không đủ ngữ nghĩa. Danh sách 761 mục chưa xử lý trong các gói đã xem lưu riêng; không tính là dịch hoặc coi tất cả là lỗi.
- Giữ tên Life như Tailor, Blacksmith, Woodcutter, Miner, Alchemist, Cook, Mercenary; giữ Rank, Level, License, Pocket. Bảy lựa chọn dùng lại bản Việt đã có để nhất quán; các mục khác được dịch theo ngữ cảnh. Các nhãn mô tả hình dạng cần so screenshot để kiểm chính xác.

## QA tĩnh

- 497 ID mới duy nhất, đều có trong nguồn; tất cả bản dịch khác source, không rỗng, Unicode NFC. 17.557 ID tích lũy không trùng; 68.276 token điều khiển giữ nguyên nội dung và thứ tự, 0 token mới.
- Ba khác biệt chữ số trong nhóm 0309 là `once/twice` -> `1/2 lần`, đã kiểm; chuỗi `6 Press the A button once` được hiểu là nhấn A 6 lần theo chuỗi liên tiếp 1–6, cần xác minh trên UI. Không có kiểm runtime.
- 17.060 ID CP012a giữ nguyên byte. Một nhãn Spanish cũ chưa xác minh, các gói 0070–0071 HOLD. % trên tổng ID nguồn, không đồng nghĩa % văn bản đã vá trên ROM.
- Chưa kiểm font, pixel width, ngắt trang, tên ngoại hình và tên gọi cơ chế trên 3DS; chưa có patch chơi được.

## Khôi phục
Chạy `python3 unpack_batches.py` trong `Fantasy-Life-USA` trên nhánh `vh/fantasy-life-usa`. Batch `translations/cp012b-497.jsonl.bz2.b64` xuất `cp012b-new-497.jsonl` và `merged-CP012b-17557.jsonl`; ghép theo ID với `01_CAN_DICH.jsonl`, giữ metadata.

- SHA-256 batch: `3a208c9c924fe24b427d058cf0c0654f772cc56854735ae930c03ba8cebbf6d1`
- SHA-256 gộp: `a66a8703876165316420fa9dbdca987bd9fb386bd90692524498eb28a9a4d7f5`
- SHA-256 tiền tố CP012a: `d0049d16bb2bc945c97d76ae94d43d971a1b687ce13f5ad6a5401cf00689dfe5`

Tiếp CP012c: còn 943 mục theo mục tiêu 2.000, rà 0306–0307, 0314–0319 và các gói UI chưa xử lý, chỉ chọn nhãn rõ nghĩa, tách tên riêng/mã nội bộ. Không lấy tên item thuần English làm bản dịch mới. Cần kiểm nguồn tiếng Nhật hoặc hình thật đối với các nhãn dịch máy mơ hồ.