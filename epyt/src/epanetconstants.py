class EpanetConstants:
    # Limits on the size of character arrays used to store ID names
    # and text messages.
    def __init__(self):
        pass

    EN_MAXID = 31 + 1  # characters in ID name
    EN_MAXMSG = 255  # characters in message text

    # Node parameters
    EN_ELEVATION = 0
    EN_BASEDEMAND = 1
    EN_PATTERN = 2
    EN_EMITTER = 3
    EN_INITQUAL = 4
    EN_SOURCEQUAL = 5
    EN_SOURCEPAT = 6
    EN_SOURCETYPE = 7
    EN_TANKLEVEL = 8
    EN_DEMAND = 9
    EN_HEAD = 10
    EN_PRESSURE = 11
    EN_QUALITY = 12
    EN_SOURCEMASS = 13
    EN_INITVOLUME = 14
    EN_MIXMODEL = 15
    EN_MIXZONEVOL = 16
    EN_TANKDIAM = 17
    EN_MINVOLUME = 18
    EN_VOLCURVE = 19
    EN_MINLEVEL = 20
    EN_MAXLEVEL = 21
    EN_MIXFRACTION = 22
    EN_TANK_KBULK = 23
    EN_TANKVOLUME = 24
    EN_MAXVOLUME = 25
    EN_CANOVERFLOW = 26
    EN_DEMANDDEFICIT = 27
    EN_NODE_INCONTROL = 28
    EN_EMITTERFLOW = 29
    EN_LEAKAGEFLOW = 30
    EN_DEMANDFLOW = 31
    EN_FULLDEMAND = 32
    # Link parameters
    EN_DIAMETER = 0
    EN_LENGTH = 1
    EN_ROUGHNESS = 2
    EN_MINORLOSS = 3
    EN_INITSTATUS = 4
    EN_INITSETTING = 5
    EN_KBULK = 6
    EN_KWALL = 7
    EN_FLOW = 8
    EN_VELOCITY = 9
    EN_HEADLOSS = 10
    EN_STATUS = 11
    EN_SETTING = 12
    EN_ENERGY = 13
    EN_LINKQUAL = 14
    EN_LINKPATTERN = 15
    EN_PUMP_STATE = 16
    EN_PUMP_EFFIC = 17
    EN_PUMP_POWER = 18
    EN_PUMP_HCURVE = 19
    EN_PUMP_ECURVE = 20
    EN_PUMP_ECOST = 21
    EN_PUMP_EPAT = 22
    EN_LINK_INCONTROL = 23
    EN_GPV_CURVE = 24
    EN_PCV_CURVE = 25
    EN_LEAK_AREA = 26
    EN_LEAK_EXPAN = 27
    EN_LINK_LEAKAGE = 28
    # Time parameters
    EN_DURATION = 0
    EN_HYDSTEP = 1
    EN_QUALSTEP = 2
    EN_PATTERNSTEP = 3
    EN_PATTERNSTART = 4
    EN_REPORTSTEP = 5
    EN_REPORTSTART = 6
    EN_RULESTEP = 7
    EN_STATISTIC = 8
    EN_PERIODS = 9
    EN_STARTTIME = 10
    EN_HTIME = 11
    EN_QTIME = 12
    EN_HALTFLAG = 13
    EN_NEXTEVENT = 14
    EN_NEXTEVENTTANK = 15

    # Component counts
    EN_NODECOUNT = 0
    EN_TANKCOUNT = 1
    EN_LINKCOUNT = 2
    EN_PATCOUNT = 3
    EN_CURVECOUNT = 4
    EN_CONTROLCOUNT = 5
    EN_RULECOUNT = 6

    # Node types
    EN_JUNCTION = 0
    EN_RESERVOIR = 1
    EN_TANK = 2

    # Link types
    EN_CVPIPE = 0
    EN_PIPE = 1
    EN_PUMP = 2
    EN_PRV = 3
    EN_PSV = 4
    EN_PBV = 5
    EN_FCV = 6
    EN_TCV = 7
    EN_GPV = 8
    EN_PCV = 9

    # Quality analysis types
    EN_NONE = 0
    EN_CHEM = 1
    EN_AGE = 2
    EN_TRACE = 3

    # Source quality types
    EN_CONCEN = 0
    EN_MASS = 1
    EN_SETPOINT = 2
    EN_FLOWPACED = 3

    # Flow units types
    EN_CFS = 0
    EN_GPM = 1
    EN_MGD = 2
    EN_IMGD = 3
    EN_AFD = 4
    EN_LPS = 5
    EN_LPM = 6
    EN_MLD = 7
    EN_CMH = 8
    EN_CMD = 9
    EN_CMS = 10

    # Pressure units type
    EN_PSI = 0
    EN_KPA = 1
    EN_METERS = 2

    EN_DDA = 0  # Demand driven analysis
    EN_PDA = 1  # Pressure driven analysis

    # Option types
    EN_TRIALS = 0
    EN_ACCURACY = 1
    EN_TOLERANCE = 2
    EN_EMITEXPON = 3
    EN_DEMANDMULT = 4
    EN_HEADERROR = 5
    EN_FLOWCHANGE = 6
    EN_HEADLOSSFORM = 7
    EN_GLOBALEFFIC = 8
    EN_GLOBALPRICE = 9
    EN_GLOBALPATTERN = 10
    EN_DEMANDCHARGE = 11
    EN_SP_GRAVITY = 12
    EN_SP_VISCOS = 13
    EN_UNBALANCED = 14
    EN_CHECKFREQ = 15
    EN_MAXCHECK = 16
    EN_DAMPLIMIT = 17
    EN_SP_DIFFUS = 18
    EN_BULKORDER = 19
    EN_WALLORDER = 20
    EN_TANKORDER = 21
    EN_CONCENLIMIT = 22
    EN_DEMANDPATTERN = 23
    EN_EMITBACKFLOW = 24
    EN_PRESS_UNITS = 25
    EN_STATUS_REPORT = 26

    # Control types
    EN_LOWLEVEL = 0
    EN_HILEVEL = 1
    EN_TIMER = 2
    EN_TIMEOFDAY = 3

    # Time statistic types
    EN_AVERAGE = 1
    EN_MINIMUM = 2
    EN_MAXIMUM = 3
    EN_RANGE = 4

    # Tank mixing models
    EN_MIX1 = 0
    EN_MIX2 = 1
    EN_FIFO = 2
    EN_LIFO = 3

    # Save-results-to-file flag
    EN_NOSAVE = 0
    EN_SAVE = 1
    EN_INITFLOW = 10
    EN_SAVE_AND_INIT = 11

    EN_CONST_HP = 0  # Constant horsepower pump curve
    EN_POWER_FUNC = 1  # Power function pump curve
    EN_CUSTOM = 2  # User-defined custom pump curve
    EN_NOCURVE = 3  # No pump curve

    EN_VOLUME_CURVE = 0  # Volume curve
    EN_PUMP_CURVE = 1  # Pump curve
    EN_EFFIC_CURVE = 2  # Efficiency curve
    EN_HLOSS_CURVE = 3  # Head loss curve
    EN_GENERIC_CURVE = 4  # Generic curve
    EN_VALVE_CURVE = 5  # Valve position curve

    EN_UNCONDITIONAL = 0  # Unconditional object deletion
    EN_CONDITIONAL = 1

    EN_NO_REPORT = 0  # No status report
    EN_NORMAL_REPORT = 1  # Normal status report
    EN_FULL_REPORT = 2  # Full status report

    # ObjectType
    EN_NODE = 0
    EN_LINK = 1
    EN_TIMEPAT = 2
    EN_CURVE = 3
    EN_CONTROL = 4
    EN_RULE = 5

    # Head Loss Type
    EN_HW = 0
    EN_DW = 1
    EN_CM = 2

    # Network objects used in rule-based controls
    EN_R_NODE = 6
    EN_R_LINK = 7
    EN_R_SYSTEM = 8

    # Object variables used in rule-based controls.
    EN_R_DEMAND = 0
    EN_R_HEAD = 1
    EN_R_GRADE = 2
    EN_R_LEVEL = 3
    EN_R_PRESSURE = 4
    EN_R_FLOW = 5
    EN_R_STATUS = 6
    EN_R_SETTING = 7
    EN_R_POWER = 8
    EN_R_TIME = 9
    EN_R_CLOCKTIME = 10
    EN_R_FILLTIME = 11
    EN_R_DRAINTIME = 12

    # Analysis convergence statistics.
    EN_ITERATIONS = 0
    EN_RELATIVEERROR = 1
    EN_MAXHEADERROR = 2
    EN_MAXFLOWCHANGE = 3
    EN_MASSBALANCE = 4
    EN_DEFICIENTNODES = 5
    EN_DEMANDREDUCTION = 6
    EN_LEAKAGELOSS = 7

    # Link status codes used in rule-based controls
    EN_R_IS_OPEN = 1
    EN_R_IS_CLOSED = 2
    EN_R_IS_ACTIVE = 3

    EN_STEP_REPORT = 0  # Types of events that cause a timestep to end
    EN_STEP_HYD = 1
    EN_STEP_WQ = 2
    EN_STEP_TANKEVENT = 3
    EN_STEP_CONTROLEVENT = 4

    EN_MISSING = -1.0E10
    EN_SET_CLOSED = -1.0E10
    EN_SET_OPEN = 1.0E10

    # MSX Constants
    MSX_NODE = 0
    MSX_LINK = 1
    MSX_TANK = 2
    MSX_SPECIES = 3
    MSX_TERM = 4
    MSX_PARAMETER = 5
    MSX_CONSTANT = 6
    MSX_PATTERN = 7

    MSX_BULK = 0
    MSX_WALL = 1

    MSX_NOSOURCE = -1
    MSX_CONCEN = 0
    MSX_MASS = 1
    MSX_SETPOINT = 2
    MSX_FLOWPACED = 3
