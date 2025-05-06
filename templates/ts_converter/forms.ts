import { FormField } from './core';
import { apiConfigs } from './api_configs';
// AUTO-GENERATED – Form DTO Configs
export const Order_create_Fields: FormField[] = [
  {
    "formAttributes": {
      "inputType": 0,
      "required": true
    },
    "field": "name",
    "label": "Sipariş Adı",
    "type": "0"
  },
  {
    "formAttributes": {
      "inputType": 1
    },
    "field": "description",
    "label": "Açıklama",
    "type": "1"
  },
  {
    "formAttributes": {
      "inputType": 2,
      "required": true
    },
    "field": "start_datetime",
    "label": "Başlangıç Zamanı",
    "type": "2"
  },
  {
    "formAttributes": {
      "inputType": 2
    },
    "field": "end_datetime",
    "label": "Bitiş Zamanı",
    "type": "2"
  },
  {
    "formAttributes": {
      "inputType": 3,
      "required": true
    },
    "field": "type",
    "label": "Sipariş Tipi",
    "type": "3",
    api: apiConfigs.orderTypeAPI,
    "model_name": "OrderType",
    "model": "OrderType",
    "serializer": "OrderTypeSerializer"
  },
  {
    "formAttributes": {
      "inputType": 4
    },
    "field": "products",
    "label": "Ürünler",
    "type": "4",
    api: apiConfigs.productAPI,
    "model_name": "Product",
    "model": "Product",
    "serializer": "ProductSerializer"
  }
];
export const Order_update_Fields: FormField[] = [
  {
    "formAttributes": {
      "disabled": true,
      "inputType": 5
    },
    "field": "id",
    "label": "ID",
    "type": "5"
  },
  {
    "formAttributes": {
      "inputType": 0
    },
    "field": "name",
    "label": "Sipariş Adı",
    "type": "0"
  },
  {
    "formAttributes": {
      "inputType": 1
    },
    "field": "description",
    "label": "Açıklama",
    "type": "1"
  },
  {
    "formAttributes": {
      "inputType": 2
    },
    "field": "start_datetime",
    "label": "Başlangıç Zamanı",
    "type": "2"
  },
  {
    "formAttributes": {
      "inputType": 2
    },
    "field": "end_datetime",
    "label": "Bitiş Zamanı",
    "type": "2"
  },
  {
    "formAttributes": {
      "inputType": 3
    },
    "field": "type",
    "label": "Sipariş Tipi",
    "type": "3",
    api: apiConfigs.orderTypeAPI,
    "model_name": "OrderType",
    "model": "OrderType",
    "serializer": "OrderTypeSerializer"
  },
  {
    "formAttributes": {
      "inputType": 4
    },
    "field": "products",
    "label": "Ürünler",
    "type": "4",
    api: apiConfigs.productAPI,
    "model_name": "Product",
    "model": "Product",
    "serializer": "ProductSerializer"
  }
];
export const Order_view_Fields: FormField[] = [
  {
    "formAttributes": {
      "disabled": true,
      "inputType": 5
    },
    "field": "id",
    "label": "ID",
    "type": "5"
  },
  {
    "formAttributes": {
      "inputType": 0,
      "disabled": true
    },
    "field": "name",
    "label": "Sipariş Adı",
    "type": "0"
  },
  {
    "formAttributes": {
      "inputType": 1,
      "disabled": true
    },
    "field": "description",
    "label": "Açıklama",
    "type": "1"
  },
  {
    "formAttributes": {
      "inputType": 2,
      "disabled": true
    },
    "field": "start_datetime",
    "label": "Başlangıç Zamanı",
    "type": "2"
  },
  {
    "formAttributes": {
      "inputType": 2,
      "disabled": true
    },
    "field": "end_datetime",
    "label": "Bitiş Zamanı",
    "type": "2"
  },
  {
    "formAttributes": {
      "inputType": 3,
      "disabled": true
    },
    "field": "type",
    "label": "Sipariş Tipi",
    "type": "3",
    api: apiConfigs.orderTypeAPI,
    "model_name": "OrderType",
    "model": "OrderType",
    "serializer": "OrderTypeSerializer"
  },
  {
    "formAttributes": {
      "inputType": 4,
      "disabled": true
    },
    "field": "products",
    "label": "Ürünler",
    "type": "4",
    api: apiConfigs.productAPI,
    "model_name": "Product",
    "model": "Product",
    "serializer": "ProductSerializer"
  }
];