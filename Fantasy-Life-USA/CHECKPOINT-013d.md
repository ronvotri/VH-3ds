# Fantasy Life (USA) — CP013d — Votri Valley

**26/11/2026 · 19.207/34.812 ID (55,17%)**, còn 15.605. CP013a–d: 285 + 208 + 118 + 96 = 707.

| Nội dung | ID |
|---|---:|
| Phản ứng NPC (0329) | 47 |
| Thông báo UI (0329) | 28 |
| Danh xưng NPC (0161–0163) | 12 |
| Nhãn phân loại (0152) | 6 |
| Vật thể luyện tập (0327) | 3 |
| Tổng | 96 |

Dịch từ 01_CAN_DICH.jsonl trong ZIP nguồn; giữ nguyên tên item Mustard, Rainbow Apples, Plains Eels và mã điều khiển. Không gán danh tính/ngôi xưng cụ thể khi nguồn không rõ người nói; dùng ngôi trung tính theo tình huống. Hai dòng chỉ gồm tên bộ trang bị Odin và chỉ số được loại khỏi batch, không tính tiến độ.

QA batch cục bộ: 96 ID duy nhất, khớp nguồn, không rỗng, khác nguồn, NFC; 68 mã CTRL giữ nguyên nội dung và thứ tự; kiểm chữ số, dấu cộng, biến printf và xuống dòng. Không trùng các batch CP010c–CP013c hiện có cục bộ; phạm vi các batch cũ hơn đối chiếu qua báo cáo checkpoint, chưa chạy kiểm trùng toàn bộ bản gộp. Đọc lại dữ liệu GitHub khớp. Chưa xác minh speaker, font, pixel width, runtime hay build patch 3DS.

Khôi phục: `python3 unpack_batches.py`, batch `translations/cp013d-96.jsonl.bz2.b64`, SHA-256 dữ liệu giải nén `694cc80972f3449b9de24b5202fd3f4df77034fa9d4be835cd48fde10c32662a`. Script dự kiến tạo `merged-CP013d-19207.jsonl` và dừng nếu có ID trùng. Chưa chạy toàn bộ script khôi phục sau cập nhật.

Tiếp CP013e: ưu tiên kiểm các chuỗi UI/thoại còn sót; tên item, skill, nhân vật, địa danh chính giữ tiếng Anh, nhãn debug/asset chưa rõ không tự vá.