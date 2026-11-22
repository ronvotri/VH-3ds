# Snack World: Trejarers — Checkpoint 006

**Trạng thái:** đã dịch 160 ID, kiểm tra thứ tự tag PASS; chờ QA font/ngữ cảnh/runtime.

## Phạm vi
- Nguồn: `SnackWorldTrejarers-BoTaiLieu-VietHoa-2026-11-19.zip` → `ban_dich/de_dich_uu_tien_update.jsonl`.
- Thứ tự nguồn: **600–759** (160 ID).
- Lũy kế CP001–CP006: **760/23.091 ID = 3,29%**.
- Lưu giữ `id`, `source_kind`, `file`, `file_sha256`, `index`, `label_hash`, `variant`, `references_known`, `pool_offset`, `raw_hex` trong JSONL bàn giao.

## Cảnh đã xử lý
Peter Pancake/Ranger, Whipper và copybat; câu chuyện Mr. Velvet; Gumbo Grotto; Master of Wood/Bandshees; Krapen, Fearnix; Mask Melon và cuốn nhật ký.

## Trích đoạn đối chiếu

| Nguồn | Bản dịch |
|---|---|
| You are a nerd! Take that! | Đúng là mọt sách! Ăn đòn đi! |
| To an untrained amateur, these trees are deadly! You'd be compost inside twenty-four hours. | Tay mơ mà vào đây thì đám cây sẽ xử đẹp trong 24 giờ, thành phân bón luôn. |
| I can't believe you can bring yourself to write mush like that! | Không tin nổi anh viết nổi mấy câu sến súa thế! |
| I'm <CG>green</C> now, but keep going until I'm <CR>red</C>! | Tôi đang <CG>xanh</C> rồi, cứ tiếp cho tới khi <CR>đỏ</C> nhé! |

## Kiểm tra
- Đối chiếu tag dạng `<...>`: **160/160 PASS** về thứ tự và nội dung tag.
- ID trong bản gộp: 760 ID không trùng.
- **Chưa kiểm thử:** giới hạn byte, độ rộng dòng, font Việt trên 3DS, repacker, build CIA.
- **Đầy đủ 160 ID mới + bản gộp 760 ID**: `SnackWorld_Trejarers_VH_CP006.zip` đính kèm trong cuộc trò chuyện. Commit GitHub này lưu nhật ký; JSONL chưa được đẩy lên repository.

Nhánh thực hiện: `vh/snack-world-trejarers`. Không thay đổi `main`.