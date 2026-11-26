# Fantasy Life (USA) — CP014b — Votri Valley

## Kết quả CP014b

744 ID chuyển khỏi HOLD:
- 519 bản ghi nhãn dự phòng, gồm 15 chuỗi nguồn khác nhau: Unknown Item / Items unknown, Unknown Equipment / Equipment unknown, Unknown Tool, Life tool unknown, Furniture unknown, Material of unknown, Trees unknown, Ore unknown, Fish of unknown, Unobtainable Item, Unknown Wardrobe, Unknown Life-Form / Unknown Life Form. Chỉ áp dụng bảng tra chính xác trong archive 6796/6800/8690. Đây là nhãn dự phòng, không phải 519 câu hội thoại mới; chưa xác nhận các nhãn có hiển thị trong gameplay.
- 19 KEEP_SOURCE_NAME khớp nguyên văn với tên đã duyệt trong bảng EN nguồn, gồm Carrot Soup, Pumpkin Pie, Apple Juice, Summer Nectar, Coyote, Bronze Sword, Iron Sword, Silver Sword, Gold Sword, Crystal Sword, Bone Sword, Rune Sword, Bronze Claymore, Iron Claymore, Silver Claymore, Flamberge, Iron Dagger, Silver Dagger, Sugar Wand. Không suy diễn tương đương ID item/monster giữa các bảng.
- 206 KEEP_FORMAT_LITERAL: 160 nhãn slot dự phòng (Unused/Preliminary/Spare frame), 34 nhãn UI resource ghi unused/not used, 12 nhãn Happy Icon ghi not used. Giữ nguyên chuỗi nguồn theo chức năng mô tả, chưa khẳng định không hiển thị.

## Tiến độ

20.228 bản ghi dịch (58,11%); 5.924 KEEP; 8.660 HOLD. Dịch + KEEP = 26.152/34.812 (75,12%). Không phải tỷ lệ hiển thị ROM. Các nhãn ngoại hình chưa rõ nghĩa và tên phiên âm chưa được giải quyết trong CP014b.

## QA

Mở ZIP nguồn, khôi phục 9.730 HOLD lịch sử, loại 326 ID đã xử lý CP014a; đối chiếu 744 ID với 9.404 HOLD còn lại và nguồn gốc. Tất cả ID duy nhất, source khớp; 519 bản ghi dịch khác nguồn, NFC, không rỗng; kiểm token, số, printf và xuống dòng. Bản ghi KEEP có lý do và bảng CSV đối chứng tên EN. Không thử runtime, font, độ rộng, hoặc toàn bộ công cụ khôi phục. Giữ nguyên lịch sử checkpoint, không sửa main.

## Khôi phục

reviews/cp014b-resolutions.jsonl.bz2.b64 — SHA256 dữ liệu giải nén aa7eb1fe89174f79833f875b2012410555e1e66966fc7f5d870725b060db27b3.
Đã đọc lại file GitHub khớp dữ liệu tải lên; unpack_batches.py thêm chuyển trạng thái và xuất merged-CP014b-20228.jsonl, remaining-HOLD-CP014b-8660.jsonl.

Tiếp CP014c: ưu tiên nhãn UI/ngoại hình có nghĩa rõ và đối chiếu tên từ các bảng nguồn đáng tin cậy; không thay tên bằng suy đoán.
