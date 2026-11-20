# Super Pokémon Rumble / Pokémon Rumble Blast — Checkpoint 009

**Bản nguồn:** EUR Rev 1, EU_English, Title ID `0004000000066D00`, product code `CTR-P-ACCP`. **KHÔNG** dùng để vá bản USA `0004000000066C00`.

## Kết quả đợt này

Đã hoàn tất bản nháp 285 record từ 5 bảng MSBT:

- `PartsDesc`: 20/20, Cool Key, Team Catapult, Charge Flag, Windup Energy Magnet, Hero's Key, v.v.
- `PasswordPiiDesc`: 25/25, tên Pokémon, Special Trait và vùng xuất hiện qua Password.
- `StageDesc`: 35/35, lời thoại đối thủ trong chiến đấu, bảo toàn phép xưng hô `ta/ngươi` theo cảnh.
- `prefix`: 86/86, mô tả Special Trait; giữ Move/Status Change, tên Type và control code.
- `makuai`: 119/119, mở đầu, chuyển cảnh và kết truyện Cobalion/Dark Rust; ngôi xưng là bản nháp, chờ QA trên hình.

**Tích lũy 1.545/1.932 record (79,97%)**. Còn 387 record ở `WazaDesc.msbt`. 2.590 record khóa tiếng Anh không sửa, 443 debug và 1.194 rỗng giữ nguyên.

## QA

- So ID trực tiếp với corpus 1.932 mục trích từ EUR Rev1, không tự sinh ID.
- 285/285 ID hợp lệ; không trùng CP003–CP008; 28/28 mã `{CTRL:hex}` đúng thứ tự, không tràn 40 ký tự/dòng theo phép đo thô; Unicode NFC đạt.
- Công cụ gốc `nhan_ban_dich.py` đã nhập lại bản tổng 1.545 mục và xuất 6.159 record, `remaining = 387`.
- 3 cảnh báo từ điển mới đều do khớp từ máy: `Moves` dùng nghĩa **di chuyển** ở `prefix #00094`, số nhiều của Move ở `prefix #00106`, và `Special Traits` số nhiều được ghi theo thuật ngữ chuẩn `Special Trait` ở `prefix #00145`. Không tự thay lời dịch khi không có ngữ cảnh.
- Tổng cảnh báo máy tích lũy: 25, cần rà UI/ngữ cảnh trước nghiệm thu.

## Nội dung gói

- `ban_tra_ve/CP009_*.jsonl`: 5 file bản nháp mới, tổng 285 record.
- `ban_tra_ve/CP003_CP009_1545.jsonl`: gộp toàn bộ phần đã dịch.
- `ban_dich_da_nhap.jsonl`: 6.159 record theo bộ gốc có cập nhật trường `vi`.
- `doi_chieu_CP009.csv`: đối chiếu EN–VI và ID/label; `bao_cao/CP009_QA.json`: số liệu kiểm thử.
- `tools/nhan_ban_dich.py` + `nguon/source_manifest.json` hỗ trợ kiểm tra khả năng nhập lại.

**Không phải patch để chơi.** Chưa repack MSBT/CX, chưa thêm glyph font Việt, chưa test chữ hay gameplay trên 3DS/giả lập.

**Đợt 010:** dịch 387 mục `WazaDesc.msbt` còn lại theo ID gốc, chú ý phân biệt hiệu ứng và tên Move/Skill tiếng Anh.