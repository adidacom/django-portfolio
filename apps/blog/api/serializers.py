from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from apps.accounts.api.serializers import UserDetailSerializer
from apps.comments.api.serializers import CommentSerializer
from apps.comments.models import Comment
from apps.blog.models import Blog


blog_detail_url = HyperlinkedIdentityField(
    view_name='blogs-api:detail',
    lookup_field='slug',

)


class BlogListSerializer(ModelSerializer):
    url = blog_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = [
            "url",
            "user",
            "title",
            "slug",
            "body",
            "pub_date",
        ]


class BlogDetailSerializer(ModelSerializer):
    url = blog_detail_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            "url",
            "id",
            "user",
            "title",
            "slug",
            "body",
            "html",
            "pub_date",
            "image",
            "comments"
        ]

    def get_html(self, obj):
        return obj.get_html()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        comments_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(comments_qs, many=True).data
        return comments


class BlogCreateUpdateSerializer(ModelSerializer):
    url = blog_detail_url

    class Meta:
        model = Blog
        fields = [
            "url",
            "title",
            "body",
            "pub_date",
        ]

