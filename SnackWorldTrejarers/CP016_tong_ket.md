# Snack World: Trejarers — CP016

## Phạm vi
- Đã dịch vị trí **1920–1999** (80 ID).
- Lũy kế **2.000/23.091 ID = 8,66%** theo số ID đã xử lý (gồm 2 placeholder chưa dịch từ CP012).
- **80/80 tag được bảo toàn**, **2.000 ID duy nhất** trong JSONL lũy kế.
- Các cảnh: pocket snacks, Commander Ciderfella, Warrior Kung Pao, Princess Melonia.
- Nguồn `ban_dich/de_dich_uu_tien_update.jsonl` trong `SnackWorldTrejarers-BoTaiLieu-VietHoa-2026-11-19.zip`.

## Trích dịch thực tế

| Thứ tự nguồn | Bản Việt hóa |
|---:|---|
| 1920 | Ngoài ra, cậu có thể xếp họ vào nhóm `<CR>pocket snacks</C>`. |
| 1921 | Cậu có thể triệu hồi pocket snacks giữa nhiệm vụ, nhưng chỉ được một lúc thôi. |
| 1923 | Buổi huấn luyện tiếp theo, cậu sẽ chiến đấu cùng một snack! |
| 1929 | `<PV#cb000310_p1100>`Cậu biết Chup mà. Cậu ta mê cô ấy như điếu đổ! |
| 1930 | `<PV#cb000110_p2500>`Bearny! Không có chuyện đó nhé! |
| 1931 | `<PV#cv002000_p02><EBI>CÁC BINH NHÌ!</E>` |
| 1932 | `<PV#cb000110_p0600>`Commander Ciderfella! Sao ngài lại ở đây ạ? Thưa ông... à không, thưa bà! |
| 1943 | `<GZ><PV#cv002000_a00_P><EBI>ĐẦU ĐẤT HẾT CẢ LŨ!</E>` |
| 1962 | Cậu làm được rồi! Đã đánh bại Euriley! |
| 1970 | Chào nhé! Tôi là Warrior Kung Pao. |
| 1982 | Là kình địch thì phải nói: “Nhắm mắt tôi cũng làm được!” chứ! |
| 1997 | `<PV#cv000200_p00>`Nhưng biết đâu vậy mới chứng tỏ công dụng cực mạnh! |

## Ghi chú QA
- ID 1951 có tag nguồn bất thường `<\\nPG>` (ký tự backslash-n bên trong tag), đã **giữ y nguyên** và cần xác minh engine.
- Dịch đang ở trạng thái **chờ QA** (font/glyph, byte limit, wrap, speaker chính xác, repacker, CIA).
- **ZIP chứa dữ liệu đầy đủ**: `SnackWorld_Trejarers_VH_CP016.zip`, bao gồm `CP016_moi_80_ID.jsonl`, `CP016_luy_ke_2000_ID.jsonl`, bảng đối chiếu và README.
- GitHub hiện lưu báo cáo/mẫu dịch ở commit này, chưa đẩy JSONL đủ 2.000 ID lên repo. Nhánh `main` không thay đổi.
- CP017 bắt đầu từ vị trí nguồn **2000**.
