def run(birthday_s):
    # birthday_s = input('Enter your birthday e.g. 1st June \n')
    # birthday_s = '22 Dec'
    # birthday_s = '22/12'  # vn date format

    try:
        from dateutil import parser; str2date=parser.parse
        d = str2date(birthday_s)
    except:
        # why need this 2nd parser? normally above dateutil parser is suffix, but w
        from datetime import datetime; d = datetime.strptime(birthday_s, '%d/%m')

    from datetime import datetime
    d = datetime(datetime.now().year, d.month, d.day)

    data = [
        {'name': 'Aries'       , 'from': str2date('21 March')     , 'to': str2date('20 April')     },
        {'name': 'Taurus'      , 'from': str2date('20 April')     , 'to': str2date('21 May')       },
        {'name': 'Gemini'      , 'from': str2date('21 May')       , 'to': str2date('21 June')      },
        {'name': 'Cancer'      , 'from': str2date('21 June')      , 'to': str2date('23 July')      },
        {'name': 'Leo'         , 'from': str2date('23 July')      , 'to': str2date('23 August')    },
        {'name': 'Virgo'       , 'from': str2date('23 August')    , 'to': str2date('23 September') },
        {'name': 'Libra'       , 'from': str2date('23 September') , 'to': str2date('23 October')   },
        {'name': 'Scorpio'     , 'from': str2date('23 October')   , 'to': str2date('22 November')  },
        {'name': 'Sagittarius' , 'from': str2date('22 November')  , 'to': str2date('22 December')  },

        #CAUTION compare this year 12-22 to 01-20 of NEXT YEAR
        {'name': 'Capricorn'   , 'from': str2date('22 December')  , 'to': str2date('20 January')   },

        {'name': 'Aquarius'    , 'from': str2date('20 January')   , 'to': str2date('19 February')  },
        {'name': 'Pisces'      , 'from': str2date('19 February')  , 'to': str2date('21 March')     },
    ]

    translate_vn = {
        'Aries'       : 'Bạch Dương - Cừu',
        'Taurus'      : 'Kim Ngưu - Bò mộng',
        'Gemini'      : 'Song Tử - Cặp song sinh',
        'Cancer'      : 'Cự Giải - Cua',
        'Leo'         : 'Sư Tử - Sư tử',
        'Virgo'       : 'Xử Nữ - Trinh nữ',
        'Libra'       : 'Thiên Bình - Cân',
        'Scorpio'     : 'Thiên Yết - Bọ cạp',
        'Sagittarius' : 'Nhân Mã - Cung thủ',
        'Capricorn'   : 'Ma Kết - Dê',
        'Aquarius'    : 'Bảo Bình - Người gánh nước',
        'Pisces'      : 'Song Ngư - Cá',    
    }
    
    found_i = None
    for i in data:
        if i['from'] <= d < i['to']:
            found_i = i

    if not found_i:
        #region 2nd effort find @ Capricorn
        #CAUTION compare this year 12-22 to 01-20 of NEXT YEAR
        #     =                                                     1900 this year                       1901 next year
        data2 = data_Capricorn = {'name': 'Capricorn', 'from': str2date('22 December 1900')  , 'to': str2date('20 January 1901') }

        # setup d2 to compare
        d2 = None
        from datetime import datetime
        if   d.month==12: d2 = datetime(1900, d.month, d.day)
        elif d.month==1:  d2 = datetime(1901, d.month, d.day)
        else: raise Exception('Something not right occured')

        is_Capricorn = data2['from'] <= d2 < data2['to']
        if is_Capricorn: found_i = data2
        #endregion 2nd effort find @ Capricorn

    name = found_i.get('name', 'Not found')
    vn   = translate_vn.get(name)
    print(f'{d.day:02d}/{d.month:02d} {name:12s} {vn}')

if __name__ == '__main__':
    run('22/12')
