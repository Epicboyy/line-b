from ..ThriftService import *
import sys
import logging
from .ttypes import *
all_structs = []


class Iface(object):
    def getSnsFriends(self, snsIdType, snsAccessToken, startIdx, limit):
        """
        Parameters:
         - snsIdType
         - snsAccessToken
         - startIdx
         - limit
        """
        pass

    def getSnsMyProfile(self, snsIdType, snsAccessToken):
        """
        Parameters:
         - snsIdType
         - snsAccessToken
        """
        pass

    def postSnsInvitationMessage(self, snsIdType, snsAccessToken, toSnsUserId):
        """
        Parameters:
         - snsIdType
         - snsAccessToken
         - toSnsUserId
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def getSnsFriends(self, snsIdType, snsAccessToken, startIdx, limit):
        """
        Parameters:
         - snsIdType
         - snsAccessToken
         - startIdx
         - limit
        """
        self.send_getSnsFriends(snsIdType, snsAccessToken, startIdx, limit)
        return self.recv_getSnsFriends()

    def send_getSnsFriends(self, snsIdType, snsAccessToken, startIdx, limit):
        self._oprot.writeMessageBegin('getSnsFriends', TMessageType.CALL, self._seqid)
        args = getSnsFriends_args()
        args.snsIdType = snsIdType
        args.snsAccessToken = snsAccessToken
        args.startIdx = startIdx
        args.limit = limit
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getSnsFriends(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getSnsFriends_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getSnsFriends failed: unknown result")

    def getSnsMyProfile(self, snsIdType, snsAccessToken):
        """
        Parameters:
         - snsIdType
         - snsAccessToken
        """
        self.send_getSnsMyProfile(snsIdType, snsAccessToken)
        return self.recv_getSnsMyProfile()

    def send_getSnsMyProfile(self, snsIdType, snsAccessToken):
        self._oprot.writeMessageBegin('getSnsMyProfile', TMessageType.CALL, self._seqid)
        args = getSnsMyProfile_args()
        args.snsIdType = snsIdType
        args.snsAccessToken = snsAccessToken
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getSnsMyProfile(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getSnsMyProfile_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getSnsMyProfile failed: unknown result")

    def postSnsInvitationMessage(self, snsIdType, snsAccessToken, toSnsUserId):
        """
        Parameters:
         - snsIdType
         - snsAccessToken
         - toSnsUserId
        """
        self.send_postSnsInvitationMessage(snsIdType, snsAccessToken, toSnsUserId)
        self.recv_postSnsInvitationMessage()

    def send_postSnsInvitationMessage(self, snsIdType, snsAccessToken, toSnsUserId):
        self._oprot.writeMessageBegin('postSnsInvitationMessage', TMessageType.CALL, self._seqid)
        args = postSnsInvitationMessage_args()
        args.snsIdType = snsIdType
        args.snsAccessToken = snsAccessToken
        args.toSnsUserId = toSnsUserId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_postSnsInvitationMessage(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = postSnsInvitationMessage_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["getSnsFriends"] = Processor.process_getSnsFriends
        self._processMap["getSnsMyProfile"] = Processor.process_getSnsMyProfile
        self._processMap["postSnsInvitationMessage"] = Processor.process_postSnsInvitationMessage

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_getSnsFriends(self, seqid, iprot, oprot):
        args = getSnsFriends_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getSnsFriends_result()
        try:
            result.success = self._handler.getSnsFriends(args.snsIdType, args.snsAccessToken, args.startIdx, args.limit)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getSnsFriends", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getSnsMyProfile(self, seqid, iprot, oprot):
        args = getSnsMyProfile_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getSnsMyProfile_result()
        try:
            result.success = self._handler.getSnsMyProfile(args.snsIdType, args.snsAccessToken)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getSnsMyProfile", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_postSnsInvitationMessage(self, seqid, iprot, oprot):
        args = postSnsInvitationMessage_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = postSnsInvitationMessage_result()
        try:
            self._handler.postSnsInvitationMessage(args.snsIdType, args.snsAccessToken, args.toSnsUserId)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("postSnsInvitationMessage", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class getSnsFriends_args(object):
    """
    Attributes:
     - snsIdType
     - snsAccessToken
     - startIdx
     - limit
    """


    def __init__(self, snsIdType=None, snsAccessToken=None, startIdx=None, limit=None,):
        self.snsIdType = snsIdType
        self.snsAccessToken = snsAccessToken
        self.startIdx = startIdx
        self.limit = limit

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I32:
                    self.snsIdType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.snsAccessToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.startIdx = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.limit = iprot.readI32()
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
        oprot.writeStructBegin('getSnsFriends_args')
        if self.snsIdType is not None:
            oprot.writeFieldBegin('snsIdType', TType.I32, 2)
            oprot.writeI32(self.snsIdType)
            oprot.writeFieldEnd()
        if self.snsAccessToken is not None:
            oprot.writeFieldBegin('snsAccessToken', TType.STRING, 3)
            oprot.writeString(self.snsAccessToken.encode('utf-8') if sys.version_info[0] == 2 else self.snsAccessToken)
            oprot.writeFieldEnd()
        if self.startIdx is not None:
            oprot.writeFieldBegin('startIdx', TType.I32, 4)
            oprot.writeI32(self.startIdx)
            oprot.writeFieldEnd()
        if self.limit is not None:
            oprot.writeFieldBegin('limit', TType.I32, 5)
            oprot.writeI32(self.limit)
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
all_structs.append(getSnsFriends_args)
getSnsFriends_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'snsIdType', None, None, ),  # 2
    (3, TType.STRING, 'snsAccessToken', 'UTF8', None, ),  # 3
    (4, TType.I32, 'startIdx', None, None, ),  # 4
    (5, TType.I32, 'limit', None, None, ),  # 5
)


class getSnsFriends_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = SnsFriends()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('getSnsFriends_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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
all_structs.append(getSnsFriends_result)
getSnsFriends_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SnsFriends, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getSnsMyProfile_args(object):
    """
    Attributes:
     - snsIdType
     - snsAccessToken
    """


    def __init__(self, snsIdType=None, snsAccessToken=None,):
        self.snsIdType = snsIdType
        self.snsAccessToken = snsAccessToken

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I32:
                    self.snsIdType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.snsAccessToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getSnsMyProfile_args')
        if self.snsIdType is not None:
            oprot.writeFieldBegin('snsIdType', TType.I32, 2)
            oprot.writeI32(self.snsIdType)
            oprot.writeFieldEnd()
        if self.snsAccessToken is not None:
            oprot.writeFieldBegin('snsAccessToken', TType.STRING, 3)
            oprot.writeString(self.snsAccessToken.encode('utf-8') if sys.version_info[0] == 2 else self.snsAccessToken)
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
all_structs.append(getSnsMyProfile_args)
getSnsMyProfile_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'snsIdType', None, None, ),  # 2
    (3, TType.STRING, 'snsAccessToken', 'UTF8', None, ),  # 3
)


class getSnsMyProfile_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = SnsProfile()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('getSnsMyProfile_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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
all_structs.append(getSnsMyProfile_result)
getSnsMyProfile_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SnsProfile, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class postSnsInvitationMessage_args(object):
    """
    Attributes:
     - snsIdType
     - snsAccessToken
     - toSnsUserId
    """


    def __init__(self, snsIdType=None, snsAccessToken=None, toSnsUserId=None,):
        self.snsIdType = snsIdType
        self.snsAccessToken = snsAccessToken
        self.toSnsUserId = toSnsUserId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I32:
                    self.snsIdType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.snsAccessToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.toSnsUserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('postSnsInvitationMessage_args')
        if self.snsIdType is not None:
            oprot.writeFieldBegin('snsIdType', TType.I32, 2)
            oprot.writeI32(self.snsIdType)
            oprot.writeFieldEnd()
        if self.snsAccessToken is not None:
            oprot.writeFieldBegin('snsAccessToken', TType.STRING, 3)
            oprot.writeString(self.snsAccessToken.encode('utf-8') if sys.version_info[0] == 2 else self.snsAccessToken)
            oprot.writeFieldEnd()
        if self.toSnsUserId is not None:
            oprot.writeFieldBegin('toSnsUserId', TType.STRING, 4)
            oprot.writeString(self.toSnsUserId.encode('utf-8') if sys.version_info[0] == 2 else self.toSnsUserId)
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
all_structs.append(postSnsInvitationMessage_args)
postSnsInvitationMessage_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'snsIdType', None, None, ),  # 2
    (3, TType.STRING, 'snsAccessToken', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'toSnsUserId', 'UTF8', None, ),  # 4
)


class postSnsInvitationMessage_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('postSnsInvitationMessage_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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
all_structs.append(postSnsInvitationMessage_result)
postSnsInvitationMessage_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
#fix_spec(all_structs)
del all_structs

