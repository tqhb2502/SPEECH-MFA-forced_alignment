# 1. Cài đặt MFA
- Cài đặt conda, cài xong thì dùng **Anaconda PowerShell**, trên Windows thì bật bằng quyền **Administrator**
- Kiểm tra: `conda --version`
- Bắt đầu với `conda init`, chạy xong tắt PowerShell đi bật lại
- Cài đặt MFA từ *conda-forge*:
`conda create -n aligner -c conda-forge montreal-forced-aligner`
- Vào môi trường: `conda activate aligner`
# 2. Chuẩn bị
## 2.1. Tải mô hình acoustic:
- `mfa models download acoustic vietnamese_mfa`
- Kiểm tra: `mfa models list acoustic`
## 2.2. Tải dictionary:
- `mfa model download dictionary vietnamese_mfa`
- Kiểm tra: `mfa model list dictionary`
## 2.3. Dữ liệu từ Common Voice:
- Xử lý file *other.tsv* để lấy transcript: `python .\make_transcipt.py`
# 3. Chạy forced alignment:
- `mfa align ./data/clips vietnamese_mfa vietnamese_mfa ./data/clips_aligned`
- Có thể lấy luôn kết quả có sẵn trong *./data/clips_aligned*
