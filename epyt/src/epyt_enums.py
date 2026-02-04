class EpytEnums:
    def __init__(self):
        self.DEMANDMODEL = ['DDA', 'PDA']
        self.TYPELINK = ['CVPIPE', 'PIPE', 'PUMP', 'PRV', 'PSV',
                         'PBV', 'FCV', 'TCV', 'GPV', 'PCV']
        self.TYPEMIXMODEL = ['MIX1', 'MIX2', 'FIFO', 'LIFO']
        self.TYPENODE = ['JUNCTION', 'RESERVOIR', 'TANK']
        self.TYPEPUMP = ['CONSTANT_HORSEPOWER', 'POWER_FUNCTION', 'CUSTOM', 'NO_CURVE']
        self.TYPEPUMPSTATE = ['XHEAD', '', 'CLOSED', 'OPEN', '', 'XFLOW']
        self.TYPEQUALITY = ['NONE', 'CHEM', 'AGE', 'TRACE', 'MULTIS']
        self.TYPESOURCE = ['CONCEN', 'MASS', 'SETPOINT', 'FLOWPACED']
        self.TYPESTATS = ['NONE', 'AVERAGE', 'MINIMUM', 'MAXIMUM', 'RANGE']
        self.TYPECONTROL = ['LOWLEVEL', 'HIGHLEVEL', 'TIMER', 'TIMEOFDAY']
        self.TYPEREPORT = ['YES', 'NO', 'FULL']
        self.TYPESTATUS = ['CLOSED', 'OPEN', 'ACTIVE']
        self.TYPECURVE = ['VOLUME', 'PUMP', 'EFFICIENCY', 'HEADLOSS', 'GENERAL', 'VALVE']
        self.TYPEHEADLOSS = ['HW', 'DW', 'CM']
        self.TYPEUNITS = ['CFS', 'GPM', 'MGD', 'IMGD', 'AFD',
                          'LPS', 'LPM', 'MLD', 'CMH', 'CMD', 'CMS']
        self.TYPEBINSTATUS = ['CLOSED (MAX. HEAD EXCEEDED)', 'TEMPORARILY CLOSED',
                              'CLOSED', 'OPEN', 'ACTIVE(PARTIALLY OPEN)',
                              'OPEN (MAX. FLOW EXCEEDED',
                              'OPEN (PRESSURE SETTING NOT MET)']
        self.RULESTATUS = ['OPEN', 'CLOSED', 'ACTIVE']
        self.LOGOP = ['IF', 'AND', 'OR']
        self.RULEOBJECT = ['NODE', 'LINK', 'SYSTEM']
        self.RULEVARIABLE = ['DEMAND', 'HEAD', 'GRADE', 'LEVEL', 'PRESSURE', 'FLOW',
                             'STATUS', 'SETTING', 'POWER', 'TIME',
                             'CLOCKTIME', 'FILLTIME', 'DRAINTIME']
        self.RULEOPERATOR = ['=', '~=', '<=', '>=', '<', '>', 'IS',
                             'NOT', 'BELOW', 'ABOVE']

    def as_dict(self):
        # Return a dict of all list attributes.
        return vars(self).copy()
