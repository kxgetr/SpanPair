# SpanPair

Kimliğe göre başlangıç ve bitiş olaylarından süre çıkarır.

## Girdi

id, kind (start/end), time. Her id bir span.

## Kullanım

Python 3.11+, standart kütüphane.

```sh
python spanpair.py input.json
python verify.py
```

Dosya verilmezse stdin okunur. Sonuç stdout üzerinde JSON olarak yazılır. Girdi hatası çıkış kodu 2 üretir.

Örnek sonuç:

```json
{
  "x": 6
}
```
