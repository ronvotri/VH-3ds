# Fantasy Life USA — CP007 hoàn tất · 23/11/2026

**Đạt 2.000 câu mới, tích lũy 8.500 / 34.812 (24,42%), còn 26.312** trên nhánh `vh/fantasy-life-usa`. Đây là tỷ lệ ID văn bản nguồn, không phải tỷ lệ game đã patch.

## Phân bố

- `0066–0069`: 348 câu tóm tắt nhiệm vụ.
- `0070–0071`: **0/200 ĐƯỢC DUYỆT**; dữ liệu debug/map tiếng Anh hỏng, chờ nguồn Nhật hoặc kiểm cảnh.
- `0072–0076`: 446 câu UI/thoại/nhãn kỹ thuật.
- `0077–0083`: 700 nhãn Quest/Event, giữ số event.
- `0084–0088`: 500 Challenge: Angler, Hunter, Blacksmith, Woodcutter, Tailor, Paladin.
- `0089`: 6 Challenge đầu; còn 94.
- **Tổng: 2.000 ID mới.** Không tính 200 tệp provisional.

## Bảo toàn

5.814 token `{CTRL:hex}` của các ID mới đối chiếu đúng nội dung và thứ tự. Các tên item, skill, địa danh, Life và thuật ngữ giữ tiếng Anh theo từng EN_A/EN_B. Chỉnh đúng ba chuỗi đặc biệt có `\r\n`, `\n` và markup chức năng.

## Khôi phục

`python3 unpack_batches.py` giải nén `translations/cp007-2000.jsonl.bz2.b64`, kiểm SHA-256 `52b047c193a310f7942c78b4409dab9d217c1982ea0110798c95677b0ad40cb8`, rồi gộp thành `translations/merged-CP007-8500.jsonl`.

SHA-256 bản gộp 8.500 dòng: `5e651e1cec4ec4ccd9e9bffb45fd670ed5055aff7eeafaba674830a10b16451e`.

## Handoff

Tiếp từ gói `0089` mục 007 rồi `0090`. Giải quyết 0070–0071 riêng, không tự đoán tên địa danh. Chưa vá font Việt hoặc build RomFS/CIA; vẫn cần QA game trên 3DS.
