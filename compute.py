import pandas as pd, json, sys
# Usage: python compute.py Norfunds-Investment-Overview-30.09.26.xlsx
# Workbook: https://www.norfund.no/investment-overview/
X=sys.argv[1] if len(sys.argv)>1 else 'Norfunds-Investment-Overview-30.09.26.xlsx'
c=pd.read_excel(X,'Investments by country'); c.columns=['inv','share','country','status','sector','sub','mandate','instr','cur','nok','usd','exnok','exusd','rep','fx']
i=pd.read_excel(X,'Investments by instrument'); i.columns=['status','inv','sector','sub','mandate','date','instr','cur','nok','usd','exnok','exusd','rep','fx']
c['country']=c['country'].astype(str).str.strip(); c['inv']=c['inv'].astype(str).str.strip(); i['inv']=i['inv'].astype(str).str.strip()
c['cur']=c['cur'].astype(str).str.strip(); i['cur']=i['cur'].astype(str).str.strip(); i['instr']=i['instr'].astype(str).str.strip()
AFR={"South Africa","Kenya","Cote D'Ivoire","Uganda","Nigeria","Tanzania, United Republic Of","Ghana","Zambia","Mozambique","Congo, Democratic Republic Of The","Cameroon","Senegal","Ethiopia","Malawi","Egypt","Madagascar","Burkina Faso","Morocco","Rwanda","Angola","Zimbabwe","Gabon","Sierra Leone","Mali","Mauritius","South Sudan","Botswana","Togo","Chad","Mauritania","Somalia","Liberia","Tunisia","Benin","Burundi","Namibia","Guinea","Congo","Niger","Eswatini","Djibouti","Central African Republic","Lesotho","Seychelles","Gambia","Guinea-Bissau","Equatorial Guinea","Cape Verde","Sao Tome and Principe","Algeria","Libya","Sudan","Eritrea"}
allc=set(c.country.unique()); print('unmapped candidates:',sorted(str(x) for x in allc if x not in AFR))
ca=c[c.status=='Active']
af=ca[ca.country.isin(AFR)]
print('country-sheet Africa',af.nok.sum()/1e9, 'countries',af[af.nok>0].country.nunique())
# instrument-level allocation: shares per investee
sh=ca.groupby(['inv','country']).nok.sum().reset_index(); sh['share']=sh.nok/sh.groupby('inv').nok.transform('sum'); sh=sh[['inv','country','share']]
ia=i[i.status=='Active'].merge(sh,on='inv',how='left')
ia['alloc']=ia.nok*ia.share
print('check total alloc',ia.alloc.sum()/1e9,'vs country sheet active',ca.nok.sum()/1e9, 'unallocated rows',ia.share.isna().sum())
A=ia[ia.country.isin(AFR)]; X=A[A.country!='South Africa']
print('Africa',A.alloc.sum()/1e9,'exSA',X.alloc.sum()/1e9)
local={'Kenya':'KES','Zambia':'ZMW','Tanzania, United Republic Of':'TZS','Mozambique':'MZN','Uganda':'UGX','Nigeria':'NGN','Ghana':'GHS','Malawi':'MWK','Ethiopia':'ETB','Rwanda':'RWF','Egypt':'EGP','Congo, Democratic Republic Of The':'CDF',"Cote D'Ivoire":'XOF','Senegal':'XOF','Madagascar':'MGA','Cameroon':'XAF','Angola':'AOA','Morocco':'MAD','Burkina Faso':'XOF','Mali':'XOF','Togo':'XOF','Benin':'XOF','Niger':'XOF','Namibia':'NAD','Lesotho':'LSL','Eswatini':'SZL','Botswana':'BWP','Zimbabwe':'ZWG','Sierra Leone':'SLE','Gabon':'XAF','Chad':'XAF','Mauritius':'MUR','Tunisia':'TND','Liberia':'LRD','Somalia':'SOS','South Sudan':'SSP','Mauritania':'MRU','Burundi':'BIF','Guinea':'GNF','Djibouti':'DJF','Central African Republic':'XAF','Congo':'XAF'}
X=X.copy(); X['own']=X.apply(lambda r: r.cur==local.get(r.country,'??'),axis=1)
X['hard']=X.cur.isin(['USD','EUR','NOK','GBP'])
print('exSA own-ccy',X[X.own].alloc.sum()/1e6, X[X.own].alloc.sum()/X.alloc.sum()*100, 'hard',X[X.hard].alloc.sum()/X.alloc.sum()*100,'other',X[~X.own&~X.hard].groupby('cur').alloc.sum()/1e6)

# ---- derived data used in the report ----
HARD=['USD','EUR','NOK','GBP']
A=A.copy(); A['hard']=A.cur.isin(HARD); A['own']=A.apply(lambda r: r.cur==local.get(r.country,'ZAR' if r.country=='South Africa' else '??'),axis=1)
out=A.groupby(['country','instr','cur']).alloc.sum().reset_index().rename(columns={'alloc':'committed_nok'})
out.to_csv('commitments_by_country_instrument_currency.csv',index=False)
summ=A.groupby('country').apply(lambda s: pd.Series({'committed_nok':s.alloc.sum(),'loans_nok':s[s.instr=='Loans'].alloc.sum(),'hard_currency_loans_nok':s[(s.instr=='Loans')&s.hard].alloc.sum(),'own_currency_nok':s[s.own].alloc.sum()})).reset_index()
summ.sort_values('committed_nok',ascending=False).to_csv('country_summary.csv',index=False)
print('wrote commitments_by_country_instrument_currency.csv and country_summary.csv')
