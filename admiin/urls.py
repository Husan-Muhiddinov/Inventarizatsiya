from django.urls import path
from .views import *



urlpatterns = [
    path('', Admin_index, name='admin-index'),
    path('unknown-devices', Unknown_Devices, name='unknown-devices'),
    path('category-create/excel-file', UploadExcelFile, name='create-by-excel'),
    path('index/category-create', CategoryCreateView.as_view(), name='category-create'),
    path('index/base/<int:pk>', baseview, name='base-view'),
    path('index/base/<int:pk>/add-equipment', EquipmentCreateView, name='equipment-create'),
    path('add-equipments/excel', product_create_excel, name='equipment-create-excel'),
    path('index/base/<int:pk>/admin-detail-of-product', ProductDetailView, name='product-detail'),
    path('index/base/<int:pk>/product-update', ProductUpdateView, name='product-update'),
    path('index/base/<int:pk>/product-delete', ProductDeleteView, name='product-delete'),
    path('index/responsible-create', ResponsibleCreateView.as_view(), name='responsible-create'),
    # path('index/rooms-add', RoomsCreateView.as_view(), name='rooms-add'),
    path('index/model-create', ModelCreateView.as_view(), name='model-create'),
    path('search', SearchResultsView.as_view(), name='admin-search'),
    path('categories', AdminCategories, name='admin-categories'),
    path('category-edit/<int:pk>', AdminCategoryEdit, name='category-edit'),
    path('category-delete/<int:pk>', AdminCategoryDelete, name='category-delete'),
    path('models', AdminModels, name='admin-models'),
    path('model-edit/<int:pk>', AdminModelEdit, name='model-edit'),
    path('model-delete/<int:pk>', AdminModelDelete, name='model-delete'),
    path('responsibles', AdminResponsibles, name='admin-responsibles'),
    path('responsible-delete/<int:pk>', AdminResponsibleDelete, name='responsible-delete'),
    path('responsible-edit/<int:pk>', AdminResponsibleEdit, name='responsible-edit'),
    path('responsible/<int:pk>/products', AdminResponsibleProducts, name='responsible-index'),
    path('rooms', AdminRooms, name='admin-rooms'),
    path('rooms/floor/<int:pk>', AdminRoomFloor, name='admin-rooms-floors'),
    path('room-detail/<str:slug>', AdminRoomDetail, name='admin-room-details'),



    path('building', test),
]
