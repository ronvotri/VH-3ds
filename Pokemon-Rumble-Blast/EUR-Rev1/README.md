# Super Pokémon Rumble — EUR Rev 1 (Việt hóa)

**Phân nhánh riêng EUR Rev 1**, không được vá vào Pokémon Rumble Blast USA.

- Title ID: `0004000000066D00`, product `CTR-P-ACCP`, nguồn `EU_English`.
- Bộ nguồn 20/11/2026: **6.159 record / 16 MSBT**, gồm **1.932 mục cần dịch**, **2.590 mục giữ EN**, 443 debug và 1.194 rỗng.
- Đã viết **558/1.932 mục (28,88%)**, gồm trọn **158 câu `kaiwa.msbt`** và **400/726 mục `main.msbt`**.
- Còn **1.374 mục** cần dịch. Nhóm giữ EN không bị sửa.

## Checkpoint & bản dịch

| Đợt | Phạm vi | Bản dịch | Báo cáo |
|---|---|---|---|
| 003 | `kaiwa.msbt`, 158 mục | [JSONL](ban_dich/kaiwa_CP003_158.jsonl) | [CP003](CHECKPOINT-003.md) |
| 004 | `main.msbt`, 200 mục đầu | [JSONL](ban_dich/main_CP004_200.jsonl) | [CP004](CHECKPOINT-004.md) |
| 005 | `main.msbt`, 200 mục tiếp theo | [JSONL](ban_dich/main_CP005_200.jsonl) | [CP005](CHECKPOINT-005.md) |

[Xưng hô theo ngữ cảnh `kaiwa`](XUNG-HO-KAIWA.md).

## Quy chuẩn

Giữ nguyên EN tên Pokémon, item, Move/Skill, tên riêng và thuật ngữ/chế độ chính; dịch lời thoại, menu, hướng dẫn, trạng thái thường sang tiếng Việt NFC. Hài hước Gen Z vừa phải, trung thành ngữ cảnh; không tự nhận diện người nói từ tên label. Mọi mã `{CTRL:hex}` phải bất biến.

## Chất lượng & hạn chế

Toàn bộ 558 mục đã được kiểm tra ID và thứ tự token, sau đó nhập qua **công cụ importer của bộ giao**, QA văn bản đạt. **Chưa thử trên 3DS, chưa sửa font, chưa repack MSBT/CX, chưa có patch chơi được**. Các mục vẫn ở trạng thái `ban_nhap` và có thể phải chỉnh khi kiểm tra kích cỡ khung thoại thật.

Gói bàn giao CP005 đầy đủ có bản gộp 558 mục, corpus đã nhập 6.159 record, file CSV đối chiếu Anh–Việt và báo cáo QA, được cung cấp trong cuộc hội thoại.
