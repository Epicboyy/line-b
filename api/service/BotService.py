from ..ThriftService import *
import sys
import logging
from .ttypes import *
all_structs = []

class Iface(object):
    def notifyLeaveGroup(self, groupMid):
        """
        Parameters:
         - groupMid
        """
        pass

    def notifyLeaveRoom(self, roomMid):
        """
        Parameters:
         - roomMid
        """
        pass

    def getBotUseInfo(self, botMid):
        """
        Parameters:
         - botMid
        """
        pass

    def sendChatCheckedByWatermark(self, seq, mid, watermark, sessionId):
        """
        Parameters:
         - seq
         - mid
         - watermark
         - sessionId
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def notifyLeaveGroup(self, groupMid):
        """
        Parameters:
         - groupMid
        """
        self.send_notifyLeaveGroup(groupMid)
        self.recv_notifyLeaveGroup()

    def send_notifyLeaveGroup(self, groupMid):
        self._oprot.writeMessageBegin('notifyLeaveGroup', TMessageType.CALL, self._seqid)
        args = notifyLeaveGroup_args()
        args.groupMid = groupMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_notifyLeaveGroup(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = notifyLeaveGroup_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def notifyLeaveRoom(self, roomMid):
        """
        Parameters:
         - roomMid
        """
        self.send_notifyLeaveRoom(roomMid)
        self.recv_notifyLeaveRoom()

    def send_notifyLeaveRoom(self, roomMid):
        self._oprot.writeMessageBegin('notifyLeaveRoom', TMessageType.CALL, self._seqid)
        args = notifyLeaveRoom_args()
        args.roomMid = roomMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_notifyLeaveRoom(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = notifyLeaveRoom_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def getBotUseInfo(self, botMid):
        """
        Parameters:
         - botMid
        """
        self.send_getBotUseInfo(botMid)
        return self.recv_getBotUseInfo()

    def send_getBotUseInfo(self, botMid):
        self._oprot.writeMessageBegin('getBotUseInfo', TMessageType.CALL, self._seqid)
        args = getBotUseInfo_args()
        args.botMid = botMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getBotUseInfo(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getBotUseInfo_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getBotUseInfo failed: unknown result")

    def sendChatCheckedByWatermark(self, seq, mid, watermark, sessionId):
        """
        Parameters:
         - seq
         - mid
         - watermark
         - sessionId
        """
        self.send_sendChatCheckedByWatermark(seq, mid, watermark, sessionId)
        self.recv_sendChatCheckedByWatermark()

    def send_sendChatCheckedByWatermark(self, seq, mid, watermark, sessionId):
        self._oprot.writeMessageBegin('sendChatCheckedByWatermark', TMessageType.CALL, self._seqid)
        args = sendChatCheckedByWatermark_args()
        args.seq = seq
        args.mid = mid
        args.watermark = watermark
        args.sessionId = sessionId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendChatCheckedByWatermark(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendChatCheckedByWatermark_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["notifyLeaveGroup"] = Processor.process_notifyLeaveGroup
        self._processMap["notifyLeaveRoom"] = Processor.process_notifyLeaveRoom
        self._processMap["getBotUseInfo"] = Processor.process_getBotUseInfo
        self._processMap["sendChatCheckedByWatermark"] = Processor.process_sendChatCheckedByWatermark

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

    def process_notifyLeaveGroup(self, seqid, iprot, oprot):
        args = notifyLeaveGroup_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = notifyLeaveGroup_result()
        try:
            self._handler.notifyLeaveGroup(args.groupMid)
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
        oprot.writeMessageBegin("notifyLeaveGroup", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_notifyLeaveRoom(self, seqid, iprot, oprot):
        args = notifyLeaveRoom_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = notifyLeaveRoom_result()
        try:
            self._handler.notifyLeaveRoom(args.roomMid)
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
        oprot.writeMessageBegin("notifyLeaveRoom", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getBotUseInfo(self, seqid, iprot, oprot):
        args = getBotUseInfo_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getBotUseInfo_result()
        try:
            result.success = self._handler.getBotUseInfo(args.botMid)
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
        oprot.writeMessageBegin("getBotUseInfo", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendChatCheckedByWatermark(self, seqid, iprot, oprot):
        args = sendChatCheckedByWatermark_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendChatCheckedByWatermark_result()
        try:
            self._handler.sendChatCheckedByWatermark(args.seq, args.mid, args.watermark, args.sessionId)
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
        oprot.writeMessageBegin("sendChatCheckedByWatermark", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class notifyLeaveGroup_args(object):
    """
    Attributes:
     - groupMid
    """


    def __init__(self, groupMid=None,):
        self.groupMid = groupMid

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
                if ftype == TType.STRING:
                    self.groupMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('notifyLeaveGroup_args')
        if self.groupMid is not None:
            oprot.writeFieldBegin('groupMid', TType.STRING, 1)
            oprot.writeString(self.groupMid.encode('utf-8') if sys.version_info[0] == 2 else self.groupMid)
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
all_structs.append(notifyLeaveGroup_args)
notifyLeaveGroup_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'groupMid', 'UTF8', None, ),  # 1
)


class notifyLeaveGroup_result(object):
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
        oprot.writeStructBegin('notifyLeaveGroup_result')
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
all_structs.append(notifyLeaveGroup_result)
notifyLeaveGroup_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class notifyLeaveRoom_args(object):
    """
    Attributes:
     - roomMid
    """


    def __init__(self, roomMid=None,):
        self.roomMid = roomMid

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
                if ftype == TType.STRING:
                    self.roomMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('notifyLeaveRoom_args')
        if self.roomMid is not None:
            oprot.writeFieldBegin('roomMid', TType.STRING, 1)
            oprot.writeString(self.roomMid.encode('utf-8') if sys.version_info[0] == 2 else self.roomMid)
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
all_structs.append(notifyLeaveRoom_args)
notifyLeaveRoom_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'roomMid', 'UTF8', None, ),  # 1
)


class notifyLeaveRoom_result(object):
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
        oprot.writeStructBegin('notifyLeaveRoom_result')
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
all_structs.append(notifyLeaveRoom_result)
notifyLeaveRoom_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getBotUseInfo_args(object):
    """
    Attributes:
     - botMid
    """


    def __init__(self, botMid=None,):
        self.botMid = botMid

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
                    self.botMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getBotUseInfo_args')
        if self.botMid is not None:
            oprot.writeFieldBegin('botMid', TType.STRING, 2)
            oprot.writeString(self.botMid.encode('utf-8') if sys.version_info[0] == 2 else self.botMid)
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
all_structs.append(getBotUseInfo_args)
getBotUseInfo_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'botMid', 'UTF8', None, ),  # 2
)


class getBotUseInfo_result(object):
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
                    self.success = BotUseInfo()
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
        oprot.writeStructBegin('getBotUseInfo_result')
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
all_structs.append(getBotUseInfo_result)
getBotUseInfo_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BotUseInfo, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendChatCheckedByWatermark_args(object):
    """
    Attributes:
     - seq
     - mid
     - watermark
     - sessionId
    """


    def __init__(self, seq=None, mid=None, watermark=None, sessionId=None,):
        self.seq = seq
        self.mid = mid
        self.watermark = watermark
        self.sessionId = sessionId

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
                if ftype == TType.I32:
                    self.seq = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.watermark = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.sessionId = iprot.readByte()
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
        oprot.writeStructBegin('sendChatCheckedByWatermark_args')
        if self.seq is not None:
            oprot.writeFieldBegin('seq', TType.I32, 1)
            oprot.writeI32(self.seq)
            oprot.writeFieldEnd()
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 2)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.watermark is not None:
            oprot.writeFieldBegin('watermark', TType.I64, 3)
            oprot.writeI64(self.watermark)
            oprot.writeFieldEnd()
        if self.sessionId is not None:
            oprot.writeFieldBegin('sessionId', TType.BYTE, 4)
            oprot.writeByte(self.sessionId)
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
all_structs.append(sendChatCheckedByWatermark_args)
sendChatCheckedByWatermark_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'seq', None, None, ),  # 1
    (2, TType.STRING, 'mid', 'UTF8', None, ),  # 2
    (3, TType.I64, 'watermark', None, None, ),  # 3
    (4, TType.BYTE, 'sessionId', None, None, ),  # 4
)


class sendChatCheckedByWatermark_result(object):
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
        oprot.writeStructBegin('sendChatCheckedByWatermark_result')
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
all_structs.append(sendChatCheckedByWatermark_result)
sendChatCheckedByWatermark_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
#fix_spec(all_structs)
del all_structs

