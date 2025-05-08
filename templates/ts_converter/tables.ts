import { Column } from './core';

import { Column } from './core';
import { typeInformation } from './models';
import { apiConfigs } from './api_configs';

export const OrderTableDto = {
  tipIsmi: "OrderTableDto",
  tipId: "OrderTableDto",
  nitelikTipIsmi: null,
  kolonTanimlar: [
    {
      alanIsmi: "Id",
      anahtar: "id",
      tipKodu: 9,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "ID"}},
        {"tipIsmi": "birincilAnahtarAttribute", "obje": {}},
      ],
      objeTipId: "coreLib_Int32",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Name",
      anahtar: "name",
      tipKodu: 18,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Sipariş Adı"}},
      ],
      objeTipId: "coreLib_String",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Description",
      anahtar: "description",
      tipKodu: null,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Açıklama"}},
      ],
      objeTipId: "any",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "StartDatetime",
      anahtar: "startDatetime",
      tipKodu: 16,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Başlangıç Zamanı"}},
      ],
      objeTipId: "coreLib_DateTime",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "EndDatetime",
      anahtar: "endDatetime",
      tipKodu: 16,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Bitiş Zamanı"}},
      ],
      objeTipId: "coreLib_DateTime",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Type",
      anahtar: "type",
      tipKodu: 18,
      kolonAttributelar: [
        {
          tipIsmi: "alanSecimSecenekTipiType",
          obje: {
            sorguObje: { ustSecenekId: null, tabloAdi: "OrderType", kolonAdi: "type", secenekTipi: null },
            sorguTipId: `orderTypeAPI`,
            etiketAnahtarlar: null,
            aciklamaAnahtar: null,
            excelAnahtar: null,
            yalnizFiltrelerdeSecim: false
          }
        },
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Sipariş Tipi"}},
      ],
      objeTipId: "coreLib_String",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Products",
      anahtar: "products",
      tipKodu: 9,
      kolonAttributelar: [
        {
          tipIsmi: "alanSecimSecenekTipiProducts",
          obje: {
            sorguObje: { ustSecenekId: null, tabloAdi: "Product", kolonAdi: "products", secenekTipi: null },
            sorguTipId: `productAPI`,
            etiketAnahtarlar: null,
            aciklamaAnahtar: null,
            excelAnahtar: null,
            yalnizFiltrelerdeSecim: false
          }
        },
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Ürünler"}},
        {"tipIsmi": "birincilAnahtarAttribute", "obje": {}},
      ],
      objeTipId: "coreLib_Int32",
      bosOlabilir: false,
      enumTipi: false
    },
  ],
  tabloAttributelar: []
};

export const WorkDetailTable = {
  tipIsmi: "WorkDetailTable",
  tipId: "WorkDetailTable",
  nitelikTipIsmi: null,
  kolonTanimlar: [
    {
      alanIsmi: "Id",
      anahtar: "id",
      tipKodu: 9,
      kolonAttributelar: [
        {"tipIsmi": "birincilAnahtarAttribute", "obje": {}},
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "ID"}},
      ],
      objeTipId: "coreLib_Int32",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Name",
      anahtar: "name",
      tipKodu: 18,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "İş Detayı Adı"}},
      ],
      objeTipId: "coreLib_String",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Products",
      anahtar: "products",
      tipKodu: 9,
      kolonAttributelar: [
        {
          tipIsmi: "alanSecimSecenekTipiProducts",
          obje: {
            sorguObje: { ustSecenekId: null, tabloAdi: "Product", kolonAdi: "products", secenekTipi: null },
            sorguTipId: `productAPI`,
            etiketAnahtarlar: null,
            aciklamaAnahtar: null,
            excelAnahtar: null,
            yalnizFiltrelerdeSecim: false
          }
        },
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Ürünler"}},
      ],
      objeTipId: "coreLib_Int32",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Type",
      anahtar: "type",
      tipKodu: 9,
      kolonAttributelar: [
        {
          tipIsmi: "alanSecimSecenekTipiType",
          obje: {
            sorguObje: { ustSecenekId: null, tabloAdi: "OrderType", kolonAdi: "type", secenekTipi: null },
            sorguTipId: `orderTypeAPI`,
            etiketAnahtarlar: null,
            aciklamaAnahtar: null,
            excelAnahtar: null,
            yalnizFiltrelerdeSecim: false
          }
        },
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Sipariş Tipi"}},
      ],
      objeTipId: "coreLib_Int32",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "StartDatetime",
      anahtar: "startDatetime",
      tipKodu: 16,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Başlangıç Zamanı"}},
      ],
      objeTipId: "coreLib_DateTime",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "EndDatetime",
      anahtar: "endDatetime",
      tipKodu: 16,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Bitiş Zamanı"}},
      ],
      objeTipId: "coreLib_DateTime",
      bosOlabilir: false,
      enumTipi: false
    },
  ],
  tabloAttributelar: []
};
