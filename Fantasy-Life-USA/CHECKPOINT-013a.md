# Fantasy Life (USA) — CP013a — Votri Valley

**25/11/2026 · 18.785/34.812 ID đã xử lý (53.96%)**, còn 16.027. CP013a thêm 285 nhãn ngoại hình từ nguồn Tây Ban Nha: 0262#96–100 (5), 0263 (100), 0264 (99), 0265 (81). Không dịch tên riêng nhân vật hoặc trang bị; 264#88, 265#46 và các tên nhân vật giữ chờ đối chiếu.

## Phân loại sơ bộ 16.027 ID còn lại

| Nhóm đề xuất | ID |
|---|---:|
| HOLD_MAP_DEBUG | 200 |
| EVENT_INTERNAL_REVIEW | 694 |
| MIXED_REVIEW | 1,567 |
| INTERNAL_ASSET_REVIEW | 1,302 |
| KEEP_EN_CANDIDATE | 3,647 |
| MAP_LOCATION_REVIEW | 300 |
| NPC_MONSTER_NAME_REVIEW | 3,588 |
| AVATAR_REVIEW | 334 |
| ITEM_LOCALE_REVIEW | 4,395 |
| Tổng | 16.027 |

Phân nhóm theo gói và ngữ cảnh nguồn, **chưa duyệt từng tên**. Không được hiểu KEEP_EN_CANDIDATE là đã xác nhận tất cả tên English. NPC_MONSTER_NAME_REVIEW và ITEM_LOCALE_REVIEW cần đối chiếu tên chính thức; nhãn âm thanh, debug, tài nguyên không tự vá. 200 HOLD ở 0070–0071 vẫn tách riêng. CSV `REMAINING-16027-TRIAGE.csv` trong ZIP liệt kê từng ID và lý do. Các nhóm nguồn còn lại do heuristic gốc phân loại: {'mo_ta_va_chu_khac': 200, 'ten_ui_va_thuat_ngu': 15525, 'vat_pham_che_tao_va_chi_so': 302}; không còn ID chưa xử lý thuộc nhãn nhóm hội thoại/hướng dẫn hoặc nhiệm vụ, nhưng không chứng minh mọi thoại trong ROM đã dịch.

## QA và khôi phục

285 ID mới đều có nguồn, không trùng, khác nguồn, Unicode NFC, 0 token mới. Bản gộp 18.785 ID giữ đủ 68.277 token và giữ nguyên byte 18.500 ID CP012. Nhãn ngoại hình Tây Ban Nha chưa đối chiếu hình thực tế. Chưa kiểm font, tràn chữ hoặc patch 3DS. 306 nhãn nội bộ sơ bộ CP012d vẫn cần kiểm.

Chạy `python3 unpack_batches.py` trong `Fantasy-Life-USA` trên nhánh `vh/fantasy-life-usa`. Gói `translations/cp013a-285.jsonl.bz2.b64` khôi phục `cp013a-new-285.jsonl` và bản gộp `merged-CP013a-18785.jsonl`. Không thay đổi `main`.

- SHA-256 mới: `00e09a7af0c7a1660713721b37e37840b1b73b43aea50c063683a5dce37da39f`
- SHA-256 gộp: `02ac3b537cd5ef62733f5753caf4a7a79b4b5d17146fb9cfd42342b3ba64d56c`
- SHA-256 CP012: `037d707bc441ca32f7ca8b36404882f56ad8ce591b8304b2e17d4d5b0baba05f`

Tiếp theo: kiểm nhóm MIXED_REVIEW và các danh xưng NPC chung, đối chiếu item Spanish với tên English tương ứng, không tính chép nguyên tên thành bản dịch mới.