# Snack World: Trejarers — CP018

## Kết quả đã kiểm tra
- Tiếp nối CP017 từ vị trí nguồn (0-based) **2120–2239**, hoàn thành **120 câu dịch mới**.
- Lũy kế **2.240/23.091 ID (9,70%)** đã xử lý, bao gồm 2 placeholder CP012 chưa dịch.
- QA tĩnh: **120/120 tag khớp chính xác nội dung và thứ tự**, **2.240 ID duy nhất**. Đã giữ nguyên metadata nguồn trong JSONL.
- Cảnh: Genie/Pigsy, Dragon Knight/Falgon, Griff the Griffalo, Ciderella và Navy HEELs, Monster Troupe.
- Tên riêng/Item/Skill/thuật ngữ chính giữ tiếng Anh; nội dung hội thoại còn lại dịch tiếng Việt tự nhiên.

## Ví dụ bản dịch thực tế
| Vị trí | Bản Việt |
|---:|---|
| 2142 | Cưng tưởng bọn ta xin cái xúc tu đó để làm gì vậy? |
| 2160 | Đấu một trận sinh tử với ta... và giành chiến thắng! |
| 2180 | Tôi đợi cậu ở Frappé Fields nhé! Đừng có nuốt lời đấy! |
| 2191 | Phải, người đang đứng trước mặt các cậu từng là tinh anh `<EBI>Navy HEELs</E>`...`<PG>`lại còn thuộc đội Glass Slipper danh tiếng nữa! |
| 2198 | `<PV#cv002000_p04><GZ>`Không phải “Vâng”, đồ ngốc! Phải là “`<CR>Rõ, thưa chỉ huy!</C>`” |
| 2218 | Ta cần dân chúng! Đế quốc mà không có thần dân thì còn gì là đế quốc! |
| 2228 | Không thể đặt ước mơ của mình lên trên ước mơ người khác. Ích kỷ lắm! |
| 2235 | Hãy chụp Snack Shot của ta, rồi gọi ta bất cứ lúc nào cần lời khuyên hay giúp đỡ. |

## File bàn giao
- `SnackWorld_Trejarers_VH_CP018.zip`
- `CP018_moi_120_ID.jsonl`
- `CP018_luy_ke_2240_ID.jsonl`
- `CP018_doi_chieu.md`
- `README.md`

**Phân biệt trạng thái:** tệp JSONL đầy đủ đã được tạo trong ZIP bàn giao ở ChatGPT; **commit GitHub này chỉ có nhật ký và ví dụ, không phải bản JSONL đầy đủ**. Chưa QA in-game, Unicode glyph, line wrap/byte budget, repacker hoặc CIA. Nhánh `main` không đổi.

CP019 bắt đầu tại vị trí nguồn **2240**.
