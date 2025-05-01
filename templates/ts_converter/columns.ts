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
  label: string;
  type: string;
  required?: boolean;
  disabled?: boolean;
  formAttributes?: { [key: string]: any };
  [key: string]: any;
}


export interface OrderDetailSerializer {
  id?: number;
  name: string;
  products: any;
  type: number;
  start_datetime: string;
  end_datetime: string;
  order_type?: string;
}

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

export const OrderFormDto_create_Fields: FormField[] = [
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
    "type": "3"
  },
  {
    "formAttributes": {
      "inputType": 4
    },
    "field": "products",
    "label": "Ürünler",
    "type": "4"
  }
];

export const OrderFormDto_update_Fields: FormField[] = [
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
    "type": "3"
  },
  {
    "formAttributes": {
      "inputType": 4
    },
    "field": "products",
    "label": "Ürünler",
    "type": "4"
  }
];

export const OrderFormDto_view_Fields: FormField[] = [
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
    "type": "3"
  },
  {
    "formAttributes": {
      "inputType": 4,
      "disabled": true
    },
    "field": "products",
    "label": "Ürünler",
    "type": "4"
  }
];