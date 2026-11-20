# Checkpoint 002 — Đối chiếu ZIP gốc (20/11/2026)

## Bằng chứng nguồn
Tệp: `PokemonRumbleBlast-BoTaiLieu-VietHoa-2026-11-19.zip`.
Đọc trực tiếp các tài liệu `tai_lieu/01_KHAO_SAT_NGUON.md`, `04_QUY_CHUAN_VA_THUAT_NGU.md`, `08_VIEC_CAN_XAC_MINH.md` và `khao_sat/cia_survey.json`.

- Game: Pokémon Rumble Blast (USA), product `CTR-P-ACCE`, Title ID `0004000000066C00`.
- CIA khảo sát dài 323.668.416 byte, SHA-256 `5fc2647105d96a6e5370eace504501d8a482d8d38d266c0b994ba871feb2ffd9`.
- `ncch_no_crypto=false`; phần RomFS/ExeFS trong CIA khảo sát **chưa đọc được plaintext**. Không thể trích câu từ header CIA.
- Trong ZIP hiện có `bieu_mau/chuoi_dich.jsonl` **0 byte** và chưa có RomFS/ExeFS giải mã.
- Số câu nguồn trích: 0. **Tổng số câu của game: chưa biết** (không được ghi 0/0 hay % hoàn thành).

## Quyết định chính thức của chủ dự án, ưu tiên hơn đề xuất trong ZIP
Giữ nguyên tên Pokémon, item, skill/move, thuật ngữ chính và tên riêng bằng English. Dịch các nội dung còn lại sang tiếng Việt có dấu; văn phong gần gũi, hài hước Gen Z vừa phải. Hệ thống xưng hô dựa speaker/scene/relationship, không tự suy luận.

**Lưu ý xung đột nguồn:** `04_QUY_CHUAN_VA_THUAT_NGU.md` đề xuất dịch tên Move, World Axle, Battle Royale, Glowdrops... Nhưng đó chỉ là **nháp** và *không khớp* yêu cầu trực tiếp của chủ dự án: mặc định phải giữ EN cho những thuật ngữ chính này. Chỉ sửa ngoại lệ khi chủ dự án duyệt dựa trên câu gốc và ảnh UI.

## Cổng kỹ thuật để bắt đầu dịch
| Mã | Điều kiện | Trạng thái |
|---|---|---|
| T01 | RomFS/ExeFS giải mã hợp lệ với cây file đọc được | Chờ nguồn |
| T02 | So Title ID, revision, SHA-256, update | Chưa đủ |
| T03 | Xác định archive/nén bằng magic & round-trip | Chờ T01 |
| T04 | Trích chuỗi có ID, encoding, pointer/control | Chờ T01 |
| T05–T06 | Kiểm font, renderer và glyph tiếng Việt NFC | Chờ T01 |
| T07 | Importer, rebuild no-change & QA trên bản sao | Chờ T03–T06 |
| T08/T19 | Pilot tutorial/menu và các xác nhận mất item/Move/Pokémon | Chờ corpus |

## Danh mục cần rà khi có dump
Menu và tutorial; 5 chương và postgame; Pokémon/form/trait; Move và mô tả; world map, World Rank; Battle Royale/Team Battle/Charge Battle; đổi/học/quên Move; Release và quà chia tay; Local Play, StreetPass, Play Coins, Password; text nằm trong texture; UI xác nhận thao tác có hậu quả.

## Xưng hô / duyệt câu
Mỗi record phải giữ: `string_id`, `source_path`, `source_en`, `speaker_id` (mặc định `unknown`), `scene`, `addressee`, `relationship_phase`, `vi`, `status`, `notes`.
Chuỗi mẫu viết ra để minh họa **không phải** lời thoại thật; không tính vào tiến độ.

## Trạng thái bàn giao
Hoàn thành đối chiếu tài liệu; chưa có văn bản nguồn nào để Việt hóa; chưa có patch, chưa thử game. Tiếp tục ngay khi nhận được bản xuất tài nguyên đã giải mã từ game thuộc quyền sở hữu người dùng.
