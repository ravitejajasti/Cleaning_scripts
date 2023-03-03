import pandas as pd
from datetime import date, timedelta


in_path = '/Users/ravitejajasti/Downloads/'
out_path = '/Users/ravitejajasti/OneDrive - Djolt/cleaned_domains/'
file_name = str(date.today()-timedelta(days=3)) + '-US'

exclude = ['admin', 'abuse', 'account', 'adm',  'billing', 'contact', 'customer', 'domain', 'domnames', 'docs', 'dns', 'develop',
'guide', 'guideus', 'general', 'help', 'helpus', 'host', 'info', 'mail@', 'manager', 'manage@', 'myweb', 'none', 'notification', 'provisioning_customer@',
'provisioning', 'project@', 'registry', 'siteadmin', 'sysadmin', 'sysmgr', 'support@', 'server', 'sales', 'support', 'server247', 'tech@', 'techsupport', 'techsystem', 'webmaster', 'web']

def read_xl(uploaded_file):
    df = pd.read_excel(uploaded_file)
    df = df.drop(columns=['domain_registrar_name', 'registrant_address'])
    df.columns = ['COMPANY_WEBSITE', 'DOMAIN_PURCHASE_DATE', 'DOMAIN_EXPIRY_DATE', 'FIRSTNAME', 'COMPANY_NAME', 'CITY','STATE', 'ZIP', 'COUNTRY', 'EMAIL', 'SMS']
    final_df = df[~df['EMAIL'].str.contains('|'.join(exclude), na=False, case=False)]
    final_df = final_df.to_csv(index=False).encode('utf-8')
    return final_df


#which python3.9
#export PYTHONPATH="${PYTHONPATH}:/Users/ravitejajasti/opt/anaconda3/lib/python3.9/site-packages://Users/ravitejajasti/opt/anaconda3/lib/python3.9/site-packages"
