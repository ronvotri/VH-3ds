# Super Pokémon Rumble (EUR Rev1) — CP011: Biên tập văn phong và xưng hô

**Phiên bản:** EU English / Title ID `0004000000066D00`. **Không áp dụng patch cho USA** `0004000000066C00`.

Đây là **đợt biên tập** trên bản nháp CP010, không phải dịch thêm ID. Các bản CP003–CP010 được giữ nguyên để đối chiếu lịch sử.

## Kết quả

- 1.932/1.932 ID vẫn có bản nháp tiếng Việt; **57 record có điều chỉnh** về ngôi xưng, ngữ khí, tính tự nhiên hoặc độ chính xác.
- Phân bổ: `kaiwa` 22, `makuai` 10, `StageDesc` 3, `NoticeDesc` 9, `main` 4, `prefix` 2, `WazaDesc` 7.
- Những điểm ưu tiên: Pawniard vẫn `ta/ngươi` kể cả lời thoại ở `NoticeDesc #00123`; Dark Rust không dùng slang; Cobalion từ `ta/ngươi` sang `tôi/bạn` khi đổi lập trường; NPC thân thiện dùng đại từ theo cảnh, không ép cùng một công thức.
- Chỉnh nghĩa quan trọng: các mục `WazaDesc` mô tả phản sát thương **chỉ ảnh hưởng Pokémon dùng chiêu**, không mở rộng thành cả đồng đội; thông báo chìa khóa bị cong; lời xác nhận xóa dữ liệu không đùa.
- Có thêm vài câu chơi chữ nhẹ chỉ khi câu gốc có cơ sở (ví dụ `tree-mendous`). Không thêm meme vào phản diện, hướng dẫn nguy hiểm hoặc mô tả kỹ năng.

## Nội dung bàn giao

- `CP011_BIEN_TAP.jsonl`: **57 chỉnh sửa** (`id`, `vi`, `status`), dùng làm lớp override trên CP010.
- `CP011_TONG_HOP_1932.jsonl`: bản gộp **1.932 mục** đã áp dụng 57 chỉnh sửa.
- `CP011_NHAP_THU_6159.jsonl`: **6.159 record** đầy đủ metadata nguồn; các record không thuộc diện dịch giữ nguyên.
- `CP011_DOI_CHIEU.csv`: từng câu tiếng Anh + CP010 + CP011 + lý do.
- `CP011_QA.json`, `bao_cao_nhan_ban_dich.json`: xác nhận QA.
- `XUNG_HO_CP011.md`: hệ thống đại từ và lưu ý độ chắc chắn theo cảnh.
- `tools/nhan_ban_dich.py`: importer gốc chỉ nhập văn bản, **không tạo patch**.

## Kết quả kỹ thuật

Importer của bộ nguồn nhận **1.932/1.932 ID** (còn 0 thiếu), giữ nguyên 2.590 mục khóa tiếng Anh, 0 lỗi control token, không sai Unicode NFC. 57 câu biên tập có dòng dài nhất **33 ký tự hiển thị** theo phép đếm sơ bộ (không phải đo chiều rộng font).

**25 cảnh báo bộ lọc thuật ngữ** vẫn tồn tại ở bản gộp; không tự động chứng minh sai tên Move. Phải rà theo ngữ cảnh khi triển khai.

**Chưa vá font BCFNT, repack MSBT/CX, build patch hay test trên máy 3DS/giả lập.** CP011 là bản văn bản đã được biên tập có trọng điểm; những lượt nói chưa có định danh NPC vẫn cần xác minh bằng cảnh thật.