// AUTO-GENERATED – Model Interfaces
export interface LogEntry {
  id?: number;
  action_time: string;
  user: User;
  content_type?: ContentType;
  object_id?: string;
  object_repr: string;
  action_flag: number;
  change_message?: string;
}
export interface Permission {
  id?: number;
  name: string;
  content_type: ContentType;
  codename: string;
}
export interface Group {
  id?: number;
  name: string;
  permissions?: Permission[];
}
export interface User {
  id?: number;
  password: string;
  last_login?: string;
  is_superuser: boolean;
  username: string;
  first_name?: string;
  last_name?: string;
  email?: string;
  is_staff: boolean;
  is_active: boolean;
  date_joined: string;
  groups?: Group[];
  user_permissions?: Permission[];
}
export interface ContentType {
  id?: number;
  app_label: string;
  model: string;
}
export interface Session {
  session_key: string;
  session_data: string;
  expire_date: string;
}
export interface Product {
  id?: number;
  name: string;
  description?: string;
  price: number;
  stock: number;
  created_at?: string;
  updated_at?: string;
  is_dismantling: boolean;
  is_plannable: boolean;
}
export interface OrderType {
  id?: number;
  name: string;
}
export interface Order {
  id?: number;
  name: string;
  description?: string;
  start_datetime: string;
  end_datetime: string;
  type: OrderType;
  products: Product[];
}

export interface CreateOrder {
  name: "coreLib_String";
  products: "any";
  type: "any";
  start_datetime: "coreLib_DateTime";
  end_datetime: "coreLib_DateTime";
}
export interface OrderDetailSerializer {
  id?: "coreLib_Int32";
  name: "coreLib_String";
  products: "any";
  type: "any";
  start_datetime: "coreLib_DateTime";
  end_datetime: "coreLib_DateTime";
}
export interface OrderTypeSerializer {
  id?: "coreLib_Int32";
  name: "coreLib_String";
}
export interface ProductSerializer {
  id?: "coreLib_Int32";
  name: "coreLib_String";
  description?: "coreLib_String";
  price: "coreLib_Decimal";
  stock: "coreLib_Int32";
  is_dismantling?: "coreLib_Boolean";
  is_plannable?: "coreLib_Boolean";
}
export interface UpdateOrder {
  name: "coreLib_String";
  products?: "any";
  type: "any";
  start_datetime: "coreLib_DateTime";
  end_datetime: "coreLib_DateTime";
}