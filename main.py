### simplerun
# import r00
# r00.run('22/12')


### multirun - all brithday value in a year
import r00
from datetime import datetime, timedelta

bd0 = datetime(2005,1,1)
for i in range(0, 365):
    bd = bd0 + timedelta(days=i)
    r00.run(str(bd))
