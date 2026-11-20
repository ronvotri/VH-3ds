# Kid Icarus: Uprising — Checkpoint 059: Dịch mới + QA song song

**Nguồn duy nhất:** `KidIcarusUprising-BoTaiLieu-VietHoa-2026-11-18.zip`, mục `KidIcarusUprising-VietHoa/ban_dich/tieng_anh_can_dich.jsonl`.
**Nhánh:** `vh/kid-icarus-uprising`.

## A. Dịch mới
- Thêm **1 ID chưa có overlay**: `romfs/us/0.arc::resident/03.bin#01655`
- Tiếng Anh gốc: `Large Arena`
- Bản Việt: `Đấu trường lớn`
- Tệp: `translations/batch_059.jsonl`; giữ `source`, `id`, `status: draft`.

## B. QA song song — 194 mục thoại, hai chỉnh sửa
Đã xem và rà bản dịch tại `batch_021.jsonl` (72 mục; Chương 6), `batch_022.jsonl` (63 mục; Chương 7), `batch_023.jsonl` (59 mục; Chương 8), đối chiếu các vị trí sửa với tiếng Anh trong ZIP.

| ID | Câu tiếng Anh | Trước | Sau | Lý do |
| --- | --- | --- | --- | --- |
| `a0700.zrc#00044` | You have my word. | Tôi xin hứa với ngài. | Ta xin hứa với ngài. | Palutena trả lời Poseidon; giữ xưng `ta` nhất quán với lời thoại khác, vẫn gọi Poseidon là `ngài`. |
| `a0800.zrc#00029` | They've grown more brittle with age, but they'll likely last a few more battles. | Qua năm tháng, chúng đã giòn hơn, nhưng chắc vẫn trụ được vài trận. | Để lâu nên chúng đã giòn, dễ vỡ, nhưng chắc vẫn dùng được vài trận. | Làm rõ `brittle` là dễ vỡ; giữ sự hài hước về tình trạng Three Sacred Treasures. |

Đã sửa trực tiếp hai file batch cũ, không thêm ID trùng. Đã fetch lại GitHub sau commit: **3/3 mục (1 mới, 2 sửa) hiện đúng nội dung**, các file 022 và 023 giữ nguyên 63 và 59 bản ghi.

## C. Phân loại phần chưa dịch
- Nguồn còn rất nhiều ID thuộc dải `resident/03.bin` là **tên Weapon, Power, Item**, không được dịch theo quy ước.
- Phần `resident/04.bin#00110–00209` phần lớn là **tên nhân vật hoặc nickname mẫu** (`Kirby`, `Mario`, `Samus`, `Link`, v.v.) phải giữ nguyên.
- Các `CPU 1–6` giữ thuật ngữ CPU, không dùng để tăng tiến độ.
- Nhóm giao diện `resident/03.bin#01655 Large Arena` là nhãn chưa dịch đã xác nhận được trong lượt này.
- Những tên chính thức còn trống chưa được tự chép nguyên văn vào overlay để thổi phồng tỷ lệ.

## D. Tiến độ
- Trước: **3.267 / 4.023** ID bản nháp (Checkpoint 058).
- Sau: **3.268 / 4.023 = 81,23%** ID có overlay.
- **+1 mục dịch mới, +194 mục thoại rà, +2 sửa QA**. Không gọi 194 mục là đã qua QA ngữ nghĩa đầy đủ hoặc QA hiển thị trên 3DS.
- Vẫn chưa kiểm tra độ dài/khung chữ, font tiếng Việt, build patch và chơi trên máy thật.
