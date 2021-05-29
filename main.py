import pandas as pd
from umamusume import Sp_Umamusume
from supportcard import Sp_SupportCard
def run():
    uma=Sp_Umamusume()
    card=Sp_SupportCard()
    excel=pd.DataFrame(uma)
    excel1=pd.DataFrame(card)
    write=pd.ExcelWriter('test.xlsx')
    excel.to_excel(write,sheet_name='umamusume',index=False)
    excel1.to_excel(write,sheet_name='supportcard',index=False)
    write.save()

if __name__ == '__main__':
    run()