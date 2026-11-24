# Snack World: Trejarers — Chỉ mục JSONL CP001–CP030

Bộ bản dịch trên nhánh `vh/snack-world-trejarers`, tổng 5.740 ID nguồn thuộc dải vị trí 0-based **0–5739**, chia thành 12 file không chồng nhau. **5.720 ID có trường dịch tiếng Việt**, **20 ID là placeholder nguồn còn giữ nguyên**. Dữ liệu chưa phải bản vá 3DS đã kiểm thử.

| Khoảng vị trí | Tệp nguồn + bản dịch | ID |
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
| 4740–5739 | [CP029_moi_500_ID.jsonl](./CP029_moi_500_ID.jsonl) | 500 |

Nguồn chuẩn: `SnackWorldTrejarers-BoTaiLieu-VietHoa-2026-11-19.zip`, `ban_dich/de_dich_uu_tien_update.jsonl`. Mỗi dòng JSONL chứa `id`, `source`, metadata nguồn và bản dịch `vi`; placeholder được đánh dấu riêng qua `status` (tên trạng thái có thể khác giữa các CP cũ). Nguyên tắc giữ tên riêng, Item/Skill/Jara/Snack bằng tiếng Anh, lời thoại Việt Gen Z nhẹ và ngôi xưng theo ngữ cảnh. Các đợt chưa được QA font có dấu, độ rộng/byte câu hoặc xây dựng CIA.

CP029: 497 dòng Việt, 3 placeholder tại vị trí 4933, 4934, 4939. Báo cáo: [CP029_tong_ket.md](../CP029_tong_ket.md).

CP030: 497 ID có bản Việt, 3 chuỗi kỹ thuật giữ nguyên (5458, 5512–5513). Commit dữ liệu `c2b978f`. CP031 tiếp từ vị trí **5740**. Không merge `main`.
