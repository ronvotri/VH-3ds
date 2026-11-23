# Fantasy Life USA — Checkpoint 005 hoàn thành (CP005c)

**23/11/2026 · CP005c = 400 câu mới, gói 0042–0045**

- CP005a: 700 ID; CP005b: 900 ID; CP005c: 400 ID → **CP005 tổng cộng 2.000 ID**.
- Tích lũy **4.500/34.812 (12,93%)**, còn **30.312**.
- Đợt này dịch: Marine Silk, Snow Runners, Sun/Star/Moon Clusters, sưu tập kiếm, Dueling/Duelling Outfit; ông nuôi rạp xiếc bọ chét, bưu điện Lettina và Roland; người sưu tập Royal Furniture, món Magical Pie/Pudding, cướp biển mê đồ Snakeskin; yêu cầu nấu ăn Dino/Monster/Dragon Meat, Alejandro và thuyền sa mạc.
- Giữ riêng EN_A và EN_B theo từng ID; không thay tên item/skill bằng từ Việt.

## Dữ liệu

- `translations/cp005c-400.jsonl.bz2.b64`: 400 câu CP005c nén bzip2/base64.
- `python3 unpack_batches.py`: giải nén và kiểm SHA-256 các checkpoint để khôi phục `translations/merged-001-045.jsonl` (4.500 ID).
- SHA-256 CP005c JSONL: `052ed3544734b7b358d86a655298e0e5d7cd238688d3c2bfe4ffce8fe456f738`.
- SHA-256 toàn CP005 2.000 ID: `309d868dc821d859cc587f5b8a80e435b1d25fb54bdaa47acc023c0a7adb3ce0`.

## QA

Đối chiếu toàn bộ 4.500 ID với bản nguồn: không thiếu/trùng ID, không mất token, không bản dịch rỗng, Unicode NFC. Đã sửa hai chỗ ghép tiền tố sai khi chọn nhân vật nữ trong gói 0043 trước khi xuất bản.

**Chưa vá font, chưa thử trên máy 3DS, chưa đo pixel width, chưa xuất bản patch/CIA.** Mốc kế: gói 0046, từ câu 4.501.
