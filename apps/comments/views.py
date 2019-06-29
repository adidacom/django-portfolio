from django.shortcuts import render, get_object_or_404, redirect, Http404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from .forms import CommentForm
from ..blog.utils import get_header_text
# Create your views here.


@login_required(login_url='/login/')
def comment_delete(request, comment_id):
    # obj = get_object_or_404(Comment, id=comment_id)
    try:
        obj = Comment.objects.get(id=comment_id)
    except:
        raise Http404
    if obj.user != request.user:
        # messages.success(request, "You do not have permission to delete!")
        # raise Http404
        response = HttpResponse()
        response.status_code = 403
        return response

    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, "Comment has been deleted.")
        return redirect(parent_obj_url)
    context = {
        "object": obj,
        "header_text": get_header_text
    }
    return render(request, "comments/confirm_delete.html", context)


def comment_thread(request, comment_id):
    # obj = get_object_or_404(Comment, id=comment_id)
    try:
        obj = Comment.objects.get(id=comment_id)
    except:
        raise Http404

    if not obj.is_parent:
        obj = obj.parent
    content_object = obj.content_object
    content_id = obj.content_object.id

    initial_data = {
        "content_type": obj.content_type,
        "object_id": obj.object_id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        # Make sure parent obj is there
        parent_obj = None
        # check/parse to see if parent id is there
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None
        # check if the parent id is in the database,
        # if it exists, we set the parent obj to be the first item in qs
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )
        return redirect(parent_obj.get_absolute_url())
    context = {
        "comment": obj,
        "form": form,
        "header_text": get_header_text
    }
    return render(request, "comments/comment_thread.html", context)

