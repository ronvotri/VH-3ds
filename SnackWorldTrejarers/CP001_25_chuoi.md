# Snack World: Trejarers — Việt hóa CP001

Nguồn: `SnackWorldTrejarers-BoTaiLieu-VietHoa-2026-11-19.zip` → `ban_dich/cau_goc_base_update.jsonl`

File nguồn: `data/txt/ja/gamedata/map/m102g01/m102g01_npc_base_text_c01_0.00.00.cfg.bin` (base)

25 bản dịch pilot, ánh xạ bằng `source_kind=base`, `file`, `index` (0–24). **Chờ QA ngữ cảnh, chưa nhập runtime.** Trong cột VI, `\n` là ký tự escape literal phải bảo toàn khi nhập. Tên riêng bản EN cần kiểm chứng khi QA.

| Index | VI |
|---:|---|
| 0 | Anh yêu em! Honey ơi!! |
| 1 | Em cũng yêu anh, Darling!! |
| 2 | Ngày nào ta cũng ra ngắm tàu. Thành thói quen mất rồi! |
| 3 | Tòa tháp lớn phía trước chính là Vinegar Palace đấy! |
| 4 | Con bé ấy cứ rời mắt một chút là chạy biến đi đâu mất! |
| 5 | Không biết nó lại chạy đi ngắm tàu rồi à? |
| 6 | Tớ mê ngắm tàu hỏa lắm luôn! |
| 7 | Gâu! Gâu! |
| 8 | (Đang được dắt đi dạo nè!) |
| 9 | Meo~ |
| 10 | (Gãi cằm cho tui đi mà~) |
| 11 | Nghe đồn quanh đây có chỗ khai thác được dầu mỏ đấy! |
| 12 | Nhưng mà... mới chỉ là lời đồn thôi nhé~ |
| 13 | Nếu là thật, ta lại càng giàu nứt vách rồi! |
| 14 | Gwahahaha~! |
| 15 | Tôi đang đợi mấy đứa con gái...\nMà chẳng thấy đứa nào đến cả! |
| 16 | Hay mình nhớ nhầm chỗ hẹn ta? |
| 17 | Bố đâu rồi nhỉ? |
| 18 | Không biết bố đang làm gì nữa? |
| 19 | Ngày nghỉ tôi thường đến đây thư giãn cho thong thả. |
| 20 | Đi dạo thấy đầu óc nhẹ tênh, dễ chịu cực kỳ! |
| 21 | Nghỉ chân tí đã.\nLàm quần quật mãi cũng đuối chứ! |
| 22 | Lần này ta chọn nhà trọ quanh đây nhé. |
| 23 | Ồ~ Đứng gần ngắm tàu chạy mới thấy đã mắt thật!! |
| 24 | Đến Yotsukoshi Department Store là gần như mua được đủ thứ đấy! |

## Quy tắc
- Giữ tên người/địa danh/Item/Skill/Jara/Snack và thuật ngữ nhận diện bằng tiếng Anh.
- Việt hóa hội thoại, mô tả, menu; Gen Z nhẹ, không tự thêm thông tin cốt truyện.
- Chưa mapping người nói: `speaker=unknown`, chưa cố định vai vế.
- Giữ nguyên ID/hash/source/tags/reference trong bản JSONL gốc khi tích hợp; checkpoint đầy đủ JSONL lưu trong gói bàn giao CP001.
- Chưa QA font tiếng Việt, repacker, hoặc build chơi được.
