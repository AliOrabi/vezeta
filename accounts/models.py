from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify

TYPE_OF_PERSON=(
    ('M' , "Male"),
    ('F' , "Female")
)

class Profile(models.Model):
    DOCTOR_IN = {
        ('بشري' , "بشري"),
        ('صيدلي' , "صيدلي"),
        ('أسنان' , "أسنان"),
    }

    SOACIALIST = {
        ('الجراحة العامة' , "الجراحة العامة"),
        ('الجراحة البولية' , "الجراحة البولية"),
        ('الجراحة العظمية' , "الجراحة العظمية"),
        ('الجراحة العصبية' , "الجراحة العصبية"),
        ('الجراحة التجميلية والتصنيعية' , "الجراحة التجميلية والتصنيعية"),
        ('جراحة الأوعية' , "جراحة الأوعية"),
        ('جراحة  القلب' , "جراحة  القلب"),
        ('التخدير والإنعاش' , "التخدير والإنعاش"),
        ('أمراض الأذن والأنف والحنجرة وجراحتها' , "أمراض الأذن والأنف والحنجرة وجراحتها"),
        ('أمراض العين وجراحتها' , "أمراض العين وجراحتها"),
        ('التوليد وأمراض النساء وجراحتها' , "التوليد وأمراض النساء وجراحتها"),
        ('الأمراض الداخلية' , "الأمراض الداخلية"),
        ('أمراض الجهاز الهضمي' , "أمراض الجهاز الهضمي"),
        ('أمراض القلب والأوعية' , "أمراض القلب والأوعية"),
        ('العناية المشددة' , "العناية المشددة"),
        ('أمراض الصدر' , "أمراض الصدر"),
        ('أمراض الغدد والاستقلاب' , "أمراض الغدد والاستقلاب"),
        ('أمراض الدم' , "أمراض الدم"),
        ('أمراض الكلية' , "أمراض الكلية"),
        ('أمراض الجهاز الحركي' , "أمراض الجهاز الحركي"),
        ('الأمراض المعدية (الخمجية)' , "الأمراض المعدية (الخمجية)"),
        ('الأمراض العصبية' , "الأمراض العصبية"),
        ('الأمراض النفسية' , "الأمراض النفسية"),
        ('طب الطوارئ' , "طب الطوارئ"),
        ('أمراض الأطفال' , "أمراض الأطفال"),
        ('أمراض الدم عند الأطفال' , "أمراض الدم عند الأطفال"),
        ('أمراض الأورام عند الأطفال' , "أمراض الأورام عند الأطفال"),
        ('أمراض الكلية عند الأطفال' , "أمراض الكلية عند الأطفال"),
        ('جراحة الأطفال' , "جراحة الأطفال"),
        ('الطب الفيزيائي و إعادة التأهيل' , "الطب الفيزيائي و إعادة التأهيل"),
        ('طب الأسرة' , "طب الأسرة"),
        ('الطب الشرعي' , "الطب الشرعي"),
        ('الأمراض الجلدية و الأمراض المنقولة بالجنس' , "الأمراض الجلدية و الأمراض المنقولة بالجنس"),
        ('التصوير الطبي والتشخيص الشعاعي' , "التصوير الطبي والتشخيص الشعاعي"),
        ('المعالجة الشعاعية للأورام' , "المعالجة الشعاعية للأورام"),
        ('طب  الأورام' , "طب  الأورام"),
        ('التشريح المرضي' , "التشريح المرضي"),
        ('علم الأدوية السريري' , "علم الأدوية السريري"),
        ('التشخيص المخبري' , "التشخيص المخبري"),
        ('الصيدلة السريرية' , "الصيدلة السريرية"),
        ('الصناعة الدوائية' , "الصناعة الدوائية"),
        ('جراحة الفم والفكين' , "جراحة الفم والفكين"),
        ('أمراض اللثة والنسج حول السنية' , "أمراض اللثة والنسج حول السنية"),
        ('تقويم الأسنان والفكين' , "تقويم الأسنان والفكين"),
        ('طب أسنان الأطفال' , "طب أسنان الأطفال"),
        ('الطب الشرعي للأسنان' , "الطب الشرعي للأسنان"),
        ('طب الفم الوقائي' , "طب الفم الوقائي"),
        ('التعويضات الثابتة' , "التعويضات الثابتة"),
        ('التعويضات المتحركة' , "التعويضات المتحركة"),
        ('النسج والتشريح المرضي الخاص بالفم والأسنان' , "النسج والتشريح المرضي الخاص بالفم والأسنان"),
        ('مداواة أسنان' , "مداواة أسنان"),
        ('زراعة الأسنان' , "زراعة الأسنان"),
        ('أسنان' , "طب الأسنان التجميلي"),
        ('أسنان' , "أسنان"),
        ('أسنان' , "أسنان"),
        ('أسنان' , "أسنان"),
        
    }

    CITY = {
        ('حماة' , 'حماة'),
        ('حمص' , 'حمص'),
        ('دمشق' , 'دمشق'),
        ('ريف دمشق' , 'ريف دمشق'),
        ('درعا' , 'درعا'),
        ('السويداء' , 'السويداء'),
        ('القنيطرة' , 'القنيطرة'),
        ('اللاذقية' , 'اللاذقية'),
        ('طرطوس' , 'طرطوس'),
        ('حلب' , 'حلب'),
        ('ادلب' , 'ادلب'),
        ('دير الزور' , 'دير الزور'),
        ('الرقة' , 'الرقة'),
        ('الحسكة' , 'الحسكة'),

    }

    user                = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name                = models.CharField(_("الاسم :"), max_length=80)
    surname             = models.CharField(_("الاسم :"), max_length=50)
    subtitle            = models.CharField(_("نبذة عنك "), max_length=50)
    address             = models.CharField(_("المحافظة :"), choices = CITY ,max_length=50)
    address_detail      = models.CharField(_("العنوان بالتفصيل :"), max_length=50)
    number_phone        = models.CharField(_("الهاتف :"), max_length=50)
    working_hours       = models.IntegerField(_("عدد ساات العمل"), blank=True , null=True)
    waiting_time        = models.IntegerField(_("مدة الانتظار : "), blank=True , null=True)
    doctor              = models.CharField(_("دكتور ؟"), choices=DOCTOR_IN , max_length=50, blank=True , null=True)
    who_i               = models.TextField(_("من أنا :") , max_length=250, blank=True , null=True)
    price               = models.IntegerField(_("سعر المعاينة :"), blank=True , null=True)
    facebook            = models.CharField(_("facebook"), max_length=100, blank=True , null=True)
    twitter             = models.CharField(_("twitter"), max_length=100, blank=True , null=True)
    google              = models.CharField(_("google"), max_length=100, blank=True , null=True)
    join_new            = models.DateTimeField(_("وقت الانضمام :"), auto_now_add=True, blank=True , null=True)
    type_of_person      = models.CharField(_("الجنس :") , choices = TYPE_OF_PERSON , max_length=50)

    image               = models.ImageField(_("الصورة الشخصية :"), upload_to='profile' , blank=True , null=True)
    spacialist_doctor   = models.CharField(_("متخصص في ؟"), choices=SOACIALIST , max_length=100, blank=True , null=True)
    slug                = models.SlugField(_("slug"), blank=True , null=True)

    def save(self , *args, **kwargs):
        self.slug = slugify(self.user.username)    
        super(Profile , self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name


def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile , sender=User)

