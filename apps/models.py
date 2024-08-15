from unittest.mock import Base

from django.db.models import Model, DateTimeField, CharField, SlugField, ImageField, ForeignKey, CASCADE, TextField, \
    DecimalField, PositiveIntegerField, ManyToManyField, IntegerField, EmailField, TextChoices
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from django_resized import ResizedImageField
from mptt.models import MPTTModel


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseSlugModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = CharField(max_length=255, unique=True)
    image = ResizedImageField(size=[200, 200], quality=100, upload_to='images/', force_format='png', blank='True')
    slug = SlugField(max_length=255, unique=True, editable=False)
    parent = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True, related_name='children')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
            unique = self.slug
            num = 1
            while Category.objects.filter(slug=unique).exists():
                unique = f'{self.slug}-{num}'
                num += 1
            self.slug = unique
        super().save(force_insert, force_update, using, update_fields)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(BaseModel, BaseSlugModel):
    name = CharField(max_length=255)
    slug = SlugField
    price = DecimalField(max_digits=7, decimal_places=2)
    quantity = PositiveIntegerField(default=0)
    description = TextField(blank=True)
    category_id = ForeignKey(Category, on_delete=CASCADE)
    # tag = ManyToManyField('Tag', related_name='tag')
    company_name = CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def in_stock(self):
        return self.quantity > 0


class ProductImage(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')


class Tag(BaseSlugModel):
    pass


class Order(Model):
    class StatusMethod(TextChoices):
        COMPLETED = 'completed', 'Completed'
        PROCESSING = 'processing', 'Processing'
        ON_HOLD = 'on hold', 'On Hold'
        PENDING = 'pending', 'Pending'

    class PaymentMethod(TextChoices):
        UZUM_BANK = 'uzum', 'Uzum'
        CLICK = 'clic', 'Click'
        Payme = 'payme', 'Payme'
        VISA_CARD = 'visa_card', 'Visa_card'
        MASTER_CARD = 'master_card', 'Master_card'

    class Delivery(TextChoices):
        COURIER = 'courier', 'Courier'
        TAKE_AWAY = 'take_away', 'Take_away'

    status = CharField(max_length=255, choices=StatusMethod)
    payment_method = CharField(max_length=255, choices=PaymentMethod)
    delivery = CharField(max_length=255, choices=Delivery)
    address = ForeignKey('apps.Address', CASCADE, related_name='order_address')
    owner = ForeignKey('apps.User', CASCADE, related_name='orders')


class SiteSettings(Model):
    phone_number = IntegerField()
    email = EmailField()
    address = TextField()
