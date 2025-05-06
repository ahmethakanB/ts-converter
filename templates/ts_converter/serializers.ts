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