"""Django with async programming"""
import asyncio
from django.http import HttpResponse

""" 
    This example follows the next steps: 
    1. It defines an async view with an async operation
    2. It simulates an async database query or API call
    3. The result variable may await other async functions 
    4. The other function simulates async work
"""
async def async_view(request):
    await asyncio.sleep(1)
    result = await fetch_data_async()
    
    return HttpResponse(f"Async result: {result}")

async def fetch_data_async():
    await asyncio.sleep(1)
    return "Data from async operation"


""" 
    Async ORM
    
    1. You can call database queries using async functionalities. 
    2. You can also use async looping and process each user asynchronously. 
"""
async def get_users_async():
    users = await User.objects.filter(is_active=True).acount()
    user = User.objects.aget(username="Example")
    
    async for user in User.objects.filter(is_active=True):
        await process_user(user)
        
    return HttpResponse(f"Processed {users} users")


"""
    Real world example
"""
import asyncio
import json
import urllib.request
from django.http import JsonResponse

def fetch_sync(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())
    
async def fetch_url(url):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, fetch_sync, url)

async def dashboard_view(request):
    weather_task = asyncio.create_task(fetch_url("some_url.com"))
    news_task = asyncio.create_task(fetch_url("other_url.com"))
    stats_task = asyncio.create_task(fetch_url("other_more.com"))
    
    weather_data = await weather_task
    news_data = await news_task
    stats_data = await stats_task
    
    dashboard_data = {
        "weather": weather_data,
        "news": news_data,
        "stats": stats_data
    }
    
    return JsonResponse(dashboard_data)