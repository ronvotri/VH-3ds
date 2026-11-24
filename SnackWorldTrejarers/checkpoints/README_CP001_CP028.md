# Snack World: Trejarers — JSONL checkpoint index (CP001–CP028)

**GitHub branch:** `vh/snack-world-trejarers`. **Source:** `SnackWorldTrejarers-BoTaiLieu-VietHoa-2026-11-19.zip`, `ban_dich/de_dich_uu_tien_update.jsonl`.

Tất cả **4.740 ID nguồn (vị trí 0–4739)** đã được đưa lên GitHub thành **10 file JSONL với đầy đủ `id`, `source`, metadata và trường `vi`**. Các file không chồng vị trí. Đối chiếu dữ liệu từ ZIP lũy kế CP028: **4.740 ID không trùng** và giữ `raw_hex` như nguồn; **14 placeholder** từ các CP cũ chưa dịch, **4.726 ID có bản Việt** (kể cả các dòng trùng nội dung). Trong đó, CP028 thêm 500 câu dịch.

| Vị trí 0-based | File JSONL trên nhánh | Số ID |
|---|---|---:|
| 0000–0499 | [CP001_026_backfill_0000_0499.jsonl](./CP001_026_backfill_0000_0499.jsonl) | 500 |
| 0500–0999 | [CP001_026_backfill_0500_0999.jsonl](./CP001_026_backfill_0500_0999.jsonl) | 500 |
| 1000–1499 | [CP001_026_backfill_1000_1499.jsonl](./CP001_026_backfill_1000_1499.jsonl) | 500 |
| 1500–1999 | [CP001_026_backfill_1500_1999.jsonl](./CP001_026_backfill_1500_1999.jsonl) | 500 |
| 2000–2499 | [CP001_026_backfill_2000_2499.jsonl](./CP001_026_backfill_2000_2499.jsonl) | 500 |
| 2500–2999 | [CP001_026_backfill_2500_2999.jsonl](./CP001_026_backfill_2500_2999.jsonl) | 500 |
| 3000–3499 | [CP001_026_backfill_3000_3499.jsonl](./CP001_026_backfill_3000_3499.jsonl) | 500 |
| 3500–3739 | [CP001_026_backfill_3500_3739.jsonl](./CP001_026_backfill_3500_3739.jsonl) | 240 |
| 3740–4239 | [CP027_moi_500_ID.jsonl](./CP027_moi_500_ID.jsonl) | 500 |
| 4240–4739 | [CP028_moi_500_ID.jsonl](./CP028_moi_500_ID.jsonl) | 500 |

## Quy tắc tiếp nối

- **CP029 bắt đầu từ vị trí 4740** trong danh sách nguồn ưu tiên, không dùng `id` engine như số thứ tự.
- Với từng ID, giữ nguyên `id`, `source_kind`, `file`, `file_sha256`, `label_hash`, `pool_offset`, `raw_hex` và tag; chỉ thêm/sửa trường dịch có kiểm soát.
- Giữ tên riêng, Item, Skill, Jara, Snack và thuật ngữ chính bằng tiếng Anh; phần thoại Việt hóa tự nhiên, hài hước có chừng mực, xưng hô theo quan hệ nhân vật.
- **Chưa có bản vá CIA đã kiểm thử.** Các bản dịch vẫn cần QA ngôi xưng, font Unicode, byte/line budget, repacker và chạy trong game.
- Dữ liệu ở các file này lấy từ snapshot CP028, không phải các tập kiểm thử runtime; không thay đổi nhánh `main`.

**Gói ZIP CP028 trong cuộc trò chuyện** còn có `CP028_luy_ke_4740_ID.jsonl` và bảng đối chiếu 500 ID.
