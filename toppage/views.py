
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ThisWeekMovies
from datetime import datetime, timedelta

class TopPageView(TemplateView):
    template_name = "toppage/toppage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)

        # 今日の日付を取得
        today = datetime.today().date()

        # 1週間後の日付を計算
        one_week_later = today + timedelta(days=7)

        # 今日から1週間後までのイベントを取得
        movies = ThisWeekMovies.objects.filter(day__range=[today, one_week_later])
        context['movies'] = movies.all().order_by('day')
        return context
        


