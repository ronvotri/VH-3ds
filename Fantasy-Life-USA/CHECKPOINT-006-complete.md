# Fantasy Life USA — Checkpoint 006 hoàn thành 🇻🇳

**Ngày 23/11/2026 · Trạng thái: hoàn thành 2.000 câu CP006**

## Tiến độ
- Đã dịch **6.500 / 34.812 ID (18,67%)**, còn **28.312 ID**.
- CP006: `CP006a:500` + `CP006b:500` + `CP006c-01:100` + `CP006c-02:300` + `CP006c-03:600` = **2.000 ID**.
- CP006c-03: 6 gói từ **0060 đến 0065**, mỗi gói 100 ID.
- Tiếp theo gói **0066**, mục thứ **6.501**.
- Nhánh riêng: `vh/fantasy-life-usa`, không tác động `main`.

## Nội dung CP006c-03
0060: Furlin/Fluffkin họa sĩ đang yêu, Tailor, nhóc chiến binh, Lord Leo.  
0061: Sir Loin nấu ăn, học giả quái vật, bà cụ chăm sóc sức khỏe.  
0062: Tate mê nấm và Broccoli, Angler học câu cá, người lính sợ Dark Wisps.  
0063: Darkzine/Calamitus, Daphne/Napollon, cô bé thích bọ, mật ong.  
0064: Divine Pods, bộ sưu tập cua, bắt đầu quest log.  
0065: quest log NPC và vật phẩm, giữ chỉ số, số lượng, địa danh và Rank.

## Khôi phục
`python3 unpack_batches.py` dùng dữ liệu nén ở `translations/` để tạo `cp006-complete-2000.jsonl` và `merged-001-065.jsonl`. Mỗi dòng dịch lưu cặp `id` và `vi`.

**SHA-256 gói mới 600 câu:** `edac3870265815e1e62dfe438075610ce77becfe5781dae18b40b7d1ace2152b`  
**SHA-256 CP006 đủ 2.000 câu:** `b49cbcc488a705ab2eba24d96f5593d4d87d2b785822d6dc7685007c1fdc18a5`  
**SHA-256 bản gộp 6.500 câu:** `fb1b4d5a41143e7f3d25bb8dc2cd404dc70c1b96515b3f80332f8f5253660064`

**Chưa phát hành patch 3DS:** chỉ là văn bản dịch; font Việt, pixel width, phân trang, cách hiển thị nhánh nam/nữ và ngôi xưng NPC còn phải kiểm thực tế.
