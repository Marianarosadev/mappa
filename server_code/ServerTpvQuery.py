import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http

@anvil.server.callable
def readTpv(initial_datetime, final_datetime=None, partner_document='', merchant_document=''):
  url = 'https://api-datascience.cappta.com.br/transactions_by_docid_date_v1v2noxus?initial_datetime={}'.format(initial_datetime.strftime('%d/%m/%Y %H:%M:%S'))
  
  if final_datetime is not None:
    url+= '&final_datetime={}'.format(final_datetime.strftime('%d/%m/%Y %H:%M:%S'))  
  if partner_document != '':
    url+= '&partner_document={}'.format(partner_document)
  if merchant_document != '':
    url+= '&merchant_document={}'.format(merchant_document) 

  url = 'https://api-datascience.cappta.com.br/transactions_by_docid_date_v1v2noxus'

  try:
    response = anvil.http.request( 
      url=url,
      method='GET',
      json=True,
    )
  except Exception as e:
    print('e: ', e)

  return response