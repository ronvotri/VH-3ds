# Fantasy Life (USA) — CP014n — Votri Valley

26/11/2026 — 264 ID chuyển khỏi HOLD, toàn bộ là chuẩn hóa tên tiếng Anh, không phải câu dịch tiếng Việt mới.

- 249 bản ghi tên quái: 201 nhãn tiếng Anh dịch thô ở 6943–8050 và 48 nhãn tiếng Tây Ban Nha ở 8710. Đối chiếu tên Bounty trong 6796 EN_A và tên NPC/quái xuất hiện trong 5990. Ánh xạ chọn lọc theo nghĩa, nhóm tên và chính tả; áp dụng cho các nhãn lặp khớp nguyên văn. Không khẳng định các tên Bounty và tên hiển thị của quái luôn giống nhau.
- 12 bản ghi tên NPC (Dragon kill → Dragonslayer, Erumi → Elmie) ở 5999; 3 tên nguyên liệu từ 8690, đối chiếu 6796 EN_A.
- Loại 42 ứng viên khỏi bản dự thảo, gồm Dark Gigant (có cả Dark Giant và Dark Gigante), Apple Uncle, Heihofu, Gustav. Các mục đó vẫn HOLD. Không tự suy diễn biến thể chất lượng +.
- Bảng name-evidence-CP014n.csv trong ZIP ghi ID, archive, hàng nguồn và đích.

## Tiến độ
21.925 bản ghi thay thế; 8.550 KEEP; 4.337 HOLD (3.881 tên chờ xác minh + 456 HOLD khác). Tổng 30.475/34.812 ID có quyết định. Tỷ lệ bản ghi thay thế không phải tỷ lệ câu tiếng Việt hoặc tỷ lệ ROM Việt hóa.

## QA
264 ID duy nhất thuộc hàng đợi tên ở CP014m, source khớp 01_CAN_DICH.jsonl. Kiểm NFC, CTRL, số, dấu + và xuống dòng, ZIP đạt kiểm toàn vẹn. Tệp GitHub đọc lại khớp. Ánh xạ ngữ nghĩa/chính tả chưa chứng minh bằng khóa thực thể hoặc runtime, cần QA tên trong game. Chưa chạy toàn bộ unpack_batches.py, chưa phục hồi đủ 13.665 bản ghi cũ, chưa kiểm font/runtime 3DS.

## Khôi phục
reviews/cp014n-resolutions.jsonl.bz2.b64 — SHA256 giải nén 7df345b0f31ab33f532adb635337ef2efe3cdd2054e9daf5cb9e6583bc218c67.
unpack_batches.py đã bổ sung CP014n, dự kiến xuất merged-CP014n-21925.jsonl, remaining-HOLD-CP014n-4337.jsonl và hai hàng đợi con. Không sửa main.

Tiếp CP014o: ưu tiên các nhóm NPC lặp và tên nguyên liệu/trang bị có bằng chứng; kiểm bản gộp trước bàn giao.
