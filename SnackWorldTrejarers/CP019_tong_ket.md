# Snack World: Trejarers — CP019

## Tiến độ thực tế
- Đã dịch **240 chuỗi từ vị trí 2240–2479**, dựa trên `SnackWorldTrejarers-BoTaiLieu-VietHoa-2026-11-19.zip`.
- Lũy kế: **2.480/23.091 ID đã xử lý = 10,74%**. Hai placeholder từ CP012 vẫn chưa được dịch.
- Mục tiêu đề ra là 600 câu/đợt, nhưng **đợt này chỉ hoàn tất 240**. Không tính 360 câu còn lại.
- Đã QA tự động: **240/240 danh sách tag đúng thứ tự**, 2.480 ID duy nhất, bảo toàn `source`, `id`, `raw_hex` và metadata nguồn.
- Chưa kiểm tra speaker mapping toàn bộ, font glyph tiếng Việt, độ rộng dòng, repacker hay bản CIA.

## Cảnh đã dịch
Falgon và ultimate gear, Vinegar lừa Velouté và đánh cắp trái tim rồng, Princess Melonia, Phil A. Mignon tìm kho hàng Vinegar, Mister E bảo vệ dungeon, P-gnocchi-0 giành trái tim công chúa, Penguin Paladins.

## Mẫu dịch
| Nguồn (vị trí 0-based) | Việt hóa |
|---:|---|
| 2279 | Không được đi đường tắt! Phải tự tay lấy trang bị. |
| 2270 | `<PV#cb000210_p1000>`Ừ, rồi cậu định khuyên bọn mình hack save luôn chắc! |
| 2325 | `<PV#cv000500_p03>`Trong lúc lũ ngốc các ngươi bận đánh Dullardhan chứ còn gì. |
| 2328 | `<PV#cv001300_p1700>`Khốn kiếp, hắn lừa ta rồi!`<SEL9601/0>` |
| 2431 | Ta không thể đứng nhìn ngươi và đồng loại từng bước tàn phá nó! |
| 2479 | Penguin Paladins, hãy tự giới thiệu với bệ hạ đi! |

## File bàn giao
Trong cuộc trò chuyện đã tạo `SnackWorld_Trejarers_VH_CP019.zip`, chứa:
- `CP019_moi_240_ID.jsonl` — **244.760 byte**
- `CP019_luy_ke_2480_ID.jsonl` — **2.560.331 byte**
- `CP019_doi_chieu.md`
- `README.md`

**Lưu ý minh bạch:** Commit GitHub này chỉ lưu nhật ký và bản dịch mẫu; JSONL đầy đủ hiện có trong ZIP đính kèm, **chưa được đẩy lên repo**. Không thay đổi nhánh `main`.

CP020 bắt đầu tại vị trí **2480**.