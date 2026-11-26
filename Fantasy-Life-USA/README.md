# Fantasy Life (USA) — CP013l — Votri Valley

26/11/2026 — CP013l thêm 11 bản dịch, 145 KEEP và 2.007 HOLD. Đã lập danh sách phân loại cho toàn bộ phần nguồn còn lại theo các checkpoint.

## Phạm vi
- 11 bản dịch: 3 ô save, 5 nhãn Stars, 2 nhãn danh mục vật phẩm (Vehicle body, Body under, dùng bản tương ứng đã có trong bảng 8690), 1 tiêu đề Florina's House. Tên riêng Florina giữ nguyên.
- 145 KEEP: 128 tên/thuật ngữ, 17 ký hiệu/đơn vị/markup/URL giữ nguyên.
- 2.007 HOLD (phân nhóm theo metadata và nội dung, chưa xác minh runtime): 772 nhãn sự kiện, 308 nhãn hiệu ứng/debug, 268 tài nguyên UI/nhãn dịch thô, 200 map/debug 0070–0071, 142 ngoại hình, 104 tên item/quái, 90 tên bản đồ dịch thô, 61 metadata nhà/thú cưng, 59 nhãn chưa rõ nghĩa, 3 placeholder.

## Tổng tiến độ
19.636 bản ghi dịch (56,40%), 5.446 KEEP, 9.730 HOLD. Tổng dịch + KEEP = 25.082/34.812 (72,05%). Tất cả 34.812 ID đã có phân loại theo ledger tái lập, nhưng HOLD chưa được duyệt và không có nghĩa là game đã dịch xong. Các ID giữ nguyên và HOLD không được chép vào trường vi.

## QA
Mở trực tiếp 01_CAN_DICH.jsonl từ ZIP gốc và các gói TXT, xác nhận cùng 34.812 ID. Tái lập 13.665 ID đầu: 10.945 theo phạm vi CP001–CP009a (gói 0001–0113 trừ 0070–0071), 2.720 ID CP009b/c–CP010a/b theo dữ liệu giải nén thực tế từ GitHub. Đọc 5.960 bản ghi dịch CP010c–CP013k từ file cục bộ và 13.024 ID KEEP/HOLD. Không trùng trong các tập ID tái lập. 2.163 ID còn lại được phân loại trong CP013l, không trùng và thuộc nguồn. 11 bản dịch NFC, bảo toàn chữ số/token, khác nguồn.
Chưa giải nén kiểm lại từng batch CP001–CP009a trong phiên này; chưa chạy toàn bộ unpack_batches.py, chưa test font/ROM/runtime. Phân loại HOLD là sơ bộ theo nhóm, không phải xác nhận chuỗi không hiển thị.

## Khôi phục
- translations/cp013l-11.jsonl.bz2.b64 — SHA256 e3d7605a53ea524bc2b41486b21b3b8e7e8c3eceae662ae4055cc004e83bde74
- reviews/cp013l-keep.jsonl.bz2.b64 — a23a695f81a72029f13dd901aea82dcb02e81140be4552eefbb87dcaaef93a9b
- reviews/cp013l-hold.jsonl.bz2.b64 — 22693f30be26e31460f03a30eeebb05e55c6e3ac53cd73332613b72cc8accad0
Ba tệp được đọc lại từ GitHub khớp bản tải lên. unpack_batches.py đã bổ sung kiểm tra tổng 34.812 ID và đầu ra merged-CP013l-19636.jsonl; chưa chạy đầy đủ.

Tiếp CP014: giải quyết HOLD có khả năng hiển thị trước (ngoại hình, UI, tên địa danh), đối chiếu bảng kỹ thuật/ID chính thức; giữ nguyên các mã thực sự nội bộ sau khi xác minh. Kiểm thử gộp toàn bộ trước bàn giao bản dịch. Không sửa main.

Mốc trước: [CP013k](CHECKPOINT-013k.md). Xem [quy tắc ngôi xưng](NGOI_XUNG.md).
