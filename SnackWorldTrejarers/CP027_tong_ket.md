# Snack World: Trejarers — Checkpoint 027

## Kết quả (đã đối chiếu nguồn)
- Tiếp nối từ CP026, xử lý **500 ID theo vị trí 0-based 3740–4239**.
- **496 câu Việt hóa mới**; **4 placeholder Nhật** tại 3952, 3953, 4226, 4227 giữ nguyên, chưa tính hoàn thành.
- Lũy kế: **4.240 / 23.091 ID = 18,36%** đã xử lý. Tổng **14 placeholder Nhật** chưa dịch trong toàn bộ lũy kế (1469–1470, 2662–2665, 3237–3238, 3506–3507, 3952–3953, 4226–4227).
- QA tĩnh: **500/500 danh sách tag khớp chính xác về nội dung/thứ tự**, toàn bộ **4.240 ID không trùng**. Source, hash, vị trí, index và raw_hex giữ nguyên trong JSONL.
- Dịch theo ngữ cảnh: Sultan/Balsam, Honeybun/Gobson, Nutmegg/Mounty, Dragon Knight/Falgon, Krapen, Penguin Knight, Spicy Galz và những hướng dẫn chiến đấu.

## Dữ liệu thực tế ĐÃ PUSH lên GitHub
- [CP027_moi_500_ID.jsonl](./checkpoints/CP027_moi_500_ID.jsonl) — **đã ghi trực tiếp 500 ID nguồn** với trường `vi`, metadata đầy đủ, status rõ ràng, commit `878de22f470dd033cadabdefe60b9be74bce98a6`.
- Tệp đã được đọc và kiểm tra parse JSONL 500 dòng trước khi commit.
- ZIP `SnackWorld_Trejarers_VH_CP027.zip` tải trong cuộc trò chuyện chứa `CP027_luy_ke_4240_ID.jsonl`, `CP027_moi_500_ID.jsonl`, `CP027_doi_chieu_500_ID.md`, `README.md` và `QA_tinh_CP027.md`.
- **Lưu ý:** bản lũy kế 4.240 ID hiện chỉ có trong ZIP, chưa push lên repo; các checkpoint CP001–026 trước chủ yếu có báo cáo/mẫu dịch. Không khẳng định GitHub đang lưu toàn bộ bản dịch cũ.

## Chưa QA
- Font Việt có dấu trên 3DS, giới hạn byte/glyph/line wrap, mapping nhân vật trong cutscene, kiểm thử repacker và CIA.
- Tag bất thường `<\\nCG>` tại vị trí 4187 được giữ nguyên theo file nguồn (chưa sửa engine).
- Tiếp CP028 từ vị trí **4240**.
