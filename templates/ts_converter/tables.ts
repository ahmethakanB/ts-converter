import { Column } from './core';

// AUTO-GENERATED – Table DTO Configs
export const WorkDetailTableColumns: Column[] = [
  {
    "title": "ID",
    "tableAttributes": {
      "hidden": true
    },
    "typeCode": 9,
    "field": "id"
  },
  {
    "title": "İş Detayı Adı",
    "tableAttributes": {
      "orderable": true
    },
    "typeCode": 18,
    "field": "name"
  },
  {
    "title": "Ürünler",
    "tableAttributes": {},
    "field": "products"
  },
  {
    "title": "Sipariş Tipi",
    "tableAttributes": {},
    "field": "type"
  },
  {
    "title": "Başlangıç Zamanı",
    "tableAttributes": {},
    "typeCode": 16,
    "field": "start_datetime"
  },
  {
    "title": "Bitiş Zamanı",
    "tableAttributes": {},
    "typeCode": 16,
    "field": "end_datetime"
  },
  {
    "title": "Sipariş Tipi",
    "tableAttributes": {
      "searchable": false
    },
    "typeCode": 18,
    "field": "order_type"
  }
];