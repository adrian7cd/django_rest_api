from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListProductAPIView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.DetailProductAPIView.as_view(), name="product-detail"),
    path("create/", views.CreateProductAPIView.as_view(), name="product_create"),
    path("update/<int:pk>/", views.UpdateProductAPIView.as_view(), name="product_update"),
    path("delete/<int:pk>/", views.DeleteProductAPIView.as_view(), name="product_delete")
]
