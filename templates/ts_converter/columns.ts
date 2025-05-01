// AUTO-GENERATED – do not edit by hand

export interface Column {
  field: string;
  title: string;
  hidden?: boolean;
  typeCode?: number;
  tableAttributes?: { [key: string]: any };
  [key: string]: any;
}

export interface FormField {
  field: string;
  title: string;
  type: string;
  required?: boolean;
  disabled?: boolean;
  formAttributes?: { [key: string]: any };
  [key: string]: any;
}


export const WorkDetailTableColumns: Column[] = [
  {
    "field": "id",
    "title": "ID",
    "typeCode": 9,
    "tableAttributes": {
      "hidden": true
    }
  },
  {
    "field": "name",
    "title": "İş Detayı Adı",
    "typeCode": 18,
    "tableAttributes": {
      "orderable": true
    }
  },
  {
    "field": "products",
    "title": "Ürünler",
    "typeCode": 1,
    "tableAttributes": {}
  },
  {
    "field": "type",
    "title": "Sipariş Tipi",
    "typeCode": 1,
    "tableAttributes": {}
  },
  {
    "field": "start_datetime",
    "title": "Başlangıç Zamanı",
    "typeCode": 16,
    "tableAttributes": {}
  },
  {
    "field": "end_datetime",
    "title": "Bitiş Zamanı",
    "typeCode": 16,
    "tableAttributes": {}
  },
  {
    "field": "order_type",
    "title": "Sipariş Tipi",
    "typeCode": 18,
    "tableAttributes": {
      "searchable": false
    }
  }
] as const;

export const OrderFormDto_create_Fields = [
  {
    "title": "Sipariş Adı",
    "formAttributes": {
      "inputType": 0,
      "required": true
    },
    "field": "name"
  },
  {
    "title": "Açıklama",
    "formAttributes": {
      "inputType": 1
    },
    "field": "description"
  },
  {
    "title": "Başlangıç Zamanı",
    "formAttributes": {
      "inputType": 2,
      "required": true
    },
    "field": "start_datetime"
  },
  {
    "title": "Bitiş Zamanı",
    "formAttributes": {
      "inputType": 2
    },
    "field": "end_datetime"
  },
  {
    "title": "Sipariş Tipi",
    "formAttributes": {
      "inputType": 3,
      "required": true
    },
    "field": "type"
  },
  {
    "title": "Ürünler",
    "formAttributes": {
      "inputType": 4
    },
    "field": "products"
  }
] as const;

export const OrderFormDto_update_Fields = [
  {
    "title": "ID",
    "formAttributes": {
      "disabled": true,
      "inputType": 5
    },
    "field": "id"
  },
  {
    "title": "Sipariş Adı",
    "formAttributes": {
      "inputType": 0
    },
    "field": "name"
  },
  {
    "title": "Açıklama",
    "formAttributes": {
      "inputType": 1
    },
    "field": "description"
  },
  {
    "title": "Başlangıç Zamanı",
    "formAttributes": {
      "inputType": 2
    },
    "field": "start_datetime"
  },
  {
    "title": "Bitiş Zamanı",
    "formAttributes": {
      "inputType": 2
    },
    "field": "end_datetime"
  },
  {
    "title": "Sipariş Tipi",
    "formAttributes": {
      "inputType": 3
    },
    "field": "type"
  },
  {
    "title": "Ürünler",
    "formAttributes": {
      "inputType": 4
    },
    "field": "products"
  }
] as const;

export const OrderFormDto_view_Fields = [
  {
    "title": "ID",
    "formAttributes": {
      "disabled": true,
      "inputType": 5
    },
    "field": "id"
  },
  {
    "title": "Sipariş Adı",
    "formAttributes": {
      "inputType": 0,
      "disabled": true
    },
    "field": "name"
  },
  {
    "title": "Açıklama",
    "formAttributes": {
      "inputType": 1,
      "disabled": true
    },
    "field": "description"
  },
  {
    "title": "Başlangıç Zamanı",
    "formAttributes": {
      "inputType": 2,
      "disabled": true
    },
    "field": "start_datetime"
  },
  {
    "title": "Bitiş Zamanı",
    "formAttributes": {
      "inputType": 2,
      "disabled": true
    },
    "field": "end_datetime"
  },
  {
    "title": "Sipariş Tipi",
    "formAttributes": {
      "inputType": 3,
      "disabled": true
    },
    "field": "type"
  },
  {
    "title": "Ürünler",
    "formAttributes": {
      "inputType": 4,
      "disabled": true
    },
    "field": "products"
  }
] as const;
