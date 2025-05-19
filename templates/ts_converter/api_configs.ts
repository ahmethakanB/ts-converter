import { typeInformation } from './tables';

export const apiConfigs = {
  productAPI: {
    link         : '/get-product',
    metot        : 'GET',
    sorguIsim    : 'ProductAPI',
    queryable    : true,
    dtoTipId     : 'ProductTable',
    dtoTipBilgi  : typeInformation.ProductTable,
    sorguTipId   : 'ProductSerializer',
    sorguTipBilgi: typeInformation.ProductSerializer,
  },
  orderTypeAPI: {
    link         : '/get-order-type',
    metot        : 'GET',
    sorguIsim    : 'OrderTypeAPI',
    queryable    : true,
    dtoTipId     : 'ProductTable',
    dtoTipBilgi  : typeInformation.ProductTable,
    sorguTipId   : 'ProductSerializer',
    sorguTipBilgi: typeInformation.ProductSerializer,
  },
  orderdetails: {
    link         : '/order-details/',
    metot        : 'GET',
    sorguIsim    : 'OrderDetailViewSet',
    queryable    : true,
    dtoTipId     : 'WorkDetailTable',
    dtoTipBilgi  : typeInformation.WorkDetailTable,
    sorguTipId   : 'OrderDetailSerializer',
    sorguTipBilgi: typeInformation.OrderDetailSerializer,
  },
};