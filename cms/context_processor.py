from cms.models import MetaTags,BodyMetaTags


def allMetaTags(request):
    head_meta_tags = MetaTags.objects.all()
    body_tags = BodyMetaTags.objects.all()
    
    context = {
        'head_meta_tags':head_meta_tags,
        'body_tags': body_tags
    }
    return context