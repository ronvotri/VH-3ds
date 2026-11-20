# Super Pokémon Rumble — EUR Rev 1 (Việt hóa)

**Chỉ dành cho bản EUR Rev 1**, Title ID `0004000000066D00`, product `CTR-P-ACCP`, bảng `EU_English`. Không sử dụng dữ liệu dịch này cho ROM USA `0004000000066C00`.

## Tiến độ Checkpoint 007

- Corpus nguồn: **6.159 record / 16 bảng MSBT**.
- Trong đó **1.932 mục cần dịch**, 2.590 mục giữ EN, 443 debug, 1.194 rỗng.
- Đã xử lý **958/1.932 mục (49,59%)**; còn **974 mục**.
- `kaiwa.msbt`: **158/158** mục.
- `main.msbt`: **726/726** mục, hoàn tất nội dung được phân loại dịch.
- `NoticeDesc.msbt`: **74/376** mục.

| Checkpoint | Nội dung | File dịch | Báo cáo |
|---|---|---|---|
| CP003 | 158 mục `kaiwa` | [JSONL](ban_dich/kaiwa_CP003_158.jsonl) | [003](CHECKPOINT-003.md) |
| CP004 | 200 mục đầu `main` | [JSONL](ban_dich/main_CP004_200.jsonl) | [004](CHECKPOINT-004.md) |
| CP005 | 200 mục `main` tiếp theo | [JSONL](ban_dich/main_CP005_200.jsonl) | [005](CHECKPOINT-005.md) |
| CP006 | 200 mục `main` tiếp theo | [JSONL](ban_dich/main_CP006_200.jsonl) | [006](CHECKPOINT-006.md) |
| CP007 | 126 mục còn lại của `main` | [JSONL](ban_dich/main_CP007_126.jsonl) | [007](CHECKPOINT-007.md) |
| CP007 | 74 mục đầu `NoticeDesc` | [JSONL](ban_dich/NoticeDesc_CP007_74.jsonl) | [007](CHECKPOINT-007.md) |

[Xem bảng ngôi xưng `kaiwa`](XUNG-HO-KAIWA.md).

## Chuẩn dịch và QA

- Giữ tên Pokémon, item, Move/Skill, địa danh và thuật ngữ/chế độ chính bằng EN.
- Dịch thoại và UI tiếng Việt NFC, Gen Z tiết chế, không tự gán người nói.
- Giữ nguyên ID, token `{CTRL:hex}`, nội dung bản quyền và giá trị biến.
- Tất cả 958 mục đã được nhập thử bằng `tools/nhan_ban_dich.py` trong nguồn bàn giao; CP007 giữ **87/87 mã điều khiển**, không lỗi ID. Có 1 cảnh báo va chạm từ điển mới (chữ Move là động từ trong câu hướng dẫn).
- Các bản dịch vẫn là `ban_nhap`, chưa duyệt hiển thị thực tế.

**Chưa repack MSBT/CX, chưa thêm glyph font Việt, chưa build patch, chưa test trên 3DS/giả lập.**

**Bước kế tiếp:** tiếp tục `NoticeDesc.msbt` sau ID `#00093`, đối chiếu ngôi xưng và QA font/khung chữ.
