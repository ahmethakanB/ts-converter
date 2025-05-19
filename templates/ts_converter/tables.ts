import { Column } from './core';
import { apiConfigs } from './api_configs';

export const typeInformation = {
  CreateOrder: { tipTanim: "CreateOrder" },
  DeleteOrder: { tipTanim: "DeleteOrder" },
  OrderTable: { tipTanim: "OrderTable" },
  OrderTypeTable: { tipTanim: "OrderTypeTable" },
  ProductTable: { tipTanim: "ProductTable" },
  UpdateOrder: { tipTanim: "UpdateOrder" },
  WorkDetailTable: { tipTanim: "WorkDetailTable" },
  OrderDetailSerializer: { tipTanim: "OrderDetailSerializer" },
  OrderTypeSerializer: { tipTanim: "OrderTypeSerializer" },
  ProductSerializer: { tipTanim: "ProductSerializer" },
};

export const CreateOrder = {
  tipIsmi: "CreateOrder",
  tipId: "CreateOrder",
  nitelikTipIsmi: null,
  kolonTanimlar: [
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
      tipKodu: 18,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Açıklama"}},
      ],
      objeTipId: "coreLib_String",
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
      ],
      objeTipId: "coreLib_Int32",
      bosOlabilir: false,
      enumTipi: false
    },
  ],
  tabloAttributelar: []
};

export const DeleteOrder = {
  tipIsmi: "DeleteOrder",
  tipId: "DeleteOrder",
  nitelikTipIsmi: null,
  kolonTanimlar: [
    {
      alanIsmi: "Id",
      anahtar: "id",
      tipKodu: 18,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Sipariş Adı"}},
      ],
      objeTipId: "coreLib_String",
      bosOlabilir: false,
      enumTipi: false
    },
  ],
  tabloAttributelar: []
};

export const OrderTable = {
  tipIsmi: "OrderTable",
  tipId: "OrderTable",
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

export const OrderTypeTable = {
  tipIsmi: "OrderTypeTable",
  tipId: "OrderTypeTable",
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
  ],
  tabloAttributelar: []
};

export const ProductTable = {
  tipIsmi: "ProductTable",
  tipId: "ProductTable",
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
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Ürün Adı"}},
      ],
      objeTipId: "coreLib_String",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Price",
      anahtar: "price",
      tipKodu: 9,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Fiyat"}},
      ],
      objeTipId: "coreLib_Int32",
      bosOlabilir: false,
      enumTipi: false
    },
    {
      alanIsmi: "Stock",
      anahtar: "stock",
      tipKodu: 9,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Stok"}},
      ],
      objeTipId: "coreLib_Int32",
      bosOlabilir: false,
      enumTipi: false
    },
  ],
  tabloAttributelar: []
};

export const UpdateOrder = {
  tipIsmi: "UpdateOrder",
  tipId: "UpdateOrder",
  nitelikTipIsmi: null,
  kolonTanimlar: [
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
      tipKodu: 18,
      kolonAttributelar: [
        {"tipIsmi": "kolonIsmiAttribute", "obje": {"baslik": "Açıklama"}},
      ],
      objeTipId: "coreLib_String",
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
