# 📘 FastAPI Practice Assignment — Products Service

**Instructor:** djumanov
**Objective:** FastAPI, SQLAlchemy ORM va PostgreSQL bilan ishlash ko‘nikmalarini mustahkamlash.
**Scope:** faqat **GET**, **query parameters** va **path parameters**.

---

# 1. Project Overview

Ushbu topshiriqda siz FastAPI asosida kichik **Products API** yaratishingiz kerak.
API ma’lumotlar bazasidagi **products** jadvali bilan ishlaydi va foydalanuvchiga mahsulotlar haqida turli so‘rovlar yuborish imkonini beradi.

Tayyorlanadigan funksionallar:

* Barcha mahsulotlarni olish
* ID bo‘yicha mahsulotni olish
* Nom bo‘yicha qidirish
* Kategoriya bo‘yicha filterlash
* Narx oralig‘i bo‘yicha filterlash
* Pagination (limit/offset)
* Sklad holatiga ko‘ra (in_stock) filterlash

Ushbu topshiriq orqali studentlar real API tuzishda qo‘llaniladigan asosiy GET-so‘rovlar va ularning parametrlarini amaliy o‘rganadilar.

---

# 2. Database Structure

API PostgreSQL bilan ishlaydi va SQLAlchemy ORM orqali `products` jadvali yaratiladi.

### Jadval: **products**

| Field    | Type         | Description                             |
| -------- | ------------ | --------------------------------------- |
| id       | Integer (PK) | Mahsulotning noyob identifikatori       |
| name     | String       | Mahsulot nomi                           |
| category | String       | Kategoriya (masalan: "phone", "laptop") |
| price    | Float        | Mahsulot narxi                          |
| in_stock | Boolean      | Skladda mavjudligi (True/False)         |

**Talaba vazifasi:**
`models.py` ichida yuqoridagi struktura asosida SQLAlchemy ORM modeli yaratish.

---

# 3. Assignment Tasks (Endpoints)

Har bir endpoint alohida funksiya ko‘rinishida bo‘lishi shart.
Har bir funksiya **docstring** bilan ta’minlanishi kerak.

---

## 3.1. **GET /products**

**Vazifa:** Bazadagi barcha mahsulotlarni qaytarish.

**Talablar:**

* SQLAlchemy orqali barcha mahsulotlar select qilinadi.
* Natija Pydantic schema orqali qaytariladi.

---

## 3.2. **GET /products/{product_id}**

**Vazifa:** `product_id` orqali bitta mahsulotni qaytarish.

**Talablar:**

* `product_id` **path parameter** sifatida olinadi.
* Agar mahsulot mavjud bo‘lmasa — 404 xatolik qaytariladi.
* Response modeli Pydantic orqali qaytariladi.

---

## 3.3. **GET /products/search**

**Query parameter:**

* `name` (optional)

**Vazifa:**
Nomida berilgan qiymat mavjud bo‘lgan mahsulotlarni (LIKE qidiruv) qaytarish.

**Misol:**
`/products/search?name=iphone`

**Talablar:**

* Parametr yuborilmasa barcha mahsulotlar qaytmasligi kerak — **faqat qidiruv bo‘yicha ishlaydigan endpoint**.
* SQLAlchemy `contains()` yoki `ilike()` ishlatish tavsiya etiladi.

---

## 3.4. **GET /products/filter/category**

**Query parameter:**

* `category` (majburiy)

**Vazifa:**
Berilgan kategoriya bo‘yicha filterlash.

**Misol:**
`/products/filter/category?category=phone`

**Talablar:**

* Parametr yuborilmasa 400/BAD REQUEST qaytarishingiz mumkin.
* Faqat kategoriya bo‘yicha filter natijalari qaytariladi.

---

## 3.5. **GET /products/filter/price**

**Query parameters:**

* `min_price` (optional)
* `max_price` (optional)

**Misol:**
`/products/filter/price?min_price=100&max_price=500`

**Vazifa:**
Narx oralig‘i bo‘yicha mahsulotlarni filterlash.

**Talablar:**

* Parametrlar optional, ikkalasi ham bo‘lmasligi mumkin.
* Quyidagi kombinatsiyalar to‘g‘ri ishlashi kerak:

  * faqat `min_price`
  * faqat `max_price`
  * ikkalasi birga
* SQLAlchemy filter shartlari bir-biriga qo‘shib borilishi kerak.

---

## 3.6. **GET /products/paginated**

**Query parameters:**

* `limit` (default = 10)
* `offset` (default = 0)

**Misol:**
`/products/paginated?limit=5&offset=10`

**Vazifa:**
Ma’lumotlarni pagination bilan qaytarish (LIMIT/OFFSET).

**Talablar:**

* Limit va offset integer bo‘lishi kerak.
* SQLAlchemy `limit()` va `offset()` ishlatiladi.

---

## 3.7. **GET /products/in-stock** (Qo‘shimcha vazifa)

**Query parameter:**

* `status`: bool (True/False)

**Misol:**
`/products/in-stock?status=true`

**Vazifa:**
Skladda mavjud mahsulotlarni yoki mavjud bo‘lmagan mahsulotlarni qaytarish.

**Talablar:**

* `status=true` → faqat `in_stock=True`
* `status=false` → faqat `in_stock=False`

---

**Talablar:**

* Barcha endpointlar `routers/products.py` ichida bo‘lishi kerak.
* `main.py` ichida router `include_router()` bilan ulanishi kerak.
* Har bir endpointga alohida funksiya yoziladi.
* Har bir funksiyada **docstring** bo‘lishi majburiy.
* SQLAlchemy querylari to‘g‘ri ishlashi kerak.
* 404, 400 kabi xatoliklar to‘g‘ri qaytarilishi shart.
* Response modeling Pydantic orqali bajariladi (ORM mode optional).

---

# 5. Test Data (Talaba qo‘lda kiritadi)

Test uchun quyidagi ma’lumotlarni bazaga qo‘lda joylashtiring:

```
1, "iPhone 13", "phone", 799, true
2, "Samsung S22", "phone", 699, true
3, "MacBook Air", "laptop", 999, false
4, "Xiaomi Redmi Note", "phone", 299, true
5, "Dell XPS 13", "laptop", 1299, true
```

---

# 6. Expected Learning Outcomes

Ushbu topshiriq yakunida talaba quyidagi ko‘nikmalarga ega bo‘ladi:

* **Path parameters**: ID bo‘yicha resurs olish
* **Query parameters**: search, filter, pagination
* SQLAlchemy ORM orqali filterlash, qidirish va limit/offset qo‘llash
* Pydantic response modellari yaratish
* Xatoliklarni to‘g‘ri qaytarish (404, 400)
* Modular project structure bilan ishlash
* Real dunyodagi GET endpointlarni qurish mantiqini tushunish
