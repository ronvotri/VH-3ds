# Super Pokémon Rumble — EUR Rev 1 (Việt hóa)

**Chỉ dành cho EU English EUR Rev 1**, Title ID `0004000000066D00`, product `CTR-P-ACCP`. Không nhập bản dịch vào ROM USA `0004000000066C00`.

## Tiến độ đến Checkpoint 012 — đã dựng bản thử MSBT/LZH8

- Nguồn: **6.159 record từ 16 bảng MSBT**.
- 1.932 record được phân loại cần dịch, 2.590 khóa EN, 443 debug, 1.194 rỗng.
- **1.932/1.932 bản nháp (100% số ID cần dịch)** đã đối chiếu ID / nhập thử; **không còn ID thuộc nhóm `translate` bị bỏ trống**.
- 9 bảng đã hoàn tất bản nháp, gồm `WazaDesc` (387/387): `kaiwa` (158/158), `main` (726/726), `NoticeDesc` (376/376), `PartsDesc` (20/20), `PasswordPiiDesc` (25/25), `StageDesc` (35/35), `prefix` (86/86), `makuai` (119/119).

| Checkpoint | Nội dung | JSONL | Báo cáo |
|---|---|---|---|
| 003 | 158 `kaiwa` | [Xem](ban_dich/kaiwa_CP003_158.jsonl) | [CP003](CHECKPOINT-003.md) |
| 004 | 200 `main` | [Xem](ban_dich/main_CP004_200.jsonl) | [CP004](CHECKPOINT-004.md) |
| 005 | 200 `main` | [Xem](ban_dich/main_CP005_200.jsonl) | [CP005](CHECKPOINT-005.md) |
| 006 | 200 `main` | [Xem](ban_dich/main_CP006_200.jsonl) | [CP006](CHECKPOINT-006.md) |
| 007 | 126 `main` + 74 `NoticeDesc` | [main](ban_dich/main_CP007_126.jsonl), [NoticeDesc](ban_dich/NoticeDesc_CP007_74.jsonl) | [CP007](CHECKPOINT-007.md) |
| 008 | 302 `NoticeDesc` | [Xem](ban_dich/NoticeDesc_CP008_302.jsonl) | [CP008](CHECKPOINT-008.md) |
| **009** | **285 mục / 5 bảng** | [PartsDesc](ban_dich/CP009_PartsDesc_20.jsonl) · [PasswordPiiDesc](ban_dich/CP009_PasswordPiiDesc_25.jsonl) · [StageDesc](ban_dich/CP009_StageDesc_35.jsonl) · [prefix](ban_dich/CP009_prefix_86.jsonl) · [makuai](ban_dich/CP009_makuai_119.jsonl) | [CP009](CHECKPOINT-009.md) |
| **010** | **387 mục cuối, `WazaDesc`** | [JSONL](ban_dich/WazaDesc_CP010_387.jsonl) | [CP010](CHECKPOINT-010.md), [QA](qa/QA_CP010.json), [134 mẫu](qa/Waza_CP010_134_templates.tsv) |

## Checkpoint 011 — Biên tập chất lượng lời thoại

- **57 mục đã chỉnh sửa** sau khi đối chiếu tiếng Anh với các bản CP003–CP010; **không tạo ID mới**, tổng vẫn **1.932/1.932 mục có bản nháp**.
- **[Bản gộp 1.932 mục đã biên tập](ban_dich/CP011_TONG_HOP_1932.jsonl)** (ưu tiên sử dụng bản này thay vì gộp trực tiếp CP010).
- [57 chỉnh sửa dưới dạng override](ban_dich/CP011_BIEN_TAP_57.jsonl), [bảng so sánh EN / CP010 / CP011](qa/CP011_DOI_CHIEU.csv), [báo cáo CP011](CHECKPOINT-011.md), [quy chuẩn xưng hô CP011](XUNG_HO_CP011.md), [QA máy](qa/CP011_QA.json).
- Đã nhập thử lại: **1.932 ID hợp lệ**, 0 thiếu, không đổi token, không lỗi Unicode. **25 cảnh báo thuật ngữ cũ** vẫn cần xem trong ngữ cảnh; 57 mục mới chỉ là vòng biên tập chọn lọc, **chưa nghiệm thu toàn bộ nội dung trên 3DS**.
- Chỉnh giọng Pawniard `ta/ngươi`, Dark Rust trang trọng đe dọa, Cobalion chuyển cách nói theo diễn biến; sửa một số lỗi nghĩa Move và câu xác nhận xóa dữ liệu.

**CP011 đã hoàn tất biên tập bản nháp. CP012 đã thử đóng gói MSBT/CX, nhưng chưa có font hoặc kiểm thử trong game.**


## Checkpoint 012 — Bộ đóng gói MSBT/LZH8

- [Báo cáo Checkpoint 012](CHECKPOINT-012.md) · [Bộ dựng nguồn MSBT](tools/build_patch.py) · [Kiểm thử](tools/test_build_patch.py) · [QA 16 MSBT/9 file nén](qa/QA_CP012.json) · [Kiểm kê glyph còn thiếu](qa/font_coverage_CP012.json).
- Dựng lại **16/16 MSBT không đổi byte**, và tạo **9 file `.msbt.cx` có bản dịch CP011**, giải nén LZH8 round-trip đạt. 1.932/1.932 ID trùng bản dịch, **1.753 nội dung khác bản gốc**, 179 record vốn không cần sửa.
- Giữ byte của `LBL1`/`ATR1`, entry không dịch và thứ tự mã `{CTRL:hex}`. Không có font BCFNT nguồn trong bộ ZIP nên **chưa sửa font**. Trong 1.932 câu CP011, kiểm kê cho thấy font gốc thiếu **62–66 glyph đang được sử dụng** tùy font.
- **Đây là bản thử kỹ thuật, không phải patch được xác nhận chơi được**. Chưa thử trong game, chưa xác minh ngôn ngữ runtime, chưa kiểm tràn chữ. Không merge vào `main`.

## Quy tắc

Giữ nguyên English đối với tên Pokémon, item, Move/Skill, tên riêng và thuật ngữ chính; Việt hóa lời thoại, menu, hướng dẫn và thông báo theo tiếng Việt NFC, Gen Z vừa phải và **xưng hô đúng từng cảnh**. Mỗi record giữ nguyên ID, placeholder, `{CTRL:hex}`. [Sơ đồ ngôi xưng `kaiwa`](XUNG-HO-KAIWA.md).

## QA và giới hạn

- Công cụ nhập gốc nhận **1.932/1.932 bản nháp**, còn 0 ID cần dịch; 2.590 record khóa EN được bảo toàn. CP010 giữ **9/9 mã điều khiển** và không có cảnh báo thuật ngữ mới.
- 25 cảnh báo từ điển tích lũy từ CP003–009 cần kiểm tra trong cảnh; CP010 không phát sinh cảnh báo mới (0).
- **Đã hoàn tất bản nháp 1.932 ID, có 9 file MSBT/CX thử nghiệm. Chưa sửa font, chưa test trên máy thật/giả lập, chưa có patch được xác nhận chơi được.** Đếm ký tự trên mỗi dòng chỉ là QA sơ bộ, không đo độ rộng pixel của font 3DS.

**Bước kế tiếp:** nhận bộ 16 font BCFNT từ nguồn EUR Rev1, thêm glyph (hiện thiếu 62–66 ký tự có sử dụng trong CP011, hoặc 100–108 khi hỗ trợ trọn bộ 134 ký tự), nén lại BCFNT/CX và test trên 3DS/giả lập với save backup.
