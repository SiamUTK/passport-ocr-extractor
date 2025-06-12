# Passport OCR Extractor (Demo)

Demo project that simulates extracting passport data into Siam On Cloud (SOC) format using mock OCR results.

## 📄 Features
- Simulated OCR from mock images
- Converts to standardized SOC format
- Age and validity calculated from DOB/DOE

## 📦 Files
- `mock_passport_data.json` — Sample OCR outputs & converted text
- `ocr_extractor.py` — Parser for converting to SOC format
- `passport_samples/` — Folder for storing test images (mock)

## 💡 Output Format
```
01-DOE-JOHN-MR--THA-P1234567-15JAN1990-10JUL2020-09JUL2030-VALID-35 YRS
```

## 📘 License
MIT License
