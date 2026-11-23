# Snack World: Trejarers — Checkpoint 023

## Kết quả thực tế
- Dịch **140 ID mới từ thứ tự 0-based 2940–3079** trong `ban_dich/de_dich_uu_tien_update.jsonl` của gói nguồn.
- Lũy kế **3.080/23.091 ID = 13,34%** theo số ID đã xử lý.
- **140/140 tag** nguồn đúng thứ tự, **3.080 ID không trùng** trong JSONL lũy kế.
- Giữ nguyên metadata nguồn như `id`, `file_sha256`, `raw_hex`, `pool_offset`.
- Bản dịch hoàn chỉnh nằm trong `SnackWorld_Trejarers_VH_CP023.zip` gồm `CP023_moi_140_ID.jsonl`, `CP023_luy_ke_3080_ID.jsonl`, `CP023_doi_chieu.md`, `README.md`.

## Nội dung
- Kết lời nguyền chêm từ “totes”, hướng dẫn zoomstone, Curberus và các boss.
- Chỉnh giờ hệ thống máy 3DS và hạn chế nhận trend bonuses/Sam Witch trong hai ngày.
- Wolfy, Fido, Pie-Pie và quá khứ của Armamint.
- Dragon Knight bị biến thành rồng hắc ám, nhiệm vụ giải cứu trong Distillery.
- Pigsy muốn ăn super spud để mạnh hơn.
- Lời hướng dẫn bắt đầu quest, các câu thoại tiếng Nhật.

## Ví dụ bản dịch
| STT nguồn | Bản Việt hóa |
|---:|---|
| 2941 | Tôi siêu biết ơn ngài Lich! Và cảm ơn cả `<PNAME>` nữa! |
| 2963 | Nghĩa là dù quay về thị trấn, `<PG>`khi sẵn sàng đi tiếp, cậu vẫn trở lại chỗ này được. |
| 2995 | Gobson!? Anh còn `<EBI>chẳng có</E>` đường chân tóc mà! |
| 3003 | Ta đã dặn Sam Witch phớt lờ cậu! Từ giờ cũng không có trend bonus nữa! |
| 3026 | Dù là quái vật, bọn tớ luôn được ông chủ đối xử tử tế. |
| 3043 | Họ biến thành những con rồng hắc ám, lang thang vô định và mất sạch ký ức về bản thân. |
| 3069 | Tuy có hơi mít ướt, Pigsy vẫn là một pigdragon rất cừ đấy! |
| 3073 | Quest... bắt đầuuu!! |

## Chưa hoàn tất
- Chưa QA font Việt, byte limit, line wrap, mapping nhân vật đầy đủ, repacker/CIA.
- Ít nhất 6 placeholder Nhật từ các CP trước chưa được dịch.
- **Commit GitHub này lưu báo cáo, KHÔNG chứa JSONL đầy đủ.** JSONL đầy đủ đã được tạo tại ZIP bàn giao và chưa đồng bộ lên repo.
- CP024 bắt đầu từ vị trí nguồn **3080**. Nhánh `main` không thay đổi.
