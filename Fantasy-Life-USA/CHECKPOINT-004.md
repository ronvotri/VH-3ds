# Fantasy Life (USA) — Checkpoint 004 🇻🇳

**Ngày:** 23/11/2026  
**Kết quả:** 2.000 mục mới, từ gói 0006–0025; tổng 2.500 / 34.812 mục (7,18%), còn 32.312.

## Nội dung

- 20 gói, mỗi gói 100 câu: trang bị, vũ khí, cung, mũ, áo, quần, phụ kiện, dụng cụ nghề, vật liệu, nội thất, cá và nấm.
- Một phần hướng dẫn UI/gameplay cuối đợt có token điều khiển dày (gói 0025).
- Các bản EN_A và EN_B giữ đúng text theo từng ID riêng; không áp tên biến thể của bản này sang bản kia.
- Giữ giọng văn vui nhẹ ở mô tả, trong khi thông tin hệ thống không tự thêm đùa.
- **Lưu ý:** bản dịch nguồn; chưa vá font, chưa chạy trên 3DS và chưa phân vai người nói ở các đoạn speaker=unknown.

## Dữ liệu trên GitHub

- `translations/cp004-2000.jsonl.bz2.b64`: 2.000 mục JSONL, nén bzip2 rồi mã hóa base64 để lưu bằng GitHub contents API.
- Chạy `python3 unpack_batches.py` để khôi phục CP001–CP004 thành `translations/merged-001-025.jsonl` gồm 2.500 mục.
- SHA-256 sau giải nén của CP004: `4b8e00d1223f7e9c4f520f816d7a11ae46fd09d3cd0bf183ee358cca2c2fa395`.

## Cần tiếp tục

- Gói 0026, mục thứ 2.501.
- Trước phát hành: patch font, kiểm biến thể ngôn ngữ, tràn khung, token runtime và ngôi xưng nhân vật theo cảnh.
