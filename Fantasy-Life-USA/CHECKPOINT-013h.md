# Fantasy Life (USA) — CP013h — Votri Valley

**26/11/2026 · 19.437/34.812 ID có bản ghi dịch (55,83%)**. CP013a–h: 937 ID mới.

## Nội dung

- 28 bản dịch mới: 17 nhãn phân loại/ngoại hình, 11 tiêu đề hướng dẫn (gói 0300–0303, 0311–0312). Một số nhãn Anh dịch thô được giải nghĩa theo những nhãn liền kề, cần xác minh giao diện 3DS. Giữ Move Silently, Life, Rank, God Mode và Woodcutter; chưa test vị trí hiển thị.
- 121 KEEP_SOURCE_NAME: 101 ID ở bảng 8690 và 20 ID ở 8710 khớp nguyên văn tên đã chốt trong bảng tiếng Anh 6796/6800/5990/5994. Khớp chuỗi không chứng minh cùng một item/nhân vật, chỉ có nghĩa không sửa nguồn.
- 4.095 HOLD: 1.916 tên item dịch thô, 986 tên tiếng Tây Ban Nha, 1.193 nhãn có dấu hiệu placeholder/unused; phân loại sơ bộ bằng metadata và mẫu chuỗi, chưa duyệt ngữ nghĩa từng ID.
- 54 ứng viên Tây Ban Nha → English (nằm trong 986 HOLD, không cộng riêng): ví dụ Sombrero de bruja → Witch's Hat; Cabeza de calabaza → Pumpkin Head. Tên ứng viên đều có trong bảng English của ZIP nguồn và có ID đối chứng. Đây chỉ là đối chiếu ngữ nghĩa, không xác nhận cùng một row. Bảng 8682/8690/8710 có cấu trúc hàng/cột khác bảng 6796/6800; không ghép theo số thứ tự và không đưa ứng viên vào bản dịch.

## Tiến độ dự kiến

Bản dịch + KEEP = 19.437 + 4.804 = 24.241 (69,63%), còn 10.571 chưa chốt. Trong ledger CP013e–h có 4.820 HOLD, còn 5.751 ID ngoài bản dịch/KEEP/HOLD của ledger này. Không phải tỷ lệ ROM đã Việt hóa. Chưa chạy kiểm tra toàn bộ bản gộp.

## QA

Batch mới 28 ID duy nhất, tồn tại trong ZIP nguồn, khác nguồn, NFC, không rỗng; số, số khoanh tròn, dấu +, biến printf, xuống dòng và token đối chiếu (0 token mới). Không trùng với các batch CP010c–CP013g khôi phục cục bộ hoặc ledger CP013e–g. Những batch cũ hơn mới đối chiếu theo phạm vi checkpoint, chưa chạy toàn bộ script khôi phục. Bốn file GitHub đã đọc lại khớp dữ liệu tải lên. Chưa test font, runtime, build ROM.

## Khôi phục

Chạy python3 unpack_batches.py; dự kiến xuất merged-CP013h-19437.jsonl và ledger tách riêng. Kiểm SHA, số lượng, trùng ID và quan hệ ứng viên/HOLD; không áp dụng ứng viên tự động.

- translations/cp013h-28.jsonl.bz2.b64 — SHA256 giải nén 6b42ba2b4df301b2d955d5073e41df85eb4395fd605f469a72c3be482de10d2e
- reviews/cp013h-keep.jsonl.bz2.b64 — 719ab70da1f510ddae80b333c6f41f1a53c54fd2580f716f3dac8cd7d06ba6c1
- reviews/cp013h-hold.jsonl.bz2.b64 — 28b2ea7bfe690efbdc9a46c7d5256268fe9c45be21bcabc9a152f8dc475d560f
- reviews/cp013h-en-candidates.jsonl.bz2.b64 — c49f2c9e1819133de96b6019310f4e11e7ddb3073e49958a7d4a6d9180f7633e

Mốc tiếp CP013i: ưu tiên 5.751 ID chưa nằm trong ledger để tìm nội dung hiển thị thực sự, phân biệt nhãn nội bộ với UI; sau đó kiểm tra và giải quyết HOLD theo bằng chứng metadata/runtime. Không sửa main.
