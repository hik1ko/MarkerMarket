from django.db.models import Model, DateTimeField, CharField, SlugField, ImageField, ForeignKey, CASCADE, TextField, \
    DecimalField, PositiveIntegerField, ManyToManyField, EmailField
from django.utils.text import slugify
from django_resized import ResizedImageField
from mptt.fields import TreeForeignKey
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


# Create your models here.
