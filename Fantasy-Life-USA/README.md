# Fantasy Life (USA) — Việt hóa Votri Valley

**Checkpoint 006 HOÀN TẤT — 23/11/2026**

- Bộ bàn giao: `FantasyLife-USA-BoBanGiaoChoBenDich-2026-11-22.zip`, Title ID `0004000000113200`, 34.812 mục nguồn.
- **Đã dịch 6.500 / 34.812 (18,67%)**, còn **28.312**. Đây là tỷ lệ trên *các ID trong bộ nguồn*, không phải % game/ROM đã được vá.
- CP001–004: 2.500 ID; CP005: **2.000 ID**; CP006: **2.000 ID**.
- CP006 gồm **500 + 500 + 100 + 300 + 600**: CP006a (0046–0050), CP006b (0051–0055), CP006c-01 (0056), CP006c-02 (0057–0059), **CP006c-03 (0060–0065)**.
- Mọi tệp trên nhánh riêng **`vh/fantasy-life-usa`**, không sửa `main`.

## Nội dung của 600 câu CP006c-03 (0060–0065)

- 0060: Furlin/Fluffkin họa sĩ đang yêu, Tailor học nghề, bé mê chiến binh, quý cô mê Lord Leo.
- 0061: Lord Leo; Sir Loin mê nấu thịt; nghiên cứu Tribal Tykes, Strongtaur, Shadow Protectors; bà cụ thử Fuzzband, Miracle và Hot Spring Egg.
- 0062: Tate mê nấm và Broccoli; Angler học câu cá; Furlin/Fluffkin mê mỹ thực; người lính sợ Dark Wisps.
- 0063: người lính luyện đánh Darkzine/Calamitus; Daphne/Napollon; cô bé thích côn trùng; bà nội trợ và Remote Island Honey.
- 0064: Divine Pods; ông thợ đa nghề; bộ sưu tập càng/mai cua; nhật ký nhiệm vụ bắt đầu.
- 0065: các mục tóm tắt nhiệm vụ NPC, giữ đúng ID, Rank nghề, tên item, số lượng/địa danh.

**Quy tắc:** giữ tiếng Anh cho tên riêng, Life, item, skill, thuật ngữ chính; tiếng Việt tự nhiên, có dấu, vui đúng người nói. Giữ riêng EN_A/EN_B và toàn bộ token `{CTRL:hex}` đúng chuỗi và thứ tự. Không tự gán quan hệ/thân phận khi nguồn không xác nhận.

## Khôi phục toàn bộ bảng dịch

Trong thư mục `Fantasy-Life-USA`, chạy:

```bash
python3 unpack_batches.py
```

Chương trình dùng thư viện chuẩn Python giải nén và **kiểm SHA-256** tất cả checkpoint trong `translations/`, chống trùng ID và ô dịch rỗng, rồi tạo:

- `translations/cp006c03-new-600.jsonl` — 600 câu mới.
- `translations/cp006-complete-2000.jsonl` — toàn bộ **2.000 câu CP006**.
- `translations/cp005-complete-2000.jsonl` — toàn bộ 2.000 câu CP005.
- **`translations/merged-001-065.jsonl` — 6.500 ID tích lũy.**

Dữ liệu dạng JSONL `{"id":"FL-USA::...","vi":"bản dịch"}`, phải ghép với `01_CAN_DICH.jsonl` trong bộ bàn giao theo `id`. Không viết đè các trường `source`, `raw_hex`, `controls_hex`, `references`, `length_bindings` hoặc `alias_ids`.

**SHA-256 CP006c-03 (600 mục):** `edac3870265815e1e62dfe438075610ce77becfe5781dae18b40b7d1ace2152b`.

**SHA-256 CP006 đầy đủ (2.000 mục):** `b49cbcc488a705ab2eba24d96f5593d4d87d2b785822d6dc7685007c1fdc18a5`.

## QA và giới hạn

- Đối chiếu **6.500/6.500 ID** với bộ nguồn: không sai ID, không trùng, không có câu rỗng, không mất/đảo token, Unicode NFC chuẩn.
- Riêng 600 câu mới đã kiểm **4.338 token**; tên item bọc marker màu giữ đúng và số lượng/phần thưởng không sai chữ số. Dịch đủ 362 mục EN_A và 238 EN_B.
- Kiểm tra cấu trúc **không thay cho QA ngữ nghĩa hoặc QA giao diện**: `speaker=unknown` phải đối chiếu scene khi chơi, token xuống trang phải đo theo font/pixel width.
- **Chưa có patch font tiếng Việt hoặc RomFS/CIA chạy được trên Nintendo 3DS.** Không ghi CP006 là bản game đã Việt hóa 18,67%.
- Xem `CHECKPOINT-006-complete.md`, `QA-006-complete.md`, `NGOI_XUNG_CP006.md`, `ISSUES-006.md`.

**Tiếp theo:** gói `0066_hoi_thoai_va_huong_dan.txt`, mục thứ **6.501**.
