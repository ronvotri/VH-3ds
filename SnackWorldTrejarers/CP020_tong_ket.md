# Snack World: Trejarers — Checkpoint 020

**Kết quả thực tế**: Đã dịch 180 ID tại vị trí 0-based **2480–2659** từ `ban_dich/de_dich_uu_tien_update.jsonl` trong ZIP nguồn. CP019 có 2.480 ID → CP020 có **2.660/23.091 ID (11,52%)** đã xử lý; còn hai placeholder CP012 chưa dịch.

## Nhóm nội dung
- Penguin Paladins và Sultan: thỏa thuận bỏ qua vụ chiếm đền.
- Princess Melonia và quà lưu niệm Metrufflis.
- Commander Ciderfella và đội quân từng do Commander chỉ huy.
- Falgon nhận thấy Smörg có khả năng hồi sinh; Al-Dante's Alcazar.
- Princess Melonia bị bắt cóc, Chup bị tình nghi; Permit hạng A.
- Rockerfella, nhóm death metal và Snack Shot; màn chọn tên Ace.

## Ví dụ dịch
| Vị trí nguồn | Bản Việt |
|---:|---|
| 2480 | Rõ rồi! Mong bệ hạ nhớ dai nhé. Tôi là Penguin Paladin A! |
| 2485 | Michael!`<SEL8011/0>` |
| 2511 | `<PV#cv000200_p00>`Điều quan trọng bây giờ không phải `<CG>quá khứ</C>`, mà là `<CR>tương lai</C>` phía trước. |
| 2538 | `<PV#cv001300_p1700>`...không còn chút dấu vết nào của `<CR>Smörg</C>`! `<MK_OW>`Đùng, đùng, `<EBI>ĐOÀNG!</E><MK_CW><SEL9302/0>` |
| 2568 | `<CR>Chup</C>!<SEL9202/0>` |
| 2583 | `<PV#cb000210_p0400>`Ồ, Permit hạng A á? Đỉnh thật! |
| 2617 | Bọn tôi muốn anh làm giọng ca chính cho ban nhạc! |
| 2653 | Vậy quyết đi, `<PNAME>`! Trong ba cái tên ấy, tên nào hợp với cậu bé nhất?`<SEL8011/0>` |

## Kiểm tra
- **180/180** ID bảo toàn tag nguồn theo nội dung và thứ tự.
- **2.660 ID duy nhất**, metadata nguồn được bảo toàn trong bản lũy kế JSONL.
- Chưa kiểm thử font Unicode/3DS, byte budget, line wrap, speaker, repacker hoặc CIA.

**Bàn giao**: `SnackWorld_Trejarers_VH_CP020.zip` trong cuộc trò chuyện chứa bản dịch 180 ID, JSONL lũy kế 2.660 ID, bảng đối chiếu 180 câu và README.

**Lưu ý**: Commit GitHub này chỉ lưu báo cáo và ví dụ, **không phải** đồng bộ JSONL đầy đủ. Không thay đổi `main`. CP021 bắt đầu từ vị trí **2660**.