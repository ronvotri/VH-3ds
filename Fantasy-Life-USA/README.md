# Fantasy Life (USA) — CP014d — Votri Valley

341 ID đã chuyển khỏi HOLD: 45 bản dịch mới, 296 giữ nguyên.

- 21 thông báo hệ thống (archive 5764, 5768, 5773, 5777): lưu game, StreetPass, Bliss, thẻ SD, Link Mode, kết nối và chế tạo. Giữ Butterfly/Flutter theo biến thể nguồn; giữ các thuật ngữ Fledgling, License, Guild Office, Ally Clerk, Link Clerk, Joyne Plaza, My Room.
- 24 tiêu đề phần thưởng Bliss (5797), đối chiếu mô tả cột 1 cùng hàng, giữ Bag/Storage và tên riêng. Hai tên tính năng Happy Audio Theater/Happy Movie Theater giữ nguyên theo glossary.
- 217 nhãn kết nối bản đồ có dấu ⇔ (5961 cột 3), 39 nhãn thú cưng/dummy đánh số (8107), 8 nhãn dummy (6952), 30 nhãn chỉ số chính có số cộng (5728), 2 tên tính năng Bliss: giữ nguyên dữ liệu, chưa xác nhận có hiển thị hay không.

## Tiến độ
20.344 bản ghi dịch, 7.180 KEEP, 7.288 HOLD; tổng 27.524/34.812 ID đã chốt theo ledger. Không phải phần trăm ROM Việt hóa.

## QA
Đọc ZIP nguồn 01_CAN_DICH.jsonl và các ZIP CP013e–CP014c; tái lập 9.730 HOLD, trừ ba đợt CP014a–c, đối chiếu 341 ID mới với 7.629 HOLD còn lại và source gốc. ID duy nhất, 45 bản dịch NFC, số, dấu cộng và CTRL khớp. Kiểm readback tệp GitHub thành công. Chưa tìm thấy khóa liên kết đáng tin cậy để thay hàng loạt tên quái/item phiên âm; giữ HOLD. Chưa chạy toàn bộ công cụ khôi phục, kiểm font hoặc runtime 3DS. Quyết định giữ các nhãn kỹ thuật là để bảo toàn nguồn, không khẳng định chúng không được hiển thị.

## Khôi phục
reviews/cp014d-resolutions.jsonl.bz2.b64 — SHA256 giải nén c603640ee8d145eca94daf8ad339045ba6a3ea10225cf39bbb2dd50a0d1095bf.
unpack_batches.py đã bổ sung CP014d, dự kiến xuất merged-CP014d-20344.jsonl và remaining-HOLD-CP014d-7288.jsonl.

Tiếp CP014e: tập trung kiểm các nhóm HOLD còn lại, đặc biệt tên định danh và nhãn ngoại hình. Không sửa main.

Mốc trước: [CP014c](CHECKPOINT-014c.md). [Quy tắc ngôi xưng](NGOI_XUNG.md).
