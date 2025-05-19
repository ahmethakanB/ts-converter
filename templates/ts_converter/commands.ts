import { typeInformation } from './tables';

export const commandsInformation = {
  deleteOrderAPIDelete: {
    link          : '/delete-order',
    istekTipId    : 'DeleteOrder',
    istekTipBilgi : typeInformation.DeleteOrder,
    komutAkisTipId: 'DeleteOrderAPICommandFlow',
  },
  createOrderAPICreate: {
    link          : '/create-order',
    istekTipId    : 'CreateOrder',
    istekTipBilgi : typeInformation.CreateOrder,
    komutAkisTipId: 'CreateOrderAPICommandFlow',
  },
};