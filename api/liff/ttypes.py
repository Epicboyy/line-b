from ..ThriftService import *

import sys
all_structs = []


class LiffErrorCode(object):
    INVALID_REQUEST = 1
    UNAUTHORIZED = 2
    CONSENT_REQUIRED = 3
    VERSION_UPDATE_REQUIRED = 4
    SERVER_ERROR = 100

    _VALUES_TO_NAMES = {
        1: "INVALID_REQUEST",
        2: "UNAUTHORIZED",
        3: "CONSENT_REQUIRED",
        4: "VERSION_UPDATE_REQUIRED",
        100: "SERVER_ERROR",
    }

    _NAMES_TO_VALUES = {
        "INVALID_REQUEST": 1,
        "UNAUTHORIZED": 2,
        "CONSENT_REQUIRED": 3,
        "VERSION_UPDATE_REQUIRED": 4,
        "SERVER_ERROR": 100,
    }


class LiffFeatureType(object):
    GEOLOCATION = 1
    ADVERTISING_ID = 2
    BLUETOOTH_LE = 3

    _VALUES_TO_NAMES = {
        1: "GEOLOCATION",
        2: "ADVERTISING_ID",
        3: "BLUETOOTH_LE",
    }

    _NAMES_TO_VALUES = {
        "GEOLOCATION": 1,
        "ADVERTISING_ID": 2,
        "BLUETOOTH_LE": 3,
    }


class LiffException(TException):
    """
    Attributes:
     - code
     - message
     - payload
    """


    def __init__(self, code=None, message=None, payload=None,):
        self.code = code
        self.message = message
        self.payload = payload

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.payload = LiffErrorPayload()
                    self.payload.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffException')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 2)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        if self.payload is not None:
            oprot.writeFieldBegin('payload', TType.STRUCT, 3)
            self.payload.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffChatContext(object):
    """
    Attributes:
     - chatMid
    """


    def __init__(self, chatMid=None,):
        self.chatMid = chatMid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.chatMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffChatContext')
        if self.chatMid is not None:
            oprot.writeFieldBegin('chatMid', TType.STRING, 1)
            oprot.writeString(self.chatMid.encode('utf-8') if sys.version_info[0] == 2 else self.chatMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffContext(object):
    """
    Attributes:
     - none
     - chat
     - squareChat
    """


    def __init__(self, none=None, chat=None, squareChat=None,):
        self.none = none
        self.chat = chat
        self.squareChat = squareChat

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.none = LiffNoneContext()
                    self.none.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.chat = LiffChatContext()
                    self.chat.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.squareChat = LiffSquareChatContext()
                    self.squareChat.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffContext')
        if self.none is not None:
            oprot.writeFieldBegin('none', TType.STRUCT, 1)
            self.none.write(oprot)
            oprot.writeFieldEnd()
        if self.chat is not None:
            oprot.writeFieldBegin('chat', TType.STRUCT, 2)
            self.chat.write(oprot)
            oprot.writeFieldEnd()
        if self.squareChat is not None:
            oprot.writeFieldBegin('squareChat', TType.STRUCT, 3)
            self.squareChat.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffErrorConsentRequired(object):
    """
    Attributes:
     - channelId
     - consentUrl
    """


    def __init__(self, channelId=None, consentUrl=None,):
        self.channelId = channelId
        self.consentUrl = consentUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.consentUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffErrorConsentRequired')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.consentUrl is not None:
            oprot.writeFieldBegin('consentUrl', TType.STRING, 2)
            oprot.writeString(self.consentUrl.encode('utf-8') if sys.version_info[0] == 2 else self.consentUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffErrorPayload(object):
    """
    Attributes:
     - consentRequired
    """


    def __init__(self, consentRequired=None,):
        self.consentRequired = consentRequired

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 3:
                if ftype == TType.STRUCT:
                    self.consentRequired = LiffErrorConsentRequired()
                    self.consentRequired.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffErrorPayload')
        if self.consentRequired is not None:
            oprot.writeFieldBegin('consentRequired', TType.STRUCT, 3)
            self.consentRequired.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffNoneContext(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffNoneContext')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffSquareChatContext(object):
    """
    Attributes:
     - squareChatMid
    """


    def __init__(self, squareChatMid=None,):
        self.squareChatMid = squareChatMid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.squareChatMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffSquareChatContext')
        if self.squareChatMid is not None:
            oprot.writeFieldBegin('squareChatMid', TType.STRING, 1)
            oprot.writeString(self.squareChatMid.encode('utf-8') if sys.version_info[0] == 2 else self.squareChatMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffView(object):
    """
    Attributes:
     - type
     - url
     - trustedDomain
     - titleIconUrl
     - titleTextColor
     - titleSubtextColor
     - titleButtonColor
     - titleBackgroundColor
     - progressBarColor
     - progressBackgroundColor
    """


    def __init__(self, type=None, url=None, trustedDomain=None, titleIconUrl=None, titleTextColor=None, titleSubtextColor=None, titleButtonColor=None, titleBackgroundColor=None, progressBarColor=None, progressBackgroundColor=None,):
        self.type = type
        self.url = url
        self.trustedDomain = trustedDomain
        self.titleIconUrl = titleIconUrl
        self.titleTextColor = titleTextColor
        self.titleSubtextColor = titleSubtextColor
        self.titleButtonColor = titleButtonColor
        self.titleBackgroundColor = titleBackgroundColor
        self.progressBarColor = progressBarColor
        self.progressBackgroundColor = progressBackgroundColor

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.type = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.url = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.BOOL:
                    self.trustedDomain = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.titleIconUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.titleTextColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.titleSubtextColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.titleButtonColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.titleBackgroundColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.progressBarColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.progressBackgroundColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffView')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.STRING, 1)
            oprot.writeString(self.type.encode('utf-8') if sys.version_info[0] == 2 else self.type)
            oprot.writeFieldEnd()
        if self.url is not None:
            oprot.writeFieldBegin('url', TType.STRING, 2)
            oprot.writeString(self.url.encode('utf-8') if sys.version_info[0] == 2 else self.url)
            oprot.writeFieldEnd()
        if self.titleTextColor is not None:
            oprot.writeFieldBegin('titleTextColor', TType.I32, 4)
            oprot.writeI32(self.titleTextColor)
            oprot.writeFieldEnd()
        if self.titleBackgroundColor is not None:
            oprot.writeFieldBegin('titleBackgroundColor', TType.I32, 5)
            oprot.writeI32(self.titleBackgroundColor)
            oprot.writeFieldEnd()
        if self.titleIconUrl is not None:
            oprot.writeFieldBegin('titleIconUrl', TType.STRING, 6)
            oprot.writeString(self.titleIconUrl.encode('utf-8') if sys.version_info[0] == 2 else self.titleIconUrl)
            oprot.writeFieldEnd()
        if self.titleSubtextColor is not None:
            oprot.writeFieldBegin('titleSubtextColor', TType.I32, 7)
            oprot.writeI32(self.titleSubtextColor)
            oprot.writeFieldEnd()
        if self.titleButtonColor is not None:
            oprot.writeFieldBegin('titleButtonColor', TType.I32, 8)
            oprot.writeI32(self.titleButtonColor)
            oprot.writeFieldEnd()
        if self.progressBarColor is not None:
            oprot.writeFieldBegin('progressBarColor', TType.I32, 9)
            oprot.writeI32(self.progressBarColor)
            oprot.writeFieldEnd()
        if self.progressBackgroundColor is not None:
            oprot.writeFieldBegin('progressBackgroundColor', TType.I32, 10)
            oprot.writeI32(self.progressBackgroundColor)
            oprot.writeFieldEnd()
        if self.trustedDomain is not None:
            oprot.writeFieldBegin('trustedDomain', TType.BOOL, 11)
            oprot.writeBool(self.trustedDomain)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffViewRequest(object):
    """
    Attributes:
     - liffId
     - context
    """


    def __init__(self, liffId=None, context=None,):
        self.liffId = liffId
        self.context = context

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.liffId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.context = LiffContext()
                    self.context.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffViewRequest')
        if self.liffId is not None:
            oprot.writeFieldBegin('liffId', TType.STRING, 1)
            oprot.writeString(self.liffId.encode('utf-8') if sys.version_info[0] == 2 else self.liffId)
            oprot.writeFieldEnd()
        if self.context is not None:
            oprot.writeFieldBegin('context', TType.STRUCT, 2)
            self.context.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LiffViewResponse(object):
    """
    Attributes:
     - view
     - contextToken
     - accessToken
     - featureToken
     - features
     - channelId
    """


    def __init__(self, view=None, contextToken=None, accessToken=None, featureToken=None, features=None, channelId=None,):
        self.view = view
        self.contextToken = contextToken
        self.accessToken = accessToken
        self.featureToken = featureToken
        self.features = features
        self.channelId = channelId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.view = LiffView()
                    self.view.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.contextToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.accessToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.featureToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.features = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readI32()
                        self.features.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffViewResponse')
        if self.view is not None:
            oprot.writeFieldBegin('view', TType.STRUCT, 1)
            self.view.write(oprot)
            oprot.writeFieldEnd()
        if self.contextToken is not None:
            oprot.writeFieldBegin('contextToken', TType.STRING, 2)
            oprot.writeString(self.contextToken.encode('utf-8') if sys.version_info[0] == 2 else self.contextToken)
            oprot.writeFieldEnd()
        if self.accessToken is not None:
            oprot.writeFieldBegin('accessToken', TType.STRING, 3)
            oprot.writeString(self.accessToken.encode('utf-8') if sys.version_info[0] == 2 else self.accessToken)
            oprot.writeFieldEnd()
        if self.featureToken is not None:
            oprot.writeFieldBegin('featureToken', TType.STRING, 4)
            oprot.writeString(self.featureToken.encode('utf-8') if sys.version_info[0] == 2 else self.featureToken)
            oprot.writeFieldEnd()
        if self.features is not None:
            oprot.writeFieldBegin('features', TType.LIST, 5)
            oprot.writeListBegin(TType.I32, len(self.features))
            for iter6 in self.features:
                oprot.writeI32(iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 6)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class RevokeTokenRequest(object):
    """
    Attributes:
     - accessToken
    """


    def __init__(self, accessToken=None,):
        self.accessToken = accessToken

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.accessToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RevokeTokenRequest')
        if self.accessToken is not None:
            oprot.writeFieldBegin('accessToken', TType.STRING, 1)
            oprot.writeString(self.accessToken.encode('utf-8') if sys.version_info[0] == 2 else self.accessToken)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(LiffException)
LiffException.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'code', None, None, ),  # 1
    (2, TType.STRING, 'message', 'UTF8', None, ),  # 2
    (3, TType.STRUCT, 'payload', [LiffErrorPayload, None], None, ),  # 3
)
all_structs.append(LiffChatContext)
LiffChatContext.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'chatMid', 'UTF8', None, ),  # 1
)
all_structs.append(LiffContext)
LiffContext.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'none', [LiffNoneContext, None], None, ),  # 1
    (2, TType.STRUCT, 'chat', [LiffChatContext, None], None, ),  # 2
    (3, TType.STRUCT, 'squareChat', [LiffSquareChatContext, None], None, ),  # 3
)
all_structs.append(LiffErrorConsentRequired)
LiffErrorConsentRequired.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'consentUrl', 'UTF8', None, ),  # 2
)
all_structs.append(LiffErrorPayload)
LiffErrorPayload.thrift_spec = (
    None,  # 0
    None,  # 1
    None,  # 2
    (3, TType.STRUCT, 'consentRequired', [LiffErrorConsentRequired, None], None, ),  # 3
)
all_structs.append(LiffNoneContext)
LiffNoneContext.thrift_spec = (
)
all_structs.append(LiffSquareChatContext)
LiffSquareChatContext.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'squareChatMid', 'UTF8', None, ),  # 1
)
all_structs.append(LiffView)
LiffView.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'type', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'url', 'UTF8', None, ),  # 2
    None,  # 3
    (4, TType.I32, 'titleTextColor', None, None, ),  # 4
    (5, TType.I32, 'titleBackgroundColor', None, None, ),  # 5
    (6, TType.STRING, 'titleIconUrl', 'UTF8', None, ),  # 6
    (7, TType.I32, 'titleSubtextColor', None, None, ),  # 7
    (8, TType.I32, 'titleButtonColor', None, None, ),  # 8
    (9, TType.I32, 'progressBarColor', None, None, ),  # 9
    (10, TType.I32, 'progressBackgroundColor', None, None, ),  # 10
    (11, TType.BOOL, 'trustedDomain', None, None, ),  # 11
)
all_structs.append(LiffViewRequest)
LiffViewRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'liffId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'context', [LiffContext, None], None, ),  # 2
)
all_structs.append(LiffViewResponse)
LiffViewResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'view', [LiffView, None], None, ),  # 1
    (2, TType.STRING, 'contextToken', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'accessToken', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'featureToken', 'UTF8', None, ),  # 4
    (5, TType.LIST, 'features', (TType.I32, None, False), None, ),  # 5
    (6, TType.STRING, 'channelId', 'UTF8', None, ),  # 6
)
all_structs.append(RevokeTokenRequest)
RevokeTokenRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'accessToken', 'UTF8', None, ),  # 1
)

del all_structs
