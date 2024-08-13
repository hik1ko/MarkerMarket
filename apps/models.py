from django.db.models import Model, DateTimeField, CharField, SlugField, ImageField, ForeignKey, CASCADE, TextField, \
    DecimalField, PositiveIntegerField, ManyToManyField
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


class ProductImage(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')

# Create your models here.
