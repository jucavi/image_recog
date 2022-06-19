CONTENT_FORMAT = {
    'DATE': {
        'rows': 1,
        'cols': 2,
        'keys': [
            ('channel_name', 'date')
        ]
    },
    'LEVES': {
        'rows': 6,
        'cols': 3,
        'keys': [
            ('pd High', 'pw High', 'pm High'),
            ('pd VAH', 'pw VAH', 'pm VAH'),
            ('pd POC', 'pw POC', 'pm POC'),
            ('pd EQ', 'pw EQ', 'pm EQ'),
            ('pd VAL', 'pw VAL', 'pm VAL'),
            ('pd Low', 'pw Low', 'pm EQLow')
        ]
    },
    'OPEN': {
        'rows': 1,
        'cols': 3,
        'keys': [
            ('Daily Open', 'Weekly Open', 'Monthly Open')
        ]
    },
    'CC': {
        'rows': 2,
        'cols': 2,
        'keys': [
            ('Global Resistance', 'Local Resistance'),
            ('Global Support', 'Local Support')
        ]
    },
    'MISCELLANEUSS': {
        'rows': 2,
        'cols': 2,
        'keys': [
            ('Current Price', 'Funding'),
            ('svwap', '15m CVD Divergences')
        ]
    },
    'NPOCS': {
        'rows': 4,
        'cols': 2,
        'keys': [
            ('Downside Daily', 'Upside Daily'),
            ('Downside Weekly', 'Upside Weekly'),
            ('Downside Monthly', 'Upside Monthly'),
            ('Downside NSPOC', 'Upside NSPOC')
        ]
    }
}