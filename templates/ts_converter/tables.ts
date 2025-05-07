import { Column } from './core';

// AUTO-GENERATED – Table DTO Configs
export const WorkDetailTable = {
  "tipIsmi": "WorkDetailTable",
  "tipId": "WorkDetailTable",
  "nitelikTipIsmi": null,
  "kolonTanimlar": [
    {
      "alanIsmi": "Id",
      "anahtar": "id",
      "tipKodu": 9,
      "kolonAttributelar": [
        {
          "tipIsmi": "birincilAnahtarAttribute",
          "obje": {}
        },
        {
          "tipIsmi": "kolonIsmiAttribute",
          "obje": {
            "baslik": "ID"
          }
        },
        {
          "tipIsmi": "kolonHideAttribute",
          "obje": {}
        }
      ],
      "objeTipId": "coreLib_Int32",
      "bosOlabilir": false,
      "enumTipi": false
    },
    {
      "alanIsmi": "Name",
      "anahtar": "name",
      "tipKodu": 18,
      "kolonAttributelar": [
        {
          "tipIsmi": "kolonIsmiAttribute",
          "obje": {
            "baslik": "İş Detayı Adı"
          }
        },
        {
          "tipIsmi": "kolonOrderableAttribute",
          "obje": {}
        }
      ],
      "objeTipId": "coreLib_String",
      "bosOlabilir": false,
      "enumTipi": false
    },
    {
      "alanIsmi": "Products",
      "anahtar": "products",
      "tipKodu": null,
      "kolonAttributelar": [
        {
          "tipIsmi": "kolonIsmiAttribute",
          "obje": {
            "baslik": "Ürünler"
          }
        }
      ],
      "objeTipId": "any",
      "bosOlabilir": false,
      "enumTipi": false
    },
    {
      "alanIsmi": "Type",
      "anahtar": "type",
      "tipKodu": null,
      "kolonAttributelar": [
        {
          "tipIsmi": "kolonIsmiAttribute",
          "obje": {
            "baslik": "Sipariş Tipi"
          }
        }
      ],
      "objeTipId": "any",
      "bosOlabilir": false,
      "enumTipi": false
    },
    {
      "alanIsmi": "StartDatetime",
      "anahtar": "startDatetime",
      "tipKodu": 16,
      "kolonAttributelar": [
        {
          "tipIsmi": "kolonIsmiAttribute",
          "obje": {
            "baslik": "Başlangıç Zamanı"
          }
        }
      ],
      "objeTipId": "coreLib_DateTime",
      "bosOlabilir": false,
      "enumTipi": false
    },
    {
      "alanIsmi": "EndDatetime",
      "anahtar": "endDatetime",
      "tipKodu": 16,
      "kolonAttributelar": [
        {
          "tipIsmi": "kolonIsmiAttribute",
          "obje": {
            "baslik": "Bitiş Zamanı"
          }
        }
      ],
      "objeTipId": "coreLib_DateTime",
      "bosOlabilir": false,
      "enumTipi": false
    },
    {
      "alanIsmi": "OrderType",
      "anahtar": "orderType",
      "tipKodu": 18,
      "kolonAttributelar": [
        {
          "tipIsmi": "kolonIsmiAttribute",
          "obje": {
            "baslik": "Sipariş Tipi"
          }
        },
        {
          "tipIsmi": "kolonSearchableAttribute",
          "obje": {}
        }
      ],
      "objeTipId": "coreLib_String",
      "bosOlabilir": false,
      "enumTipi": false
    }
  ],
  "tabloAttributelar": []
};