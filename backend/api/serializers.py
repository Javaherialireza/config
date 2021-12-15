from rest_framework import serializers
from blog.models import Article
class Articleserializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #field = ("title" ,"slug","author","content","publish","status")
         

