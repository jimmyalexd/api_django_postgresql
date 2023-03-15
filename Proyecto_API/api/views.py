from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Point
import json
import folium

# Create your views here.


class PointView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            points = list(Point.objects.filter(id=id).values())
            if len(points) > 0:
                point = points[0]
                data = {'message': "Success", 'point': point}
            else:
                data = {'message': "Punto no encontrado..."}
            return JsonResponse(data)
        else:
            points = list(Point.objects.values())
            if len(points) > 0:
                data = {'message': "Success", 'points': points}
            else:
                data = {'message': "Puntos no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Point.objects.create(
            name=jd['name'], latitude=jd['latitude'],longitude=jd['longitude'],address=jd['address'], phone=jd['phone'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request,id):
        jd = json.loads(request.body)
        points = list(Point.objects.filter(id=id).values())
        if len(points) > 0:
            point = Point.objects.get(id=id)
            point.name=jd['name']
            point.latitude=jd['latitude']
            point.longitude=jd['longitude']
            point.address=jd['address']
            point.phone=jd['phone']
            point.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Punto no encontrado..."}
        return JsonResponse(data)
    
    
    def delete(self, request, id):
        points = list(Point.objects.filter(id=id).values())
        if len(points) > 0:
            Point.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Punto no encontrado..."}
        return JsonResponse(data)


def map_view(request):
    points = Point.objects.all()
    map = folium.Map(location=[points.first().latitude, points.first().longitude], zoom_start=12)
    for point in points:
        popup_text = f"<b>{point.name}</b><br>{point.address}<br>Phone: {point.phone}"
        folium.Marker([point.latitude, point.longitude], popup=popup_text).add_to(map)
    return render(request, 'api/map.html', {'map': map._repr_html_()})