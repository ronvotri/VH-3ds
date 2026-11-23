# Fantasy Life USA — CP008 HOÀN TẤT 🇻🇳

**24/11/2026 · Mốc 10.500 / 34.812 (30,16%)**

CP008a có 1.610 ID dịch Challenge/Quest/UI, CP008b dịch thêm **390 ID NPC quests**, tổng **2.000 mục**. Còn **24.312 mục nguồn**. 200 ID trong 0070–0071 tiếp tục HOLD; không gộp nhầm vào bản được duyệt.

## Phạm vi CP008b
- `0105`: mục 17–100 (84 câu).
- `0106`, `0107`, `0108`: toàn bộ 100 câu mỗi gói (300 câu).
- `0109`: mục 1–6 (6 câu).
- **390 câu mới**.

Hội thoại nhân vật (Hansel, Gaites, Tufts, Barker, Honey, Bomba, Pepperonita, Calumnus...) được dịch theo mạch quest. Dữ kiện vật phẩm, kỹ năng, Life/Rank, quái, số lượng và phần thưởng giữ theo nguồn EN_A/EN_B. Ngôi xưng theo ngữ cảnh, chờ xác minh speaker/target bằng gameplay.

## Khôi phục

Tệp GitHub: `translations/cp008b-390.jsonl.bz2.b64` (bzip2→base64).

Chạy `python3 unpack_batches.py` tạo:
- `translations/cp008b-new-390.jsonl` (390 câu)
- `translations/cp008-complete-2000.jsonl` (2.000 câu)
- `translations/merged-CP008-10500.jsonl` (10.500 ID)

**SHA-256 CP008b:** `9640411f905472d66a00225a5ac0df777802835e0555d01fcb3d6d869556dec5`  
**SHA-256 CP008 trọn:** `daeac626ec53a92aba0952cb36ca7c9638e977010ca3e7afbebcf1f01ccad6e6`  
**SHA-256 gộp 10.500 ID:** `cf9d2da1080e0e4f1ce172bb126fd18088d64af1eafbf401e531975ebd665d05`

**Mốc tiếp:** `0109` mục 7. Không làm lại sáu mục đầu đã hoàn thành.

**Chưa có patch chơi được:** chưa vá font, đo pixel width, ngắt trang và thử nhánh nam/nữ thực tế trên 3DS.
