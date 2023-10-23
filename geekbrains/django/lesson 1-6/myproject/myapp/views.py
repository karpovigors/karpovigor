from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import datetime, timedelta
from .models import Order, Client

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Visited the home page')
    html = """
    <h1>Welcome to my Django site!</h1>
    """
    return HttpResponse(html)

def about(request):
    logger.info('Visited the about page')
    html = """
    <h1>About Me</h1>
    <p>This is my first Django website.</p>
    """
    return HttpResponse(html)

def client_orders(request, client_id):
    client = Client.objects.get(id=client_id)
    today = datetime.today()

    periods = {
        "7 days": today - timedelta(days=7),
        "30 days": today - timedelta(days=30),
        "365 days": today - timedelta(days=365)
    }

    ordered_products = {
        period: Order.objects.filter(client=client, order_date__gte=start_date).distinct()
        for period, start_date in periods.items()
    }

    return render(request, 'myapp/client_orders.html', {
        'client': client,
        'ordered_products': ordered_products
    })