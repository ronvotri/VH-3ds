# Pokémon Rumble Blast / Super Pokémon Rumble — EUR Rev1
## Checkpoint 012 — MSBT + LZH8 rebuild (bản thử, chưa nghiệm thu trong game)

**Chỉ bản EUR Rev1**: Title ID `0004000000066D00`, product `CTR-P-ACCP`, bảng `EU_English`. **Không phải** bản USA `0004000000066C00`.

### Kết quả thực tế

Đã viết bộ dựng MSBT từ file gốc đã giải nén + `CP011_TONG_HOP_1932.jsonl`, sau đó xuất file thay thế `*.msbt.cx` dạng **LZH8 (`0x40`)**. Không dùng cách ghi đè chuỗi vào TXT2 offset cũ: công cụ xây lại offset, section TXT2, căn hàng 16 byte và tổng kích thước MSBT. Giữ nguyên thứ tự section và byte của `LBL1`/`ATR1`.

- 16/16 file MSBT nguồn round-trip không sửa: **byte-identical**.
- 9 file MSBT có bản dịch: **MSBT parse PASS, LZH8 decompress PASS**.
- 1.932/1.932 ID tiếng Việt CP011 khớp chính xác sau build; 1.753 chuỗi khác văn bản gốc, 179 chuỗi tương đương nên không sửa.
- Mọi mã `{CTRL:hex}` được chuyển thành byte, đối chiếu đúng với bản EN; các entry không thuộc nhóm dịch vẫn giữ nguyên byte TXT2.
- Bài test cố tình xóa token hoặc dùng Unicode không NFC đều được công cụ từ chối.
- **Chưa thử tải vào game trên máy 3DS hoặc giả lập**; chưa xác minh chi tiết runtime chọn bảng `EU_English` và chưa kiểm tra tràn chữ theo pixel.

### Font: CHƯA XỬ LÝ

Bộ nguồn gốc bàn giao có báo cáo kiểm kê **16 font BCFNT** nhưng **không chứa binary font `.bcfnt` / `.bcfnt.cx`**. Audit theo 1.932 câu CP011: trong tập ký tự thực sự được sử dụng, mỗi font thiếu khoảng **62–66 glyph Unicode tiếng Việt** (bảng khảo sát tổng quát trước đó thiếu 100–108/134 ký tự thử). Điều này đồng nghĩa các file MSBT dù nén đúng có thể hiện ô vuông, trống hoặc lỗi ký tự. **Không gọi đây là bản vá Việt hóa chơi được.**

Xem `font_coverage_CP012.json`. Không chuyển toàn bộ câu thành không dấu; không thay `đ` bằng ký tự khác; không lấy font trang trí làm font game khi chưa đo baseline/width/cmap.

### Bố cục gói

- `luma/titles/0004000000066D00/romfs/msg/EU_English/*.msbt.cx`: **9 file MSBT nén đã dịch, CANDIDATE** (không có font).
- `tools/build_patch.py`: tạo lại 9 file nén từ nguồn MSBT do người dùng tự trích.
- `tools/test_build_patch.py`: kiểm cấu trúc MSBT và nén giải nén, kiểm thay đổi ngoài phạm vi.
- `QA_CP012.json`: hash và kiểm thử từng MSBT.
- `font_coverage_CP012.json`: các ký tự Unicode còn thiếu theo 16 font (dựa vào audit của bộ nguồn).

### Tạo lại (không cần CIA nếu đã có bản xuất MSBT)

```bash
python tools/build_patch.py --source-msbt-dir ./nguon_msbt/EU_English \
  --translations ./CP011_TONG_HOP_1932.jsonl --output ./out
python tools/test_build_patch.py --source-msbt-dir ./nguon_msbt/EU_English \
  --translations ./CP011_TONG_HOP_1932.jsonl --patch-root ./out
```

**Lưu ý:** Để chạy các lệnh trên cần nguồn MSBT giải nén và JSONL CP011 của chủ game; không cung cấp nguồn này trên repo public. Không cần khóa giải mã để xử lý 16 MSBT đã được xuất.

### Thử nghiệm LayeredFS (sau khi vá font)

Luma3DS hỗ trợ thay RomFS tại `sd:/luma/titles/<TitleID>/romfs/` khi bật **Enable game patching**. Đường dẫn của bản EUR Rev1 là `sd:/luma/titles/0004000000066D00/romfs/`. **Chưa xác minh game sử dụng file dịch ở runtime.** Trước khi thử, sao lưu save và kiểm tra phiên bản game, SD cũng như cài đặt ngôn ngữ; có thể tắt Game Patching/đổi tên thư mục để hoàn tác. *Không thử trên bản lưu quan trọng trước khi có font và pilot*. Tài liệu: https://github.com/LumaTeam/Luma3DS/wiki/Optional-features

### Cổng cần vượt ở CP013

1. Nhận được **16 font BCFNT nguyên gốc** từ RomFS game EUR Rev1, đối chiếu hash trong `khao_sat/font_glyph_audit.json`.
2. Phân tích cấu trúc atlas/TGLP, CWDH và CMAP; bổ sung 62–66 glyph còn thiếu trong thực tế, giữ cả glyph icon, ký hiệu giới tính, ngôn ngữ khác.
3. Repack `.bcfnt.cx` có no-change round-trip và glyph bitmap phù hợp.
4. Pilot ít nhất menu, thoại có control, mô tả Move, lời xác nhận thả Pokémon, tiếng Việt nhiều dấu và lưu/nạp trên máy/giả lập; sửa khung chữ.

Không merge vào main hoặc tuyên bố bản mod đã QA gameplay ở thời điểm CP012.