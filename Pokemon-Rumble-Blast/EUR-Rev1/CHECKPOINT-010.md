# Pokémon Rumble Blast / Super Pokémon Rumble — Checkpoint 010 🇻🇳

**Game/region:** EUR Rev 1, `EU_English`, Title ID `0004000000066D00` (product `CTR-P-ACCP`). KHÔNG áp dụng cho bản USA `0004000000066C00`.

## Kết quả dịch văn bản

- **387/387 record `WazaDesc.msbt`** thuộc nhóm cần dịch: đã chuyển ngữ toàn bộ mô tả Move.
- Từ 387 record có **134 mẫu mô tả tiếng Anh độc nhất**. Các câu trùng lặp dùng đúng cùng một bản dịch tiếng Việt.
- Tổng tiến độ bản nháp: **1.932/1.932 mục được phân loại cần dịch (100% số ID)**. Bốn nhóm khác: 2.590 giữ EN, 443 debug, 1.194 trống. Tổng corpus 6.159 record.
- Bản dịch giữ nguyên tên Pokémon, tên Move/item, Attack/Defense/Speed/Power/Hit Ratio/HP, tên hệ và các thuật ngữ chính; dịch mô tả sát nghĩa, dễ hiểu; không nhồi tiếng lóng vào thông số gameplay.

## QA

- Công cụ `tools/nhan_ban_dich.py` đi kèm bộ nguồn đã nhập thử **1.932/1.932 ID** vào corpus (không sửa 2.590 ID khóa tiếng Anh).
- CP010: **9/9 mã `{CTRL:hex}`** giữ nguyên thứ tự và giá trị, không trùng ID, **0 vi phạm NFC**, 0 dòng trên 40 ký tự ở văn bản kiểm tra sơ bộ, 0 cảnh báo thiếu thuật ngữ được bảo vệ mới.
- Trong toàn bộ 1.932 ID có **25 cảnh báo từ điển tích lũy từ các đợt trước** (như `Move` dùng theo nghĩa động từ hoặc `Moves/Special Traits` ở dạng số nhiều); cần duyệt tay, chưa phải 25 lỗi đã xác nhận.
- Không có câu mô tả Move để nguyên nguyên văn tiếng Anh trong nhóm cần dịch.
- QA chưa đo độ rộng chữ theo pixel, số hàng tối đa từng textbox hoặc font rendering thực tế.

## Vấn đề kỹ thuật để có bản vá game thật

Bộ nguồn có **16 font BCFNT** ở `/font/…`, theo `khao_sat/font_glyph_audit.json` **mỗi font còn thiếu 100–108 ký tự** trong bộ glyph tiếng Việt yêu cầu. Chưa hề tích hợp glyph/độ rộng chữ vào BCFNT và chưa thử runtime. Việc có text nháp không có nghĩa 3DS sẽ hiển thị tiếng Việt có dấu.

Các bước kỹ thuật tiếp theo: thêm dấu/glyph cho BCFNT, sửa CMAP/CWDH/TGLP tương ứng; thử đọc–ghi MSBT bảo toàn label/section/offset, tái nén CX, tạo bản patch chỉ gồm tài nguyên dịch, thử trên máy/giả lập với đúng EU Rev 1, kiểm tra thoại, menu và Move Description bị tràn.

## Nội dung ZIP

- `ban_tra_ve/WazaDesc_CP010_387.jsonl`: bản nháp mới chính thức để import.
- `ban_tra_ve/CP003_CP010_1932.jsonl`: toàn bộ ID cần dịch và bản dịch tích lũy.
- `ban_dich_da_nhap.jsonl`: bản gộp 6.159 ID, giữ nguyên nguồn và metadata.
- `ban_dich/00_TOAN_BO_EN.jsonl`: bản nguồn để dùng lại importer.
- `tools/nhan_ban_dich.py`: công cụ kiểm tra/nhập văn bản từ nguồn đã cung cấp (KHÔNG repack game).
- `doi_chieu/DOI_CHIEU_WAZA_CP010.csv`: đối chiếu 387 mục.
- `doi_chieu/Waza_CP010_134_templates.tsv`: 134 mô tả duy nhất EN–VI.
- `bao_cao/QA_CP010.json`: báo cáo kiểm tra.
- `nguon/source_manifest.json`: manifest xác nhận phiên bản và SHA nguồn.

**Chốt phạm vi:** 100% bản nháp văn bản được phân loại cần dịch, **chưa có patch playable**, chưa bổ sung font, chưa thử trên 3DS/giả lập; ngôi xưng và bố cục của các đợt trước cần vòng QA hình ảnh riêng.