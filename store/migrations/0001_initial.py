# Generated by Django 4.2 on 2025-02-27 11:57

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields
from django.db import migrations, models

import userauths.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=200)),
                ("mobile", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("town_city", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("zip", models.CharField(max_length=100)),
                ("status", models.BooleanField(default=False)),
                ("same_as_billing_address", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name_plural": "Address",
            },
        ),
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="brand.jpg", null=True, upload_to=userauths.models.user_directory_path
                    ),
                ),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name_plural": "Brands",
            },
        ),
        migrations.CreateModel(
            name="CancelledOrder",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.CharField(max_length=100)),
                ("refunded", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name_plural": "Cancelled Order",
            },
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("qty", models.PositiveIntegerField(blank=True, default=0, null=True)),
                ("price", models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ("sub_total", models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                (
                    "shipping_amount",
                    models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True),
                ),
                (
                    "service_fee",
                    models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True),
                ),
                ("tax_fee", models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ("total", models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("size", models.CharField(blank=True, max_length=100, null=True)),
                ("color", models.CharField(blank=True, max_length=100, null=True)),
                ("cart_id", models.CharField(blank=True, max_length=1000, null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="CartOrder",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sub_total", models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ("shipping_amount", models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ("tax_fee", models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ("service_fee", models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ("total", models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[
                            ("paid", "Paid"),
                            ("pending", "Pending"),
                            ("processing", "Processing"),
                            ("cancelled", "Cancelled"),
                            ("initiated", "Initiated"),
                            ("failed", "failed"),
                            ("refunding", "refunding"),
                            ("refunded", "refunded"),
                            ("unpaid", "unpaid"),
                            ("expired", "expired"),
                        ],
                        default="initiated",
                        max_length=100,
                    ),
                ),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Fulfilled", "Fulfilled"),
                            ("Partially Fulfilled", "Partially Fulfilled"),
                            ("Cancelled", "Cancelled"),
                        ],
                        default="Pending",
                        max_length=100,
                    ),
                ),
                (
                    "initial_total",
                    models.DecimalField(
                        decimal_places=2, default=0.0, help_text="The original total before discounts", max_digits=12
                    ),
                ),
                (
                    "saved",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        help_text="Amount saved by customer",
                        max_digits=12,
                        null=True,
                    ),
                ),
                ("full_name", models.CharField(max_length=1000)),
                ("email", models.CharField(max_length=1000)),
                ("mobile", models.CharField(max_length=1000)),
                ("address", models.CharField(blank=True, max_length=1000, null=True)),
                ("city", models.CharField(blank=True, max_length=1000, null=True)),
                ("state", models.CharField(blank=True, max_length=1000, null=True)),
                ("country", models.CharField(blank=True, max_length=1000, null=True)),
                ("stripe_session_id", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "oid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz", length=10, max_length=25, prefix=""
                    ),
                ),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name_plural": "Cart Order",
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="CartOrderItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("qty", models.IntegerField(default=0)),
                ("color", models.CharField(blank=True, max_length=100, null=True)),
                ("size", models.CharField(blank=True, max_length=100, null=True)),
                ("price", models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                (
                    "sub_total",
                    models.DecimalField(
                        decimal_places=2, default=0.0, help_text="Total of Product price * Product Qty", max_digits=12
                    ),
                ),
                (
                    "shipping_amount",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Estimated Shipping Fee = shipping_fee * total",
                        max_digits=12,
                    ),
                ),
                (
                    "tax_fee",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Estimated Vat based on delivery country = tax_rate * (total + shipping)",
                        max_digits=12,
                    ),
                ),
                (
                    "service_fee",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Estimated Service Fee = service_fee * total (paid by buyer to platform)",
                        max_digits=12,
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, default=0.0, help_text="Grand Total of all amount listed above", max_digits=12
                    ),
                ),
                ("expected_delivery_date_from", models.DateField(blank=True, null=True)),
                ("expected_delivery_date_to", models.DateField(blank=True, null=True)),
                (
                    "initial_total",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Grand Total of all amount listed above before discount",
                        max_digits=12,
                    ),
                ),
                (
                    "saved",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        help_text="Amount saved by customer",
                        max_digits=12,
                        null=True,
                    ),
                ),
                ("order_placed", models.BooleanField(default=False)),
                ("processing_order", models.BooleanField(default=False)),
                ("quality_check", models.BooleanField(default=False)),
                ("product_shipped", models.BooleanField(default=False)),
                ("product_arrived", models.BooleanField(default=False)),
                ("product_delivered", models.BooleanField(default=False)),
                (
                    "delivery_status",
                    models.CharField(
                        choices=[
                            ("On Hold", "On Hold"),
                            ("Shipping Processing", "Shipping Processing"),
                            ("Shipped", "Shipped"),
                            ("Arrived", "Arrived"),
                            ("Delivered", "Delivered"),
                            ("Returning", "Returning"),
                            ("Returned", "Returned"),
                        ],
                        default="On Hold",
                        max_length=100,
                    ),
                ),
                ("tracking_id", models.CharField(blank=True, max_length=100000, null=True)),
                ("applied_coupon", models.BooleanField(default=False)),
                (
                    "oid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz", length=10, max_length=25, prefix=""
                    ),
                ),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name_plural": "Cart Order Item",
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="category.jpg", null=True, upload_to=userauths.models.user_directory_path
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("slug", models.SlugField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("color_code", models.CharField(blank=True, max_length=100, null=True)),
                ("image", models.FileField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name="Coupon",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=1000)),
                (
                    "discount",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "cid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz", length=10, max_length=25, prefix=""
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="CouponUsers",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=1000)),
                ("email", models.CharField(max_length=1000)),
                ("mobile", models.CharField(max_length=1000)),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="DeliveryCouriers",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=1000, null=True)),
                ("tracking_website", models.URLField(blank=True, null=True)),
                ("url_parameter", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "verbose_name_plural": "Delivery Couriers",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Gallery",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.FileField(default="gallery.jpg", upload_to=userauths.models.user_directory_path)),
                ("active", models.BooleanField(default=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "gid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz", length=10, max_length=25, prefix=""
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Images",
                "ordering": ["date"],
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("seen", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Notification",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    models.FileField(
                        blank=True, default="product.jpg", null=True, upload_to=userauths.models.user_directory_path
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("tags", models.CharField(blank=True, max_length=1000, null=True)),
                ("brand", models.CharField(blank=True, max_length=100, null=True)),
                ("price", models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ("old_price", models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ("shipping_amount", models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ("stock_qty", models.PositiveIntegerField(default=0)),
                ("in_stock", models.BooleanField(default=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("draft", "Draft"),
                            ("disabled", "Disabled"),
                            ("rejected", "Rejected"),
                            ("in_review", "In Review"),
                            ("published", "Published"),
                        ],
                        default="published",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("regular", "Regular"), ("auction", "Auction"), ("offer", "Offer")],
                        default="regular",
                        max_length=50,
                    ),
                ),
                ("featured", models.BooleanField(default=False)),
                ("hot_deal", models.BooleanField(default=False)),
                ("special_offer", models.BooleanField(default=False)),
                ("digital", models.BooleanField(default=False)),
                ("views", models.PositiveIntegerField(blank=True, default=0, null=True)),
                ("orders", models.PositiveIntegerField(blank=True, default=0, null=True)),
                ("saved", models.PositiveIntegerField(blank=True, default=0, null=True)),
                ("rating", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "sku",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="1234567890", length=5, max_length=50, prefix="SKU", unique=True
                    ),
                ),
                (
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz", length=10, max_length=20, prefix="", unique=True
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name_plural": "Products",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="ProductFaq",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz", length=10, max_length=20, prefix="", unique=True
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("question", models.CharField(max_length=1000)),
                ("answer", models.CharField(blank=True, max_length=10000, null=True)),
                ("active", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Product Faqs",
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("review", models.TextField()),
                ("reply", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[(1, "★☆☆☆☆"), (2, "★★☆☆☆"), (3, "★★★☆☆"), (4, "★★★★☆"), (5, "★★★★★")], default=None
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Reviews & Rating",
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("price", models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name="Specification",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("content", models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=30)),
                ("active", models.BooleanField(default=True)),
                ("slug", models.SlugField(max_length=30, unique=True, verbose_name="Tag slug")),
            ],
            options={
                "verbose_name_plural": "Tags",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="wishlist", to="store.product"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Wishlist",
            },
        ),
    ]
