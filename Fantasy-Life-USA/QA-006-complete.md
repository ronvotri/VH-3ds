# QA tĩnh — Fantasy Life CP006 hoàn thành

| Hạng mục | Kết quả |
|---|---|
| Gói mới | **0060–0065** |
| Mục mới | **600/600** |
| Tổng tích lũy | **6.500/34.812** |
| Còn lại | **28.312** |
| Riêng CP006 | **2.000/2.000** |
| EN_A / EN_B gói mới | **362 / 238** |
| Token gói mới | **4.338** |
| Token sai nội dung/thứ tự | **0** |
| ID không có trong bộ nguồn | **0** |
| ID trùng trong 6.500 mục | **0** |
| Bản dịch rỗng | **0** |
| Tên item màu bị đổi | **0** |
| Sai trị số dạng số | **0** |
| Unicode NFC | **PASS** |
| Cảnh báo dài chữ thô | **0** |
| SHA-256 600 câu mới | `edac3870265815e1e62dfe438075610ce77becfe5781dae18b40b7d1ace2152b` |
| SHA-256 CP006 hoàn chỉnh | `b49cbcc488a705ab2eba24d96f5593d4d87d2b785822d6dc7685007c1fdc18a5` |
| QA font/tràn pixel/ngắt trang trên 3DS | **CHƯA QA** |
| QA câu chọn nam/nữ trong game | **CHƯA QA** |
| Kiểm speaker/target và xưng hô theo scene | **CHƯA QA** |
| Patch RomFS/CIA chơi được | **CHƯA CÓ** |

QA thực hiện: đối chiếu 600 ID với `01_CAN_DICH.jsonl` gốc; thêm 5.900 ID cũ để phát hiện trùng, kiểm toàn bộ 6.500 chuỗi điều khiển, chuẩn hóa Unicode NFC; riêng 600 mục kiểm đúng tên item trong marker màu và các số lượng/dạng số.

**Đây chỉ là QA cấu trúc.** Chưa đánh giá chính thức độ tự nhiên mỗi câu trong cảnh game hoặc độ rộng chữ theo font. Không dùng kết quả này để khẳng định đã có bản ROM Việt hóa chơi được.
