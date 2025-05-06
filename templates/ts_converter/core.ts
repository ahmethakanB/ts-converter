// AUTO-GENERATED – Core Interfaces
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
  api?: any;
  model_name?: string;
  model?: string;
  serializer?: string;
}