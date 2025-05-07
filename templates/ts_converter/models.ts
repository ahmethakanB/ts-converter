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

// AUTO-GENERATED – Serializer Interfaces
export interface OrderDetailSerializer {
  id?: number;
  name: string;
  products: any;
  type: number;
  start_datetime: string;
  end_datetime: string;
  order_type?: string;
}
export interface OrderSerializer {
  id?: number;
  name: string;
  products: any;
  type: number;
  start_datetime: string;
  end_datetime: string;
  order_type?: string;
}
export interface OrderTypeSerializer {
  id?: number;
  name: string;
}
export interface ProductSerializer {
  id?: number;
  name: string;
  description?: string;
  price: number;
  stock: number;
  is_dismantling?: boolean;
  is_plannable?: boolean;
}

// AUTO-GENERATED – Metadata for DTOs & Serializers
export const typeInformation = {
  LogEntry: { tipIsmi: "LogEntry" },
  Permission: { tipIsmi: "Permission" },
  Group: { tipIsmi: "Group" },
  User: { tipIsmi: "User" },
  ContentType: { tipIsmi: "ContentType" },
  Session: { tipIsmi: "Session" },
  Product: { tipIsmi: "Product" },
  OrderType: { tipIsmi: "OrderType" },
  Order: { tipIsmi: "Order" },
  OrderDetailSerializer: { tipIsmi: "OrderDetailSerializer" },
  OrderSerializer: { tipIsmi: "OrderSerializer" },
  OrderTypeSerializer: { tipIsmi: "OrderTypeSerializer" },
  ProductSerializer: { tipIsmi: "ProductSerializer" },
};