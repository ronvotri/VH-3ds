# Snack World: Trejarers — CP024

## Tiến độ xác minh từ ZIP nguồn
- Đã xử lý **320 ID** tại vị trí ưu tiên 0-based **3080–3399**.
- **318 câu dịch tiếng Việt**, **2 placeholder Nhật** tại 3237–3238 chưa dịch.
- Lũy kế **3.400 / 23.091 ID = 14,72%** đã xử lý. Có tối thiểu 8 placeholder chưa dịch (6 từ trước và 2 mới).
- QA: **320/320 danh sách tag khớp chính xác thứ tự và nội dung**; **3.400 ID không trùng** và `id`, `raw_hex`, metadata nguồn không sửa.
- Chưa QA font tiếng Việt, byte limit, line wrap, speaker mapping đầy đủ, repacker hoặc CIA.

## Đoạn thoại
Commander Ciderfella hướng dẫn Pix-e Bay, Sam Witch và golden lamp, Pigsy, Mayonna học tấu hài từ fantail, purrate, Master of Wood, Princess Melonia tìm Xtreme Moisturizing Cream, tranh cãi Pancake syrup/honey giữa gobblin và kobolt.

## Các đoạn dịch tiêu biểu
| Vị trí nguồn | Việt hóa |
|---:|---|
| 3114 | Nó tên là “`<CG>Pix-e Bay</C>`”! Nhớ chữ “Pix-e” nhé. Quan trọng đấy! |
| 3121 | `<PV#cv002000_p04>`Đồ đầu đất! Đấy là chuyện của cậu! Ta chỉ quan tâm cậu có gan hay không! |
| 3137 | `<PV#cv003000_p03>`Không, không, sai bét! Chỉ có vần cuối là gần đúng thôi! |
| 3171 | Nếu tôi không thỉnh thoảng đáp trả thật bén, cả hội đi diễn xiếc luôn cho rồi! |
| 3279 | `<PV#cv002200_p02>`Tôi đâu chỉ là kẻ ẩn dật! Tôi còn là trùm mọt sách ẩn dật! |
| 3322 | Cậu PHẢI lấy `<CG>Xtreme Moisturizing Cream</C>` từ `<CR>Krapen</C>`! |
| 3366 | Còn kobolt chúng tôi chỉ công nhận honey! Cậu nghĩ sao?`<SEL8041/0>` |
| 3376 | Syrup hay honey cũng vậy thôi. Quan trọng là tôn trọng nhau, đúng không? |

## Dữ liệu
Bản đầy đủ được tạo tại `SnackWorld_Trejarers_VH_CP024.zip` trong cuộc trò chuyện, chứa:
- `CP024_moi_320_ID.jsonl`
- `CP024_luy_ke_3400_ID.jsonl`
- `CP024_doi_chieu.md`
- `README.md`

**Quan trọng:** GitHub commit này **chỉ lưu báo cáo và câu dịch mẫu**, chưa chứa bản JSONL đầy đủ; dữ liệu JSONL có trong ZIP. Nhánh `main` không thay đổi.

CP025 bắt đầu từ vị trí nguồn **3400**.