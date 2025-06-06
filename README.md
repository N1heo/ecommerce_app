# 🛒 E-Commerce Backend API

A scalable and extensible RESTful API backend for an e-commerce platform, built using **Django** and **Django REST Framework (DRF)**. This API supports full shopping functionality, user authentication, cart and order management, and integrates with Stripe payment service. API documentation is provided via **Swagger UI** for developer-friendly exploration.

---

## 🔧 Tech Stack

- **Backend Framework:** Django 4.x
- **API:** Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Documentation:** Swagger (drf-yasg)
- **Payment system:** [Stripe](https://stripe.com/)
- **Image processing:** Cloudinary
- **Containerization:** Docker
- **Deployment:** AWS

---

## 🚀 Features

- ✅ B2C model implementation
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
├── app/                          # Main Django application
│   ├── cart/                     # Shopping cart app
│   │   ├── api/                  # API endpoints
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── urls.py
│   │
│   ├── checkout/                 # Checkout & payments
│   │   ├── api/                  # Stripe integration
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py             # Order, Payment models
│   │   ├── tests.py
│   │   └── urls.py
│   │
│   ├── product/                  # Product catalog
│   │   ├── api/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py             
│   │   ├── tests.py
│   │   └── urls.py
│   │
│   ├── ecommerce_app/            # Project config
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings/             # Split settings
│   │   │   ├── base.py
│   │   │   ├── development.py
│   │   │   └── production.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── __init__.py
│   ├── dockerignore
│   ├── Dockerfile.prod           # Production Dockerfile
│   ├── entrypoint_prod.sh        # Production entrypoint
│   ├── manage.py
│   └── requirements.txt          # Split into base.txt, prod.txt, dev.txt
│
├── nginx/                        # Nginx configuration
│   ├── Dockerfile
│   ├── custom.conf               # Custom nginx config
│   └── vhost.d/                  # Virtual host configs
│
│
├── .env.prod                     # Production environment vars
├── .gitignore
├── docker-compose.prod.yml       # Production compose
└── README.md
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
