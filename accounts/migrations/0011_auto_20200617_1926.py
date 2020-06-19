# Generated by Django 2.2.7 on 2020-06-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200616_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='spacialist_doctor',
            field=models.CharField(blank=True, choices=[('أمراض الكلية عند الأطفال', 'أمراض الكلية عند الأطفال'), ('أمراض القلب والأوعية', 'أمراض القلب والأوعية'), ('الصناعة الدوائية', 'الصناعة الدوائية'), ('أمراض العين وجراحتها', 'أمراض العين وجراحتها'), ('أسنان', 'أسنان'), ('جراحة الفم والفكين', 'جراحة الفم والفكين'), ('الأمراض الداخلية', 'الأمراض الداخلية'), ('الطب الفيزيائي و إعادة التأهيل', 'الطب الفيزيائي و إعادة التأهيل'), ('النسج والتشريح المرضي الخاص بالفم والأسنان', 'النسج والتشريح المرضي الخاص بالفم والأسنان'), ('أمراض الجهاز الهضمي', 'أمراض الجهاز الهضمي'), ('التعويضات الثابتة', 'التعويضات الثابتة'), ('طب  الأورام', 'طب  الأورام'), ('أمراض الكلية', 'أمراض الكلية'), ('أمراض الدم عند الأطفال', 'أمراض الدم عند الأطفال'), ('التخدير والإنعاش', 'التخدير والإنعاش'), ('التوليد وأمراض النساء وجراحتها', 'التوليد وأمراض النساء وجراحتها'), ('أمراض الأورام عند الأطفال', 'أمراض الأورام عند الأطفال'), ('جراحة الأطفال', 'جراحة الأطفال'), ('أمراض الصدر', 'أمراض الصدر'), ('الطب الشرعي للأسنان', 'الطب الشرعي للأسنان'), ('جراحة  القلب', 'جراحة  القلب'), ('التعويضات المتحركة', 'التعويضات المتحركة'), ('الأمراض الجلدية و الأمراض المنقولة بالجنس', 'الأمراض الجلدية و الأمراض المنقولة بالجنس'), ('أمراض الأذن والأنف والحنجرة وجراحتها', 'أمراض الأذن والأنف والحنجرة وجراحتها'), ('التشخيص المخبري', 'التشخيص المخبري'), ('طب أسنان الأطفال', 'طب أسنان الأطفال'), ('الأمراض المعدية (الخمجية)', 'الأمراض المعدية (الخمجية)'), ('الجراحة التجميلية والتصنيعية', 'الجراحة التجميلية والتصنيعية'), ('أمراض الأطفال', 'أمراض الأطفال'), ('التصوير الطبي والتشخيص الشعاعي', 'التصوير الطبي والتشخيص الشعاعي'), ('الجراحة العظمية', 'الجراحة العظمية'), ('طب الطوارئ', 'طب الطوارئ'), ('زراعة الأسنان', 'زراعة الأسنان'), ('التشريح المرضي', 'التشريح المرضي'), ('العناية المشددة', 'العناية المشددة'), ('الأمراض النفسية', 'الأمراض النفسية'), ('أمراض الغدد والاستقلاب', 'أمراض الغدد والاستقلاب'), ('جراحة الأوعية', 'جراحة الأوعية'), ('الجراحة العصبية', 'الجراحة العصبية'), ('أمراض الجهاز الحركي', 'أمراض الجهاز الحركي'), ('طب الفم الوقائي', 'طب الفم الوقائي'), ('الصيدلة السريرية', 'الصيدلة السريرية'), ('الجراحة البولية', 'الجراحة البولية'), ('مداواة أسنان', 'مداواة أسنان'), ('الأمراض العصبية', 'الأمراض العصبية'), ('أسنان', 'طب الأسنان التجميلي'), ('طب الأسرة', 'طب الأسرة'), ('الطب الشرعي', 'الطب الشرعي'), ('أمراض اللثة والنسج حول السنية', 'أمراض اللثة والنسج حول السنية'), ('تقويم الأسنان والفكين', 'تقويم الأسنان والفكين'), ('المعالجة الشعاعية للأورام', 'المعالجة الشعاعية للأورام'), ('علم الأدوية السريري', 'علم الأدوية السريري'), ('الجراحة العامة', 'الجراحة العامة'), ('أمراض الدم', 'أمراض الدم')], max_length=100, null=True, verbose_name='متخصص في ؟'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='working_hours',
            field=models.IntegerField(blank=True, null=True, verbose_name='عدد ساات العمل'),
        ),
    ]