from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from fcuser.models import Fcuser
from .forms import BoardForm
from .models import Board
from django.http import Http404
from tag.models import Tag
# Create your views here.
def board_detail(requset, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(requset, 'board_detail.html', {'board': board})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 2)
    boards = paginator.get_page(page)
    return render(request,'board_list.html', {'boards':boards})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk = user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                if not tag:
                    pass
                else:
                    _tag, _ = Tag.objects.get_or_create(name=tag)
                    board.tags.add(_tag)


            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_writer.html', {'form': form})