# Snack World: Trejarers — CP028 🇻🇳

## Tiến độ thực tế
- Nối từ CP027 tại **vị trí 4240**, dịch đủ **500 ID liên tiếp (4240–4739)**.
- Lũy kế: **4.740 / 23.091 ID được xử lý = 20,53%**.
- **14 placeholder chưa dịch** từ CP trước, nên có **4.726 ID đã có bản Việt** (gồm các ID có nội dung lặp).
- QA tĩnh CP028: **500/500 tag khớp nguyên bản**, không trùng ID. QA nguồn lũy kế: **4.740/4.740 id, source, raw_hex** khớp.
- Kiểm tra này chưa xác nhận chiều dài bản dịch, bố cục, font có dấu, speaker chính xác hay khả năng repack/chạy trên 3DS.

## Các cảnh đã dịch
- Huấn luyện một triệu hiệp ở Wonton Way; Coldimari và chuyện đế chế biển.
- Minestrone Mines, Krapen và cuộc săn kho báu.
- Trái tim rồng giả và nguy cơ Smörg hồi sinh.
- Sam Witch: channeling permit, jara touch, mana charge.
- Giao lưu fan của Spicy Galz; Pigsy và nhóm pluglet; Honeybun tại Metrufflis.
- Rah-rah tome; Ginja Spicy/Baklava; Madusa/Purple Eye; Curberus và lời thoại cứu đồng đội.

## Ví dụ bản dịch
| Vị trí nguồn | Bản Việt |
|---:|---|
| 4240 | Trông ta giống loại tép riu dễ bị bắt nạt lắm hả!? |
| 4250 | Ta sẽ tập một trăm hiệp! Một nghìn! Một trăm nghìn! Không, MỘT TRIỆU!!! |
| 4299 | Dùng đòn điện của kẻ địch để kích hoạt công tắc! |
| 4394 | <PV#cv001300_p0400>Đây đâu phải trái tim rồng! Là đồ giả! |
| 4427 | Nhưng phép mạnh thế này rút sạch sức bà già Sam Witch! Ta chỉ làm được <CR>mỗi ngày một lần</C> thôi. |
| 4579 | Tôi làm mất cuốn Juicy vô cùng quan trọng—<MK_OW>Khụ!<MK_CW> Ý là cuốn nhật ký vô cùng quan trọng. |
| 4688 | Phù, cuối cùng cũng tới! Nghỉ một chút lấy hơi không? |
| 4703 | <PV#cv900120_p01>Mừng cậu trở về lành lặn, <PNAME>! Còn dẫn thêm bạn tôm mới nữa nhỉ? |

## Bàn giao và GitHub
- **Đã push dữ liệu JSONL CP028 thật** (500 ID, đầy đủ metadata, trường `vi`, không chỉ báo cáo): [CP028_moi_500_ID.jsonl](./checkpoints/CP028_moi_500_ID.jsonl). Commit dữ liệu: `ab71bf5fb83123eb9ec4c311c29c237cbdeb76a9`.
- ZIP `SnackWorld_Trejarers_VH_CP028.zip` trong cuộc trò chuyện gồm: `CP028_moi_500_ID.jsonl`, `CP028_luy_ke_4740_ID.jsonl`, `CP028_doi_chieu_500_ID.md`, `README.md`, `QA_tinh_CP028.md`.
- **Bản lũy kế 4.740 ID vẫn chỉ nằm trong ZIP**; GitHub hiện có JSONL đầy đủ cho CP027 + CP028 nhưng chưa có dữ liệu đầy đủ của CP001–CP026. Không thay đổi `main`.

**CP029 bắt đầu tại vị trí nguồn 4740.**
