from ..ThriftService import *
import sys
import logging
from .ttypes import *

all_structs = []


class Iface(object):
    def fetchMessageOperations(self, localRevision, lastOpTimestamp, count):
        """
        Parameters:
         - localRevision
         - lastOpTimestamp
         - count
        """
        pass

    def getLastReadMessageIds(self, chatId):
        """
        Parameters:
         - chatId
        """
        pass

    def multiGetLastReadMessageIds(self, chatIds):
        """
        Parameters:
         - chatIds
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def fetchMessageOperations(self, localRevision, lastOpTimestamp, count):
        """
        Parameters:
         - localRevision
         - lastOpTimestamp
         - count
        """
        self.send_fetchMessageOperations(localRevision, lastOpTimestamp, count)
        return self.recv_fetchMessageOperations()

    def send_fetchMessageOperations(self, localRevision, lastOpTimestamp, count):
        self._oprot.writeMessageBegin('fetchMessageOperations', TMessageType.CALL, self._seqid)
        args = fetchMessageOperations_args()
        args.localRevision = localRevision
        args.lastOpTimestamp = lastOpTimestamp
        args.count = count
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_fetchMessageOperations(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = fetchMessageOperations_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "fetchMessageOperations failed: unknown result")

    def getLastReadMessageIds(self, chatId):
        """
        Parameters:
         - chatId
        """
        self.send_getLastReadMessageIds(chatId)
        return self.recv_getLastReadMessageIds()

    def send_getLastReadMessageIds(self, chatId):
        self._oprot.writeMessageBegin('getLastReadMessageIds', TMessageType.CALL, self._seqid)
        args = getLastReadMessageIds_args()
        args.chatId = chatId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getLastReadMessageIds(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getLastReadMessageIds_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getLastReadMessageIds failed: unknown result")

    def multiGetLastReadMessageIds(self, chatIds):
        """
        Parameters:
         - chatIds
        """
        self.send_multiGetLastReadMessageIds(chatIds)
        return self.recv_multiGetLastReadMessageIds()

    def send_multiGetLastReadMessageIds(self, chatIds):
        self._oprot.writeMessageBegin('multiGetLastReadMessageIds', TMessageType.CALL, self._seqid)
        args = multiGetLastReadMessageIds_args()
        args.chatIds = chatIds
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_multiGetLastReadMessageIds(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = multiGetLastReadMessageIds_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "multiGetLastReadMessageIds failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["fetchMessageOperations"] = Processor.process_fetchMessageOperations
        self._processMap["getLastReadMessageIds"] = Processor.process_getLastReadMessageIds
        self._processMap["multiGetLastReadMessageIds"] = Processor.process_multiGetLastReadMessageIds

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

    def process_fetchMessageOperations(self, seqid, iprot, oprot):
        args = fetchMessageOperations_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = fetchMessageOperations_result()
        try:
            result.success = self._handler.fetchMessageOperations(args.localRevision, args.lastOpTimestamp, args.count)
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
        oprot.writeMessageBegin("fetchMessageOperations", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getLastReadMessageIds(self, seqid, iprot, oprot):
        args = getLastReadMessageIds_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getLastReadMessageIds_result()
        try:
            result.success = self._handler.getLastReadMessageIds(args.chatId)
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
        oprot.writeMessageBegin("getLastReadMessageIds", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_multiGetLastReadMessageIds(self, seqid, iprot, oprot):
        args = multiGetLastReadMessageIds_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = multiGetLastReadMessageIds_result()
        try:
            result.success = self._handler.multiGetLastReadMessageIds(args.chatIds)
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
        oprot.writeMessageBegin("multiGetLastReadMessageIds", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class fetchMessageOperations_args(object):
    """
    Attributes:
     - localRevision
     - lastOpTimestamp
     - count
    """


    def __init__(self, localRevision=None, lastOpTimestamp=None, count=None,):
        self.localRevision = localRevision
        self.lastOpTimestamp = lastOpTimestamp
        self.count = count

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
                if ftype == TType.I64:
                    self.localRevision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.lastOpTimestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
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
        oprot.writeStructBegin('fetchMessageOperations_args')
        if self.localRevision is not None:
            oprot.writeFieldBegin('localRevision', TType.I64, 2)
            oprot.writeI64(self.localRevision)
            oprot.writeFieldEnd()
        if self.lastOpTimestamp is not None:
            oprot.writeFieldBegin('lastOpTimestamp', TType.I64, 3)
            oprot.writeI64(self.lastOpTimestamp)
            oprot.writeFieldEnd()
        if self.count is not None:
            oprot.writeFieldBegin('count', TType.I32, 4)
            oprot.writeI32(self.count)
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
all_structs.append(fetchMessageOperations_args)
fetchMessageOperations_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'localRevision', None, None, ),  # 2
    (3, TType.I64, 'lastOpTimestamp', None, None, ),  # 3
    (4, TType.I32, 'count', None, None, ),  # 4
)


class fetchMessageOperations_result(object):
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
                    self.success = MessageOperations()
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
        oprot.writeStructBegin('fetchMessageOperations_result')
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
all_structs.append(fetchMessageOperations_result)
fetchMessageOperations_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [MessageOperations, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getLastReadMessageIds_args(object):
    """
    Attributes:
     - chatId
    """


    def __init__(self, chatId=None,):
        self.chatId = chatId

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
                if ftype == TType.STRING:
                    self.chatId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getLastReadMessageIds_args')
        if self.chatId is not None:
            oprot.writeFieldBegin('chatId', TType.STRING, 2)
            oprot.writeString(self.chatId.encode('utf-8') if sys.version_info[0] == 2 else self.chatId)
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
all_structs.append(getLastReadMessageIds_args)
getLastReadMessageIds_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'chatId', 'UTF8', None, ),  # 2
)


class getLastReadMessageIds_result(object):
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
                    self.success = LastReadMessageIds()
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
        oprot.writeStructBegin('getLastReadMessageIds_result')
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
all_structs.append(getLastReadMessageIds_result)
getLastReadMessageIds_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [LastReadMessageIds, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class multiGetLastReadMessageIds_args(object):
    """
    Attributes:
     - chatIds
    """


    def __init__(self, chatIds=None,):
        self.chatIds = chatIds

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
                if ftype == TType.LIST:
                    self.chatIds = []
                    (_etype1309, _size1306) = iprot.readListBegin()
                    for _i1310 in range(_size1306):
                        _elem1311 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.chatIds.append(_elem1311)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('multiGetLastReadMessageIds_args')
        if self.chatIds is not None:
            oprot.writeFieldBegin('chatIds', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.chatIds))
            for iter1312 in self.chatIds:
                oprot.writeString(iter1312.encode('utf-8') if sys.version_info[0] == 2 else iter1312)
            oprot.writeListEnd()
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
all_structs.append(multiGetLastReadMessageIds_args)
multiGetLastReadMessageIds_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.LIST, 'chatIds', (TType.STRING, 'UTF8', False), None, ),  # 2
)


class multiGetLastReadMessageIds_result(object):
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
                if ftype == TType.LIST:
                    self.success = []
                    (_etype1316, _size1313) = iprot.readListBegin()
                    for _i1317 in range(_size1313):
                        _elem1318 = LastReadMessageIds()
                        _elem1318.read(iprot)
                        self.success.append(_elem1318)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('multiGetLastReadMessageIds_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1319 in self.success:
                iter1319.write(oprot)
            oprot.writeListEnd()
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
all_structs.append(multiGetLastReadMessageIds_result)
multiGetLastReadMessageIds_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [LastReadMessageIds, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
#fix_spec(all_structs)
del all_structs
