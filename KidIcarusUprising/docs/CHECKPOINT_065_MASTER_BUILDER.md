# Kid Icarus: Uprising — Checkpoint 065: chuẩn bị bản dịch chủ và chặn lỗi trước khi tạo patch

## Đã thực hiện

Đã thêm **`KidIcarusUprising/build_master.py`** lên nhánh `vh/kid-icarus-uprising`.

Công cụ nhận ZIP nguồn `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip` và thư mục `translations/batch_*.jsonl`, ghép theo đúng **ID nguồn**, rồi xuất:

- `kid_icarus_master.jsonl`: giữ nguyên tất cả **4.067 dòng nguồn**, gồm 44 mục rỗng; dòng nào có overlay hợp lệ thì thêm `vi`, dòng chưa dịch thì giữ `vi` rỗng, không tự lấp bằng tên tiếng Anh.
- `preflight_report.json`: tổng bản ghi, số bản dịch được áp dụng, số nguồn chưa có overlay, mọi lỗi phát hiện.

Chặn các trường hợp **ID trùng**, ID không tồn tại, source snapshot không khớp, tự điền bản dịch vào source rỗng, bản dịch rỗng, và sai thứ tự/số lượng token `{CTRL:hex}`. Chế độ `--strict` sẽ trả exit code 1 khi có lỗi.

### Cách chạy (Windows / PowerShell)

```powershell
python .\KidIcarusUprising\build_master.py `
  --zip ".\KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip" `
  --translations ".\KidIcarusUprising\translations" `
  --out ".\build\kid-icarus-master" `
  --strict
```

Hoặc gọi trên một dòng bằng các tham số tương đương.

## Đã kiểm thử bằng ZIP thật

Dùng ZIP gốc của người dùng và thư mục batch **mẫu thử riêng**:
- **Ca hợp lệ:** một ID nguồn có bản nháp, script xuất **4.067 dòng**, 4.023 nguồn không trống, 44 nguồn rỗng, 1 overlay áp dụng, **0 lỗi**, exit code **0**.
- **Ca cố ý sai:** tạo hai batch có cùng một ID và xóa token điều khiển của câu; script phát hiện **1 `duplicate_overlay` + 1 `control_mismatch`**, exit code **1** ở `--strict`.
- Đã fetch lại file script từ GitHub sau commit, xác nhận có nội dung.

**Chưa chạy script trên trọn bộ 49 batch thực tế từ GitHub**; kiểm thử ở đây chỉ xác minh chức năng trên mẫu, không chứng nhận bản dịch toàn dự án đã PASS.

## Tình trạng và tồn đọng

- Mốc kiểm kê trước: **3.264/4.023** ID có overlay sau khi loại các batch trùng; **1.696/1.696** câu thoại có nội dung đã có bản nháp. Các số này chưa được thay thế bởi kết quả build full checkout.
- Các tên Weapon, Power, Item và tên riêng theo quy ước giữ tiếng Anh.
- Hai mục `Heart` và `Food` cần xem ngữ cảnh để quyết định dịch hay giữ nguyên.
- **Chưa có bộ nhập ngược MSBT**, tái đóng DARC/LZ11, xử lý glyph/font tiếng Việt hoặc LayeredFS patch đã kiểm thử.
- Công cụ CP065 chỉ tạo **bản dịch chủ trung gian**, tuyệt đối không tạo ROM/patch chơi được.

## Tiếp theo

1. Chạy `build_master.py --strict` với toàn bộ batch thực tế của GitHub, sửa từng lỗi được báo.
2. Thực hiện bộ nhập MSBT có round-trip byte/structure và kiểm thử khung chữ/font, rồi mới tái đóng archive và tạo LayeredFS.
3. Xác minh dump RomFS của game gốc để không bỏ sót nguồn text ngoài phạm vi ZIP C-Stick/Gyro v172.
