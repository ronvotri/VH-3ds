# Kid Icarus: Uprising — Checkpoint 058 (dịch mới + QA)

## Nguồn
- ZIP: `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`
- Dữ liệu gốc trong ZIP: `KidIcarusUprising-VietHoa/ban_dich/tieng_anh_can_dich.jsonl`
- Repository: `ronvotri/VH-3ds`; nhánh `vh/kid-icarus-uprising`

## A. 12 ID mới đã Việt hóa

Tệp: `translations/batch_058.jsonl`.

| ID trong resident/03.bin | English | Tiếng Việt |
|---|---|---|
| 01650 | Forgotten City | Thành phố bị lãng quên |
| 01651 | Cave of Spirits | Hang linh hồn |
| 01652 | Rail Temple | Đền Đường Ray |
| 01653 | Twilight Stratosphere | Tầng bình lưu chạng vạng |
| 01654 | Spiral Tower | Tháp xoắn ốc |
| 01734 | Light Fighter | Chiến binh ánh sáng |
| 01735 | Dark Fighter | Chiến binh bóng tối |
| 01736 | Fighter | Chiến binh |
| 01780 | Soul-Eating Monster | Quái vật ăn linh hồn |
| 01782 | Hades's Heart | Trái tim Hades |
| 01783 | Pseudo-Palutena | Palutena giả |
| 02110 | Labyrinth of Deceit | Mê cung lừa lọc |

Tên nhân vật, Weapon, Power, Item và thuật ngữ đặc thù khác không bị đổi. Đã đối chiếu 12 ID và tiếng Anh gốc với ZIP; đọc lại file trên GitHub sau commit: 12 ID duy nhất, đủ cặp source/vi.

## B. QA song song — hai câu đã sửa trong batch cũ

| Source ID | English | Trước | Sau | Lý do |
|---|---|---|---|---|
| `a1000.zrc#00000` | I can't believe Hades was behind the entire Underworld invasion! | Không ngờ Hades đứng sau toàn bộ cuộc xâm lược Underworld! | Không ngờ Hades đứng sau cuộc xâm lược của quân Underworld! | Là quân Underworld đi xâm lược, không phải Underworld là bên bị xâm lược. |
| `a1100.zrc#00023` | And you're Viridi, ruler of the earth and all living things. | Còn cô là Viridi, người cai quản đất đai và mọi sinh vật. | Còn cô là Viridi, người cai quản Trái Đất và muôn loài. | `the earth` là Trái Đất, không chỉ đất đai; câu gọn hơn. |

Đã cập nhật trực tiếp `translations/batch_025.jsonl` và `translations/batch_026.jsonl`, không tạo ID trùng. Đã đọc lại hai file GitHub xác nhận cả hai bản sửa, giữ nguyên 66 và 57 bản ghi.

## C. Phạm vi rà
- Đối chiếu nguyên văn 117 câu trong các nguồn `a1100` (57) và `a1200` (60) với hai batch trước; rà lại những câu dễ sai nghĩa và lỗi xưng hô.
- Rà chọn mẫu Chương 9–10, ưu tiên lời thoại Pit và Palutena, kiểm chứng `a1000#00000` trước khi sửa.
- Không đánh đồng việc đọc soát chọn mẫu với QA ngữ nghĩa PASS toàn chương.

## D. Tiến độ và giới hạn
- Checkpoint 057: **3.255/4.023** ID có bản nháp.
- Checkpoint 058: **+12 ID**, thành **3.267/4.023 = 81,2%** ID đã xử lý.
- **+2 lỗi QA sửa** không cộng vào tiến độ ID.
- Các mục chưa xử lý vẫn gồm nhiều tên Weapon, Power, Item và định danh mẫu cần giữ nguyên.
- Chưa kiểm thử font, glyph, chèn ROM, xuống dòng hoặc gameplay trên 3DS; trạng thái các bản dịch là `draft`.
