// AUTO-GENERATED – Core Interfaces
export interface Column {
  alanIsmi: string;
  anahtar: string;
  hidden?: boolean;
  typeCode?: number;
  kolonAttributelar?: { [key: string]: any };
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
}