from cab import managers
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from markdown import markdown
from pygments import formatters, highlight, lexers
from tagging.fields import TagField
import datetime
import tagging


class Language(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    language_code = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)
    objects = managers.LanguageManager()
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('cab_language_detail', (), { 'slug': self.slug })

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.language_code)


class Snippet(models.Model):
    title = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    highlighted_code = models.TextField(editable=False)
    pub_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    objects = managers.SnippetManager()
    tags = TagField()
 
    class Meta:
        ordering = ['-pub_date']
    
    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        self.description_html = markdown(self.description)
        self.highlighted_code = self.highlight()
        super(Snippet, self).save(force_insert, force_update)

    @models.permalink
    def get_absolute_url(self):
        return ('cab_snippet_detail', (), { 'object_id': self.id })
    
    def highlight(self):
        return highlight(self.code,
                         self.language.get_lexer(),
                         formatters.HtmlFormatter(linenos=True))

# See http://blog.sveri.de/index.php?/categories/2-Django
tagging.register(Snippet, tag_descriptor_attr='etags')


class Bookmark(models.Model):
    snippet = models.ForeignKey(Snippet)
    user = models.ForeignKey(User, related_name='cab_bookmarks')
    date = models.DateTimeField(editable=False)
    
    class Meta:
        ordering = ['-date']
    
    def __unicode__(self):
        return "%s bookmarked by %s" % (self.snippet, self.user)

    # See http://blog.haydon.id.au/2008/09/10-finishing-code-sharing-application.html
    def save(self, **kwargs):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Bookmark, self).save(**kwargs)


class Rating(models.Model):
    RATING_UP = 1
    RATING_DOWN = -1
    RATING_CHOICES = ((RATING_UP, 'useful'),
                      (RATING_DOWN, 'not useful'))
    snippet = models.ForeignKey(Snippet)
    user = models.ForeignKey(User, related_name='cab_rating')
    rating = models.IntegerField(choices=RATING_CHOICES)
    date = models.DateTimeField()
    
    def __unicode__(self):
        return "%s rating %s (%s)" % (self.user, self.snippet, self.get_rating_display())
    
    def save(self):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Rating, self).save()
    
    def get_score(self):
        return self.rating_set.aggregate(Sum('rating'))
        