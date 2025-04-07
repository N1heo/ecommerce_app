# 🛒 E-Commerce Backend API

A scalable and extensible RESTful API backend for an e-commerce platform, built using **Django** and **Django REST Framework (DRF)**. This API supports full shopping functionality, user authentication, cart and order management, and integrates with **Firebase** for user-device pairing (e.g., smart beekeeping sensors). API documentation is provided via **Swagger UI** for developer-friendly exploration.

---

## 🔧 Tech Stack

- **Backend Framework:** Django 4.x
- **API:** Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Documentation:** Swagger (drf-yasg)
- **Payment system:** [Stripe](https://stripe.com/) 

---

## 🚀 Features

- ✅ RESTful APIs for products, carts, and orders
- ✅ User registration & login via Tokens
- ✅ Admin panel for product and order management
- ✅ Cart & Order management with `CartItem` model linked via `ForeignKey`
- ✅ API-first approach (no templates or frontend dependencies)
- ✅ Swagger UI for API testing and exploration
- ✅ Modular code structure with clear separation of concerns

---

## 📂 Project Structure

```
ecommerce_app/
│
├── cart/                         # Shopping cart app
│   ├── api/                      # API logic for cart (views, serializers)
│   ├── migrations/               # Django migration files
│   ├── __init__.py
│   ├── admin.py                  # Cart admin config
│   ├── apps.py                   # App config
│   ├── models.py                 # Cart-related models (e.g., CartItem)
│   ├── tests.py                  
│   └── urls.py                   # URL routes for the cart API
│
├── checkout/                     # Checkout & order finalization app
│   ├── api/                      # API logic for checkout (views, serializers)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                  # Admin config for orders
│   ├── apps.py
│   ├── forms.py                  # (If used for Django admin or DRF HTML rendering)
│   ├── models.py                 # Order model and related entities
│   ├── tests.py
│   └── urls.py
│
├── ecommerce_app/                # Project-level Django settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Installed apps, middleware, Firebase, etc.
│   ├── urls.py                   # Root URLs (includes app URLs)
│   └── wsgi.py
│
├── media/                        # Uploaded media (e.g., product images)
│
├── product/                      # Product catalog app
│   ├── api/                      # API views, serializers, viewsets
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── filters.py                # Product filtering logic
│   ├── models.py                 # Product, Category, etc.
│   ├── tests.py
│   └── urls.py
│
├── venv/                         # Python virtual environment
│
├── .env                          # Environment variables (DB, Firebase config, etc.)
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

```

---

## 📦 API Endpoints (Sample)

| Method | Endpoint                 | Description                    |
|--------|--------------------------|--------------------------------|
| GET    | `/products/`         | List all products              |
| POST   | `/cart/add/`         | Add item to cart               |
| GET    | `/cart/`             | View cart                      |
| POST   | `/checkout/payment`  | Place an order and pay         |
| GET    | `/swagger/`          | View Swagger documentation     |

---

## 📄 Swagger API Docs

Visit: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)  
You’ll find all available endpoints and can test them directly.

---

## 🛠️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/N1heo/ecommerce_app.git
   cd ecommerce-backend
   ```

2. **Set environment variables** (DB settings, etc.)

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

---

## 🙋 Contact

For questions, feel free to reach out via GitHub issues or [nazar.apsatarov@alatoo.edu.kg].
