# Checkpoint 008 — Super Pokémon Rumble EUR Rev 1

**Nguồn:** `SuperPokemonRumble-EUR-Rev1-BoDeDich-2026-11-20.zip`, EU English, Title ID `0004000000066D00`. **Không áp dụng cho bản USA** `0004000000066C00`.

## Đã thực hiện

- Dịch **302 mục còn lại** thuộc `NoticeDesc.msbt` từ `#00094` đến `#00423` (bỏ qua chỉ số không thuộc phân loại dịch).
- [302 bản nháp tiếng Việt — JSONL](ban_dich/NoticeDesc_CP008_302.jsonl).
- Trong 302 record, **286 mục có văn bản để dịch** và **16 mục chỉ là dấu phân cách/placeholder** (`-----`, `...`, `Dummy`) được giữ nguyên để bảo toàn dữ liệu.
- Nội dung: luật Battle Royale, NPC ba thị trấn, các pháo đài, Dark Legion, Path of Heroes, World Axle, hệ Move/Type/Special Trait, bảng Power đề xuất, chỉ dẫn Co-op/Team Battle.
- Thống nhất tên riêng, Pokémon, Move/Skill, item, chế độ và thuật ngữ chính giữ **English**; lời thoại Việt hóa gần gũi, không đoán speaker ID.

## Tiến độ tích lũy

| Bảng | Đã xử lý | Tổng cần dịch |
|---|---:|---:|
| `kaiwa.msbt` | 158 | 158 |
| `main.msbt` | 726 | 726 |
| `NoticeDesc.msbt` | 376 | 376 |
| **Tổng toàn corpus** | **1.260** | **1.932** |
| **Còn lại** | **672** | |

**Đã xử lý 65,22%** (record thuộc phân loại dịch), không phải % patch đã chạy được.

## QA tĩnh

- Importer gốc `tools/nhan_ban_dich.py` nhận **1.260/1.260 bản nháp**, không sai ID, không trùng, không ghi đè mục khóa English.
- **77 token điều khiển ở 302 mục CP008 được bảo toàn chính xác**, đủ số lượng và thứ tự. Unicode NFC đạt, không có dòng vượt ngưỡng 40 ký tự sau khi bỏ mã điều khiển và tách trang.
- **22 cảnh báo thuật ngữ trong toàn bộ bản gộp**, gồm 8 cảnh báo mới CP008: `Return` được dịch như lựa chọn menu thành “Về thị trấn”; `Moves`/`Special Traits` (số nhiều) được thể hiện dưới dạng thuật ngữ chuẩn `Move`/`Special Trait`. Đây là các điểm cần rà theo ngữ cảnh, không tự sửa máy móc.
- SHA-256 file CP008 JSONL: `41cbb4481844b16ebd21390a1787663b6bcd4d24f728383cab7ae4c3a7ecf6b8`.

## Giới hạn kỹ thuật

**Chưa repack MSBT/CX, chưa vá font glyph tiếng Việt, chưa thử màn hình máy thật/giả lập, chưa build patch chơi được.** Các mục vẫn ở trạng thái `ban_nhap`, ngôi xưng ở cảnh chưa định danh cần xác minh với hình hoặc dữ liệu speaker.

## Bàn giao

ZIP `PokemonRumbleBlast_EUR_Rev1_Checkpoint008.zip` trong cuộc hội thoại gồm 302 câu mới, bản gộp 1.260 câu, 6.159 record có trường `vi`, CSV Anh–Việt, báo cáo QA, manifest nguồn và công cụ nhập thử.

**Bước CP009:** tiếp tục 672 mục thuộc các bảng còn lại, ưu tiên `PartsDesc`, `PasswordPiiDesc`, `StageDesc`, `WazaDesc`, `makuai`, `prefix` theo ID và nhóm phân loại nguồn; QA font và dựng patch là giai đoạn kỹ thuật độc lập.
